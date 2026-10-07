package com.netmap.ai.simulator;

import com.netmap.ai.model.*;
import org.springframework.stereotype.Component;

import java.util.*;

@Component
public class NetworkSimulator {

    public NetworkTopology generateTopology(int deviceCount) {
        if (deviceCount < 5) deviceCount = 5;
        if (deviceCount > 50) deviceCount = 50;

        List<Device> devices = new ArrayList<>();
        List<Connection> connections = new ArrayList<>();

        int connCounter = 1;

        // 1. Always 1 Internet Gateway
        Device internet = new Device(
                "dev-internet",
                "Internet",
                DeviceType.INTERNET,
                "203.0.113.1",
                "00:1B:77:AA:01:01"
        );
        internet.setTrafficKbps(9800);
        internet.setPacketRatePps(3400);
        devices.add(internet);

        // Calculate device distribution ensuring exact sum = deviceCount
        int remaining = deviceCount - 1; // excluding internet

        int routerCount;
        int switchCount;
        int serverCount;
        int apCount;
        int pcCount;

        if (deviceCount == 5) {
            routerCount = 1;
            switchCount = 1;
            serverCount = 1;
            apCount = 0;
            pcCount = 1;
        } else if (deviceCount <= 10) {
            routerCount = 1;
            switchCount = 2;
            serverCount = 1;
            apCount = 1;
            pcCount = remaining - (routerCount + switchCount + serverCount + apCount);
        } else if (deviceCount <= 20) {
            routerCount = 2;
            switchCount = 3;
            serverCount = 2;
            apCount = 2;
            pcCount = remaining - (routerCount + switchCount + serverCount + apCount);
        } else if (deviceCount <= 35) {
            routerCount = 3;
            switchCount = 5;
            serverCount = 3;
            apCount = 3;
            pcCount = remaining - (routerCount + switchCount + serverCount + apCount);
        } else {
            routerCount = 4;
            switchCount = 7;
            serverCount = 5;
            apCount = 4;
            pcCount = remaining - (routerCount + switchCount + serverCount + apCount);
        }

        // Adjust if pcCount < 1
        if (pcCount < 1) {
            pcCount = 1;
            if (apCount > 1) apCount--;
            else if (serverCount > 1) serverCount--;
            else if (switchCount > 1) switchCount--;
        }

        // Final sanity adjustment so devices.size() == deviceCount
        int currentTotalWithoutPcs = 1 + routerCount + switchCount + serverCount + apCount;
        pcCount = deviceCount - currentTotalWithoutPcs;

        // Create Routers
        List<Device> routers = new ArrayList<>();
        for (int i = 1; i <= routerCount; i++) {
            String name = String.format("Router-%02d", i);
            String id = "dev-router-" + i;
            String ip = String.format("192.168.%d.1", i);
            String mac = String.format("00:0A:95:9D:%02X:%02X", i, i * 2);
            Device router = new Device(id, name, DeviceType.ROUTER, ip, mac);
            router.setTrafficKbps(4500 + i * 200);
            router.setPacketRatePps(1200 + i * 50);
            devices.add(router);
            routers.add(router);
        }

        // Connect Internet to Router-01
        connections.add(new Connection(
                "conn-" + (connCounter++),
                internet.getId(),
                routers.get(0).getId(),
                "Fiber"
        ));

        // If multiple routers, connect them hierarchically or in a ring
        for (int i = 1; i < routers.size(); i++) {
            connections.add(new Connection(
                "conn-" + (connCounter++),
                routers.get(i - 1).getId(),
                routers.get(i).getId(),
                "Fiber"
            ));
        }

        // Create Switches
        List<Device> switches = new ArrayList<>();
        for (int i = 1; i <= switchCount; i++) {
            String name = String.format("Switch-%02d", i);
            String id = "dev-switch-" + i;
            String ip = String.format("192.168.1.%d", 10 + i);
            String mac = String.format("00:1E:13:B4:%02X:%02X", i, i * 3);
            Device sw = new Device(id, name, DeviceType.SWITCH, ip, mac);
            sw.setTrafficKbps(3000 + i * 150);
            sw.setPacketRatePps(1400 + i * 80);
            devices.add(sw);
            switches.add(sw);

            // Connect switch to a router
            Device targetRouter = routers.get((i - 1) % routers.size());
            connections.add(new Connection(
                    "conn-" + (connCounter++),
                    targetRouter.getId(),
                    sw.getId(),
                    "Ethernet"
            ));
        }

        // If multiple switches, link pairs for backbone trunk
        if (switches.size() >= 2) {
            connections.add(new Connection(
                    "conn-" + (connCounter++),
                    switches.get(0).getId(),
                    switches.get(1).getId(),
                    "Ethernet"
            ));
        }
        if (switches.size() >= 4) {
            connections.add(new Connection(
                    "conn-" + (connCounter++),
                    switches.get(2).getId(),
                    switches.get(3).getId(),
                    "Ethernet"
            ));
        }

        // Create Servers
        List<Device> servers = new ArrayList<>();
        String[] serverPrefixes = {"Web", "DB", "DNS", "Mail", "File", "App", "Backup"};
        for (int i = 1; i <= serverCount; i++) {
            String prefix = serverPrefixes[(i - 1) % serverPrefixes.length];
            String name = String.format("Server-%02d (%s)", i, prefix);
            String id = "dev-server-" + i;
            String ip = String.format("192.168.1.%d", 100 + i);
            String mac = String.format("00:50:56:A1:%02X:%02X", i, i * 4);
            Device srv = new Device(id, name, DeviceType.SERVER, ip, mac);
            srv.setTrafficKbps(5500 + i * 300);
            srv.setPacketRatePps(800 + i * 40);
            devices.add(srv);
            servers.add(srv);

            // Connect to switch
            Device targetSwitch = switches.get((i - 1) % switches.size());
            connections.add(new Connection(
                    "conn-" + (connCounter++),
                    targetSwitch.getId(),
                    srv.getId(),
                    "Ethernet"
            ));
        }

        // Create Access Points
        List<Device> aps = new ArrayList<>();
        for (int i = 1; i <= apCount; i++) {
            String name = String.format("AP-%02d", i);
            String id = "dev-ap-" + i;
            String ip = String.format("192.168.1.%d", 50 + i);
            String mac = String.format("00:26:86:C3:%02X:%02X", i, i * 5);
            Device ap = new Device(id, name, DeviceType.ACCESS_POINT, ip, mac);
            ap.setTrafficKbps(1800 + i * 100);
            ap.setPacketRatePps(450 + i * 30);
            devices.add(ap);
            aps.add(ap);

            // Connect AP to a switch
            Device targetSwitch = switches.get((i - 1) % switches.size());
            connections.add(new Connection(
                    "conn-" + (connCounter++),
                    targetSwitch.getId(),
                    ap.getId(),
                    "Ethernet"
            ));
        }

        // Create PCs / Clients
        List<Device> pcs = new ArrayList<>();
        for (int i = 1; i <= pcCount; i++) {
            String name = String.format("PC-%02d", i);
            String id = "dev-pc-" + i;
            String ip = String.format("192.168.1.%d", 150 + i);
            String mac = String.format("00:15:5D:8E:%02X:%02X", i, i * 7);
            Device pc = new Device(id, name, DeviceType.PC, ip, mac);
            pc.setTrafficKbps(350 + (i % 5) * 50);
            pc.setPacketRatePps(80 + (i % 4) * 20);
            devices.add(pc);
            pcs.add(pc);

            // If APs exist, distribute some PCs wirelessly to APs and some to switches
            if (!aps.isEmpty() && (i % 2 == 0 || switches.isEmpty())) {
                Device targetAp = aps.get((i / 2) % aps.size());
                connections.add(new Connection(
                        "conn-" + (connCounter++),
                        targetAp.getId(),
                        pc.getId(),
                        "Wireless"
                ));
            } else {
                Device targetSwitch = switches.get((i - 1) % switches.size());
                connections.add(new Connection(
                        "conn-" + (connCounter++),
                        targetSwitch.getId(),
                        pc.getId(),
                        "Ethernet"
                ));
            }
        }

        // Update connection lists and metadata for every device
        updateDeviceConnectionsMetadata(devices, connections);

        return new NetworkTopology(devices, connections, "AUTOMATIC");
    }

    public void updateDeviceConnectionsMetadata(List<Device> devices, List<Connection> connections) {
        Map<String, Device> map = new HashMap<>();
        for (Device d : devices) {
            d.getConnectedDeviceIds().clear();
            d.getConnectedDeviceNames().clear();
            map.put(d.getId(), d);
        }

        for (Connection c : connections) {
            Device src = map.get(c.getSourceDeviceId());
            Device tgt = map.get(c.getTargetDeviceId());
            if (src != null && tgt != null) {
                c.setSourceDeviceName(src.getName());
                c.setTargetDeviceName(tgt.getName());

                if (!src.getConnectedDeviceIds().contains(tgt.getId())) {
                    src.getConnectedDeviceIds().add(tgt.getId());
                    src.getConnectedDeviceNames().add(tgt.getName());
                }
                if (!tgt.getConnectedDeviceIds().contains(src.getId())) {
                    tgt.getConnectedDeviceIds().add(src.getId());
                    tgt.getConnectedDeviceNames().add(src.getName());
                }
            }
        }

        for (Device d : devices) {
            d.setConnectionsCount(d.getConnectedDeviceIds().size());
        }
    }
}
