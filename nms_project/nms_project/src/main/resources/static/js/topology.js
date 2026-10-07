// Cytoscape.js Topology Visualizer and Manual Canvas Manager

class NetworkTopologyView {
    constructor(containerId, options = {}) {
        this.container = document.getElementById(containerId);
        this.onNodeSelected = options.onNodeSelected || (() => {});
        this.onEdgeSelected = options.onEdgeSelected || (() => {});
        this.onBackgroundClicked = options.onBackgroundClicked || (() => {});
        this.onNodeMoved = options.onNodeMoved || (() => {});
        this.onConnectDevices = options.onConnectDevices || (() => {});

        this.cy = null;
        this.isConnectMode = false;
        this.connectSourceId = null;
        this.currentFilter = 'ALL';

        this.init();
    }

    init() {
        if (!window.cytoscape) {
            console.error('Cytoscape.js is not loaded');
            return;
        }

        this.cy = cytoscape({
            container: this.container,
            boxSelectionEnabled: false,
            autounselectify: false,
            minZoom: 0.2,
            maxZoom: 3.0,
            wheelSensitivity: 0.25,
            style: [
                {
                    selector: 'node',
                    style: {
                        'label': 'data(name)',
                        'color': '#f8fafc',
                        'font-size': '11px',
                        'font-weight': '600',
                        'font-family': 'Segoe UI, sans-serif',
                        'text-valign': 'bottom',
                        'text-margin-y': 6,
                        'text-background-color': 'rgba(6, 9, 19, 0.85)',
                        'text-background-opacity': 0.85,
                        'text-background-padding': '3px',
                        'text-background-shape': 'roundrectangle',
                        'width': 64,
                        'height': 64,
                        'shape': 'roundrectangle',
                        'background-color': '#0d1527',
                        'background-image': ele => NetworkIcons.getIconDataUri(ele.data('type')),
                        'background-fit': 'contain',
                        'background-clip': 'none',
                        'border-width': 2,
                        'border-color': '#1e2c4f',
                        'transition-property': 'background-color, border-color, border-width, opacity, shadow-blur',
                        'transition-duration': '0.2s'
                    }
                },
                {
                    selector: 'node:selected',
                    style: {
                        'border-color': '#00f5d4',
                        'border-width': 3.5,
                        'shadow-blur': 16,
                        'shadow-color': '#00f5d4',
                        'shadow-opacity': 0.9
                    }
                },
                {
                    selector: 'node.highlighted',
                    style: {
                        'border-color': '#00f5d4',
                        'border-width': 3,
                        'shadow-blur': 12,
                        'shadow-color': '#00f5d4',
                        'shadow-opacity': 0.85
                    }
                },
                {
                    selector: 'node.cable-source',
                    style: {
                        'border-color': '#f59e0b',
                        'border-width': 4,
                        'shadow-blur': 18,
                        'shadow-color': '#f59e0b',
                        'shadow-opacity': 1.0
                    }
                },
                {
                    selector: 'node.dimmed',
                    style: {
                        'opacity': 0.18
                    }
                },
                {
                    selector: 'edge',
                    style: {
                        'width': 2.5,
                        'line-color': '#00b4d8',
                        'curve-style': 'bezier',
                        'opacity': 0.8,
                        'target-arrow-shape': 'none',
                        'transition-property': 'line-color, width, opacity',
                        'transition-duration': '0.2s'
                    }
                },
                {
                    selector: 'edge[cableType = "Fiber"]',
                    style: {
                        'line-color': '#f59e0b',
                        'width': 3
                    }
                },
                {
                    selector: 'edge[cableType = "Wireless"]',
                    style: {
                        'line-color': '#10b981',
                        'line-style': 'dashed',
                        'line-dash-pattern': [6, 4],
                        'width': 2.5
                    }
                },
                {
                    selector: 'edge:selected',
                    style: {
                        'line-color': '#00f5d4',
                        'width': 4,
                        'opacity': 1
                    }
                },
                {
                    selector: 'edge.highlighted',
                    style: {
                        'line-color': '#00f5d4',
                        'width': 3.5,
                        'opacity': 1
                    }
                },
                {
                    selector: 'edge.dimmed',
                    style: {
                        'opacity': 0.12
                    }
                }
            ],
            elements: []
        });

        this.bindEvents();
    }

