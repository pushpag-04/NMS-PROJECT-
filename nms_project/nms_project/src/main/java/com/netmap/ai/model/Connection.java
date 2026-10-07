package com.netmap.ai.model;

public class Connection {
    private String id;
    private String sourceDeviceId;
    private String targetDeviceId;
    private String sourceDeviceName;
    private String targetDeviceName;
    private String cableType; // "Ethernet", "Fiber", "Wireless"
    private String status;    // "Active"

    public Connection() {
        this.status = "Active";
        this.cableType = "Ethernet";
    }

    public Connection(String id, String sourceDeviceId, String targetDeviceId, String cableType) {
        this.id = id;
        this.sourceDeviceId = sourceDeviceId;
        this.targetDeviceId = targetDeviceId;
        this.cableType = cableType != null ? cableType : "Ethernet";
        this.status = "Active";
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getSourceDeviceId() {
        return sourceDeviceId;
    }

    public void setSourceDeviceId(String sourceDeviceId) {
        this.sourceDeviceId = sourceDeviceId;
    }

    public String getTargetDeviceId() {
        return targetDeviceId;
    }

    public void setTargetDeviceId(String targetDeviceId) {
        this.targetDeviceId = targetDeviceId;
    }

    public String getSourceDeviceName() {
        return sourceDeviceName;
    }

    public void setSourceDeviceName(String sourceDeviceName) {
        this.sourceDeviceName = sourceDeviceName;
    }

    public String getTargetDeviceName() {
        return targetDeviceName;
    }

    public void setTargetDeviceName(String targetDeviceName) {
        this.targetDeviceName = targetDeviceName;
    }

    public String getCableType() {
        return cableType;
    }

    public void setCableType(String cableType) {
        this.cableType = cableType;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
}
