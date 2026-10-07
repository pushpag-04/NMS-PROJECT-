// Network Device SVG Icons for Cytoscape.js
// Styled with authentic Cisco / GNS3 networking iconography

const NetworkIcons = {
    // Router: Circular disk with 4 crossing directional arrows
    routerSvg: `
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
            <defs>
                <radialGradient id="routerGrad" cx="40%" cy="35%" r="65%">
                    <stop offset="0%" stop-color="#00d2ff"/>
                    <stop offset="100%" stop-color="#004e92"/>
                </radialGradient>
                <filter id="glow">
                    <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#00d2ff" flood-opacity="0.4"/>
                </filter>
            </defs>
            <circle cx="50" cy="50" r="44" fill="url(#routerGrad)" stroke="#38ef7d" stroke-width="2.5" filter="url(#glow)"/>
            <!-- 4 Crossing Arrows (Cisco Router Standard) -->
            <!-- Arrow Up-Right -->
            <path d="M 50 50 L 72 28 M 72 28 L 60 28 M 72 28 L 72 40" stroke="#ffffff" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>
            <!-- Arrow Down-Left -->
            <path d="M 50 50 L 28 72 M 28 72 L 40 72 M 28 72 L 28 60" stroke="#ffffff" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>
            <!-- Arrow Up-Left -->
            <path d="M 50 50 L 32 32 M 32 32 L 32 44 M 32 32 L 44 32" stroke="#ffffff" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>
            <!-- Arrow Down-Right -->
            <path d="M 50 50 L 68 68 M 68 68 L 68 56 M 68 68 L 56 68" stroke="#ffffff" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>
            <circle cx="50" cy="50" r="5" fill="#ffffff"/>
        </svg>
    `,

    // Switch: Rectangular switch box with opposing horizontal arrows
    switchSvg: `
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
            <defs>
                <linearGradient id="switchGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="#0f2027"/>
                    <stop offset="50%" stop-color="#203a43"/>
                    <stop offset="100%" stop-color="#2c5364"/>
                </linearGradient>
            </defs>
            <!-- Outer switch chassis -->
            <rect x="8" y="24" width="84" height="52" rx="8" fill="url(#switchGrad)" stroke="#00f5d4" stroke-width="3"/>
            <!-- Port LEDs top row -->
            <circle cx="20" cy="34" r="2.5" fill="#00f5d4"/>
            <circle cx="28" cy="34" r="2.5" fill="#00f5d4"/>
            <circle cx="36" cy="34" r="2.5" fill="#00f5d4"/>
            <circle cx="44" cy="34" r="2.5" fill="#00f5d4"/>
            <circle cx="56" cy="34" r="2.5" fill="#00f5d4"/>
            <circle cx="64" cy="34" r="2.5" fill="#00f5d4"/>
            <circle cx="72" cy="34" r="2.5" fill="#00f5d4"/>
            <circle cx="80" cy="34" r="2.5" fill="#00f5d4"/>
            <!-- Cisco Switching Arrows -->
            <!-- Arrow Left to Right -->
            <path d="M 22 50 L 76 50 M 70 44 L 78 50 L 70 56" fill="none" stroke="#ffffff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
            <!-- Arrow Right to Left -->
            <path d="M 78 62 L 24 62 M 30 56 L 22 62 L 30 68" fill="none" stroke="#00f5d4" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
    `,

    // Server: Enterprise Rack / Tower Server
    serverSvg: `
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
            <defs>
                <linearGradient id="serverGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                    <stop offset="0%" stop-color="#2b5876"/>
                    <stop offset="100%" stop-color="#4e4376"/>
                </linearGradient>
            </defs>
            <!-- Server chassis -->
            <rect x="18" y="10" width="64" height="80" rx="6" fill="url(#serverGrad)" stroke="#9d4edd" stroke-width="3"/>
            <!-- Bay 1 -->
            <rect x="24" y="18" width="52" height="16" rx="3" fill="#141829" stroke="#7b2cbf" stroke-width="1.5"/>
            <circle cx="32" cy="26" r="3" fill="#00f5d4"/>
            <circle cx="40" cy="26" r="2" fill="#38ef7d"/>
            <line x1="50" y1="26" x2="70" y2="26" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
            <!-- Bay 2 -->
            <rect x="24" y="42" width="52" height="16" rx="3" fill="#141829" stroke="#7b2cbf" stroke-width="1.5"/>
            <circle cx="32" cy="50" r="3" fill="#00f5d4"/>
            <circle cx="40" cy="50" r="2" fill="#38ef7d"/>
            <line x1="50" y1="50" x2="70" y2="50" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
            <!-- Bay 3 -->
            <rect x="24" y="66" width="52" height="16" rx="3" fill="#141829" stroke="#7b2cbf" stroke-width="1.5"/>
            <circle cx="32" cy="74" r="3" fill="#00f5d4"/>
            <circle cx="40" cy="74" r="2" fill="#38ef7d"/>
            <line x1="50" y1="74" x2="70" y2="74" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
        </svg>
    `,

    // PC / Client: Workstation Monitor & Base
    pcSvg: `
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
            <defs>
                <linearGradient id="screenGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="#1f4037"/>
                    <stop offset="100%" stop-color="#99f2c8"/>
                </linearGradient>
            </defs>
            <!-- Monitor screen border -->
            <rect x="14" y="14" width="72" height="48" rx="5" fill="#0f172a" stroke="#38bdf8" stroke-width="3"/>
            <!-- Screen display area -->
            <rect x="20" y="20" width="60" height="36" rx="2" fill="#0284c7"/>
            <!-- Terminal code lines on screen -->
            <line x1="26" y1="28" x2="48" y2="28" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round"/>
            <line x1="26" y1="36" x2="64" y2="36" stroke="#bae6fd" stroke-width="2" stroke-linecap="round"/>
            <line x1="26" y1="44" x2="54" y2="44" stroke="#38ef7d" stroke-width="2" stroke-linecap="round"/>
            <!-- Monitor stand -->
            <polygon points="44,62 56,62 60,76 40,76" fill="#334155" stroke="#38bdf8" stroke-width="1.5"/>
            <!-- Monitor base -->
            <rect x="30" y="76" width="40" height="8" rx="3" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        </svg>
    `,

    // Access Point: Wi-Fi symbol emitting waves
    apSvg: `
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
            <defs>
                <linearGradient id="apGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="#f7971e"/>
                    <stop offset="100%" stop-color="#ffd200"/>
                </linearGradient>
            </defs>
            <!-- Dome base -->
            <circle cx="50" cy="50" r="44" fill="#1e293b" stroke="#f59e0b" stroke-width="3"/>
            <!-- Center emitter point -->
            <circle cx="50" cy="68" r="6" fill="#fbbf24"/>
            <!-- Wave 1 -->
            <path d="M 38 56 A 16 16 0 0 1 62 56" fill="none" stroke="#fbbf24" stroke-width="4.5" stroke-linecap="round"/>
            <!-- Wave 2 -->
            <path d="M 28 44 A 28 28 0 0 1 72 44" fill="none" stroke="#f59e0b" stroke-width="4.5" stroke-linecap="round"/>
            <!-- Wave 3 -->
            <path d="M 18 32 A 40 40 0 0 1 82 32" fill="none" stroke="#fcd34d" stroke-width="4.5" stroke-linecap="round"/>
        </svg>
    `,

    // Internet: Cloud with WAN globe lines
    internetSvg: `
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
            <defs>
                <linearGradient id="cloudGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="#0284c7"/>
                    <stop offset="100%" stop-color="#0369a1"/>
                </linearGradient>
            </defs>
            <!-- Cloud body -->
            <path d="M 32 72 L 72 72 A 16 16 0 0 0 72 40 A 24 24 0 0 0 34 32 A 18 18 0 0 0 32 72 Z"
                  fill="url(#cloudGrad)" stroke="#38bdf8" stroke-width="3.5" stroke-linejoin="round"/>
            <!-- Globe latitude/longitude in cloud -->
            <circle cx="52" cy="52" r="14" fill="none" stroke="#ffffff" stroke-width="2"/>
            <line x1="38" y1="52" x2="66" y2="52" stroke="#ffffff" stroke-width="1.5"/>
            <ellipse cx="52" cy="52" rx="7" ry="14" fill="none" stroke="#ffffff" stroke-width="1.5"/>
        </svg>
    `,

    toDataUri: function(svgString) {
        return 'data:image/svg+xml;utf8,' + encodeURIComponent(svgString.trim());
    },

    getIconDataUri: function(type) {
        if (!type) return this.toDataUri(this.pcSvg);
        const t = type.toUpperCase();
        if (t.includes('ROUTER')) return this.toDataUri(this.routerSvg);
        if (t.includes('SWITCH')) return this.toDataUri(this.switchSvg);
        if (t.includes('SERVER')) return this.toDataUri(this.serverSvg);
        if (t.includes('ACCESS') || t.includes('AP') || t.includes('WIFI')) return this.toDataUri(this.apSvg);
        if (t.includes('INTERNET') || t.includes('CLOUD')) return this.toDataUri(this.internetSvg);
        return this.toDataUri(this.pcSvg);
    }
};
