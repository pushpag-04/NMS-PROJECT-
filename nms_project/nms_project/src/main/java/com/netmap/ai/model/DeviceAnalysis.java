package com.netmap.ai.model;

public class DeviceAnalysis {
    private String deviceId;
    private String deviceName;
    private String actualType;
    private String predictedRole;
    private int confidence; // e.g. 96
    private boolean roleMatched;
    private String featureSummary;

    public DeviceAnalysis() {
    }

    public DeviceAnalysis(String deviceId, String deviceName, String actualType, String predictedRole, int confidence) {
        this.deviceId = deviceId;
        this.deviceName = deviceName;
        this.actualType = actualType;
        this.predictedRole = predictedRole;
        this.confidence = confidence;
        this.roleMatched = actualType != null && actualType.equalsIgnoreCase(predictedRole);
    }

    public String getDeviceId() {
        return deviceId;
    }

    public void setDeviceId(String deviceId) {
        this.deviceId = deviceId;
    }

    public String getDeviceName() {
        return deviceName;
    }

    public void setDeviceName(String deviceName) {
        this.deviceName = deviceName;
    }

    public String getActualType() {
        return actualType;
    }

    public void setActualType(String actualType) {
        this.actualType = actualType;
        if (this.predictedRole != null && actualType != null) {
            this.roleMatched = actualType.equalsIgnoreCase(this.predictedRole);
        }
    }

    public String getPredictedRole() {
        return predictedRole;
    }

    public void setPredictedRole(String predictedRole) {
        this.predictedRole = predictedRole;
        if (this.actualType != null && predictedRole != null) {
            this.roleMatched = this.actualType.equalsIgnoreCase(predictedRole);
        }
    }

    public int getConfidence() {
        return confidence;
    }

    public void setConfidence(int confidence) {
        this.confidence = confidence;
    }

    public boolean isRoleMatched() {
        return roleMatched;
    }

    public void setRoleMatched(boolean roleMatched) {
        this.roleMatched = roleMatched;
    }

    public String getFeatureSummary() {
        return featureSummary;
    }

    public void setFeatureSummary(String featureSummary) {
        this.featureSummary = featureSummary;
    }
}
