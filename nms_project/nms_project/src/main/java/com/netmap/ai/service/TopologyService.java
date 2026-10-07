package com.netmap.ai.service;

import com.netmap.ai.ai.DeviceRoleAIService;
import com.netmap.ai.model.*;
import com.netmap.ai.simulator.NetworkSimulator;
import org.springframework.stereotype.Service;

import jakarta.annotation.PostConstruct;
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import java.util.stream.Collectors;

@Service
public class TopologyService {

    private final NetworkSimulator simulator;
    private final DeviceRoleAIService aiService;

    private NetworkTopology currentTopology;
    private AnalysisResult currentAnalysisResult;
    private final Map<String, Device> deviceCache = new ConcurrentHashMap<>();

    public TopologyService(NetworkSimulator simulator, DeviceRoleAIService aiService) {
        this.simulator = simulator;
        this.aiService = aiService;
    }

    @PostConstruct
    public void init() {
        // Initialize with default 10-device network on startup
        generateNetwork(10);
    }

    public synchronized NetworkTopology generateNetwork(int count) {
        NetworkTopology topology = simulator.generateTopology(count);

        // Run AI Role Mapping on all devices
        List<DeviceAnalysis> analyses = new ArrayList<>();
        int routers = 0, switches = 0, servers = 0, clients = 0, aps = 0;

        for (Device d : topology.getDevices()) {
            DeviceAnalysis analysis = aiService.analyzeDevice(d, topology.getDevices(), topology.getConnections());
            if (analysis != null) {
                analyses.add(analysis);
                String pred = analysis.getPredictedRole();
                if ("Router".equalsIgnoreCase(pred)) routers++;
                else if ("Switch".equalsIgnoreCase(pred)) switches++;
                else if ("Server".equalsIgnoreCase(pred)) servers++;
                else if ("Client".equalsIgnoreCase(pred)) clients++;
                else if ("Access Point".equalsIgnoreCase(pred)) aps++;
            }
        }

        AnalysisResult result = new AnalysisResult();
        result.setConnected(true);
        result.setTotalDevices(topology.getDevices().size());
        result.setTotalConnections(topology.getConnections().size());
        result.setIsolatedDeviceCount(0);
        result.setMessage("Topology successfully connected.");
        result.setAnalyses(analyses);
        result.setAiIdentifiedRouters(routers);
        result.setAiIdentifiedSwitches(switches);
        result.setAiIdentifiedServers(servers);
        result.setAiIdentifiedClients(clients);
        result.setAiIdentifiedAccessPoints(aps);

        this.currentAnalysisResult = result;
        this.currentTopology = topology;

        deviceCache.clear();
        for (Device d : topology.getDevices()) {
            deviceCache.put(d.getId(), d);
        }

        return currentTopology;
    }

    public synchronized NetworkTopology getTopology() {
        if (currentTopology == null) {
            generateNetwork(10);
        }
        return currentTopology;
    }

    public synchronized void setTopology(NetworkTopology topology) {
        this.currentTopology = topology;
        deviceCache.clear();
        if (topology != null && topology.getDevices() != null) {
            for (Device d : topology.getDevices()) {
                deviceCache.put(d.getId(), d);
            }
        }
    }

    public synchronized List<Device> getDevices() {
        if (currentTopology == null) return Collections.emptyList();
        return new ArrayList<>(currentTopology.getDevices());
    }

    public Device getDevice(String id) {
        if (id == null) return null;
        return deviceCache.get(id);
    }

    public List<Device> searchDevices(String name) {
        if (name == null || name.trim().isEmpty() || currentTopology == null) {
            return Collections.emptyList();
        }
        String q = name.trim().toLowerCase();
        return currentTopology.getDevices().stream()
                .filter(d -> d.getName().toLowerCase().contains(q) ||
                             d.getId().toLowerCase().contains(q) ||
                             (d.getIpAddress() != null && d.getIpAddress().contains(q)))
                .collect(Collectors.toList());
    }

