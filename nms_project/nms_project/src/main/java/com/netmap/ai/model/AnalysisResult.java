package com.netmap.ai.model;

import java.util.ArrayList;
import java.util.List;

public class AnalysisResult {
    private boolean connected;
    private int totalDevices;
    private int totalConnections;
    private int isolatedDeviceCount;
    private List<String> isolatedDeviceNames = new ArrayList<>();
    private String message;
    private List<DeviceAnalysis> analyses = new ArrayList<>();
    private int aiIdentifiedRouters;
    private int aiIdentifiedSwitches;
    private int aiIdentifiedServers;
    private int aiIdentifiedClients;
    private int aiIdentifiedAccessPoints;

    public AnalysisResult() {
    }

    public boolean isConnected() {
        return connected;
    }

    public void setConnected(boolean connected) {
        this.connected = connected;
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

    public int getIsolatedDeviceCount() {
        return isolatedDeviceCount;
    }

    public void setIsolatedDeviceCount(int isolatedDeviceCount) {
        this.isolatedDeviceCount = isolatedDeviceCount;
    }

    public List<String> getIsolatedDeviceNames() {
        return isolatedDeviceNames;
    }

    public void setIsolatedDeviceNames(List<String> isolatedDeviceNames) {
        this.isolatedDeviceNames = isolatedDeviceNames;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public List<DeviceAnalysis> getAnalyses() {
        return analyses;
    }

    public void setAnalyses(List<DeviceAnalysis> analyses) {
        this.analyses = analyses;
    }

    public int getAiIdentifiedRouters() {
        return aiIdentifiedRouters;
    }

    public void setAiIdentifiedRouters(int aiIdentifiedRouters) {
        this.aiIdentifiedRouters = aiIdentifiedRouters;
    }

    public int getAiIdentifiedSwitches() {
        return aiIdentifiedSwitches;
    }

    public void setAiIdentifiedSwitches(int aiIdentifiedSwitches) {
        this.aiIdentifiedSwitches = aiIdentifiedSwitches;
    }

    public int getAiIdentifiedServers() {
        return aiIdentifiedServers;
    }

    public void setAiIdentifiedServers(int aiIdentifiedServers) {
        this.aiIdentifiedServers = aiIdentifiedServers;
    }

    public int getAiIdentifiedClients() {
        return aiIdentifiedClients;
    }

    public void setAiIdentifiedClients(int aiIdentifiedClients) {
        this.aiIdentifiedClients = aiIdentifiedClients;
    }

    public int getAiIdentifiedAccessPoints() {
        return aiIdentifiedAccessPoints;
    }

    public void setAiIdentifiedAccessPoints(int aiIdentifiedAccessPoints) {
        this.aiIdentifiedAccessPoints = aiIdentifiedAccessPoints;
    }
}