    bindEvents() {
        if (!this.cy) return;

        // Node click
        this.cy.on('tap', 'node', evt => {
            const node = evt.target;
            const nodeData = node.data();

            if (this.isConnectMode) {
                this.handleConnectClick(nodeData.id);
                return;
            }

            this.highlightDirectConnections(node.id());
            this.onNodeSelected(nodeData);
        });

        // Edge click
        this.cy.on('tap', 'edge', evt => {
            const edge = evt.target;
            this.onEdgeSelected(edge.data());
        });

        // Background click (unselect)
        this.cy.on('tap', evt => {
            if (evt.target === this.cy) {
                if (this.isConnectMode) {
                    this.cancelConnectMode();
                } else {
                    this.clearHighlight();
                    this.onBackgroundClicked();
                }
            }
        });

        // Node drag end
        this.cy.on('dragfree', 'node', evt => {
            const node = evt.target;
            const pos = node.position();
            this.onNodeMoved(node.id(), pos.x, pos.y);
        });
    }

    renderTopology(topology, preservePositions = false) {
        if (!this.cy || !topology) return;

        const elements = [];

        // Build nodes
        (topology.devices || []).forEach(d => {
            const nodeElem = {
                group: 'nodes',
                data: {
                    id: d.id,
                    name: d.name,
                    type: d.type ? d.type.toString() : 'PC',
                    ipAddress: d.ipAddress,
                    macAddress: d.macAddress,
                    status: d.status,
                    connectionsCount: d.connectionsCount || 0,
                    connectedDeviceIds: d.connectedDeviceIds || [],
                    connectedDeviceNames: d.connectedDeviceNames || [],
                    aiPredictedRole: d.aiPredictedRole,
                    aiConfidence: d.aiConfidence,
                    openPortsCount: d.openPortsCount,
                    trafficKbps: d.trafficKbps,
                    packetRatePps: d.packetRatePps
                }
            };
            if (preservePositions && d.x !== 0 && d.y !== 0) {
                nodeElem.position = { x: d.x, y: d.y };
            }
            elements.push(nodeElem);
        });

        // Build edges
        (topology.connections || []).forEach(c => {
            elements.push({
                group: 'edges',
                data: {
                    id: c.id,
                    source: c.sourceDeviceId,
                    target: c.targetDeviceId,
                    cableType: c.cableType || 'Ethernet',
                    status: c.status || 'Active'
                }
            });
        });

        this.cy.elements().remove();
        this.cy.add(elements);

        if (!preservePositions) {
            this.applyOptimalLayout(topology.devices ? topology.devices.length : 10);
        } else {
            this.cy.fit(30);
        }

        if (this.currentFilter !== 'ALL') {
            this.filterByType(this.currentFilter);
        }
    }

    applyOptimalLayout(deviceCount) {
        if (!this.cy) return;

        // For hierarchical clean look
        const roots = this.cy.nodes().filter(n => {
            const t = (n.data('type') || '').toUpperCase();
            return t.includes('INTERNET') || t.includes('ROUTER');
        });

        let layoutConfig;

        if (deviceCount <= 15) {
            // Hierarchical breadthfirst
            layoutConfig = {
                name: 'breadthfirst',
                directed: false,
                roots: roots.length > 0 ? roots : undefined,
                spacingFactor: 1.4,
                animate: true,
                animationDuration: 400,
                padding: 40
            };
        } else {
            // Cose organic force-directed for medium-to-large networks
            layoutConfig = {
                name: 'cose',
                animate: true,
                animationDuration: 500,
                componentSpacing: 60,
                nodeOverlap: 20,
                idealEdgeLength: edge => {
                    const cType = edge.data('cableType');
                    if (cType === 'Fiber') return 90;
                    if (cType === 'Wireless') return 70;
                    return 80;
                },
                nodeRepulsion: 400000,
                padding: 40,
                fit: true
            };
        }

        const layout = this.cy.layout(layoutConfig);
        layout.run();
    }

