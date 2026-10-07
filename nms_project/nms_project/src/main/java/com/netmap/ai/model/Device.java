package com.netmap.ai.model;

import java.util.ArrayList;
import java.util.List;

public class Device {
    private String id;
    private String name;
    private DeviceType type;
    private String ipAddress;
    private String macAddress;
    private String status; // "Active" or "Inactive"
    private double x;
    private double y;
    private int connectionsCount;
    private List<String> connectedDeviceIds = new ArrayList<>();
    private List<String> connectedDeviceNames = new ArrayList<>();
    private String aiPredictedRole;
    private int aiConfidence; // e.g. 96
    private int openPortsCount;
    private double trafficKbps;
    private double packetRatePps;

    public Device() {
        this.status = "Active";
    }

    public Device(String id, String name, DeviceType type, String ipAddress, String macAddress) {
        this.id = id;
        this.name = name;
        this.type = type;
        this.ipAddress = ipAddress;
        this.macAddress = macAddress;
        this.status = "Active";
        this.openPortsCount = type != null ? type.getDefaultOpenPorts() : 0;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public DeviceType getType() {
        return type;
    }

    public void setType(DeviceType type) {
        this.type = type;
    }

    public String getIpAddress() {
        return ipAddress;
    }

    public void setIpAddress(String ipAddress) {
        this.ipAddress = ipAddress;
    }

    public String getMacAddress() {
        return macAddress;
    }

    public void setMacAddress(String macAddress) {
        this.macAddress = macAddress;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public double getX() {
        return x;
    }

    public void setX(double x) {
        this.x = x;
    }

    public double getY() {
        return y;
    }

    public void setY(double y) {
        this.y = y;
    }

    public int getConnectionsCount() {
        return connectionsCount;
    }

    public void setConnectionsCount(int connectionsCount) {
        this.connectionsCount = connectionsCount;
    }

    public List<String> getConnectedDeviceIds() {
        return connectedDeviceIds;
    }

    public void setConnectedDeviceIds(List<String> connectedDeviceIds) {
        this.connectedDeviceIds = connectedDeviceIds;
    }

    public List<String> getConnectedDeviceNames() {
        return connectedDeviceNames;
    }

    public void setConnectedDeviceNames(List<String> connectedDeviceNames) {
        this.connectedDeviceNames = connectedDeviceNames;
    }

    public String getAiPredictedRole() {
        return aiPredictedRole;
    }

    public void setAiPredictedRole(String aiPredictedRole) {
        this.aiPredictedRole = aiPredictedRole;
    }

    public int getAiConfidence() {
        return aiConfidence;
    }

    public void setAiConfidence(int aiConfidence) {
        this.aiConfidence = aiConfidence;
    }

    public int getOpenPortsCount() {
        return openPortsCount;
    }

    public void setOpenPortsCount(int openPortsCount) {
        this.openPortsCount = openPortsCount;
    }

    public double getTrafficKbps() {
        return trafficKbps;
    }

    public void setTrafficKbps(double trafficKbps) {
        this.trafficKbps = trafficKbps;
    }

    public double getPacketRatePps() {
        return packetRatePps;
    }

    public void setPacketRatePps(double packetRatePps) {
        this.packetRatePps = packetRatePps;
    }
}
