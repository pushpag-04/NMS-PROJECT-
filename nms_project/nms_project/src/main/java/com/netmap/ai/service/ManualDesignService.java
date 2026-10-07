package com.netmap.ai.service;

import com.netmap.ai.model.*;
import com.netmap.ai.simulator.NetworkSimulator;
import org.springframework.stereotype.Service;

import java.util.*;
import java.util.concurrent.atomic.AtomicInteger;

@Service
public class ManualDesignService {

    private final TopologyService topologyService;
    private final NetworkSimulator simulator;

    private final List<Device> manualDevices = new ArrayList<>();
    private final List<Connection> manualConnections = new ArrayList<>();
    private final AtomicInteger idCounter = new AtomicInteger(1);
    private final AtomicInteger connCounter = new AtomicInteger(1);

    private final Map<String, Integer> typeCounters = new HashMap<>();

    public ManualDesignService(TopologyService topologyService, NetworkSimulator simulator) {
        this.topologyService = topologyService;
        this.simulator = simulator;
        resetCounters();
    }

    private void resetCounters() {
        typeCounters.put("INTERNET", 1);
        typeCounters.put("ROUTER", 1);
        typeCounters.put("SWITCH", 1);
        typeCounters.put("SERVER", 1);
        typeCounters.put("PC", 1);
        typeCounters.put("ACCESS_POINT", 1);
    }

    public synchronized Device addDevice(ManualDeviceRequest request) {
        DeviceType type = DeviceType.fromString(request.getType());
        String typeKey = type.name();
        int num = typeCounters.getOrDefault(typeKey, 1);
        typeCounters.put(typeKey, num + 1);

        String defaultName = switch (type) {
            case INTERNET -> "Internet";
            case ROUTER -> String.format("Router-%02d", num);
            case SWITCH -> String.format("Switch-%02d", num);
            case SERVER -> String.format("Server-%02d", num);
            case ACCESS_POINT -> String.format("AP-%02d", num);
            case PC -> String.format("PC-%02d", num);
        };

        String name = (request.getName() != null && !request.getName().trim().isEmpty())
                ? request.getName().trim() : defaultName;

        String id = "manual-" + type.name().toLowerCase() + "-" + idCounter.getAndIncrement();
        String ip = generateIpForType(type, num);
        String mac = String.format("02:00:%02X:%02X:%02X:%02X",
                type.ordinal(), num, (int)(Math.random() * 255), (int)(Math.random() * 255));

        Device device = new Device(id, name, type, ip, mac);
        device.setX(request.getX());
        device.setY(request.getY());
        device.setStatus("Active");
        device.setOpenPortsCount(type.getDefaultOpenPorts());

        manualDevices.add(device);
        simulator.updateDeviceConnectionsMetadata(manualDevices, manualConnections);
        syncToTopologyService();
        return device;
    }

    private String generateIpForType(DeviceType type, int num) {
        return switch (type) {
            case INTERNET -> "203.0.113.1";
            case ROUTER -> String.format("192.168.%d.1", num);
            case SWITCH -> String.format("192.168.1.%d", 10 + num);
            case SERVER -> String.format("192.168.1.%d", 100 + num);
            case ACCESS_POINT -> String.format("192.168.1.%d", 50 + num);
            case PC -> String.format("192.168.1.%d", 150 + num);
        };
    }

    public synchronized boolean updateDevice(String id, String newName, Double x, Double y, String status) {
        for (Device d : manualDevices) {
            if (d.getId().equals(id)) {
                if (newName != null && !newName.trim().isEmpty()) {
                    d.setName(newName.trim());
                }
                if (x != null) d.setX(x);
                if (y != null) d.setY(y);
                if (status != null) d.setStatus(status);

                simulator.updateDeviceConnectionsMetadata(manualDevices, manualConnections);
                syncToTopologyService();
                return true;
            }
        }
        return false;
    }

    public synchronized boolean deleteDevice(String id) {
        boolean removed = manualDevices.removeIf(d -> d.getId().equals(id));
        if (removed) {
            manualConnections.removeIf(c -> c.getSourceDeviceId().equals(id) || c.getTargetDeviceId().equals(id));
            simulator.updateDeviceConnectionsMetadata(manualDevices, manualConnections);
            syncToTopologyService();
        }
        return removed;
    }

    public synchronized Connection addConnection(ManualConnectionRequest req) {
        if (req.getSourceDeviceId() == null || req.getTargetDeviceId() == null) {
            return null;
        }
        if (req.getSourceDeviceId().equals(req.getTargetDeviceId())) {
            return null; // No self-loops
        }

        // Check if connection already exists
        for (Connection c : manualConnections) {
            if ((c.getSourceDeviceId().equals(req.getSourceDeviceId()) && c.getTargetDeviceId().equals(req.getTargetDeviceId())) ||
                (c.getSourceDeviceId().equals(req.getTargetDeviceId()) && c.getTargetDeviceId().equals(req.getSourceDeviceId()))) {
                return c; // Already connected
            }
        }

        String connId = "manual-conn-" + connCounter.getAndIncrement();
        String cableType = req.getCableType() != null ? req.getCableType() : "Ethernet";
        Connection conn = new Connection(connId, req.getSourceDeviceId(), req.getTargetDeviceId(), cableType);

        manualConnections.add(conn);
        simulator.updateDeviceConnectionsMetadata(manualDevices, manualConnections);
        syncToTopologyService();
        return conn;
    }

    public synchronized boolean deleteConnection(String id) {
        boolean removed = manualConnections.removeIf(c -> c.getId().equals(id));
        if (removed) {
            simulator.updateDeviceConnectionsMetadata(manualDevices, manualConnections);
            syncToTopologyService();
        }
        return removed;
    }

    public synchronized void clearDesign() {
        manualDevices.clear();
        manualConnections.clear();
        resetCounters();
        syncToTopologyService();
    }

    public synchronized NetworkTopology saveDesign() {
        syncToTopologyService();
        return topologyService.getTopology();
    }

    public synchronized AnalysisResult analyzeDesign() {
        syncToTopologyService();
        return topologyService.runAiAnalysisOnCurrent();
    }

    public synchronized void initializeFromTopology(NetworkTopology topology) {
        manualDevices.clear();
        manualConnections.clear();
        if (topology != null) {
            manualDevices.addAll(topology.getDevices());
            manualConnections.addAll(topology.getConnections());
        }
    }

    private void syncToTopologyService() {
        NetworkTopology topology = new NetworkTopology(
                new ArrayList<>(manualDevices),
                new ArrayList<>(manualConnections),
                "MANUAL"
        );
        topologyService.setTopology(topology);
    }

    public synchronized List<Device> getManualDevices() {
        return new ArrayList<>(manualDevices);
    }

    public synchronized List<Connection> getManualConnections() {
        return new ArrayList<>(manualConnections);
    }
}
