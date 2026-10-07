package com.netmap.ai.controller;

import com.netmap.ai.model.*;
import com.netmap.ai.service.ManualDesignService;
import com.netmap.ai.service.TopologyService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/network")
public class NetworkController {

    private final TopologyService topologyService;
    private final ManualDesignService manualDesignService;

    public NetworkController(TopologyService topologyService, ManualDesignService manualDesignService) {
        this.topologyService = topologyService;
        this.manualDesignService = manualDesignService;
    }

    @PostMapping("/generate")
    public ResponseEntity<NetworkTopology> generate(@RequestBody GenerateRequest request) {
        int count = (request != null && request.getCount() >= 5) ? request.getCount() : 10;
        NetworkTopology topology = topologyService.generateNetwork(count);
        // Also populate manual designer so user can switch seamlessly to manual mode
        manualDesignService.initializeFromTopology(topology);
        return ResponseEntity.ok(topology);
    }

    @GetMapping("/topology")
    public ResponseEntity<NetworkTopology> getTopology() {
        return ResponseEntity.ok(topologyService.getTopology());
    }

    @GetMapping("/devices")
    public ResponseEntity<List<Device>> getDevices() {
        return ResponseEntity.ok(topologyService.getDevices());
    }

    @GetMapping("/devices/{id}")
    public ResponseEntity<Device> getDevice(@PathVariable String id) {
        Device device = topologyService.getDevice(id);
        if (device != null) {
            return ResponseEntity.ok(device);
        }
        return ResponseEntity.notFound().build();
    }

    @GetMapping("/statistics")
    public ResponseEntity<NetworkStatistics> getStatistics() {
        return ResponseEntity.ok(topologyService.getStatistics());
    }

    @GetMapping("/search")
    public ResponseEntity<List<Device>> search(@RequestParam(name = "name", defaultValue = "") String name) {
        return ResponseEntity.ok(topologyService.searchDevices(name));
    }

    @PostMapping("/reset")
    public ResponseEntity<NetworkTopology> reset() {
        topologyService.reset();
        manualDesignService.initializeFromTopology(topologyService.getTopology());
        return ResponseEntity.ok(topologyService.getTopology());
    }

    // --- MANUAL DESIGN ENDPOINTS ---

    @PostMapping("/manual/device")
    public ResponseEntity<Device> addManualDevice(@RequestBody ManualDeviceRequest request) {
        Device device = manualDesignService.addDevice(request);
        return ResponseEntity.ok(device);
    }

    @PutMapping("/manual/device/{id}")
    public ResponseEntity<?> updateManualDevice(@PathVariable String id, @RequestBody Map<String, Object> updates) {
        String name = updates.containsKey("name") ? (String) updates.get("name") : null;
        String status = updates.containsKey("status") ? (String) updates.get("status") : null;
        Double x = updates.containsKey("x") ? Double.valueOf(updates.get("x").toString()) : null;
        Double y = updates.containsKey("y") ? Double.valueOf(updates.get("y").toString()) : null;

        boolean updated = manualDesignService.updateDevice(id, name, x, y, status);
        if (updated) {
            topologyService.updateDeviceStatus(id, status);
            return ResponseEntity.ok(Map.of("success", true, "message", "Device updated"));
        }
        return ResponseEntity.notFound().build();
    }

    @DeleteMapping("/manual/device/{id}")
    public ResponseEntity<?> deleteManualDevice(@PathVariable String id) {
        boolean deleted = manualDesignService.deleteDevice(id);
        return ResponseEntity.ok(Map.of("success", deleted));
    }

    @PostMapping("/manual/connection")
    public ResponseEntity<Connection> addManualConnection(@RequestBody ManualConnectionRequest request) {
        Connection conn = manualDesignService.addConnection(request);
        if (conn != null) {
            return ResponseEntity.ok(conn);
        }
        return ResponseEntity.badRequest().build();
    }

    @DeleteMapping("/manual/connection/{id}")
    public ResponseEntity<?> deleteManualConnection(@PathVariable String id) {
        boolean deleted = manualDesignService.deleteConnection(id);
        return ResponseEntity.ok(Map.of("success", deleted));
    }

    @PostMapping("/manual/clear")
    public ResponseEntity<?> clearManualDesign() {
        manualDesignService.clearDesign();
        return ResponseEntity.ok(Map.of("success", true, "message", "Canvas cleared"));
    }

    @PostMapping("/manual/save")
    public ResponseEntity<NetworkTopology> saveManualDesign() {
        NetworkTopology saved = manualDesignService.saveDesign();
        return ResponseEntity.ok(saved);
    }

    @PostMapping("/manual/analyze")
    public ResponseEntity<AnalysisResult> analyzeManualDesign() {
        AnalysisResult result = manualDesignService.analyzeDesign();
        return ResponseEntity.ok(result);
    }

    @GetMapping("/ai-analysis")
    public ResponseEntity<AnalysisResult> getAiAnalysis() {
        return ResponseEntity.ok(topologyService.getAiAnalysis());
    }
}