    public synchronized NetworkStatistics getStatistics() {
        NetworkStatistics stats = new NetworkStatistics();
        if (currentTopology == null) return stats;

        List<Device> devices = currentTopology.getDevices();
        List<Connection> connections = currentTopology.getConnections();

        stats.setTotalDevices(devices.size());
        stats.setTotalConnections(connections.size());

        int routers = 0, switches = 0, servers = 0, clients = 0, aps = 0, internet = 0;
        int active = 0, inactive = 0;

        for (Device d : devices) {
            if ("Active".equalsIgnoreCase(d.getStatus())) active++;
            else inactive++;

            if (d.getType() != null) {
                switch (d.getType()) {
                    case ROUTER -> routers++;
                    case SWITCH -> switches++;
                    case SERVER -> servers++;
                    case PC -> clients++;
                    case ACCESS_POINT -> aps++;
                    case INTERNET -> internet++;
                }
            }
        }

        stats.setRouterCount(routers);
        stats.setSwitchCount(switches);
        stats.setServerCount(servers);
        stats.setClientCount(clients);
        stats.setAccessPointCount(aps);
        stats.setInternetCount(internet);
        stats.setActiveCount(active);
        stats.setInactiveCount(inactive);

        return stats;
    }

    public synchronized AnalysisResult getAiAnalysis() {
        if (currentAnalysisResult == null && currentTopology != null) {
            runAiAnalysisOnCurrent();
        }
        return currentAnalysisResult;
    }

    public synchronized void setAnalysisResult(AnalysisResult result) {
        this.currentAnalysisResult = result;
    }

    public synchronized AnalysisResult runAiAnalysisOnCurrent() {
        if (currentTopology == null) return new AnalysisResult();

        simulator.updateDeviceConnectionsMetadata(currentTopology.getDevices(), currentTopology.getConnections());

        List<DeviceAnalysis> analyses = new ArrayList<>();
        int routers = 0, switches = 0, servers = 0, clients = 0, aps = 0;

        for (Device d : currentTopology.getDevices()) {
            DeviceAnalysis analysis = aiService.analyzeDevice(d, currentTopology.getDevices(), currentTopology.getConnections());
            if (analysis != null) {
                analyses.add(analysis);
                String pred = analysis.getPredictedRole();
                if ("Router".equalsIgnoreCase(pred)) routers++;
                else if ("Switch".equalsIgnoreCase(pred)) switches++;
                else if ("Server".equalsIgnoreCase(pred)) servers++;
                else if ("Client".equalsIgnoreCase(pred)) clients++;
                else if ("Access Point".equalsIgnoreCase(pred)) aps++;
            }
        }

        AnalysisResult result = new AnalysisResult();
        result.setTotalDevices(currentTopology.getDevices().size());
        result.setTotalConnections(currentTopology.getConnections().size());

        // Check for isolated devices
        List<String> isolated = new ArrayList<>();
        for (Device d : currentTopology.getDevices()) {
            if (d.getConnectionsCount() == 0) {
                isolated.add(d.getName());
            }
        }

        result.setIsolatedDeviceCount(isolated.size());
        result.setIsolatedDeviceNames(isolated);
        result.setConnected(isolated.isEmpty() && currentTopology.getDevices().size() > 1);

        if (!isolated.isEmpty()) {
            result.setMessage(isolated.size() + " device(s) are not connected to the network.");
        } else {
            result.setMessage("Topology successfully connected.");
        }

        result.setAnalyses(analyses);
        result.setAiIdentifiedRouters(routers);
        result.setAiIdentifiedSwitches(switches);
        result.setAiIdentifiedServers(servers);
        result.setAiIdentifiedClients(clients);
        result.setAiIdentifiedAccessPoints(aps);

        this.currentAnalysisResult = result;
        return result;
    }

    public synchronized boolean updateDeviceStatus(String id, String status) {
        Device d = deviceCache.get(id);
        if (d != null) {
            d.setStatus(status);
            return true;
        }
        return false;
    }

    public synchronized void reset() {
        generateNetwork(5);
    }
}
