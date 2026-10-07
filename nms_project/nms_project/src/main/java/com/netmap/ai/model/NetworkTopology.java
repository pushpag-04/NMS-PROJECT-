package com.netmap.ai.model;

import java.util.ArrayList;
import java.util.List;

public class NetworkTopology {
    private List<Device> devices = new ArrayList<>();
    private List<Connection> connections = new ArrayList<>();
    private String mode = "AUTOMATIC";
    private long timestamp = System.currentTimeMillis();

    public NetworkTopology() {
    }

    public NetworkTopology(List<Device> devices, List<Connection> connections, String mode) {
        this.devices = devices;
        this.connections = connections;
        this.mode = mode;
        this.timestamp = System.currentTimeMillis();
    }

    public List<Device> getDevices() {
        return devices;
    }

    public void setDevices(List<Device> devices) {
        this.devices = devices;
    }

    public List<Connection> getConnections() {
        return connections;
    }

    public void setConnections(List<Connection> connections) {
        this.connections = connections;
    }

    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }

    public long getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(long timestamp) {
        this.timestamp = timestamp;
    }
}
