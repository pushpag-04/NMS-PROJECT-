package com.netmap.ai.model;

public class NetworkStatistics {
    private int totalDevices;
    private int totalConnections;
    private int routerCount;
    private int switchCount;
    private int serverCount;
    private int clientCount;
    private int accessPointCount;
    private int internetCount;
    private int activeCount;
    private int inactiveCount;

    public NetworkStatistics() {
    }

    public int getTotalDevices() {
        return totalDevices;
    }

    public void setTotalDevices(int totalDevices) {
        this.totalDevices = totalDevices;
    }

    public int getTotalConnections() {
        return totalConnections;
    }

    public void setTotalConnections(int totalConnections) {
        this.totalConnections = totalConnections;
    }

    public int getRouterCount() {
        return routerCount;
    }

    public void setRouterCount(int routerCount) {
        this.routerCount = routerCount;
    }

    public int getSwitchCount() {
        return switchCount;
    }

    public void setSwitchCount(int switchCount) {
        this.switchCount = switchCount;
    }

    public int getServerCount() {
        return serverCount;
    }

    public void setServerCount(int serverCount) {
        this.serverCount = serverCount;
    }

    public int getClientCount() {
        return clientCount;
    }

    public void setClientCount(int clientCount) {
        this.clientCount = clientCount;
    }

    public int getAccessPointCount() {
        return accessPointCount;
    }

    public void setAccessPointCount(int accessPointCount) {
        this.accessPointCount = accessPointCount;
    }

    public int getInternetCount() {
        return internetCount;
    }

    public void setInternetCount(int internetCount) {
        this.internetCount = internetCount;
    }

    public int getActiveCount() {
        return activeCount;
    }

    public void setActiveCount(int activeCount) {
        this.activeCount = activeCount;
    }

    public int getInactiveCount() {
        return inactiveCount;
    }

    public void setInactiveCount(int inactiveCount) {
        this.inactiveCount = inactiveCount;
    }
}
