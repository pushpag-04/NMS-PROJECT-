package com.netmap.ai.model;

public class ManualConnectionRequest {
    private String sourceDeviceId;
    private String targetDeviceId;
    private String cableType; // "Ethernet", "Fiber", "Wireless"

    public ManualConnectionRequest() {
    }

    public ManualConnectionRequest(String sourceDeviceId, String targetDeviceId, String cableType) {
        this.sourceDeviceId = sourceDeviceId;
        this.targetDeviceId = targetDeviceId;
        this.cableType = cableType;
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

    public String getCableType() {
        return cableType;
    }

    public void setCableType(String cableType) {
        this.cableType = cableType;
    }
}
