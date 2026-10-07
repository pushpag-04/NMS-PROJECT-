package com.netmap.ai.model;

public enum DeviceType {
    INTERNET("Internet", "cloud", 0),
    ROUTER("Router", "router", 2),
    SWITCH("Switch", "switch", 1),
    SERVER("Server", "server", 4),
    PC("PC / Client", "pc", 0),
    ACCESS_POINT("Access Point", "access-point", 2);

    private final String displayName;
    private final String iconType;
    private final int defaultOpenPorts;

    DeviceType(String displayName, String iconType, int defaultOpenPorts) {
        this.displayName = displayName;
        this.iconType = iconType;
        this.defaultOpenPorts = defaultOpenPorts;
    }

    public String getDisplayName() {
        return displayName;
    }

    public String getIconType() {
        return iconType;
    }

    public int getDefaultOpenPorts() {
        return defaultOpenPorts;
    }

    public static DeviceType fromString(String text) {
        if (text == null) return PC;
        String clean = text.trim().toUpperCase().replace(" ", "_").replace("/", "_").replace("-", "_");
        if (clean.contains("INTERNET") || clean.contains("CLOUD")) return INTERNET;
        if (clean.contains("ROUTER")) return ROUTER;
        if (clean.contains("SWITCH")) return SWITCH;
        if (clean.contains("SERVER")) return SERVER;
        if (clean.contains("ACCESS") || clean.contains("AP") || clean.contains("WIFI")) return ACCESS_POINT;
        if (clean.contains("PC") || clean.contains("CLIENT") || clean.contains("COMPUTER") || clean.contains("HOST")) return PC;
        return PC;
    }
}
