// NetMap AI - Frontend Application Controller

document.addEventListener('DOMContentLoaded', () => {
    NetMapApp.init();
});

const NetMapApp = {
    currentMode: 'AUTOMATIC', // 'AUTOMATIC' or 'MANUAL'
    selectedDevice: null,
    selectedEdge: null,
    topologyView: null,
    currentUser: null,

    init: function() {
        this.bindAuthEvents();
        this.checkAuthStatus();
        this.bindDashboardEvents();
    },

    // =========================================================================
    // AUTHENTICATION MODULE
    // =========================================================================
    checkAuthStatus: async function() {
        try {
            const res = await fetch('/api/auth/status');
            const data = await res.json();
            if (data.authenticated) {
                this.currentUser = data.username;
                this.showDashboard();
            } else {
                this.showLogin();
            }
        } catch (e) {
            console.error('Auth check error:', e);
            this.showLogin();
        }
    },

    bindAuthEvents: function() {
        const loginForm = document.getElementById('loginForm');
        if (loginForm) {
            loginForm.addEventListener('submit', async (e) => {
                e.preventDefault();
                await this.handleLogin();
            });
        }

        const logoutBtn = document.getElementById('logoutBtn');
        if (logoutBtn) {
            logoutBtn.addEventListener('click', async () => {
                await this.handleLogout();
            });
        }
    },

    handleLogin: async function() {
        const usernameInput = document.getElementById('loginUsername');
        const passwordInput = document.getElementById('loginPassword');
        const errorAlert = document.getElementById('loginError');

        const username = usernameInput.value.trim();
        const password = passwordInput.value.trim();

        errorAlert.style.display = 'none';

        try {
            const res = await fetch('/api/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username, password })
            });

            const data = await res.json();
            if (res.ok && data.authenticated) {
                this.currentUser = data.username;
                this.showDashboard();
            } else {
                errorAlert.textContent = data.message || 'Invalid username or password';
                errorAlert.style.display = 'block';
            }
        } catch (e) {
            errorAlert.textContent = 'Network error connecting to server';
            errorAlert.style.display = 'block';
        }
    },

    handleLogout: async function() {
        try {
            await fetch('/api/logout', { method: 'POST' });
        } catch (e) {
            console.error('Logout error:', e);
        }
        this.currentUser = null;
        this.showLogin();
    },

    showLogin: function() {
        document.getElementById('loginView').style.display = 'flex';
        document.getElementById('dashboardView').style.display = 'none';
        document.getElementById('loginPassword').value = '';
    },

    showDashboard: function() {
        document.getElementById('loginView').style.display = 'none';
        document.getElementById('dashboardView').style.display = 'flex';
        document.getElementById('currentUsername').textContent = this.currentUser || 'admin';

        if (!this.topologyView) {
            this.initTopology();
        }
        this.loadCurrentTopology();
    },

    // =========================================================================
    // TOPOLOGY & DASHBOARD CONTROLLER
    // =========================================================================
    initTopology: function() {
        this.topologyView = new NetworkTopologyView('cy', {
            onNodeSelected: (nodeData) => this.showDeviceDetails(nodeData),
            onEdgeSelected: (edgeData) => this.showEdgeDetails(edgeData),
            onBackgroundClicked: () => this.clearSelection(),
            onNodeMoved: (id, x, y) => this.handleNodeMoved(id, x, y),
            onConnectDevices: (src, tgt) => this.handleConnectDevices(src, tgt)
        });
    },

    bindDashboardEvents: function() {
        // Mode Switcher
        const btnAutoMode = document.getElementById('btnAutoMode');
        const btnManualMode = document.getElementById('btnManualMode');

        btnAutoMode.addEventListener('click', () => this.setMode('AUTOMATIC'));
        btnManualMode.addEventListener('click', () => this.setMode('MANUAL'));

        // Auto Generation Toolbar
        document.getElementById('btnGenerate').addEventListener('click', () => this.generateNetwork());
        document.getElementById('btnReset').addEventListener('click', () => this.resetTopology());
        document.getElementById('btnFitScreen').addEventListener('click', () => this.topologyView && this.topologyView.fitScreen());
        document.getElementById('btnResetLayout').addEventListener('click', () => this.topologyView && this.topologyView.resetLayout());

        // Zoom Controls
        document.getElementById('btnZoomIn').addEventListener('click', () => this.topologyView && this.topologyView.zoomIn());
        document.getElementById('btnZoomOut').addEventListener('click', () => this.topologyView && this.topologyView.zoomOut());

        // Device Type Filters
        const filterPills = document.querySelectorAll('.filter-pill');
        filterPills.forEach(pill => {
            pill.addEventListener('click', (e) => {
                filterPills.forEach(p => p.classList.remove('active'));
                pill.classList.add('active');
                const type = pill.getAttribute('data-filter');
                if (this.topologyView) this.topologyView.filterByType(type);
            });
        });

        // Search Box
        const searchInput = document.getElementById('deviceSearchInput');
        searchInput.addEventListener('input', (e) => {
            const query = e.target.value.trim();
            if (query.length >= 2) {
                this.topologyView.searchAndFocus(query);
            } else if (query.length === 0) {
                this.topologyView.clearHighlight();
            }
        });
        searchInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                const query = e.target.value.trim();
                if (query) this.topologyView.searchAndFocus(query);
            }
        });

        // Manual Palette Buttons
        document.querySelectorAll('.palette-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                const type = btn.getAttribute('data-type');
                this.addManualDevice(type);
            });
        });

        // Manual Mode Action Buttons
        const btnCableTool = document.getElementById('btnCableTool');
        btnCableTool.addEventListener('click', () => this.toggleCableTool());

        document.getElementById('btnDeleteSelected').addEventListener('click', () => this.deleteSelectedElement());
        document.getElementById('btnClearDesign').addEventListener('click', () => this.clearManualDesign());
        document.getElementById('btnSaveDesign').addEventListener('click', () => this.saveManualDesign());
        document.getElementById('btnAnalyzeManual').addEventListener('click', () => this.analyzeManualDesign());

        // Device Details Action Buttons
        document.getElementById('btnHighlightConnections').addEventListener('click', () => {
            if (this.selectedDevice) {
                this.topologyView.highlightDirectConnections(this.selectedDevice.id);
            }
        });

        document.getElementById('btnClearHighlight').addEventListener('click', () => {
            this.topologyView.clearHighlight();
        });

        document.getElementById('btnToggleStatus').addEventListener('click', () => this.toggleDeviceStatus());
        document.getElementById('btnRenameDevice').addEventListener('click', () => this.promptRenameDevice());
        document.getElementById('btnDeleteDeviceDetail').addEventListener('click', () => this.deleteSelectedElement());
    },

    setMode: function(mode) {
        this.currentMode = mode;
        const btnAuto = document.getElementById('btnAutoMode');
        const btnManual = document.getElementById('btnManualMode');
        const autoControls = document.getElementById('autoControls');
        const manualPalette = document.getElementById('manualPaletteBar');

        if (mode === 'AUTOMATIC') {
            btnAuto.classList.add('active');
            btnManual.classList.remove('active');
            autoControls.style.display = 'flex';
            manualPalette.style.display = 'none';
            this.topologyView.cancelConnectMode();
            document.getElementById('btnCableTool').classList.remove('active');
        } else {
            btnManual.classList.add('active');
            btnAuto.classList.remove('active');
            autoControls.style.display = 'none';
            manualPalette.style.display = 'flex';
        }
    },

    // =========================================================================
    // API CALLS & DATA SYNC
    // =========================================================================
    loadCurrentTopology: async function() {
        try {
            const res = await fetch('/api/network/topology');
            const topology = await res.json();
            this.topologyView.renderTopology(topology);
            this.updateStatistics();
            this.updateAIAnalysis();
        } catch (e) {
            console.error('Error loading topology:', e);
        }
    },

    generateNetwork: async function() {
        const select = document.getElementById('deviceCountSelect');
        const count = parseInt(select.value, 10) || 10;

        try {
            const res = await fetch('/api/network/generate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ count })
            });

            const topology = await res.json();
            this.topologyView.renderTopology(topology);
            this.clearSelection();
            this.updateStatistics();
            this.updateAIAnalysis();
            this.showBanner(`Generated realistic hierarchical network with ${topology.devices.length} devices`, 'success');
        } catch (e) {
            console.error('Error generating network:', e);
        }
    },

    resetTopology: async function() {
        try {
            const res = await fetch('/api/network/reset', { method: 'POST' });
            const topology = await res.json();
            this.topologyView.renderTopology(topology);
            this.clearSelection();
            this.updateStatistics();
            this.updateAIAnalysis();
            this.showBanner('Network topology reset to 5 devices', 'success');
        } catch (e) {
            console.error('Error resetting topology:', e);
        }
    },

    updateStatistics: async function() {
        try {
            const res = await fetch('/api/network/statistics');
            const stats = await res.json();

            document.getElementById('statTotalDevices').textContent = stats.totalDevices;
            document.getElementById('statTotalConnections').textContent = stats.totalConnections;
            document.getElementById('statRouters').textContent = stats.routerCount;
            document.getElementById('statSwitches').textContent = stats.switchCount;
            document.getElementById('statServers').textContent = stats.serverCount;
            document.getElementById('statClients').textContent = stats.clientCount;
            document.getElementById('statAPs').textContent = stats.accessPointCount;
        } catch (e) {
            console.error('Error updating statistics:', e);
        }
    },

    updateAIAnalysis: async function() {
        try {
            const res = await fetch('/api/network/ai-analysis');
            const data = await res.json();
            this.renderAIAnalysis(data);
        } catch (e) {
            console.error('Error fetching AI analysis:', e);
        }
    },

    renderAIAnalysis: function(data) {
        if (!data) return;

        // Update counts
        document.getElementById('aiCountRouters').textContent = data.aiIdentifiedRouters || 0;
        document.getElementById('aiCountSwitches').textContent = data.aiIdentifiedSwitches || 0;
        document.getElementById('aiCountServers').textContent = data.aiIdentifiedServers || 0;
        document.getElementById('aiCountClients').textContent = data.aiIdentifiedClients || 0;
        document.getElementById('aiCountAPs').textContent = data.aiIdentifiedAccessPoints || 0;

        // Populate Table
        const tbody = document.getElementById('aiAnalysisTableBody');
        tbody.innerHTML = '';

        const analyses = data.analyses || [];
        analyses.forEach(item => {
            const tr = document.createElement('tr');
            const matchBadge = item.roleMatched
                ? `<span class="badge badge-status-active">Matched</span>`
                : `<span class="badge badge-status-inactive">Refined</span>`;

            tr.innerHTML = `
                <td><b>${item.deviceName}</b></td>
                <td><span class="text-secondary">${item.actualType}</span></td>
                <td><span class="badge-role">${item.predictedRole}</span></td>
                <td><span class="badge-confidence">${item.confidence}%</span></td>
                <td>${matchBadge}</td>
                <td><small class="text-muted">${item.featureSummary || ''}</small></td>
            `;
            tbody.appendChild(tr);
        });
    },

    // =========================================================================
    // MANUAL DESIGN ACTIONS
    // =========================================================================
    addManualDevice: async function(type) {
        const center = this.topologyView.cy.extent();
        // Place near center with slight jitter
        const x = (center.x1 + center.x2) / 2 + (Math.random() * 80 - 40);
        const y = (center.y1 + center.y2) / 2 + (Math.random() * 80 - 40);

        try {
            const res = await fetch('/api/network/manual/device', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ type, x, y })
            });

            const newDev = await res.json();
            await this.refreshTopologyKeepPositions();
            this.topologyView.searchAndFocus(newDev.id);
            this.showBanner(`Added new ${newDev.name} to topology`, 'success');
        } catch (e) {
            console.error('Error adding device:', e);
        }
    },

    toggleCableTool: function() {
        const btn = document.getElementById('btnCableTool');
        if (this.topologyView.isConnectMode) {
            this.topologyView.cancelConnectMode();
            btn.classList.remove('active');
            btn.innerHTML = '<i class="bi bi-link-45deg"></i> Connect Devices';
            this.hideBanner();
        } else {
            this.topologyView.startConnectMode();
            btn.classList.add('active');
            btn.innerHTML = '<i class="bi bi-x-circle"></i> Cancel Cable Tool';
            this.showBanner('Cable Tool Active: Click first device, then click second device to link.', 'warning');
        }
    },

    handleConnectDevices: async function(sourceId, targetId) {
        document.getElementById('btnCableTool').classList.remove('active');
        document.getElementById('btnCableTool').innerHTML = '<i class="bi bi-link-45deg"></i> Connect Devices';

        try {
            const res = await fetch('/api/network/manual/connection', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ sourceDeviceId: sourceId, targetDeviceId: targetId, cableType: 'Ethernet' })
            });

            if (res.ok) {
                await this.refreshTopologyKeepPositions();
                this.showBanner('Devices connected with Ethernet link.', 'success');
            }
        } catch (e) {
            console.error('Error connecting devices:', e);
        }
    },

    handleNodeMoved: async function(id, x, y) {
        if (this.currentMode !== 'MANUAL') return;
        try {
            await fetch(`/api/network/manual/device/${id}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ x, y })
            });
        } catch (e) {
            console.error('Error saving node position:', e);
        }
    },

    deleteSelectedElement: async function() {
        if (this.selectedDevice) {
            const id = this.selectedDevice.id;
            try {
                await fetch(`/api/network/manual/device/${id}`, { method: 'DELETE' });
                this.clearSelection();
                await this.refreshTopologyKeepPositions();
                this.showBanner('Device removed from canvas.', 'success');
            } catch (e) {
                console.error('Error deleting device:', e);
            }
        } else if (this.selectedEdge) {
            const id = this.selectedEdge.id;
            try {
                await fetch(`/api/network/manual/connection/${id}`, { method: 'DELETE' });
                this.clearSelection();
                await this.refreshTopologyKeepPositions();
                this.showBanner('Link removed from canvas.', 'success');
            } catch (e) {
                console.error('Error deleting connection:', e);
            }
        } else {
            alert('Please click on a device or link first to select it.');
        }
    },

    clearManualDesign: async function() {
        if (confirm('Are you sure you want to clear all devices and links from the canvas?')) {
            try {
                await fetch('/api/network/manual/clear', { method: 'POST' });
                this.clearSelection();
                await this.loadCurrentTopology();
                this.showBanner('Canvas cleared.', 'success');
            } catch (e) {
                console.error('Error clearing canvas:', e);
            }
        }
    },

    saveManualDesign: async function() {
        try {
            const res = await fetch('/api/network/manual/save', { method: 'POST' });
            if (res.ok) {
                this.showBanner('Manual topology design saved in runtime memory.', 'success');
            }
        } catch (e) {
            console.error('Error saving design:', e);
        }
    },

    analyzeManualDesign: async function() {
        try {
            const res = await fetch('/api/network/manual/analyze', { method: 'POST' });
            const data = await res.json();
            this.renderAIAnalysis(data);
            this.updateStatistics();

            if (data.isolatedDeviceCount > 0) {
                this.showBanner(`${data.isolatedDeviceCount} device(s) are not connected to the network.`, 'warning');
            } else {
                this.showBanner('Topology successfully connected.', 'success');
            }
        } catch (e) {
            console.error('Error analyzing design:', e);
        }
    },

    refreshTopologyKeepPositions: async function() {
        try {
            const res = await fetch('/api/network/topology');
            const topology = await res.json();
            this.topologyView.renderTopology(topology, true);
            this.updateStatistics();
            this.updateAIAnalysis();
        } catch (e) {
            console.error('Error refreshing topology:', e);
        }
    },

    // =========================================================================
    // DETAILS INSPECTION
    // =========================================================================
    showDeviceDetails: function(device) {
        this.selectedDevice = device;
        this.selectedEdge = null;

        document.getElementById('noSelectionPlaceholder').style.display = 'none';
        document.getElementById('deviceDetailsContent').style.display = 'block';

        document.getElementById('detailDeviceName').textContent = device.name;
        document.getElementById('detailDeviceType').textContent = device.type;
        document.getElementById('detailIpAddress').textContent = device.ipAddress || '192.168.1.X';
        document.getElementById('detailMacAddress').textContent = device.macAddress || '00:1A:2B:3C:4D:5E';

        const statusBadge = document.getElementById('detailStatus');
        statusBadge.textContent = device.status || 'Active';
        statusBadge.className = (device.status === 'Active') ? 'badge badge-status-active' : 'badge badge-status-inactive';

        document.getElementById('detailConnCount').textContent = device.connectionsCount || 0;
        document.getElementById('detailAiRole').textContent = device.aiPredictedRole || device.type;
        document.getElementById('detailAiConfidence').textContent = (device.aiConfidence || 95) + '%';

        // Connected devices list
        const tagsContainer = document.getElementById('detailConnectedTags');
        tagsContainer.innerHTML = '';
        const names = device.connectedDeviceNames || [];
        const ids = device.connectedDeviceIds || [];

        if (names.length === 0) {
            tagsContainer.innerHTML = '<span class="text-muted"><small>None (Isolated)</small></span>';
        } else {
            names.forEach((name, idx) => {
                const tag = document.createElement('span');
                tag.className = 'connected-tag';
                tag.textContent = name;
                tag.addEventListener('click', () => {
                    if (ids[idx]) this.topologyView.searchAndFocus(ids[idx]);
                });
                tagsContainer.appendChild(tag);
            });
        }
    },

    showEdgeDetails: function(edge) {
        this.selectedEdge = edge;
        this.selectedDevice = null;
        this.showBanner(`Selected Link: ${edge.cableType} (${edge.source} ↔ ${edge.target})`, 'success');
    },

    clearSelection: function() {
        this.selectedDevice = null;
        this.selectedEdge = null;
        document.getElementById('deviceDetailsContent').style.display = 'none';
        document.getElementById('noSelectionPlaceholder').style.display = 'block';
    },

    toggleDeviceStatus: async function() {
        if (!this.selectedDevice) return;
        const newStatus = (this.selectedDevice.status === 'Active') ? 'Inactive' : 'Active';
        try {
            await fetch(`/api/network/manual/device/${this.selectedDevice.id}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ status: newStatus })
            });
            this.selectedDevice.status = newStatus;
            this.showDeviceDetails(this.selectedDevice);
            this.updateStatistics();
            this.showBanner(`Device status changed to ${newStatus}`, 'success');
        } catch (e) {
            console.error('Error updating status:', e);
        }
    },

    promptRenameDevice: async function() {
        if (!this.selectedDevice) return;
        const newName = prompt('Enter new device name:', this.selectedDevice.name);
        if (newName && newName.trim() && newName.trim() !== this.selectedDevice.name) {
            try {
                await fetch(`/api/network/manual/device/${this.selectedDevice.id}`, {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ name: newName.trim() })
                });
                this.selectedDevice.name = newName.trim();
                await this.refreshTopologyKeepPositions();
                this.showDeviceDetails(this.selectedDevice);
                this.showBanner(`Device renamed to ${newName.trim()}`, 'success');
            } catch (e) {
                console.error('Error renaming device:', e);
            }
        }
    },

    // =========================================================================
    // UI HELPERS
    // =========================================================================
    showBanner: function(text, type = 'success') {
        const banner = document.getElementById('canvasStatusBanner');
        banner.textContent = text;
        banner.className = `canvas-status-banner ${type}`;
        banner.style.display = 'flex';

        clearTimeout(this.bannerTimer);
        this.bannerTimer = setTimeout(() => {
            banner.style.display = 'none';
        }, 4000);
    },

    hideBanner: function() {
        document.getElementById('canvasStatusBanner').style.display = 'none';
    }
};
