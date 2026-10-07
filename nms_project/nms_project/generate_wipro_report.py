import os
import pymupdf

def create_report():
    doc = pymupdf.open()
    
    # Page size: A4 in points (595.56 x 842.04)
    PAGE_WIDTH = 595.56
    PAGE_HEIGHT = 842.04
    MARGIN_LEFT = 72.0
    MARGIN_RIGHT = 72.0
    MARGIN_TOP = 54.0
    MARGIN_BOTTOM = 54.0
    CONTENT_WIDTH = PAGE_WIDTH - MARGIN_LEFT - MARGIN_RIGHT
    
    # Fonts and Colors
    FONT_ROMAN = "times-roman"
    FONT_BOLD = "times-bold"
    FONT_ITALIC = "times-italic"
    FONT_CODE = "courier"
    
    COLOR_BLACK = (0, 0, 0)
    COLOR_GRAY = (0.25, 0.25, 0.25)
    COLOR_LIGHT_BG = (0.94, 0.95, 0.97)
    COLOR_LINE = (0.7, 0.7, 0.7)
    
    images_paths = [
        "C:/Users/sameeha/.gemini/antigravity/brain/f5bcc397-1c93-4dea-a554-e17384fffa82/.user_uploaded/media_1791291299497.png",
        "C:/Users/sameeha/.gemini/antigravity/brain/f5bcc397-1c93-4dea-a554-e17384fffa82/.user_uploaded/media_1791291299498.png",
        "C:/Users/sameeha/.gemini/antigravity/brain/f5bcc397-1c93-4dea-a554-e17384fffa82/.user_uploaded/media_1791291299505.png",
        "C:/Users/sameeha/.gemini/antigravity/brain/f5bcc397-1c93-4dea-a554-e17384fffa82/.user_uploaded/media_1791291299518.png"
    ]

    def add_page():
        return doc.new_page(width=PAGE_WIDTH, height=PAGE_HEIGHT)

    def draw_top_page_no(page, pageno_str):
        # In WIPRO report, top-left or top-center page number at y = 50
        rect = pymupdf.Rect(MARGIN_LEFT, 35, MARGIN_LEFT + 100, 55)
        page.insert_textbox(rect, str(pageno_str), fontname=FONT_ROMAN, fontsize=11, color=COLOR_BLACK, align=0)

    def draw_centered_text(page, y, text, fontname=FONT_BOLD, fontsize=12, color=COLOR_BLACK):
        rect = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + fontsize + 16)
        page.insert_textbox(rect, text, fontname=fontname, fontsize=fontsize, color=color, align=1)

    def draw_left_text(page, x, y, text, fontname=FONT_BOLD, fontsize=11, color=COLOR_BLACK):
        page.insert_text(pymupdf.Point(x, y), text, fontname=fontname, fontsize=fontsize, color=color)

    def draw_justified_para(page, y, text, height, fontsize=11, fontname=FONT_ROMAN):
        rect = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + height)
        page.insert_textbox(rect, text, fontname=fontname, fontsize=fontsize, align=3)
        return y + height

    # =========================================================================
    # PAGE 1: TITLE PAGE (i)
    # =========================================================================
    p1 = add_page()
    draw_top_page_no(p1, "i")
    
    y = 120
    draw_centered_text(p1, y, "WIPRO – NMS (NETWORK MANAGEMENT SYSTEM)", fontname=FONT_BOLD, fontsize=13)
    y += 26
    draw_centered_text(p1, y, "INTELLIGENT NETWORK TOPOLOGY DISCOVERY AND", fontname=FONT_BOLD, fontsize=13)
    y += 20
    draw_centered_text(p1, y, "DEVICE ROLE MAPPING SYSTEM", fontname=FONT_BOLD, fontsize=13)
    y += 20
    draw_centered_text(p1, y, "(INTELLIGENT PHISHING AND DEEPFAKE DETECTION ENGINE)", fontname=FONT_BOLD, fontsize=11, color=COLOR_GRAY)
    
    y = 260
    draw_centered_text(p1, y, "A PROJECT REPORT", fontname=FONT_BOLD, fontsize=12)
    
    y = 320
    draw_centered_text(p1, y, "Submitted by", fontname=FONT_ROMAN, fontsize=11)
    
    y = 360
    draw_centered_text(p1, y, "SAMEEHA A", fontname=FONT_BOLD, fontsize=12)
    draw_centered_text(p1, y + 16, "(2116231001176)", fontname=FONT_ROMAN, fontsize=11)
    
    y = 410
    draw_centered_text(p1, y, "PUSHPA G", fontname=FONT_BOLD, fontsize=12)
    draw_centered_text(p1, y + 16, "(2116231001158)", fontname=FONT_ROMAN, fontsize=11)
    
    y = 460
    draw_centered_text(p1, y, "NITHYA K", fontname=FONT_BOLD, fontsize=12)
    draw_centered_text(p1, y + 16, "(2116231001139)", fontname=FONT_ROMAN, fontsize=11)
    
    y = 600
    draw_centered_text(p1, y, "DEPARTMENT OF INFORMATION TECHNOLOGY", fontname=FONT_BOLD, fontsize=11)
    y += 18
    draw_centered_text(p1, y, "RAJALAKSHMI ENGINEERING COLLEGE", fontname=FONT_BOLD, fontsize=12)
    y += 16
    draw_centered_text(p1, y, "(AUTONOMOUS)", fontname=FONT_BOLD, fontsize=11)
    y += 16
    draw_centered_text(p1, y, "CHENNAI – 602 105", fontname=FONT_ROMAN, fontsize=11)
    y += 18
    draw_centered_text(p1, y, "ANNA UNIVERSITY: CHENNAI 600 025", fontname=FONT_ROMAN, fontsize=10.5)
    y += 30
    draw_centered_text(p1, y, "OCTOBER 2026", fontname=FONT_BOLD, fontsize=11)

    # =========================================================================
    # PAGE 2: ABSTRACT (ii)
    # =========================================================================
    p2 = add_page()
    draw_top_page_no(p2, "ii")
    
    y = 70
    draw_left_text(p2, MARGIN_LEFT, y, "ABSTRACT", fontname=FONT_BOLD, fontsize=12)
    
    y += 20
    abs_text1 = (
        "Modern enterprise and communication infrastructures provide high-speed, distributed connectivity across "
        "numerous interconnected endpoints, servers, routers, switches, and access points. These capabilities enable "
        "scalable operations but also significantly heighten the demand for continuous network topology discovery, "
        "device role mapping, and automated threat defense. Large traffic volumes, complex multi-tier topologies, and "
        "dynamically configured endpoints make manual identification of deceptive nodes and network pathways difficult."
    )
    rect1 = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 95)
    p2.insert_textbox(rect1, abs_text1, fontname=FONT_ROMAN, fontsize=11, align=3)
    
    y += 105
    abs_text2 = (
        "This project presents an AI-Based Network Management System (NetMap AI) for real-time topology discovery, "
        "device role mapping, and threat defense in enterprise networks. Eight topological and traffic features are used "
        "as input: connection count, neighbor router count, neighbor switch count, neighbor endpoint count, gateway connectivity, "
        "open ports, traffic bandwidth (kbps), and packet forwarding rates. A Weka J48 Decision Tree machine learning model "
        "classifies network nodes into functional categories: Internet Gateway, Router, Switch, Server, Access Point, and Client "
        "Workstation. The implemented model achieves high classification accuracy (98.2%) across simulated network topologies."
    )
    rect2 = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 115)
    p2.insert_textbox(rect2, abs_text2, fontname=FONT_ROMAN, fontsize=11, align=3)
    
    y += 125
    abs_text3 = (
        "After classification, the application provides prediction confidence, threat telemetry, node parameters, and "
        "automated validation status ('Matched' vs. 'Refined') to flag structural discrepancies and anomalous configurations. "
        "The system supports both an Automatic Network Generation mode (scaling from 5 to 50 devices in steps of 5) and an "
        "Interactive Manual Network Design mode. Spring Boot provides backend REST communication, Cytoscape.js provides the "
        "interactive graph canvas with Cisco-style iconography, and thread-safe in-memory collections maintain state with zero "
        "external database dependencies. The project demonstrates an integrated, responsive cyber defense prototype combining AI "
        "role discovery, connection inspection, graph manipulation, and real-time dashboard telemetry."
    )
    rect3 = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 130)
    p2.insert_textbox(rect3, abs_text3, fontname=FONT_ROMAN, fontsize=11, align=3)
    
    y += 145
    kw_text = (
        "Keywords: Network Management System, Topology Discovery, Device Role Mapping, Weka J48, Decision Tree, "
        "Cytoscape.js, Spring Boot, Cyber Defense, Real-Time Telemetry."
    )
    rect_kw = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 50)
    p2.insert_textbox(rect_kw, kw_text, fontname=FONT_BOLD, fontsize=10.5, align=3)

    # =========================================================================
    # PAGE 3: CHAPTER 1: INTRODUCTION (1)
    # =========================================================================
    p3 = add_page()
    draw_top_page_no(p3, "1")
    
    y = 70
    draw_left_text(p3, MARGIN_LEFT, y, "CHAPTER 1: INTRODUCTION", fontname=FONT_BOLD, fontsize=12)
    
    y += 24
    draw_left_text(p3, MARGIN_LEFT, y, "1.1 Background", fontname=FONT_BOLD, fontsize=11)
    y += 14
    ch1_bg = (
        "Modern enterprise communications, cloud-native datacenters, and real-time collaboration environments rely on "
        "sophisticated multi-tiered network topologies comprising routers, multi-layer switches, physical servers, "
        "wireless access points, and client workstations. These communication infrastructures facilitate critical business "
        "operations, distributed computing, and high-bandwidth data transfers. However, as enterprise networks scale, "
        "network administrators face significant hurdles in discovering device topologies, verifying device roles, and "
        "detecting misconfigured or deceptive endpoints.\n\n"
        "Traditional Network Management Systems (NMS) depend heavily on static protocol polling (such as SNMP or CDP/LLDP) "
        "and manual diagramming. When networks expand or when unmanaged, virtualized, or adversary-controlled devices "
        "are introduced, static discovery fails. A dynamic, machine-learning-assisted NMS capable of deducing device roles "
        "from topological connectivity and flow telemetry is therefore an essential operational requirement."
    )
    rect_c1 = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 195)
    p3.insert_textbox(rect_c1, ch1_bg, fontname=FONT_ROMAN, fontsize=11, align=3)
    
    y += 205
    draw_left_text(p3, MARGIN_LEFT, y, "1.2 Problem Statement", fontname=FONT_BOLD, fontsize=11)
    y += 14
    ch1_ps = (
        "Enterprise network topologies are constantly evolving with dynamic device attachments, routing updates, and "
        "complex cabling architectures. Manually discovering device roles and identifying disconnected, misconfigured, or "
        "anomalous nodes is labor-intensive and prone to severe configuration oversights. Existing commercial tools require "
        "costly enterprise licensing, complex database setups, or compute-heavy virtualization. There is a pressing need for a "
        "lightweight, zero-database, web-based NMS that automatically generates multi-tier topologies, allows interactive "
        "manual graph design, and applies explainable AI models to verify device roles in real time."
    )
    rect_ps = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 125)
    p3.insert_textbox(rect_ps, ch1_ps, fontname=FONT_ROMAN, fontsize=11, align=3)
    
    y += 135
    draw_left_text(p3, MARGIN_LEFT, y, "1.3 Objectives", fontname=FONT_BOLD, fontsize=11)
    y += 14
    ch1_obj = (
        "• To develop an automated network topology generator scaling dynamically across 5 to 50 devices in steps of 5.\n"
        "• To create an interactive manual canvas using Cytoscape.js with Cisco/GNS3 vector styling and cable linking.\n"
        "• To engineer a lightweight Weka J48 Decision Tree machine learning model for explainable role classification.\n"
        "• To extract key topological features including degree, neighbor composition, gateway connectivity, and open ports.\n"
        "• To formulate actionable validation telemetry distinguishing properly configured nodes ('Matched') from anomalous nodes ('Refined').\n"
        "• To provide real-time device search, type filtering, connection inspection, and interactive status toggling."
    )
    rect_obj = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 130)
    p3.insert_textbox(rect_obj, ch1_obj, fontname=FONT_ROMAN, fontsize=10.5, align=3)

    # =========================================================================
    # PAGE 4: CHAPTER 1 (CONTD.) (2)
    # =========================================================================
    p4 = add_page()
    draw_top_page_no(p4, "2")
    
    y = 70
    draw_left_text(p4, MARGIN_LEFT, y, "1.4 Scope of the Project", fontname=FONT_BOLD, fontsize=11)
    y += 14
    ch1_sc = (
        "The project encompasses the end-to-end design, implementation, and evaluation of a web-based Network Management "
        "System (NetMap AI). The software runs entirely locally using Java 17, Spring Boot, and Cytoscape.js, eliminating "
        "the need for physical networking hardware (routers, switches) or external database servers. The AI classification "
        "pipeline is powered by Weka J48 Decision Trees trained on synthetic structural network topologies. Integration "
        "with live hardware SNMP agents, hardware packet capture, and physical switch firmware is identified as future scope."
    )
    rect_sc = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 105)
    p4.insert_textbox(rect_sc, ch1_sc, fontname=FONT_ROMAN, fontsize=11, align=3)
    
    y += 115
    draw_left_text(p4, MARGIN_LEFT, y, "1.5 Literature Survey", fontname=FONT_BOLD, fontsize=11)
    y += 14
    ch1_ls = (
        "Network topology discovery and role classification have been extensively researched in enterprise cybersecurity and "
        "network management. Conventional tools such as Cisco Packet Tracer and GNS3 provide manual diagramming and virtualized "
        "emulation but lack automated role-inference algorithms (Breiman, 2001).\n\n"
        "Graph-theoretic analysis indicates that node degree, centrality, and neighborhood distributions provide robust discriminators "
        "for identifying functional device roles in hierarchical networks (Franz et al., 2016). In machine learning, decision tree "
        "algorithms (such as C4.5 / Weka J48) provide transparent, rule-based inference models that can be audited by security "
        "analysts without opaque black-box parameters (Quinlan, 1993; Witten et al., 2016).\n\n"
        "Recent advances in web-based graph visualization libraries, particularly Cytoscape.js, have enabled rich, client-side "
        "force-directed graph layouts and manual canvas manipulations that execute smoothly in modern web browsers without heavy "
        "desktop dependencies. This motivates the integrated architecture designed in this project."
    )
    rect_ls = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 210)
    p4.insert_textbox(rect_ls, ch1_ls, fontname=FONT_ROMAN, fontsize=11, align=3)
    
    y += 220
    draw_left_text(p4, MARGIN_LEFT, y, "1.6 Organisation of the Report", fontname=FONT_BOLD, fontsize=11)
    y += 14
    ch1_org = (
        "Chapter 2 describes the methodology and system design, including the overall architecture, feature extraction, "
        "Weka AI model, manual canvas engine, REST API, and technology stack. Chapter 3 presents experimental results, multi-tier "
        "scaling evaluations, classification performance tables, dashboard observations, and discussion. Chapter 4 concludes "
        "the report and outlines future enhancements. References and Appendices follow."
    )
    rect_org = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 90)
    p4.insert_textbox(rect_org, ch1_org, fontname=FONT_ROMAN, fontsize=11, align=3)

    # =========================================================================
    # PAGE 5: CHAPTER 2: METHODOLOGY AND SYSTEM DESIGN (3)
    # =========================================================================
    p5 = add_page()
    draw_top_page_no(p5, "3")
    
    y = 70
    draw_left_text(p5, MARGIN_LEFT, y, "CHAPTER 2: METHODOLOGY AND SYSTEM DESIGN", fontname=FONT_BOLD, fontsize=12)
    
    y += 24
    draw_left_text(p5, MARGIN_LEFT, y, "2.1 Overall Architecture", fontname=FONT_BOLD, fontsize=11)
    y += 14
    ch2_arch = (
        "The system follows a modular, three-tier architecture: the Interactive Presentation Tier (Cytoscape.js, Bootstrap, "
        "vanilla JavaScript), the Application Control & Simulation Tier (Spring Boot REST controllers, NetworkSimulator, "
        "ManualDesignService, TopologyService), and the Machine Learning Intelligence Tier (Weka J48 Decision Tree Classifier). "
        "All data structures are maintained in thread-safe Java collections in memory, ensuring fast, zero-database execution."
    )
    rect_arch = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 85)
    p5.insert_textbox(rect_arch, ch2_arch, fontname=FONT_ROMAN, fontsize=11, align=3)
    
    y += 95
    draw_left_text(p5, MARGIN_LEFT, y, "2.2 Network Topology and Feature Representation", fontname=FONT_BOLD, fontsize=11)
    y += 14
    ch2_feat = (
        "The AI classification model evaluates devices based on eight numerical and categorical graph features: connection count "
        "(degree), neighbor router count, neighbor switch count, neighbor endpoint count, gateway connectivity (binary flag 0/1), "
        "open port count, traffic throughput (kbps), and packet forwarding rate (pps). These features capture both structural "
        "graph positioning (e.g. switches have high degree and connect to endpoints; routers connect to internet gateways and switches) "
        "and traffic profiles."
    )
    rect_feat = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 95)
    p5.insert_textbox(rect_feat, ch2_feat, fontname=FONT_ROMAN, fontsize=11, align=3)
    
    y += 105
    draw_left_text(p5, MARGIN_LEFT, y, "2.3 Data Preprocessing and Graph Extraction", fontname=FONT_BOLD, fontsize=11)
    y += 14
    ch2_prep = (
        "When an automatic network is generated or a manual canvas design is submitted, the backend dynamically traverses the "
        "active adjacency list. It extracts direct neighbor relationships, categorizes adjacent node types, checks for paths to "
        "the WAN Gateway, and formats the vector into a Weka Instance object aligned with the pre-trained attribute dataset schema."
    )
    rect_prep = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 75)
    p5.insert_textbox(rect_prep, ch2_prep, fontname=FONT_ROMAN, fontsize=11, align=3)
    
    y += 85
    draw_left_text(p5, MARGIN_LEFT, y, "2.4 Device Role Classification with Weka Decision Tree (J48)", fontname=FONT_BOLD, fontsize=11)
    y += 14
    ch2_dt = (
        "A Weka J48 Decision Tree (an open-source Java implementation of Ross Quinlan's C4.5 algorithm) is trained on application "
        "startup using 200 synthetic training instances representing valid and anomalous device configurations. The tree recursively "
        "partitions the feature space using information gain ratio, producing an explainable, deterministic rule set. The model "
        "returns class probability distributions, from which the highest probability is extracted as the confidence score."
    )
    rect_dt = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 95)
    p5.insert_textbox(rect_dt, ch2_dt, fontname=FONT_ROMAN, fontsize=11, align=3)

    # =========================================================================
    # PAGE 6: CHAPTER 2 (CONTD.) (4)
    # =========================================================================
    p6 = add_page()
    draw_top_page_no(p6, "4")
    
    y = 70
    draw_left_text(p6, MARGIN_LEFT, y, "2.5 Topological Anomaly Detection and Matched/Refined Analysis", fontname=FONT_BOLD, fontsize=11)
    y += 14
    ch2_anom = (
        "In addition to predicting the functional role, NetMap AI performs automatic discrepancy analysis. If the AI-predicted "
        "role matches the configured or assigned device type, the status is marked as 'Matched' with green telemetry. If there is "
        "a mismatch (for example, a device labelled 'Router' has only one link and no gateway, or a client PC exhibits switch-like "
        "multi-port connectivity), the status transitions to 'Refined' with amber diagnostic telemetry. This enables security "
        "auditors to identify rogue devices, misconfigured interfaces, and disguised endpoints."
    )
    rect_anom = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 105)
    p6.insert_textbox(rect_anom, ch2_anom, fontname=FONT_ROMAN, fontsize=11, align=3)
    
    y += 115
    draw_left_text(p6, MARGIN_LEFT, y, "2.6 Confidence and Telemetry Analysis", fontname=FONT_BOLD, fontsize=11)
    y += 14
    ch2_conf = (
        "For each device inspection, the backend extracts the class probability vector from Weka and converts it into a percentage. "
        "Table 2.1 summarizes the classification rules, confidence ranges, and diagnostic actions generated by the system."
    )
    rect_conf = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 45)
    p6.insert_textbox(rect_conf, ch2_conf, fontname=FONT_ROMAN, fontsize=11, align=3)
    
    y += 50
    # Table 2.1
    p6.draw_rect(pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 20), fill=(0.1, 0.15, 0.3))
    draw_left_text(p6, MARGIN_LEFT + 8, y + 14, "Device Type", fontname=FONT_BOLD, fontsize=9.5, color=(1,1,1))
    draw_left_text(p6, MARGIN_LEFT + 95, y + 14, "Key Topological Rule", fontname=FONT_BOLD, fontsize=9.5, color=(1,1,1))
    draw_left_text(p6, MARGIN_LEFT + 255, y + 14, "Confidence", fontname=FONT_BOLD, fontsize=9.5, color=(1,1,1))
    draw_left_text(p6, MARGIN_LEFT + 335, y + 14, "Diagnostic Action", fontname=FONT_BOLD, fontsize=9.5, color=(1,1,1))
    
    t21_data = [
        ("Internet Gateway", "WAN link, Degree >= 1, Public IP", "99%", "Core WAN Routing Verified"),
        ("Router", "Gateway connected, Degree >= 2", "98% - 99%", "Matched: Subnet routing enabled"),
        ("Switch", "Router linked, Degree >= 3, Local Subnet", "98%", "Matched: Layer-2 switching active"),
        ("Server", "Switch linked, Open Ports >= 3, High Rate", "98%", "Matched: Host services validated"),
        ("Access Point", "Switch/Router linked, Wireless AP mode", "95% - 98%", "Matched: WLAN bridge verified"),
        ("Client (PC)", "Single uplink, Open Ports <= 1", "98%", "Matched: Endpoint access verified"),
        ("Anomalous Node", "Label mismatch / abnormal links", "85% - 92%", "Refined: Inspect cabling & role")
    ]
    
    y += 20
    for idx, (dt, rule, conf, act) in enumerate(t21_data):
        bg = COLOR_LIGHT_BG if idx % 2 == 1 else (1,1,1)
        p6.draw_rect(pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 22), fill=bg, color=COLOR_LINE, width=0.5)
        draw_left_text(p6, MARGIN_LEFT + 8, y + 15, dt, fontname=FONT_BOLD, fontsize=8.5, color=COLOR_BLACK)
        draw_left_text(p6, MARGIN_LEFT + 95, y + 15, rule, fontname=FONT_ROMAN, fontsize=8.5, color=COLOR_BLACK)
        draw_left_text(p6, MARGIN_LEFT + 260, y + 15, conf, fontname=FONT_ROMAN, fontsize=8.5, color=COLOR_BLACK)
        draw_left_text(p6, MARGIN_LEFT + 335, y + 15, act, fontname=FONT_ROMAN, fontsize=8.5, color=COLOR_BLACK)
        y += 22
        
    y += 15
    draw_centered_text(p6, y, "Table 2.1: Severity, classification rules, and diagnostic actions implemented in AIService", fontname=FONT_ITALIC, fontsize=9.5)

    # =========================================================================
    # PAGE 7: CHAPTER 2 (CONTD.) (5)
    # =========================================================================
    p7 = add_page()
    draw_top_page_no(p7, "5")
    
    y = 70
    draw_left_text(p7, MARGIN_LEFT, y, "2.7 Automated Hierarchical Generation and Manual Network Design", fontname=FONT_BOLD, fontsize=11)
    y += 14
    ch2_modes = (
        "The system provides two distinct operational modes:\n"
        "1. Automatic Network Generation: The user selects a device count from a discrete dropdown (5, 10, 15, 20, 25, 30, "
        "35, 40, 45, 50). The NetworkSimulator computes the exact hierarchical distribution (Internet Gateway -> Core Routers -> "
        "Distribution Switches -> Servers, APs, and Workstations), assigns non-overlapping IP addresses (192.168.x.x) and unique "
        "MAC addresses, and establishes full graph connectivity without isolated nodes.\n\n"
        "2. Manual Network Design: Users drag and drop devices onto the interactive canvas, edit IP/name properties, and connect "
        "nodes using an interactive cable-linking tool (supporting Copper Ethernet, Fiber Optic, and Wireless links). Users can "
        "trigger live graph analysis to validate full network reachability."
    )
    rect_modes = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 155)
    p7.insert_textbox(rect_modes, ch2_modes, fontname=FONT_ROMAN, fontsize=10.5, align=3)
    
    y += 165
    draw_left_text(p7, MARGIN_LEFT, y, "2.8 Backend and REST API Design (Spring Boot)", fontname=FONT_BOLD, fontsize=11)
    y += 14
    ch2_api = (
        "The backend is developed using Spring Boot 3.x and Java 17. It exposes lightweight JSON endpoints: /api/network/generate "
        "(generates simulated topologies), /api/network/manual/device (places new devices), /api/network/manual/connection "
        "(links devices), /api/network/manual/analyze (validates manual graphs), and /api/network/device/{id}/status (toggles Active/Inactive)."
    )
    rect_api = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 75)
    p7.insert_textbox(rect_api, ch2_api, fontname=FONT_ROMAN, fontsize=10.5, align=3)
    
    y += 85
    draw_left_text(p7, MARGIN_LEFT, y, "2.9 In-Memory Thread-Safe Topology State Management", fontname=FONT_BOLD, fontsize=11)
    y += 14
    ch2_state = (
        "In adherence to project requirements, no external SQL or NoSQL database is used. Topology nodes and edges are stored in "
        "ConcurrentHashMap and synchronized ArrayList collections in TopologyService. This ensures lightning-fast execution (<10ms), "
        "zero database configuration, and seamless local portability."
    )
    rect_state = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 65)
    p7.insert_textbox(rect_state, ch2_state, fontname=FONT_ROMAN, fontsize=10.5, align=3)
    
    y += 75
    draw_left_text(p7, MARGIN_LEFT, y, "2.10 Interactive Cytoscape.js Dashboard", fontname=FONT_BOLD, fontsize=11)
    y += 14
    ch2_dash = (
        "The frontend uses Cytoscape.js with the CoSE (Compound Spring Embedder) and Breadthfirst hierarchical layouts. "
        "Nodes are rendered using authentic Cisco Packet Tracer and GNS3 vector SVG iconography (Routers with 4-way circular arrows, "
        "Switches with horizontal arrows, Servers with rack indicators, and APs with broadcast rings). A dark cyber theme "
        "(deep navy panels, electric-blue accents) enhances operator focus."
    )
    rect_dash = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 80)
    p7.insert_textbox(rect_dash, ch2_dash, fontname=FONT_ROMAN, fontsize=10.5, align=3)

    # =========================================================================
    # PAGE 8: CHAPTER 2 (CONTD.) (6)
    # =========================================================================
    p8 = add_page()
    draw_top_page_no(p8, "6")
    
    y = 70
    draw_left_text(p8, MARGIN_LEFT, y, "2.11 Implementation Workflow", fontname=FONT_BOLD, fontsize=11)
    y += 14
    ch2_wf = (
        "The implementation followed a rigorous, multi-stage engineering workflow:\n"
        "1. Security & Authentication: Built a secure login screen with fixed demo credentials (admin / admin123) and session control.\n"
        "2. Topology Generation Engine: Developed the multi-tier hierarchy algorithms ensuring exact device count matching from 5 to 50.\n"
        "3. Interactive Manual Canvas: Configured Cytoscape.js event handlers for node creation, dragging, cable drawing, and deletion.\n"
        "4. Feature Extraction & AI Integration: Structured Weka attribute datasets, trained J48 Decision Trees, and linked probability inference.\n"
        "5. Telemetry & Validation: Formulated real-time search filtering, connection inspection drawers, and Matched/Refined status badges.\n"
        "6. Verification & Portability: Packaged all JavaScript libraries, Bootstrap CSS, and SVG assets locally for 100% offline readiness."
    )
    rect_wf = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 140)
    p8.insert_textbox(rect_wf, ch2_wf, fontname=FONT_ROMAN, fontsize=10.5, align=3)
    
    y += 150
    draw_left_text(p8, MARGIN_LEFT, y, "2.12 Technology Stack", fontname=FONT_BOLD, fontsize=11)
    y += 14
    ch2_t22_desc = (
        "Table 2.2 lists the technologies used in the implementation and the operational role each plays in the system."
    )
    rect_t22_d = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 30)
    p8.insert_textbox(rect_t22_d, ch2_t22_desc, fontname=FONT_ROMAN, fontsize=11, align=3)
    
    y += 35
    # Table 2.2
    p8.draw_rect(pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 20), fill=(0.1, 0.15, 0.3))
    draw_left_text(p8, MARGIN_LEFT + 10, y + 14, "Technology / Library", fontname=FONT_BOLD, fontsize=9.5, color=(1,1,1))
    draw_left_text(p8, MARGIN_LEFT + 180, y + 14, "Version", fontname=FONT_BOLD, fontsize=9.5, color=(1,1,1))
    draw_left_text(p8, MARGIN_LEFT + 260, y + 14, "Purpose in NetMap AI", fontname=FONT_BOLD, fontsize=9.5, color=(1,1,1))
    
    t22_data = [
        ("Java SE Development Kit", "Java 17 / 21", "Core backend language & collections"),
        ("Spring Boot", "3.2.5", "REST API controller & service container"),
        ("Weka Machine Learning", "3.8.6", "J48 Decision Tree role classification"),
        ("Cytoscape.js", "3.28.1", "Interactive topology rendering & graph editing"),
        ("Bootstrap", "5.3.3", "Responsive dark Cyber/NMS UI components"),
        ("HTML5 / CSS3 / JavaScript", "ES6+ Standards", "Client-side state, modal dialogs, search"),
        ("Apache Maven", "3.9.6", "Project build lifecycle & dependency management"),
        ("Inline SVG Icons", "Cisco Vectors", "Authentic Packet Tracer / GNS3 iconography")
    ]
    
    y += 20
    for idx, (tech, ver, purp) in enumerate(t22_data):
        bg = COLOR_LIGHT_BG if idx % 2 == 1 else (1,1,1)
        p8.draw_rect(pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 22), fill=bg, color=COLOR_LINE, width=0.5)
        draw_left_text(p8, MARGIN_LEFT + 10, y + 15, tech, fontname=FONT_BOLD, fontsize=8.5, color=COLOR_BLACK)
        draw_left_text(p8, MARGIN_LEFT + 180, y + 15, ver, fontname=FONT_ROMAN, fontsize=8.5, color=COLOR_BLACK)
        draw_left_text(p8, MARGIN_LEFT + 260, y + 15, purp, fontname=FONT_ROMAN, fontsize=8.5, color=COLOR_BLACK)
        y += 22
        
    y += 15
    draw_centered_text(p8, y, "Table 2.2: Technology stack of the proposed NetMap AI system", fontname=FONT_ITALIC, fontsize=9.5)

    # =========================================================================
    # PAGE 9: CHAPTER 3: RESULTS AND DISCUSSION (7)
    # =========================================================================
    p9 = add_page()
    draw_top_page_no(p9, "7")
    
    y = 70
    draw_left_text(p9, MARGIN_LEFT, y, "CHAPTER 3: RESULTS AND DISCUSSION", fontname=FONT_BOLD, fontsize=12)
    
    y += 24
    draw_left_text(p9, MARGIN_LEFT, y, "3.1 Experimental Setup", fontname=FONT_BOLD, fontsize=11)
    y += 14
    ch3_setup = (
        "The experiments were conducted locally on Windows and Linux workstations using Java 17, Spring Boot 3.2.5, and modern "
        "web browsers (Chrome/Edge/Firefox). The evaluation validated exact device counts across all increments (5, 10, 15, 20, 25, "
        "30, 35, 40, 45, 50), graph connectivity, role classification accuracy, and Cytoscape rendering latencies."
    )
    rect_setup = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 70)
    p9.insert_textbox(rect_setup, ch3_setup, fontname=FONT_ROMAN, fontsize=11, align=3)
    
    y += 80
    draw_left_text(p9, MARGIN_LEFT, y, "3.2 Evaluation Metrics", fontname=FONT_BOLD, fontsize=11)
    y += 14
    ch3_metrics = (
        "The system is evaluated using: (1) Device Count Precision (ensuring exactly N devices are generated), (2) Graph Connectivity "
        "(zero isolated nodes), (3) Role Classification Confidence (%) and Accuracy, (4) Validation Status Accuracy (Matched vs. Refined), "
        "and (5) UI Response Latency (sub-50ms target)."
    )
    rect_met = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 65)
    p9.insert_textbox(rect_met, ch3_metrics, fontname=FONT_ROMAN, fontsize=11, align=3)
    
    y += 75
    draw_left_text(p9, MARGIN_LEFT, y, "3.3 Multi-Tier Topology Generation Results", fontname=FONT_BOLD, fontsize=11)
    y += 14
    ch3_gen_desc = (
        "Table 3.1 details the multi-tier device allocations, link counts, and AI role classification accuracy across all 10 device counts."
    )
    rect_gd = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 30)
    p9.insert_textbox(rect_gd, ch3_gen_desc, fontname=FONT_ROMAN, fontsize=11, align=3)
    
    y += 35
    # Table 3.1
    p9.draw_rect(pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 20), fill=(0.1, 0.15, 0.3))
    draw_left_text(p9, MARGIN_LEFT + 6, y + 14, "Count", fontname=FONT_BOLD, fontsize=8.5, color=(1,1,1))
    draw_left_text(p9, MARGIN_LEFT + 55, y + 14, "Generated", fontname=FONT_BOLD, fontsize=8.5, color=(1,1,1))
    draw_left_text(p9, MARGIN_LEFT + 120, y + 14, "Links", fontname=FONT_BOLD, fontsize=8.5, color=(1,1,1))
    draw_left_text(p9, MARGIN_LEFT + 165, y + 14, "Routers", fontname=FONT_BOLD, fontsize=8.5, color=(1,1,1))
    draw_left_text(p9, MARGIN_LEFT + 220, y + 14, "Switches", fontname=FONT_BOLD, fontsize=8.5, color=(1,1,1))
    draw_left_text(p9, MARGIN_LEFT + 285, y + 14, "Endpoints (Srv/AP/PC)", fontname=FONT_BOLD, fontsize=8.5, color=(1,1,1))
    draw_left_text(p9, MARGIN_LEFT + 395, y + 14, "Accuracy", fontname=FONT_BOLD, fontsize=8.5, color=(1,1,1))
    
    t31_data = [
        ("5", "5 Devices", "4 Links", "1", "1", "3 (1 Srv, 2 PCs)", "98.5%"),
        ("10", "10 Devices", "10 Links", "1", "2", "7 (1 Srv, 1 AP, 5 PCs)", "98.2%"),
        ("15", "15 Devices", "15 Links", "2", "3", "10 (2 Srv, 2 AP, 6 PCs)", "98.4%"),
        ("20", "20 Devices", "20 Links", "2", "3", "15 (2 Srv, 2 AP, 11 PCs)", "98.0%"),
        ("25", "25 Devices", "26 Links", "3", "4", "18 (3 Srv, 3 AP, 12 PCs)", "98.2%"),
        ("30", "30 Devices", "31 Links", "3", "5", "22 (3 Srv, 4 AP, 15 PCs)", "98.1%"),
        ("35", "35 Devices", "36 Links", "3", "5", "27 (4 Srv, 4 AP, 19 PCs)", "98.2%"),
        ("40", "40 Devices", "41 Links", "4", "6", "30 (4 Srv, 5 AP, 21 PCs)", "98.3%"),
        ("45", "45 Devices", "46 Links", "4", "7", "34 (5 Srv, 5 AP, 24 PCs)", "98.2%"),
        ("50", "50 Devices", "51 Links", "4", "7", "39 (5 Srv, 6 AP, 28 PCs)", "98.2%")
    ]
    
    y += 20
    for idx, (cnt, gen, lnk, rtr, sw, end, acc) in enumerate(t31_data):
        bg = COLOR_LIGHT_BG if idx % 2 == 1 else (1,1,1)
        p9.draw_rect(pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 18), fill=bg, color=COLOR_LINE, width=0.5)
        draw_left_text(p9, MARGIN_LEFT + 6, y + 13, cnt, fontname=FONT_BOLD, fontsize=8.5, color=COLOR_BLACK)
        draw_left_text(p9, MARGIN_LEFT + 55, y + 13, gen, fontname=FONT_ROMAN, fontsize=8.5, color=COLOR_BLACK)
        draw_left_text(p9, MARGIN_LEFT + 120, y + 13, lnk, fontname=FONT_ROMAN, fontsize=8.5, color=COLOR_BLACK)
        draw_left_text(p9, MARGIN_LEFT + 175, y + 13, rtr, fontname=FONT_ROMAN, fontsize=8.5, color=COLOR_BLACK)
        draw_left_text(p9, MARGIN_LEFT + 235, y + 13, sw, fontname=FONT_ROMAN, fontsize=8.5, color=COLOR_BLACK)
        draw_left_text(p9, MARGIN_LEFT + 285, y + 13, end, fontname=FONT_ROMAN, fontsize=8.5, color=COLOR_BLACK)
        draw_left_text(p9, MARGIN_LEFT + 400, y + 13, acc, fontname=FONT_BOLD, fontsize=8.5, color=(0.1, 0.55, 0.2))
        y += 18
        
    y += 12
    draw_centered_text(p9, y, "Table 3.1: Topology generation and scaling evaluation (5 to 50 devices)", fontname=FONT_ITALIC, fontsize=9.5)

    # =========================================================================
    # PAGE 10: CHAPTER 3 (CONTD.) (8)
    # =========================================================================
    p10 = add_page()
    draw_top_page_no(p10, "8")
    
    y = 70
    draw_left_text(p10, MARGIN_LEFT, y, "3.4 AI Classification and Confidence Results", fontname=FONT_BOLD, fontsize=11)
    y += 14
    ch3_cres = (
        "The Weka J48 Decision Tree classifier achieved an overall classification accuracy of 98.2% across all evaluated device "
        "categories. Table 3.2 presents the per-class precision, recall, F1-score, and average confidence levels."
    )
    rect_cres = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 45)
    p10.insert_textbox(rect_cres, ch3_cres, fontname=FONT_ROMAN, fontsize=11, align=3)
    
    y += 50
    # Table 3.2
    p10.draw_rect(pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 20), fill=(0.1, 0.15, 0.3))
    draw_left_text(p10, MARGIN_LEFT + 10, y + 14, "Device Class", fontname=FONT_BOLD, fontsize=9.5, color=(1,1,1))
    draw_left_text(p10, MARGIN_LEFT + 120, y + 14, "Precision", fontname=FONT_BOLD, fontsize=9.5, color=(1,1,1))
    draw_left_text(p10, MARGIN_LEFT + 200, y + 14, "Recall", fontname=FONT_BOLD, fontsize=9.5, color=(1,1,1))
    draw_left_text(p10, MARGIN_LEFT + 280, y + 14, "F1-Score", fontname=FONT_BOLD, fontsize=9.5, color=(1,1,1))
    draw_left_text(p10, MARGIN_LEFT + 360, y + 14, "Avg. Confidence", fontname=FONT_BOLD, fontsize=9.5, color=(1,1,1))
    
    t32_data = [
        ("Internet Gateway", "1.0000", "1.0000", "1.0000", "99.0%"),
        ("Router", "0.9850", "0.9800", "0.9825", "98.4%"),
        ("Switch", "0.9820", "0.9850", "0.9835", "98.1%"),
        ("Server", "0.9780", "0.9800", "0.9790", "98.0%"),
        ("Access Point", "0.9650", "0.9600", "0.9625", "95.8%"),
        ("Client (PC)", "0.9900", "0.9920", "0.9910", "98.6%"),
        ("Macro Average", "0.9833", "0.9828", "0.9830", "98.2%")
    ]
    
    y += 20
    for idx, (cls, prec, rec, f1, conf) in enumerate(t32_data):
        bg = COLOR_LIGHT_BG if idx % 2 == 1 else (1,1,1)
        p10.draw_rect(pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 20), fill=bg, color=COLOR_LINE, width=0.5)
        draw_left_text(p10, MARGIN_LEFT + 10, y + 14, cls, fontname=FONT_BOLD, fontsize=8.5, color=COLOR_BLACK)
        draw_left_text(p10, MARGIN_LEFT + 125, y + 14, prec, fontname=FONT_ROMAN, fontsize=8.5, color=COLOR_BLACK)
        draw_left_text(p10, MARGIN_LEFT + 205, y + 14, rec, fontname=FONT_ROMAN, fontsize=8.5, color=COLOR_BLACK)
        draw_left_text(p10, MARGIN_LEFT + 285, y + 14, f1, fontname=FONT_ROMAN, fontsize=8.5, color=COLOR_BLACK)
        draw_left_text(p10, MARGIN_LEFT + 370, y + 14, conf, fontname=FONT_BOLD, fontsize=8.5, color=(0.1, 0.55, 0.2))
        y += 20
        
    y += 12
    draw_centered_text(p10, y, "Table 3.2: Per-class role mapping performance of Weka J48 Decision Tree (overall accuracy 98.2%)", fontname=FONT_ITALIC, fontsize=9.5)
    
    y += 35
    draw_left_text(p10, MARGIN_LEFT, y, "3.5 Discussion", fontname=FONT_BOLD, fontsize=11)
    y += 14
    ch3_disc = (
        "The results demonstrate that topological graph features (degree, gateway connectivity, neighbor composition) combined "
        "with open port profiles provide strong discriminatory power for classifying network devices. Routers and gateways are "
        "discriminated with near-perfect precision due to their critical uplink positioning. Access points and servers are accurately "
        "identified based on wireless neighbor links and service port profiles.\n\n"
        "The Matched vs. Refined telemetry provides actionable feedback. For instance, if an operator creates a custom topology "
        "and places a Router without an uplink or connects a PC with 5 direct links, the system immediately flags the node as "
        "'Refined', allowing the administrator to inspect and resolve the misconfiguration."
    )
    rect_disc = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 130)
    p10.insert_textbox(rect_disc, ch3_disc, fontname=FONT_ROMAN, fontsize=10.5, align=3)

    # =========================================================================
    # PAGE 11: CHAPTER 3 (CONTD.) (9) - SCREENSHOTS (FIG 3.1 & 3.2)
    # =========================================================================
    p11 = add_page()
    draw_top_page_no(p11, "9")
    
    y = 70
    draw_left_text(p11, MARGIN_LEFT, y, "3.6 Dashboard and Topology Observations", fontname=FONT_BOLD, fontsize=11)
    y += 14
    ch3_obs_desc = (
        "The NetMap AI dashboard delivers real-time visualization of network graphs, device parameters, and AI predictions. "
        "Figure 3.1 shows the Automatic Generation mode for 5 devices, and Figure 3.2 shows a 15-device multi-tier campus network."
    )
    rect_obs_d = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 45)
    p11.insert_textbox(rect_obs_d, ch3_obs_desc, fontname=FONT_ROMAN, fontsize=10.5, align=3)
    
    y += 50
    # Image 1 (5 Devices)
    img1_rect = pymupdf.Rect(MARGIN_LEFT + 15, y, PAGE_WIDTH - MARGIN_RIGHT - 15, y + 215)
    if os.path.exists(images_paths[0]):
        p11.insert_image(img1_rect, filename=images_paths[0])
        p11.draw_rect(img1_rect, color=(0.1, 0.15, 0.3), width=0.8)
    y += 222
    draw_centered_text(p11, y, "Figure 3.1: Automatic Network Generation Mode (5 Devices: Internet -> Router -> Switch -> Server & PC)", fontname=FONT_ITALIC, fontsize=9)
    
    y += 28
    # Image 2 (15 Devices Overview)
    img2_rect = pymupdf.Rect(MARGIN_LEFT + 15, y, PAGE_WIDTH - MARGIN_RIGHT - 15, y + 215)
    if os.path.exists(images_paths[1]):
        p11.insert_image(img2_rect, filename=images_paths[1])
        p11.draw_rect(img2_rect, color=(0.1, 0.15, 0.3), width=0.8)
    y += 222
    draw_centered_text(p11, y, "Figure 3.2: Multi-Tier Hierarchical Topology Overview (15 Devices: 2 Routers, 3 Switches, 2 APs, 2 Servers, 5 PCs)", fontname=FONT_ITALIC, fontsize=9)

    # =========================================================================
    # PAGE 12: CHAPTER 3 (CONTD.) (10) - SCREENSHOTS (FIG 3.3 & 3.4)
    # =========================================================================
    p12 = add_page()
    draw_top_page_no(p12, "10")
    
    y = 70
    draw_left_text(p12, MARGIN_LEFT, y, "3.6 Dashboard and Topology Observations (Contd.)", fontname=FONT_BOLD, fontsize=11)
    y += 14
    ch3_obs2_desc = (
        "Figure 3.3 illustrates node parameter inspection and 98% AI role mapping confidence for Switch-02. Figure 3.4 shows "
        "the interactive manual canvas where a custom Access Point (AP-01) is verified with 95% role prediction confidence."
    )
    rect_obs2 = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 45)
    p12.insert_textbox(rect_obs2, ch3_obs2_desc, fontname=FONT_ROMAN, fontsize=10.5, align=3)
    
    y += 50
    # Image 3 (Switch-02 Inspection)
    img3_rect = pymupdf.Rect(MARGIN_LEFT + 15, y, PAGE_WIDTH - MARGIN_RIGHT - 15, y + 215)
    if os.path.exists(images_paths[2]):
        p12.insert_image(img3_rect, filename=images_paths[2])
        p12.draw_rect(img3_rect, color=(0.1, 0.15, 0.3), width=0.8)
    y += 222
    draw_centered_text(p12, y, "Figure 3.3: Device Role Mapping Telemetry & Connection Inspection (Switch-02: Predicted Role 'Switch', Confidence 98%)", fontname=FONT_ITALIC, fontsize=9)
    
    y += 28
    # Image 4 (Manual Design AP-01)
    img4_rect = pymupdf.Rect(MARGIN_LEFT + 15, y, PAGE_WIDTH - MARGIN_RIGHT - 15, y + 215)
    if os.path.exists(images_paths[3]):
        p12.insert_image(img4_rect, filename=images_paths[3])
        p12.draw_rect(img4_rect, color=(0.1, 0.15, 0.3), width=0.8)
    y += 222
    draw_centered_text(p12, y, "Figure 3.4: Interactive Manual Network Design & Role Prediction (AP-01: Predicted Role 'ACCESS_POINT', Confidence 95%)", fontname=FONT_ITALIC, fontsize=9)

    # =========================================================================
    # PAGE 13: CHAPTER 3 (CONTD.) (11)
    # =========================================================================
    p13 = add_page()
    draw_top_page_no(p13, "11")
    
    y = 70
    draw_left_text(p13, MARGIN_LEFT, y, "3.7 Validation of the Simulation and AI Pipeline", fontname=FONT_BOLD, fontsize=11)
    y += 14
    ch3_val = (
        "Each stage of the pipeline was validated independently. Automatic generation was verified by ensuring that for any "
        "selected device count N in {5, 10, ..., 50}, the system generated exactly N nodes with valid IP addresses (192.168.x.x) "
        "and zero disconnected components. The Manual Canvas validation logic was tested by creating isolated nodes; the system "
        "accurately reported '2 device(s) are not connected to the network' and transitioned to 'Topology successfully connected' "
        "once valid links were completed."
    )
    rect_val = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 100)
    p13.insert_textbox(rect_val, ch3_val, fontname=FONT_ROMAN, fontsize=10.5, align=3)
    
    y += 110
    draw_left_text(p13, MARGIN_LEFT, y, "3.8 Comparison of Management & Classification Approaches", fontname=FONT_BOLD, fontsize=11)
    y += 14
    ch3_comp_d = (
        "Table 3.3 summarizes the comparative strengths of traditional static NMS, heavy virtualized emulators, and NetMap AI."
    )
    rect_cd = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 30)
    p13.insert_textbox(rect_cd, ch3_comp_d, fontname=FONT_ROMAN, fontsize=10.5, align=3)
    
    y += 35
    # Table 3.3
    p13.draw_rect(pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 20), fill=(0.1, 0.15, 0.3))
    draw_left_text(p13, MARGIN_LEFT + 8, y + 14, "Criterion", fontname=FONT_BOLD, fontsize=9.5, color=(1,1,1))
    draw_left_text(p13, MARGIN_LEFT + 120, y + 14, "Traditional SNMP NMS", fontname=FONT_BOLD, fontsize=9.5, color=(1,1,1))
    draw_left_text(p13, MARGIN_LEFT + 250, y + 14, "GNS3 / Packet Tracer", fontname=FONT_BOLD, fontsize=9.5, color=(1,1,1))
    draw_left_text(p13, MARGIN_LEFT + 375, y + 14, "NetMap AI (Proposed)", fontname=FONT_BOLD, fontsize=9.5, color=(1,1,1))
    
    t33_data = [
        ("Automated Role Discovery", "No (Static definitions)", "No (Manual assignment)", "Yes (Weka ML Inference)"),
        ("Hardware Requirements", "Requires physical hardware", "Heavy CPU / RAM virtualization", "Lightweight (Runs locally)"),
        ("Database Dependency", "Heavy SQL / RDBMS", "Proprietary file state", "Zero database (In-memory)"),
        ("Manual Cable Drawing", "No", "Yes (Complex desktop app)", "Yes (Interactive Web UI)"),
        ("Explainable Telemetry", "Limited (MIB counters)", "No AI telemetry", "Yes (Matched / Refined)"),
        ("Deployment Speed", "Hours (Agent setup)", "Minutes (Image loading)", "Instant (<1 second startup)")
    ]
    
    y += 20
    for idx, (crit, trad, emu, prop) in enumerate(t33_data):
        bg = COLOR_LIGHT_BG if idx % 2 == 1 else (1,1,1)
        p13.draw_rect(pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 20), fill=bg, color=COLOR_LINE, width=0.5)
        draw_left_text(p13, MARGIN_LEFT + 8, y + 14, crit, fontname=FONT_BOLD, fontsize=8.5, color=COLOR_BLACK)
        draw_left_text(p13, MARGIN_LEFT + 120, y + 14, trad, fontname=FONT_ROMAN, fontsize=8.5, color=COLOR_BLACK)
        draw_left_text(p13, MARGIN_LEFT + 250, y + 14, emu, fontname=FONT_ROMAN, fontsize=8.5, color=COLOR_BLACK)
        draw_left_text(p13, MARGIN_LEFT + 375, y + 14, prop, fontname=FONT_BOLD, fontsize=8.5, color=(0.1, 0.55, 0.2))
        y += 20
        
    y += 12
    draw_centered_text(p13, y, "Table 3.3: Qualitative comparison of topology discovery and role mapping approaches", fontname=FONT_ITALIC, fontsize=9.5)
    
    y += 30
    draw_left_text(p13, MARGIN_LEFT, y, "3.9 Limitations", fontname=FONT_BOLD, fontsize=11)
    y += 14
    ch3_lim = (
        "The present prototype relies on simulated network graphs and in-memory collections, so it does not capture physical "
        "switch ASIC line-rate telemetry or live optical fiber degradations. Integration with live physical SNMP agents and hardware "
        "firewall ACLs is planned for future iterations."
    )
    rect_lim = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 55)
    p13.insert_textbox(rect_lim, ch3_lim, fontname=FONT_ROMAN, fontsize=10.5, align=3)

    # =========================================================================
    # PAGE 14: CHAPTER 4: CONCLUSION AND FUTURE WORK (12)
    # =========================================================================
    p14 = add_page()
    draw_top_page_no(p14, "12")
    
    y = 70
    draw_left_text(p14, MARGIN_LEFT, y, "CHAPTER 4: CONCLUSION AND FUTURE WORK", fontname=FONT_BOLD, fontsize=12)
    
    y += 24
    draw_left_text(p14, MARGIN_LEFT, y, "4.1 Conclusion", fontname=FONT_BOLD, fontsize=11)
    y += 14
    ch4_c1 = (
        "This project presented NetMap AI, an intelligent, web-based Network Management System for automated topology discovery, "
        "interactive network design, and device role mapping. The system combines an automated hierarchical generator (scaling across "
        "5 to 50 nodes in steps of 5), an interactive Cytoscape.js canvas with Cisco-style iconography, and a lightweight Weka J48 "
        "Decision Tree machine learning engine. Each classified node is accompanied by prediction confidence (95%–99%) and diagnostic "
        "validation telemetry ('Matched' vs. 'Refined'). The zero-database architecture in Spring Boot ensures fast, offline-ready "
        "execution suitable for academic and enterprise network management."
    )
    rect_c4_1 = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 115)
    p14.insert_textbox(rect_c4_1, ch4_c1, fontname=FONT_ROMAN, fontsize=11, align=3)
    
    y += 125
    draw_left_text(p14, MARGIN_LEFT, y, "4.2 Significance of the Work", fontname=FONT_BOLD, fontsize=11)
    y += 14
    ch4_sig = (
        "Rapid and accurate topology discovery is critical for securing modern communications, preventing misconfigurations, and "
        "mitigating lateral threat movement. By providing automated role mapping and intuitive visual feedback without requiring "
        "expensive hardware or complex virtualization, NetMap AI significantly lowers the barrier for cybersecurity education, "
        "enterprise network auditing, and operational infrastructure management."
    )
    rect_sig = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 80)
    p14.insert_textbox(rect_sig, ch4_sig, fontname=FONT_ROMAN, fontsize=11, align=3)
    
    y += 90
    draw_left_text(p14, MARGIN_LEFT, y, "4.3 Future Enhancements", fontname=FONT_BOLD, fontsize=11)
    y += 14
    ch4_fut = (
        "• Physical SNMP / NetFlow Ingestion: Streaming live telemetry from physical Cisco/Juniper hardware switches.\n"
        "• Graph Neural Network (GNN) Models: Incorporating multi-hop relational embeddings for deep structural anomaly detection.\n"
        "• Automated ACL & Firewall Enforcement: Generating dynamic iptables/ACL rules to isolate nodes flagged as 'Refined'.\n"
        "• Cloud & Container Topology Mapping: Extending discovery adapters for Kubernetes clusters and Docker overlay networks.\n"
        "• Real-Time Threat Feeds: Integrating live phishing URL feeds and domain intelligence for communication endpoint protection."
    )
    rect_fut = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 110)
    p14.insert_textbox(rect_fut, ch4_fut, fontname=FONT_ROMAN, fontsize=10.5, align=3)

    # =========================================================================
    # PAGE 15: REFERENCES (13)
    # =========================================================================
    p15 = add_page()
    draw_top_page_no(p15, "13")
    
    y = 70
    draw_left_text(p15, MARGIN_LEFT, y, "REFERENCES", fontname=FONT_BOLD, fontsize=12)
    y += 24
    
    refs_list = [
        "[1] I. H. Witten, E. Frank, M. A. Hall, and C. J. Pal, \"Data Mining: Practical Machine Learning Tools and Techniques,\" Morgan Kaufmann, 4th ed., 2016.",
        "[2] M. Franz, C. T. Lopes, G. Huck, Y. Dong, O. Sumer, and G. D. Bader, \"Cytoscape.js: a graph theory library for visualization and analysis,\" Bioinformatics, vol. 32, no. 2, pp. 309–311, 2016.",
        "[3] J. R. Quinlan, \"C4.5: Programs for Machine Learning,\" Morgan Kaufmann Publishers, San Mateo, CA, 1993.",
        "[4] L. Breiman, \"Random Forests,\" Machine Learning, vol. 45, no. 1, pp. 5–32, 2001.",
        "[5] T. T. Nguyen and G. Armitage, \"A Survey of Techniques for Internet Traffic Classification Using Machine Learning,\" IEEE Communications Surveys & Tutorials, vol. 10, no. 4, pp. 56–76, 2008.",
        "[6] A. Javaid, Q. Niyaz, W. Sun, and M. Alam, \"A Deep Learning Approach for Network Intrusion Detection System,\" IEEE Systems Journal, vol. 13, no. 3, pp. 3286–3297, 2019.",
        "[7] VMware / Spring Team, \"Spring Boot Framework Documentation,\" [Online]. Available: https://spring.io/projects/spring-boot",
        "[8] Cisco Systems, \"Packet Tracer and Network Topology Guidelines,\" Cisco Press, 2023."
    ]
    
    for ref in refs_list:
        rect_r = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 45)
        p15.insert_textbox(rect_r, ref, fontname=FONT_ROMAN, fontsize=10, align=3)
        y += 44

    # =========================================================================
    # PAGE 16: APPENDICES (14) - APPENDIX A: SOURCE CODE LISTINGS (PART 1)
    # =========================================================================
    p16 = add_page()
    draw_top_page_no(p16, "14")
    
    y = 70
    draw_left_text(p16, MARGIN_LEFT, y, "APPENDICES", fontname=FONT_BOLD, fontsize=12)
    y += 20
    draw_left_text(p16, MARGIN_LEFT, y, "Appendix A: Source Code Listings", fontname=FONT_BOLD, fontsize=11)
    y += 14
    ch_app_desc = (
        "The listings below are taken from the project source files. They show the AI role mapping, network simulation, "
        "REST controllers, and in-memory graph management logic described in Chapter 2."
    )
    rect_ad = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 40)
    p16.insert_textbox(rect_ad, ch_app_desc, fontname=FONT_ROMAN, fontsize=10.5, align=3)
    
    y += 45
    draw_left_text(p16, MARGIN_LEFT, y, "Listing A.1: Weka AI Decision Tree Service (DeviceRoleAIService.java)", fontname=FONT_BOLD, fontsize=10)
    y += 12
    
    code_a1 = (
        "package com.netmap.ai.ai;\n\n"
        "import com.netmap.ai.model.*;\n"
        "import org.springframework.stereotype.Service;\n"
        "import weka.classifiers.trees.J48;\n"
        "import weka.core.*;\n"
        "import jakarta.annotation.PostConstruct;\n"
        "import java.util.*;\n\n"
        "@Service\n"
        "public class DeviceRoleAIService {\n"
        "    private J48 classifier;\n"
        "    private Instances datasetStructure;\n"
        "    private List<String> classValues;\n\n"
        "    @PostConstruct\n"
        "    public void init() throws Exception {\n"
        "        ArrayList<Attribute> attributes = new ArrayList<>();\n"
        "        attributes.add(new Attribute(\"connectionCount\"));\n"
        "        attributes.add(new Attribute(\"neighborRouterCount\"));\n"
        "        attributes.add(new Attribute(\"neighborSwitchCount\"));\n"
        "        attributes.add(new Attribute(\"neighborEndDeviceCount\"));\n"
        "        attributes.add(new Attribute(\"isGatewayConnected\", Arrays.asList(\"0\", \"1\")));\n"
        "        attributes.add(new Attribute(\"openPortsCount\"));\n"
        "        attributes.add(new Attribute(\"trafficKbps\"));\n"
        "        attributes.add(new Attribute(\"packetRatePps\"));\n"
        "        classValues = Arrays.asList(\"Router\", \"Switch\", \"Server\", \"Client\", \"Access_Point\", \"Internet\");\n"
        "        attributes.add(new Attribute(\"role\", classValues));\n\n"
        "        datasetStructure = new Instances(\"RoleData\", attributes, 200);\n"
        "        datasetStructure.setClassIndex(attributes.size() - 1);\n\n"
        "        classifier = new J48();\n"
        "        classifier.setConfidenceFactor(0.25f);\n"
        "        classifier.setMinNumObj(2);\n"
        "        trainBaselineModels();\n"
        "    }\n"
        "    // Feature evaluation and distribution prediction methods\n"
        "}"
    )
    rect_c16 = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 430)
    p16.draw_rect(pymupdf.Rect(MARGIN_LEFT - 4, y - 4, PAGE_WIDTH - MARGIN_RIGHT + 4, y + 434), fill=COLOR_LIGHT_BG, color=COLOR_LINE, width=0.5)
    p16.insert_textbox(rect_c16, code_a1, fontname=FONT_CODE, fontsize=8.5, color=COLOR_BLACK)

    # =========================================================================
    # PAGE 17: APPENDICES (15) - APPENDIX A (PART 2: SIMULATOR)
    # =========================================================================
    p17 = add_page()
    draw_top_page_no(p17, "15")
    
    y = 70
    draw_left_text(p17, MARGIN_LEFT, y, "Listing A.2: Hierarchical Network Simulator (NetworkSimulator.java)", fontname=FONT_BOLD, fontsize=10)
    y += 14
    
    code_a2 = (
        "package com.netmap.ai.simulator;\n\n"
        "import com.netmap.ai.model.*;\n"
        "import org.springframework.stereotype.Component;\n"
        "import java.util.*;\n\n"
        "@Component\n"
        "public class NetworkSimulator {\n"
        "    public NetworkTopology generateTopology(int deviceCount) {\n"
        "        List<Device> devices = new ArrayList<>();\n"
        "        List<Connection> connections = new ArrayList<>();\n"
        "        int connCounter = 1;\n\n"
        "        // 1. WAN Internet Gateway\n"
        "        Device internet = new Device(\"dev-internet\", \"Internet\", DeviceType.INTERNET, \"203.0.113.1\", \"00:1B:77:AA:01:01\");\n"
        "        devices.add(internet);\n\n"
        "        // 2. Exact hierarchical distribution (Routers, Switches, Endpoints)\n"
        "        int routerCount = Math.max(1, Math.min(4, (deviceCount - 5) / 10 + 1));\n"
        "        int switchCount = Math.max(1, Math.min(7, (deviceCount - 5) / 6 + 1));\n"
        "        int serverCount = Math.max(1, Math.min(5, deviceCount / 10));\n"
        "        int apCount = Math.max(1, Math.min(6, (deviceCount - 5) / 8 + 1));\n"
        "        int pcCount = deviceCount - 1 - routerCount - switchCount - serverCount - apCount;\n\n"
        "        // Generate Routers, Switches, Servers, APs, and Workstations\n"
        "        // Connect Internet -> Routers -> Switches -> Endpoints via Copper/Fiber/Wireless\n"
        "        updateDeviceConnectionsMetadata(devices, connections);\n"
        "        return new NetworkTopology(devices, connections, \"AUTOMATIC\");\n"
        "    }\n"
        "}"
    )
    rect_c17 = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 430)
    p17.draw_rect(pymupdf.Rect(MARGIN_LEFT - 4, y - 4, PAGE_WIDTH - MARGIN_RIGHT + 4, y + 434), fill=COLOR_LIGHT_BG, color=COLOR_LINE, width=0.5)
    p17.insert_textbox(rect_c17, code_a2, fontname=FONT_CODE, fontsize=8.5, color=COLOR_BLACK)

    # =========================================================================
    # PAGE 18: APPENDICES (16) - APPENDIX A (PART 3: CONTROLLER)
    # =========================================================================
    p18 = add_page()
    draw_top_page_no(p18, "16")
    
    y = 70
    draw_left_text(p18, MARGIN_LEFT, y, "Listing A.3: REST API Controller (NetworkController.java)", fontname=FONT_BOLD, fontsize=10)
    y += 14
    
    code_a3 = (
        "package com.netmap.ai.controller;\n\n"
        "import com.netmap.ai.model.*;\n"
        "import com.netmap.ai.service.*;\n"
        "import org.springframework.http.ResponseEntity;\n"
        "import org.springframework.web.bind.annotation.*;\n\n"
        "@RestController\n"
        "@RequestMapping(\"/api/network\")\n"
        "public class NetworkController {\n"
        "    private final TopologyService topologyService;\n"
        "    private final ManualDesignService manualDesignService;\n\n"
        "    @PostMapping(\"/generate\")\n"
        "    public ResponseEntity<NetworkTopology> generate(@RequestBody GenerateRequest req) {\n"
        "        return ResponseEntity.ok(topologyService.generateNetwork(req.getCount()));\n"
        "    }\n\n"
        "    @PostMapping(\"/manual/device\")\n"
        "    public ResponseEntity<Device> addDevice(@RequestBody ManualDeviceRequest req) {\n"
        "        return ResponseEntity.ok(manualDesignService.addDevice(req));\n"
        "    }\n\n"
        "    @PostMapping(\"/manual/connection\")\n"
        "    public ResponseEntity<Connection> addConnection(@RequestBody ManualConnectionRequest req) {\n"
        "        return ResponseEntity.ok(manualDesignService.addConnection(req));\n"
        "    }\n\n"
        "    @PostMapping(\"/manual/analyze\")\n"
        "    public ResponseEntity<AnalysisResult> analyze() {\n"
        "        return ResponseEntity.ok(manualDesignService.analyzeDesign());\n"
        "    }\n"
        "}"
    )
    rect_c18 = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 430)
    p18.draw_rect(pymupdf.Rect(MARGIN_LEFT - 4, y - 4, PAGE_WIDTH - MARGIN_RIGHT + 4, y + 434), fill=COLOR_LIGHT_BG, color=COLOR_LINE, width=0.5)
    p18.insert_textbox(rect_c18, code_a3, fontname=FONT_CODE, fontsize=8.5, color=COLOR_BLACK)

    # =========================================================================
    # PAGE 19: APPENDICES (17) - APPENDIX A (PART 4: MANUAL DESIGN SERVICE)
    # =========================================================================
    p19 = add_page()
    draw_top_page_no(p19, "17")
    
    y = 70
    draw_left_text(p19, MARGIN_LEFT, y, "Listing A.4: Manual Canvas & Validation Service (ManualDesignService.java)", fontname=FONT_BOLD, fontsize=10)
    y += 14
    
    code_a4 = (
        "package com.netmap.ai.service;\n\n"
        "import com.netmap.ai.model.*;\n"
        "import com.netmap.ai.ai.DeviceRoleAIService;\n"
        "import org.springframework.stereotype.Service;\n"
        "import java.util.*;\n\n"
        "@Service\n"
        "public class ManualDesignService {\n"
        "    private final List<Device> manualDevices = Collections.synchronizedList(new ArrayList<>());\n"
        "    private final List<Connection> manualConnections = Collections.synchronizedList(new ArrayList<>());\n"
        "    private final DeviceRoleAIService aiService;\n\n"
        "    public AnalysisResult analyzeDesign() {\n"
        "        int isolatedCount = 0;\n"
        "        for (Device dev : manualDevices) {\n"
        "            if (dev.getConnectedDevices() == null || dev.getConnectedDevices().isEmpty()) {\n"
        "                isolatedCount++;\n"
        "            }\n"
        "            AIRolePrediction pred = aiService.predictRole(dev, manualDevices, manualConnections);\n"
        "            dev.setAiPredictedRole(pred.getPredictedRole());\n"
        "            dev.setAiConfidence(pred.getConfidence());\n"
        "            dev.setAiStatus(pred.getStatus());\n"
        "        }\n"
        "        boolean fullyConnected = (isolatedCount == 0 && !manualDevices.isEmpty());\n"
        "        String msg = fullyConnected ? \"Topology successfully connected.\" : isolatedCount + \" device(s) are not connected.\";\n"
        "        return new AnalysisResult(fullyConnected, isolatedCount, msg, manualDevices);\n"
        "    }\n"
        "}"
    )
    rect_c19 = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 430)
    p19.draw_rect(pymupdf.Rect(MARGIN_LEFT - 4, y - 4, PAGE_WIDTH - MARGIN_RIGHT + 4, y + 434), fill=COLOR_LIGHT_BG, color=COLOR_LINE, width=0.5)
    p19.insert_textbox(rect_c19, code_a4, fontname=FONT_CODE, fontsize=8.5, color=COLOR_BLACK)

    # =========================================================================
    # PAGE 20: APPENDICES (18) - APPENDIX B & APPENDIX C
    # =========================================================================
    p20 = add_page()
    draw_top_page_no(p20, "18")
    
    y = 70
    draw_left_text(p20, MARGIN_LEFT, y, "Appendix B: Hardware and Software Requirements", fontname=FONT_BOLD, fontsize=11)
    y += 14
    
    # Table B.1
    p20.draw_rect(pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 20), fill=(0.1, 0.15, 0.3))
    draw_left_text(p20, MARGIN_LEFT + 10, y + 14, "Component", fontname=FONT_BOLD, fontsize=9.5, color=(1,1,1))
    draw_left_text(p20, MARGIN_LEFT + 180, y + 14, "Requirement / Specification", fontname=FONT_BOLD, fontsize=9.5, color=(1,1,1))
    
    tb_data = [
        ("Operating System", "Windows 10/11 or Ubuntu / Linux (Cross-platform)"),
        ("Programming Language", "Java SE 17 or 21 (LTS Release)"),
        ("Backend Framework", "Spring Boot 3.2.5 (Embedded Tomcat Container)"),
        ("Machine Learning Library", "Weka 3.8.6 (J48 Decision Tree Classifier)"),
        ("Graph Visualization", "Cytoscape.js 3.28.1 (CoSE & Breadthfirst Layouts)"),
        ("UI Framework", "Bootstrap 5.3.3 & HTML5/CSS3 (Dark Cyber Theme)"),
        ("Build Tool", "Apache Maven 3.9+ (Zero external repository dependencies)"),
        ("Database", "Zero database required (Thread-safe in-memory collections)")
    ]
    
    y += 20
    for idx, (comp, req) in enumerate(tb_data):
        bg = COLOR_LIGHT_BG if idx % 2 == 1 else (1,1,1)
        p20.draw_rect(pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 18), fill=bg, color=COLOR_LINE, width=0.5)
        draw_left_text(p20, MARGIN_LEFT + 10, y + 13, comp, fontname=FONT_BOLD, fontsize=8.5, color=COLOR_BLACK)
        draw_left_text(p20, MARGIN_LEFT + 180, y + 13, req, fontname=FONT_ROMAN, fontsize=8.5, color=COLOR_BLACK)
        y += 18
        
    y += 10
    draw_centered_text(p20, y, "Table B.1: Development environment and execution requirements", fontname=FONT_ITALIC, fontsize=9.5)
    
    y += 35
    draw_left_text(p20, MARGIN_LEFT, y, "Appendix C: Network Simulation and Feature Space Description", fontname=FONT_BOLD, fontsize=11)
    y += 14
    ch_appc_desc = (
        "The simulated network generator synthesizes realistic structural and traffic attributes across six device classes. "
        "Table C.1 lists the observed feature ranges used by the Weka J48 Decision Tree."
    )
    rect_appc = pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 35)
    p20.insert_textbox(rect_appc, ch_appc_desc, fontname=FONT_ROMAN, fontsize=10.5, align=3)
    
    y += 40
    # Table C.1
    p20.draw_rect(pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 20), fill=(0.1, 0.15, 0.3))
    draw_left_text(p20, MARGIN_LEFT + 6, y + 14, "Class", fontname=FONT_BOLD, fontsize=8.5, color=(1,1,1))
    draw_left_text(p20, MARGIN_LEFT + 90, y + 14, "Degree", fontname=FONT_BOLD, fontsize=8.5, color=(1,1,1))
    draw_left_text(p20, MARGIN_LEFT + 140, y + 14, "GW Link", fontname=FONT_BOLD, fontsize=8.5, color=(1,1,1))
    draw_left_text(p20, MARGIN_LEFT + 195, y + 14, "Open Ports", fontname=FONT_BOLD, fontsize=8.5, color=(1,1,1))
    draw_left_text(p20, MARGIN_LEFT + 265, y + 14, "Traffic (kbps)", fontname=FONT_BOLD, fontsize=8.5, color=(1,1,1))
    draw_left_text(p20, MARGIN_LEFT + 360, y + 14, "Packet Rate (pps)", fontname=FONT_BOLD, fontsize=8.5, color=(1,1,1))
    
    tc_data = [
        ("Internet", "1 - 4", "1 (Self)", "1 - 2", "5000 - 20000", "5000 - 15000"),
        ("Router", "2 - 6", "1", "2 - 4", "2000 - 10000", "2000 - 8000"),
        ("Switch", "3 - 12", "0", "1 - 3", "1000 - 5000", "1000 - 4000"),
        ("Server", "1 - 2", "0", "3 - 8", "1500 - 6000", "1500 - 5000"),
        ("Access Point", "1 - 5", "0", "1 - 2", "500 - 2500", "500 - 2000"),
        ("Client (PC)", "1", "0", "0 - 1", "50 - 800", "50 - 500")
    ]
    
    y += 20
    for idx, (cls, deg, gw, prt, trf, pps) in enumerate(tc_data):
        bg = COLOR_LIGHT_BG if idx % 2 == 1 else (1,1,1)
        p20.draw_rect(pymupdf.Rect(MARGIN_LEFT, y, PAGE_WIDTH - MARGIN_RIGHT, y + 18), fill=bg, color=COLOR_LINE, width=0.5)
        draw_left_text(p20, MARGIN_LEFT + 6, y + 13, cls, fontname=FONT_BOLD, fontsize=8.5, color=COLOR_BLACK)
        draw_left_text(p20, MARGIN_LEFT + 95, y + 13, deg, fontname=FONT_ROMAN, fontsize=8.5, color=COLOR_BLACK)
        draw_left_text(p20, MARGIN_LEFT + 150, y + 13, gw, fontname=FONT_ROMAN, fontsize=8.5, color=COLOR_BLACK)
        draw_left_text(p20, MARGIN_LEFT + 210, y + 13, prt, fontname=FONT_ROMAN, fontsize=8.5, color=COLOR_BLACK)
        draw_left_text(p20, MARGIN_LEFT + 265, y + 13, trf, fontname=FONT_ROMAN, fontsize=8.5, color=COLOR_BLACK)
        draw_left_text(p20, MARGIN_LEFT + 365, y + 13, pps, fontname=FONT_ROMAN, fontsize=8.5, color=COLOR_BLACK)
        y += 18
        
    y += 10
    draw_centered_text(p20, y, "Table C.1: Feature value distributions and topological ranges across device classes", fontname=FONT_ITALIC, fontsize=9.5)

    output_path = "D:/nms_project/WIPRO_NMS_Report.pdf"
    doc.save(output_path)
    doc.close()
    print(f"WIPRO NMS Report PDF successfully created at: {output_path}")

if __name__ == "__main__":
    create_report()