    highlightDirectConnections(nodeId) {
        if (!this.cy) return;
        this.clearHighlight();

        const node = this.cy.getElementById(nodeId);
        if (node.empty()) return;

        node.addClass('highlighted');
        const connectedEdges = node.connectedEdges();
        connectedEdges.addClass('highlighted');
        connectedEdges.connectedNodes().addClass('highlighted');
    }

    clearHighlight() {
        if (!this.cy) return;
        this.cy.elements().removeClass('highlighted');
        this.cy.elements().removeClass('cable-source');
        if (this.currentFilter === 'ALL') {
            this.cy.elements().removeClass('dimmed');
        } else {
            this.filterByType(this.currentFilter);
        }
    }

    filterByType(filterType) {
        this.currentFilter = filterType;
        if (!this.cy) return;

        if (filterType === 'ALL') {
            this.cy.elements().removeClass('dimmed');
            return;
        }

        this.cy.batch(() => {
            this.cy.elements().addClass('dimmed');

            const matchingNodes = this.cy.nodes().filter(n => {
                const t = (n.data('type') || '').toUpperCase();
                switch (filterType) {
                    case 'ROUTER': return t.includes('ROUTER');
                    case 'SWITCH': return t.includes('SWITCH');
                    case 'SERVER': return t.includes('SERVER');
                    case 'PC': return t.includes('PC') || t.includes('CLIENT');
                    case 'ACCESS_POINT': return t.includes('ACCESS') || t.includes('AP');
                    default: return true;
                }
            });

            matchingNodes.removeClass('dimmed');
            matchingNodes.connectedEdges().removeClass('dimmed');
        });
    }

    searchAndFocus(query) {
        if (!this.cy || !query) return false;
        const q = query.trim().toLowerCase();

        const target = this.cy.nodes().filter(n => {
            const name = (n.data('name') || '').toLowerCase();
            const id = (n.data('id') || '').toLowerCase();
            const ip = (n.data('ipAddress') || '').toLowerCase();
            return name.includes(q) || id === q || ip === q;
        }).first();

        if (!target.empty()) {
            this.cy.elements().unselect();
            target.select();
            this.highlightDirectConnections(target.id());
            this.cy.animate({
                center: { eles: target },
                zoom: 1.5,
                duration: 400
            });
            this.onNodeSelected(target.data());
            return true;
        }
        return false;
    }

    startConnectMode() {
        this.isConnectMode = true;
        this.connectSourceId = null;
        if (this.cy) {
            this.cy.elements().removeClass('cable-source');
        }
    }

    cancelConnectMode() {
        this.isConnectMode = false;
        this.connectSourceId = null;
        if (this.cy) {
            this.cy.elements().removeClass('cable-source');
        }
    }

    handleConnectClick(nodeId) {
        if (!this.connectSourceId) {
            this.connectSourceId = nodeId;
            const srcNode = this.cy.getElementById(nodeId);
            srcNode.addClass('cable-source');
        } else {
            if (this.connectSourceId === nodeId) {
                this.cancelConnectMode();
                return;
            }
            const src = this.connectSourceId;
            const tgt = nodeId;
            this.cancelConnectMode();
            this.onConnectDevices(src, tgt);
        }
    }

    zoomIn() {
        if (this.cy) this.cy.zoom(this.cy.zoom() * 1.25);
    }

    zoomOut() {
        if (this.cy) this.cy.zoom(this.cy.zoom() * 0.8);
    }

    fitScreen() {
        if (this.cy) this.cy.fit(30);
    }

    resetLayout() {
        if (this.cy) {
            this.applyOptimalLayout(this.cy.nodes().length);
        }
    }

    getSelectedElement() {
        if (!this.cy) return null;
        const selected = this.cy.$(':selected');
        if (selected.empty()) return null;
        return selected.first();
    }
}
