# -*- coding: utf-8 -*-
"""Page bodies for the AI4SM Lab site.

Text is carried over from the previous site. Obvious typos were corrected
(proceedings, anomalies, existing, causal inference, Division, automated,
Networking, Deanship of Research) and the house style is American English with
no em dashes.
"""

LEAFLET = ('<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">\n'
           '<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>\n')

PILLARS = [
    ("Situational awareness",
     "Multimodal sensing and perception, vulnerable road user behavior and intent prediction, "
     "cooperative perception, and contextual observability for software-defined vehicles."),
    ("Reasoning and action",
     "Agentic AI systems that connect perception, reasoning, and action, together with causal "
     "inference for root-cause analysis in complex mobility systems."),
    ("Optimization",
     "Routing, supply and demand matching, resource allocation, and eco-efficient last-mile "
     "delivery across people mobility, logistics, and transportation infrastructure."),
]

CURRENT_PROJECTS = [
    ("images/CAV_Safety.png",
     "Enhancing Safety and Trust in Mixed Traffic Environments with Connected and Automated Vehicles",
     ["The project aims to enhance safety and trust in mixed traffic environments by developing an "
      "integrated framework for interactions between Connected and Automated Vehicles (CAVs) and "
      "Vulnerable Road Users (VRUs). The research combines multimodal sensing, perception, behavior "
      "and intent prediction, VRU adversarial behavior recognition, cooperative perception, and "
      "risk-aware decision-making to enable automated vehicles to recognize both normal and "
      "potentially unsafe or adversarial VRU behaviors and respond appropriately. The framework will "
      "be validated through advanced simulation, hardware-in-the-loop, vehicle-in-the-loop, and "
      "controlled field testing, supporting Saudi Vision 2030 goals for safe, trustworthy, and "
      "human-centered autonomous mobility."],
     "KFUPM Deanship of Research", "2026 to 2029"),

    ("images/SDV.png",
     "Contextual Observability of Software-Defined Vehicles",
     ["SDV architecture decouples hardware and software, enabling OEMs to manage, update, and enhance "
      "vehicle features and functions through software alone. However, SDVs introduce unique "
      "challenges in ensuring system resilience, reliability, and real-time fault diagnosis. "
      "Observability is critical in such environments but remains underdeveloped for SDVs. This "
      "project aims to develop a testbed for SDV contextual observability that enables collecting "
      "multimodal telemetry data, facilitating continuous monitoring, advanced analytics, causal "
      "inferencing, and automated incident response."],
     "IRC for Smart Mobility and Logistics (SML) at KFUPM", "2025 to 2027"),

    ("images/SIM.png",
     "Agentic AI-based Framework for Seamless Integrated Mobility",
     ["Aligning with Saudi Vision 2030, this project supports Saudi Arabia's goals to increase public "
      "transit use and improve accessibility for all citizens, including individuals with "
      "disabilities, the elderly, and low-income groups. The research focuses on developing an "
      "agentic AI-based framework for Seamless Integrated Mobility (SIM), envisioned as a unified "
      "platform that integrates multimodal transportation options."],
     "KFUPM Deanship of Research", "2025 to 2027"),

    ("images/Last_mile.jpg",
     "SmartDispatch: AI-driven Optimization for Eco-Efficient Last-Mile Delivery",
     ["Saudi Arabia is a major market for eCommerce, with a growing number of people shopping online "
      "regularly. This growth has driven an increase in last-mile delivery services, creating a need "
      "for more efficient digital platforms. This project addresses the eco-efficient and adaptive "
      "routing problem during both liveheading and deadheading states of delivery vehicles, including "
      "trucks, cars, cargo bikes, and motorcycles. By optimizing last-mile delivery routes, the "
      "project contributes to Saudi Arabia's goal of significantly reducing transportation costs by "
      "2030."],
     "IRC for Smart Mobility and Logistics (SML) at KFUPM", "2025 to 2026"),
]

# (image, video url or None, title, paragraphs, funder or None, duration or None, topics or None)
PAST_PROJECTS = [
    ("images/GM.png", None, "General Motors Projects",
     ["Before joining KFUPM, the PI served as the AI and Smart Mobility Technical Leader at General "
      "Motors Canada. He led AI/ML projects focused on software-defined vehicles, connected and "
      "automated driving technologies, active safety systems, and prognostics, achieving successful "
      "technology insertions. He co-invented and filed 72 patents, trade secrets, and defensive "
      "publications, earning recognition as &ldquo;Inventor of the Month&rdquo; multiple times by "
      "GM's Global Patent &amp; Invention Management team. The advanced features developed were for "
      "future GM vehicle models; therefore, further details cannot be disclosed due to "
      "confidentiality agreements with GM. Additional information about the filed patents can be "
      "found <a href=\"https://alaakhamis.org/publications.html\" target=\"_blank\" "
      "rel=\"noopener noreferrer\">here</a>."],
     None, None, None),

    ("images/VRU.png", None, "VRU Crossing Intent Prediction",
     ["This research project introduces an innovative framework for pedestrian crossing intention "
      "prediction. The framework incorporates an image enhancement pipeline, which enables the "
      "detection and rectification of various defects that may arise during unfavorable weather "
      "conditions. Subsequently, a transformer-based network, featuring a self-attention mechanism, "
      "is employed to predict the crossing intentions of target pedestrians. This augmentation "
      "enhances the model's resilience and accuracy in classification tasks. Through evaluation on "
      "the JAAD dataset, our framework attains state-of-the-art performance while maintaining a "
      "notably low inference time. Moreover, a deployment environment is established to assess the "
      "real-time performance of the model."],
     "IoT Research Laboratory, Ontario Tech University", "2022 to 2024",
     "image enhancement, self-attention, vision transformers"),

    ("images/Robustness.png", None, "Robustness of Deep Learning-based VRU Detection Models",
     ["This research project highlights the critical role of accurate pedestrian detection in "
      "assisted and automated driving systems to enhance road safety. Real-world deployment faces "
      "challenges like image corruption and occlusions, addressed here through robust, stylized, and "
      "occluded training techniques. Robust training uses intentionally corrupted examples to "
      "simulate real-world scenarios, significantly improving model resilience. Stylized training "
      "employs Adaptive Instance Normalization (AdaIN) to introduce texture and style variations, "
      "enriching the dataset. Occluded training generates datasets simulating different occlusion "
      "levels, improving performance on occluded samples. Together these methods achieve a 2 to 4 "
      "percent performance boost, establishing a foundation for deploying reliable pedestrian "
      "detection models in complex environments."],
     "Nile University", "2022 to 2024",
     "assisted and automated driving, VRU detection, model robustness"),

    ("images/Bus.png", None, "Optimal Placement of Bus Stops",
     ["Bus systems play an important role in the modern city, and carefully designed bus stop "
      "locations can lift overall transportation efficiency and save time for passengers. A Particle "
      "Swarm Optimization (PSO)-based approach is proposed to find the optimal placement of bus stops "
      "in the Waterloo and Kitchener area. The selection takes into account neighborhood population, "
      "family income, age distribution, and other factors, with the goal of minimizing average "
      "passenger travel time. Experimental results on real bus lines showed that both PSO and "
      "adaptive PSO provide shorter average commuting time than the original routes, using fewer "
      "stops."],
     "University of Toronto", "2022 to 2023",
     "optimal placement, swarm intelligence, particle swarm optimization"),

    ("images/epaymenet.png", "https://www.youtube.com/watch?v=lWci4P_Q5ho",
     "Future of Public Transport Experience",
     ["E-payment for public transport is a use case built by DM TECH featuring a smart bus-station "
      "experience. The concept was designed to visualize the influence of digitalizing public "
      "transport accessibility, ticketing, and payment. The experience is also available in VR for "
      "user-friendly and interactive simulation.",
      "This work was conducted under direct supervision of the PI in his capacity as CTO of "
      "Disruptive Mobility Tech (DMTech)."],
     None, None, None),

    ("images/smartcity.png", "https://www.youtube.com/watch?v=GIWQZ4giurE", "Smart City Walkthrough",
     ["A smart city concept designed by the DM TECH Experience Design team. The concept features a "
      "street walkthrough integrating different technologies to support a smarter, sustainable, and "
      "personalized city experience. The experience is also available in VR for user-friendly and "
      "interactive simulation.",
      "This work was conducted under direct supervision of the PI in his capacity as CTO of "
      "Disruptive Mobility Tech (DMTech)."],
     None, None, None),

    ("images/AV.png", "https://www.youtube.com/watch?v=gT1hhBZg5dU",
     "Virtual Ride Experience for Autonomous Driving",
     ["A virtual ride experience for autonomous driving built around Responsibility-Sensitive Safety "
      "(RSS), the model-based approach to safety introduced by Mobileye (Shalev-Shwartz et al., "
      "2017). RSS highlights five safety rules an automated driving vehicle should follow: safe "
      "distance, cutting in, right of way, limited visibility, and avoiding crashes without causing "
      "another one. The environment, vehicle interior, and assessment criteria were built to enable "
      "virtual testing and passenger-centric feedback collection using VR.",
      "This work was conducted under direct supervision of the PI in his capacity as CTO of "
      "Disruptive Mobility Tech (DMTech)."],
     None, None, None),

    ("images/Hyperloop.png", "https://www.youtube.com/watch?v=uSGsItMBHnQ",
     "Hyperloop Station Concept: El-Waha Revival",
     ["The El-Waha (The Oasis) Hyperloop station concept simulates the contribution of transportation "
      "technology to building the future. The revival story features accessibility, availability, "
      "smartness, and design creativity to support smart city infrastructure and user expectations. "
      "The architecture concept, design, model, and visualization are owned by DM TECH. The "
      "experience is also available in VR.",
      "This work was conducted under direct supervision of the PI in his capacity as CTO of "
      "Disruptive Mobility Tech (DMTech)."],
     None, None, None),

    ("images/testbed.png", "https://www.youtube.com/watch?v=n5RzepPWwbU", "Hyperloop Lab Facility",
     ["A quick tour of the first Hyperloop lab facility in the world. The Hyperloop is a disruptive "
      "solution for the future of mobility and high-speed transport, yet information accessibility "
      "and testing availability remain limited worldwide. This lab facility can be used for "
      "professional and educational training on Hyperloop and related technologies, allowing "
      "students, trainees, and researchers to study and experiment with disruptive transportation "
      "systems.",
      "This work was conducted under direct supervision of the PI in his capacity as CTO of "
      "Disruptive Mobility Tech (DMTech)."],
     None, None, None),

    ("images/Z21.png", "https://www.youtube.com/watch?v=h-SNTHZiomE", "Fa&ccedil;ade Cleaning Robot",
     ["Z21 is a smart automated fa&ccedil;ade cleaning system comprising a rooftop robot and a "
      "cleaning robot. The rooftop robot is a two-degrees-of-freedom motorized gantry crane "
      "responsible for positioning the cleaning robot and carrying the cleaning reagent tanks, "
      "hanging cables, and computation tools. The cleaning robot is equipped with advanced motion and "
      "stabilization mechanisms and can automatically inspect and clean glass windows and "
      "fa&ccedil;ades, with much higher cleaning capacity than state-of-the-art systems and manual "
      "cleaning, and is designed to work in severe weather conditions.",
      "This work was conducted under direct supervision of the PI in his capacity as AI Division "
      "Head at Sypron Solutions."],
     None, None, None),

    ("images/Agatha.png", "https://www.youtube.com/watch?v=tceMP_r89-4", "Agatha",
     ["Predictive maintenance is a cornerstone of Industry 4.0. Agatha is a predictive maintenance "
      "system built on cognitive IoT. It encompasses spatially distributed, interoperable, and "
      "accessible smart sensors able to selectively collect, fuse, and share data about machine "
      "condition. The fused data is analyzed to produce real-time insights, determine and dynamically "
      "update the likelihood of failures, and make timely decisions or recommendations. Maintenance "
      "schedules can be planned without costly downtime: productivity increases, equipment lifetime "
      "is extended, energy is saved, and unplanned stops are reduced or eliminated.",
      "This system was architected by the PI in his capacity as AI Division Head at Sypron "
      "Solutions."],
     None, None, None),

    ("images/MineProbe.png", "https://www.youtube.com/watch?v=FP61hqxA2fM", "MineProbe",
     ["MineProbe is a minefield reconnaissance and mapping system encompassing a number of spatially "
      "distributed unmanned ground vehicles (UGVs) equipped with an efficient multimodal landmine and "
      "unexploded ordnance (UXO) detection system and an accurate hybrid localization system. The "
      "UGVs move fluidly and efficiently in the rough terrain of the North West Coast of Egypt. A "
      "centimeter-level accuracy outdoor hybrid localization system was developed in this project, "
      "along with a GPR-EMI dual sensor for landmine detection with high detection rates and low "
      "false alarms. The system produces a mine map showing the exact locations of detected landmines "
      "and UXOs.",
      "This project was conducted under direct supervision of the PI in his capacity as Autonomous "
      "Vehicles Professor at Zewail City, Consultant at InnoVision, and PI of MineProbe."],
     None, None, None),
]

COLLABORATOR_UNIS = [
    ("University of Toronto", 43.6629, -79.3957, "https://www.utoronto.ca"),
    ("Ontario Tech University", 43.9456, -78.8967, "https://ontariotechu.ca"),
    ("Carlos III University of Madrid", 40.3326, -3.7677, "https://www.uc3m.es"),
    ("Nile University", 30.0272, 31.0139, "https://nu.edu.eg"),
    ("Julius-Maximilians-Universit&auml;t W&uuml;rzburg", 49.7876, 9.9352, "https://www.uni-wuerzburg.de"),
    ("University of Waterloo", 43.4723, -80.5449, "https://uwaterloo.ca"),
    ("University of New Brunswick", 45.9454, -66.6421, "https://www.unb.ca"),
    ("Virginia Tech", 37.2296, -80.4243, "https://www.vt.edu"),
    ("Federal University of Rio Grande do Sul", -30.0346, -51.2177, "https://www.ufrgs.br"),
    ("Zhejiang University", 30.2638, 120.1230, "https://www.zju.edu.cn/english"),
    ("Universidad Cat&oacute;lica del Norte", -23.6436, -70.3994, "https://www.ucn.cl"),
    ("&Oacute;buda University", 47.5636, 19.0843, "https://www.uni-obuda.hu"),
    ("FARI Institute", 50.845889, 4.357649, "https://fari.brussels"),
    ("Amrita University", 11.0240, 76.9278, "https://www.amrita.edu"),
]

RESEARCHERS = [
    ("images/team/Ousman.jpeg", "Ousman Khan", "PhD Student",
     [("linkedin", "https://www.linkedin.com/in/ousman-khan-ab3696146/")]),
    ("images/team/Usman.png", "Usman Ibrahim", "PhD Student",
     [("linkedin", "https://www.linkedin.com/in/usman-ibrahim-314a54277")]),
    ("images/team/Mahmoud.png", "Mahmoud Hamza", "PhD Student",
     [("linkedin", "https://www.linkedin.com/in/mahmoudhamza2020/")]),
    ("images/team/Muhsen.jpg", "Abdulmuhsen Fawzi Fakih", "Undergraduate Researcher",
     [("linkedin", "https://www.linkedin.com/in/abdulmuhsen-fakih/")]),
    ("images/AI4SM_lab.png", "Banan Al-Shahrani", "Undergraduate Researcher",
     [("linkedin", "https://www.linkedin.com/in/banan-abdullah-2100a7336/")]),
]

COLLABORATORS = [
    ("images/team/Dr_Masoud.jpg", "Dr. Mahmoud Masoud", "Associate Professor at KFUPM",
     [("linkedin", "https://www.linkedin.com/in/mahmoud-masoud-74195016b/"),
      ("scholar", "https://scholar.google.com/citations?user=9aaJNEkAAAAJ&hl=en"),
      ("researchgate", "https://www.researchgate.net/profile/Mahmoud-Masoud-3")]),
    ("images/team/Zishan.png", "Zishan Yusuf", "External collaborator<br>Amazon supply chain expert",
     [("linkedin", "https://www.linkedin.com/in/zishan-yusuf/")]),
    ("images/OTU.png", "IoT Lab", "Ontario Tech University",
     [("web", "https://iotresearchlab.ca/")]),
    ("images/SusRobotics.png", "Sustainable Robotics Group", "International research group",
     [("web", "https://www.sustainablerobotics.org/")]),
]

FACILITIES = [
    ("images/AV2.png", "Assisted and Automated Driving Research Platform",
     "A state-of-the-art platform supporting research across perception, planning, control, "
     "connectivity, and remote operation. It enables comprehensive experimentation across the full "
     "driving stack, supporting sensor fusion from LiDAR, radar, and cameras, along with real-time "
     "object detection and tracking for situational awareness. Advanced planning and control modules "
     "facilitate research in motion prediction, trajectory generation, and adaptive vehicle control "
     "for both assisted and fully automated driving scenarios. Connectivity features enable "
     "exploration of cooperative driving concepts using Vehicle-to-Everything (V2X) communication, "
     "while the tele-driving module supports studies on remote vehicle operation and supervision."),

    ("images/SDV_testbed.png", "Software-Defined Vehicle (SDV) Testbed",
     "An open, modular, software-defined architecture that decouples hardware and software layers and "
     "follows a centralized zonal design aligned with modern automotive electronic and electrical "
     "(E/E) systems. The platform allows researchers to develop, deploy, and test new functionalities "
     "independently of physical vehicle components. Vehicle functions are consolidated into powerful "
     "computing domains connected through high-speed networks, enabling research into over-the-air "
     "software updates, embedded intelligence, cross-domain integration, and real-time data "
     "processing. The platform also supports experimentation with digital twins, edge computing, and "
     "AI-driven control strategies."),

    ("images/dreamKit.jpg", "SDV Prototyping Platforms: dreamKIT and digital.auto",
     "The lab leverages dreamKIT and digital.auto as complementary platforms for rapid prototyping, "
     "experimentation, and education in software-defined vehicles. dreamKIT provides a hands-on "
     "environment for developing and demonstrating SDV concepts, enabling researchers and students to "
     "experiment with vehicle functions, sensors, interfaces, and software applications without "
     "requiring a full-scale vehicle. digital.auto complements this with an open, collaborative "
     "ecosystem for prototyping software-defined vehicle functionality using standardized vehicle "
     "APIs and virtual vehicle environments. Together they provide a flexible bridge between software "
     "prototyping and deployment on the lab's physical SDV testbed."),

    ("images/Spark.jpg", "High-Performance Computing Workstations",
     "The lab is equipped with high-performance computing resources that enable data-intensive "
     "research and advanced simulation studies. The facility includes two NVIDIA DGX Spark systems "
     "with 4 TB storage and integrated DLI bundles, providing GPU computing capabilities for deep "
     "learning, perception, and control algorithm development. These systems are complemented by Dell "
     "Precision 5860 workstations powered by Intel Xeon W3-2423 processors and Dell U4025QW "
     "UltraSharp 40-inch curved Thunderbolt hub monitors, providing a powerful environment for "
     "software development, large-scale data visualization, simulation, and AI model training."),
]

BOOKS = [
    ("images/SM.jpg", "Smart Mobility: Exploring Foundational Technologies and Wider Impacts",
     "Alaa Khamis. Apress (Springer Nature), 2021.",
     [("web", "https://link.springer.com/book/10.1007/978-1-4842-7101-8", "Publisher"),
      ("amazon", "https://www.amazon.com/Smart-Mobility-Exploring-Foundational-Technologies-ebook/dp/B097GM1NF6", "Amazon"),
      ("scholar", "https://scholar.google.ca/citations?view_op=view_citation&hl=en&user=btM72xsAAAAJ&cstart=20&pagesize=80&sortby=pubdate&citation_for_view=btM72xsAAAAJ:ZfRJV9d4-WMC", "Scholar")]),
    ("images/OptimizationAlgorithms.jpeg",
     "Optimization Algorithms: AI techniques for design, planning, and control problems",
     "Alaa Khamis. Manning Publications, ISBN 978-1633438835, 2024.",
     [("web", "https://www.manning.com/books/optimization-algorithms", "Publisher"),
      ("github", "https://github.com/Optimization-Algorithms-Book/Code-Listings", "Code"),
      ("amazon", "https://www.amazon.com/Optimization-Algorithms-techniques-planning-problems/dp/163343883X", "Amazon"),
      ("scholar", "https://scholar.google.ca/citations?view_op=view_citation&hl=en&user=btM72xsAAAAJ&sortby=pubdate&citation_for_view=btM72xsAAAAJ:a9-T7VOCCH8C", "Scholar")]),
]

JOURNALS = [
    ("Alaa Khamis.", "Agentic Ontology-guided Image Generation and Evaluation for Rare-Event Data Augmentation in Safety-Critical Perception",
     "Array, 2026.",
     [("web", "https://doi.org/10.1016/j.array.2026.100932", "DOI"),
      ("github", "https://github.com/ai4smlab/Rare-Event-Data-Augmentation", "Code")]),
    ("Alaa Khamis.", "Design and Evaluation of an Agentic AI Framework for Personalized Umrah Trip Planning",
     "Arabian Journal for Science and Engineering, 2026.",
     [("web", "https://rdcu.be/eY50o", "Paper")]),
    ("Alaa Khamis.", "Agentic AI Systems: Architecture and Evaluation using a Frictionless Parking Scenario",
     "IEEE Access, 2025.",
     [("web", "https://ieeexplore.ieee.org/abstract/document/11083588", "IEEE Xplore"),
      ("scholar", "https://scholar.google.ca/citations?view_op=view_citation&hl=en&user=btM72xsAAAAJ&sortby=pubdate&citation_for_view=btM72xsAAAAJ:raTqNPD5sRQC", "Scholar")]),
    ("Alaa Khamis.", "Smart Mobility Education and Capacity Building for Sustainable Development: A Review and Case Study",
     "Sustainability 17, 7999, 2025.",
     [("web", "https://www.mdpi.com/2071-1050/17/17/7999", "Paper")]),
    ("Alaa Khamis and Partha Goswami.", "Rethinking Vehicle Architecture Through Softwarization and Servitization",
     "IEEE Access, 2025.",
     [("web", "https://ieeexplore.ieee.org/abstract/document/11078249", "IEEE Xplore"),
      ("scholar", "https://scholar.google.ca/citations?view_op=view_citation&hl=en&user=btM72xsAAAAJ&sortby=pubdate&citation_for_view=btM72xsAAAAJ:YsrPvlHIBpEC", "Scholar")]),
    ("Ahmed Elgazwy, Khalid Elgazzar, and Alaa Khamis.", "Predicting Pedestrian Crossing Intentions in Adverse Weather with Self-Attention Models",
     "IEEE Transactions on Intelligent Transportation Systems (T-ITS), 2025.",
     [("web", "https://ieeexplore.ieee.org/abstract/document/10878122", "IEEE Xplore"),
      ("github", "https://github.com/ahmedelgazwy/Predicting-Pedestrian-Crossing-Intentions-in-Adverse-Weather-with-Self-Attention-Models", "Code"),
      ("scholar", "https://scholar.google.ca/citations?view_op=view_citation&hl=en&user=btM72xsAAAAJ&sortby=pubdate&citation_for_view=btM72xsAAAAJ:KNjnJ3z-R6IC", "Scholar")]),
]

CONFERENCES = [
    ("Mohammed Alromema, Osamah H. Hussein, Ahmed AlHanbli, Ahmed Azab, and Alaa Khamis.",
     "Hybrid Optimization Framework for Crowdsourced Last-Mile Delivery",
     "IEEE International Conference on Smart Mobility, 2026.",
     [("web", "https://ieeexplore.ieee.org/abstract/document/11614133/", "IEEE Xplore"),
      ("github", "https://github.com/ai4smlab/Crowdsourced-LMD", "Code")]),
    ("Ahmed Senan, Zead Saleh, Ahmad Al Hanbali, and Alaa Khamis.",
     "Adaptive Metaheuristic Optimization for 3PL Vehicle Routing",
     "IEEE International Conference on Smart Mobility, 2026.",
     [("web", "https://ieeexplore.ieee.org/abstract/document/11614081", "IEEE Xplore"),
      ("github", "https://github.com/ai4smlab/3PL-VRP-Metaheuristics", "Code")]),
    ("Rahaf M. Alzahrani, Zead Saleh, and Alaa Khamis.",
     "A Comparative Study of Two-Phase Clustering-TSP and DQN-Enhanced Metaheuristic Approaches for CVRP",
     "Transportation Research Procedia, Volume 96, 2026.",
     [("web", "https://www.sciencedirect.com/science/article/pii/S2352146526002474", "Paper"),
      ("github", "https://github.com/ai4smlab/Beverage-Distribution-Logistics", "Code")]),
    ("Mahmoud Masoud, Amera Mohamed, Alaa Khamis, Mohammed Elhenawy, and Karim Asif Sattar.",
     "Vision-based Camel Detection and VMS Alert System for Enhanced Road Safety in KSA",
     "Transportation Research Procedia, Volume 96, 2026.",
     [("web", "https://www.sciencedirect.com/science/article/pii/S2352146526003121", "Paper")]),
    ("Md. Aqib Aman, Ashiqur Rahman Ashiq, Alaa Khamis, Ahmad Al-Hanbali, and Ahmed Ghaithan.",
     "Deadheading Minimization in Last-Mile Delivery",
     "Transportation Research Procedia, Volume 96, 2026.",
     [("web", "https://www.sciencedirect.com/science/article/pii/S2352146526003339", "Paper")]),
    ("Alaa Khamis.", "Agentic AI for Personalized Trip Planning",
     "2025 IEEE Global Conference on Artificial Intelligence and Internet of Things (GCAIoT), Marrakech, Morocco, 2025.",
     [("web", "https://ieeexplore.ieee.org/document/11275553", "IEEE Xplore")]),
    ("Ousman Khan and Alaa Khamis.", "Heuristics-based Resource Allocation in Software-defined Vehicles",
     "2025 IEEE Global Conference on Artificial Intelligence and Internet of Things (GCAIoT), Marrakech, Morocco, 2025.",
     [("web", "https://ieeexplore.ieee.org/document/11275567", "IEEE Xplore"),
      ("github", "https://github.com/ai4smlab/SDV-Resource-Allocation", "Code")]),
    ("Ziqi Zhou, Jingyue Zhang, Jingyuan Zhang, Boyue Wang, Tianyu Shi, and Alaa Khamis.",
     "Human-centric Reward Optimization for Reinforcement Learning-based Automated Driving using Large Language Models",
     "TRB Annual Meeting, Washington, D.C., 2026. arXiv:2405.04135.",
     [("arxiv", "https://arxiv.org/abs/2405.04135", "arXiv"),
      ("scholar", "https://scholar.google.ca/citations?view_op=view_citation&hl=en&user=btM72xsAAAAJ&pagesize=80&sortby=pubdate&citation_for_view=btM72xsAAAAJ:LO7wyVUgiFcC", "Scholar")]),
    ("Haowei Li, Mufeng Wang, Jiarui Zhang, Tianyu Shi, and Alaa Khamis.",
     "A Contextual Multi-armed Bandit Approach to Personalized Trip Itinerary Planning",
     "2024 IEEE International Conference on Smart Mobility (SM), 2024.",
     [("scholar", "https://scholar.google.ca/citations?view_op=view_citation&hl=en&user=btM72xsAAAAJ&sortby=pubdate&citation_for_view=btM72xsAAAAJ:DUooU5lO8OsC", "Scholar")]),
    ("Tamas Haidegger, Vincent Mai, Carl M&ouml;rch, Dominik B. O. Boesl, An Jacobs, Alaa Khamis, Luca Lach, and Bram Vanderborght.",
     "Sustainable Robotics: Translating the UN Sustainable Development Goals to our Domain",
     "40th Anniversary of the IEEE Conference on Robotics and Automation, 2024.",
     [("scholar", "https://scholar.google.ca/citations?view_op=view_citation&hl=en&user=btM72xsAAAAJ&sortby=pubdate&citation_for_view=btM72xsAAAAJ:NXb4pA-qfm4C", "Scholar")]),
]

TALKS = [
    ("Agentic AI: Connecting Perception, Reasoning, and Action in Smart Mobility and Logistics",
     "School of Business Public Seminar, KFUPM", "April 16, 2026", "talks/Agentic_AI.pdf"),
    ("Agentic AI for Smart Mobility", "ISE Seminar Series, KFUPM", "November 5, 2025",
     "talks/Agentic_AI_for_SM.pdf"),
    ("Automotive AI: From Situational Awareness to Automation and Optimization",
     "ICS/SWE Seminar Series, KFUPM", "November 3, 2025", "talks/Automotive_AI.pdf"),
    ("AI for Smart Mobility",
     "IEEE International Conference on Smart Applications, Communications and Networking "
     "(SmartNets 2024), Harrisonburg and Washington DC, USA", "May 28 to 30, 2024", None),
    ("Smart Mobility for Traffic Safety",
     "Sixth International Traffic Safety Forum and Exhibition, Dammam, Saudi Arabia", "2023",
     "https://www.researchgate.net/publication/376380220_Smart_Mobility_for_Traffic_Safety"),
    ("Smart Mobility for Sustainable Development Goals: Enablers and Barriers",
     "FARI Conference: Local and Sustainable AI, Data, and Robotics, Brussels, Belgium", "2023",
     "https://www.researchgate.net/publication/374119615_Smart_Mobility_for_Sustainable_Development_Goals_Enablers_and_Barriers"),
    ("Smart Mobility Foundational Technologies, Technology Enablers and Disruptors",
     "IEEE International Conference on Smart Mobility (IEEE SM'22)", "2022",
     "https://www.researchgate.net/publication/359193494_Smart_Mobility_Foundational_Technologies_Technology_Enablers_and_Disruptors"),
]

NEWS = [
    ("2026", 'As part of KFUPM&rsquo;s Ibn Battuta Global Scholarship Program, Dr. Alaa Khamis spent '
             'June and July 2026 as a Visiting Professor at the <a href="https://uttri.utoronto.ca/" '
             'target="_blank" rel="noopener noreferrer">University of Toronto Transportation Research '
             'Institute (UTTRI)</a>, collaborating on a research project focused on adaptive traffic '
             'signal control.', None),
    ("2026", 'Our paper &ldquo;Agentic Ontology-guided Image Generation and Evaluation for Rare-Event '
             'Data Augmentation in Safety-Critical Perception&rdquo; has been accepted for publication '
             'in <em>Array</em>. The paper is available <a href="https://doi.org/10.1016/j.array.2026.100932" '
             'target="_blank" rel="noopener noreferrer">here</a>.', None),
    ("2026", 'Dr. Alaa Khamis gave a seminar titled &ldquo;Agentic AI: Connecting Perception, '
             'Reasoning, and Action in Smart Mobility and Logistics&rdquo; at the KFUPM Business '
             'School. Slides are available <a href="talks/Agentic_AI.pdf" target="_blank" '
             'rel="noopener noreferrer">here</a>.', None),
    ("2025", 'Dr. Alaa Khamis has been appointed Founding Chair of the '
             '<a href="https://ieee-itss.org/chapters-committees/saudi-chapter/" target="_blank" '
             'rel="noopener noreferrer">IEEE Intelligent Transportation Systems Society (ITSS) Saudi '
             'Arabia Chapter</a>, leading the establishment and development of the Society&rsquo;s '
             'activities within the Kingdom.', None),
    ("2025", 'Dr. Alaa Khamis gave a seminar titled &ldquo;Agentic AI for Smart Mobility&rdquo; as '
             'part of the ISE seminar series at KFUPM. Slides are available '
             '<a href="talks/Agentic_AI_for_SM.pdf" target="_blank" rel="noopener noreferrer">here</a>.', None),
    ("2025", 'Dr. Alaa Khamis gave a seminar titled &ldquo;Automotive AI: From Situational Awareness '
             'to Automation and Optimization&rdquo; as part of the ICS/SWE seminar series at KFUPM. '
             'Slides are available <a href="talks/Automotive_AI.pdf" target="_blank" '
             'rel="noopener noreferrer">here</a>.', None),
    ("2025", 'Our papers &ldquo;<a href="https://ieeexplore.ieee.org/abstract/document/11083588" '
             'target="_blank" rel="noopener noreferrer">Agentic AI Systems: Architecture and '
             'Evaluation using a Frictionless Parking Scenario</a>&rdquo; and &ldquo;'
             '<a href="https://ieeexplore.ieee.org/abstract/document/11078249" target="_blank" '
             'rel="noopener noreferrer">Rethinking Vehicle Architecture Through Softwarization and '
             'Servitization</a>&rdquo; have been accepted for publication by IEEE Access.', None),
    ("2025", 'The AI for Smart Mobility Lab team won first place in the '
             '<a href="https://umrah.sspchallenge.com/en/" target="_blank" rel="noopener noreferrer">'
             'Sustainable Solutions for Pilgrims Challenge (Umrah Challenge)</a>, part of the Umrah '
             'and Ziyarah Forum (UZF) organized by the Ministry of Hajj and Umrah in Al-Madinah from '
             'April 14 to 16, 2025. The competition featured 153 participants from 21 countries '
             'across two tracks: ideas and startups. Our patent-pending solution enables natural '
             'interaction, personalized end-to-end planning, and over-the-air updatable service '
             'bundles for local and international Umrah performers.',
     ("images/Wasel.jpeg", "AI4SM Lab team receiving the first-place award at the Umrah and Ziyarah Forum 2025")),
    ("2025", 'Our paper with Ahmed Elgazwy and Khalid Elgazzar titled &ldquo;Predicting Pedestrian '
             'Crossing Intentions in Adverse Weather with Self-Attention Models&rdquo; has been '
             'accepted for publication in IEEE Transactions on Intelligent Transportation Systems '
             '(T-ITS).', None),
    ("2025", 'Professor Hesham Rakha of Virginia Tech and Dr. Alaa Khamis are co-editing a special '
             'issue of <em>Sustainability</em> (Impact Factor 3.3, CiteScore 6.8) titled '
             '<a href="https://www.mdpi.com/journal/sustainability/special_issues/U6O0IQ11RS" '
             'target="_blank" rel="noopener noreferrer">Smart Mobility for Sustainable Development</a>.', None),
    ("2025", 'Two postdoctoral fellow positions are available to join the AI for Smart Mobility Lab at '
             'KFUPM. These positions focus on agentic AI for seamless integrated mobility and '
             'contextual observability of software-defined vehicles. Learn more on the '
             '<a href="join.html">Join</a> page.', None),
    ("2024", 'The proceedings of the 2024 IEEE International Conference on Smart Mobility (SM\'24) '
             'are now available on <a href="https://ieeexplore.ieee.org/xpl/conhome/1846284/all-proceedings" '
             'target="_blank" rel="noopener noreferrer">IEEE Xplore</a>.', None),
]

# (anchor, title, track, intro, responsibilities, required, preferred, offer)
POSITIONS = [
    ("postdoc-sdv", "Postdoctoral Researcher in SDVs and Contextual Observability",
     "Software-Defined Vehicles",
     'We are seeking a highly motivated postdoctoral researcher to join a new project funded by the '
     '<a href="https://ri.kfupm.edu.sa/irc-sml" target="_blank" rel="noopener noreferrer">'
     'Interdisciplinary Research Center for Smart Mobility and Logistics</a>. This position offers a '
     'unique opportunity to contribute to cutting-edge advancements in software-defined vehicles '
     '(SDVs), software observability, data analytics, causal inference, and system resilience.',
     ["Develop and implement a testbed for contextual observability, using open-source tools to collect and analyze multimodal telemetry data from SDVs.",
      "Design and evaluate techniques for real-time fault detection, anomaly identification, and trend analysis.",
      "Conduct research in causal inference to recognize the root causes of identified anomalies.",
      "Explore and prototype automated incident response systems for real-time troubleshooting in SDVs.",
      "Publish high-impact research findings in leading journals and present results at international conferences."],
     ["PhD in computer science or engineering, systems engineering, or a related field, with expertise in one or more of: software-defined systems, cyber-physical systems, software observability.",
      "A solid understanding of existing and emerging machine learning techniques.",
      "Proficiency in programming languages such as Python and C++, preferably both.",
      "Strong analytical and problem-solving skills, with experience in data collection and analysis from complex systems.",
      "Excellent communication and interpersonal skills.",
      "Demonstrated ability to conduct independent research and collaborate within multidisciplinary teams."],
     ["Familiarity with service-oriented and microservice architectures.",
      "Expertise in data serialization languages such as YAML, JSON, and Protobuf, as well as data distribution and messaging protocols such as MQTT and Zenoh.",
      "Expertise in API protocols such as REST, GraphQL, WebSocket, and gRPC, along with query languages such as SQL, KQL, PromQL, and LogQL.",
      "Knowledge of causal modeling."],
     ['Competitive salary and benefits package. More information is available <a href="https://postdoc.kfupm.edu.sa/policies-salaries-and-benefits.html" target="_blank" rel="noopener noreferrer">here</a>.',
      "Opportunities to engage with leading experts in smart mobility and logistics."]),

    ("phd-sdv", "PhD Student in SDVs and Contextual Observability", "Software-Defined Vehicles",
     "We are seeking a dedicated PhD student to contribute to advancing the technological foundation "
     "for software-defined vehicles (SDVs). The research will be conducted at KFUPM&rsquo;s "
     "Interdisciplinary Research Center for Smart Mobility and Logistics (SML), focusing on causal "
     "inference for SDVs.",
     ["Develop and refine a testbed for contextual observability, using open-source tools to collect and analyze multimodal telemetry data.",
      "Conduct in-depth studies on causal inference to evaluate the effects of software updates, environmental variations, and network conditions on SDVs.",
      "Present findings at international conferences and publish in peer-reviewed journals."],
     ["Bachelor's or master's degree in computer science or engineering, systems engineering, or a related field.",
      "Background in AI, machine learning, and causal inference.",
      "Proficiency in programming languages such as Python and C++, preferably both.",
      "Demonstrated ability to undertake independent research and solve complex problems."],
     ["Familiarity with DevOps, OpenTelemetry, and observability frameworks.",
      "Expertise in data serialization languages such as YAML, JSON, and Protobuf, as well as data distribution and messaging protocols such as MQTT and Zenoh.",
      "Expertise in API protocols such as REST, GraphQL, WebSocket, and gRPC, along with query languages such as SQL, KQL, PromQL, and LogQL.",
      "Interest in real-time systems and connected vehicle technologies."],
     None),

    ("msc-sdv", "MSc Student in SDVs and Contextual Observability", "Software-Defined Vehicles",
     "We are looking for a motivated MSc student to participate in cutting-edge research on "
     "software-defined vehicles (SDVs). This position offers an opportunity to contribute to advances "
     "in observability, data analytics, and system resilience for SDVs.",
     ["Assist in the development and validation of a testbed for contextual observability in SDVs.",
      "Conduct experiments to collect and analyze telemetry data for real-time system monitoring.",
      "Explore anomaly detection techniques and resource optimization methods for SDVs.",
      "Publish research findings in leading journals and present results at international conferences."],
     ["Bachelor's degree in computer science or engineering, systems engineering, or a related field.",
      "Proficiency in programming languages such as Python and C++, preferably both.",
      "Basic knowledge of artificial intelligence, machine learning, or data analytics.",
      "Strong problem-solving skills and a passion for research."],
     ["Familiarity with DevOps, OpenTelemetry, and observability frameworks.",
      "Expertise in data serialization languages such as YAML, JSON, and Protobuf, as well as data distribution and messaging protocols such as MQTT and Zenoh.",
      "Expertise in API protocols such as REST, GraphQL, WebSocket, and gRPC, along with query languages such as SQL, KQL, PromQL, and LogQL.",
      "Interest in real-time systems and connected vehicle technologies."],
     None),

    ("postdoc-sim", "Postdoctoral Researcher in Seamless Integrated Mobility",
     "Seamless Integrated Mobility",
     "We are seeking a highly motivated postdoctoral researcher to lead cutting-edge research on "
     "developing an AI-based framework for Seamless Integrated Mobility (SIM). This project focuses "
     "on creating an inclusive and unified mobility platform that integrates multimodal "
     "transportation options while addressing the diverse needs of all citizens, including "
     "individuals with disabilities, the elderly, and low-income groups.",
     ["Lead the design and implementation of AI agents for specific mobility functions such as trip planning, service bundling, demand-supply matching, and user profiling.",
      "Conduct comprehensive stakeholder analyses to identify key players in Saudi Arabia's mobility ecosystem and assess current urban mobility challenges.",
      "Develop detailed user personas and use them to inform the design and deployment of the SIM platform.",
      "Prototype and test the SIM platform using real-time data, ensuring adaptability to evolving user needs.",
      "Publish high-impact research findings in leading journals and present results at international conferences."],
     ["PhD in computer science or engineering, AI, transportation engineering, or a related field.",
      "Strong expertise in AI, machine learning, and service-oriented architectures.",
      "Proficiency in programming languages such as Python and C++, preferably both.",
      "Experience in developing and deploying agent-based systems.",
      "Demonstrated ability to conduct independent research and lead complex projects."],
     ["Knowledge of multimodal transportation systems or smart mobility frameworks.",
      "Familiarity with user-centered design methods, including persona development.",
      "Background in urban mobility challenges and solutions.",
      "Expertise in data serialization languages such as YAML, JSON, and Protobuf, as well as data distribution and messaging protocols such as MQTT and Zenoh.",
      "Expertise in API protocols such as REST, GraphQL, WebSocket, and gRPC, along with query languages such as SQL, KQL, PromQL, and LogQL."],
     ['Competitive salary and benefits package. More information is available <a href="https://postdoc.kfupm.edu.sa/policies-salaries-and-benefits.html" target="_blank" rel="noopener noreferrer">here</a>.',
      "Opportunities for interdisciplinary collaboration and engagement with key stakeholders in the mobility sector."]),

    ("phd-sim", "PhD Student in Seamless Integrated Mobility", "Seamless Integrated Mobility",
     "We are looking for a dedicated PhD student to contribute to the development of an AI-based "
     "framework for Seamless Integrated Mobility (SIM). The research will focus on designing and "
     "implementing AI agents and leveraging service-oriented architectures to enhance accessibility, "
     "inclusivity, and efficiency in urban mobility systems.",
     ["Conduct research on AI agents for multimodal transportation functions such as service bundling, demand-supply matching, and personalized service delivery.",
      "Develop user personas and analyze urban mobility challenges to inform platform design.",
      "Prototype AI models for real-time data processing and context-aware mobility services.",
      "Collaborate with the project team to integrate research findings into the SIM platform prototype.",
      "Present research results at academic conferences and publish in peer-reviewed journals."],
     ["Bachelor's or master's degree in computer science or engineering, transportation engineering, or a related field.",
      "Proficiency in programming languages such as Python and C++, preferably both.",
      "Background in AI, machine learning, or agent-based modeling.",
      "Interest in solving urban mobility challenges through innovative technologies."],
     ["Familiarity with service-oriented architectures or multimodal transportation systems.",
      "Experience with user-centered design or persona development.",
      "Expertise in data serialization languages such as YAML, JSON, and Protobuf, as well as data distribution and messaging protocols such as MQTT and Zenoh.",
      "Expertise in API protocols such as REST, GraphQL, WebSocket, and gRPC, along with query languages such as SQL, KQL, PromQL, and LogQL."],
     None),

    ("msc-sim", "MSc Student in Seamless Integrated Mobility", "Seamless Integrated Mobility",
     "We are seeking a motivated MSc student to join a research project focused on developing a "
     "unified AI-based platform for Seamless Integrated Mobility (SIM). This role offers hands-on "
     "experience in applying AI and service-oriented architectures to solve real-world challenges in "
     "urban mobility.",
     ["Assist in the design and implementation of AI agents for specific mobility functions, focusing on multi-criteria end-to-end trip planning.",
      "Analyze urban mobility challenges and develop user personas to guide platform development.",
      "Work collaboratively with the project team to ensure research goals are met.",
      "Contribute to project documentation and publications."],
     ["Bachelor's degree in computer science or engineering, transportation engineering, or a related field.",
      "Basic understanding of AI, machine learning, and optimization algorithms.",
      "Interest in urban mobility and sustainable transportation systems."],
     ["Familiarity with service-oriented architectures, agent-based systems, or route optimization.",
      "Background in user-centered design or multimodal mobility systems.",
      "Expertise in data serialization languages such as YAML, JSON, and Protobuf, as well as data distribution and messaging protocols such as MQTT and Zenoh.",
      "Expertise in API protocols such as REST, GraphQL, WebSocket, and gRPC, along with query languages such as SQL, KQL, PromQL, and LogQL."],
     None),
]

CONTACT = [
    ("pin", "Mailing address",
     "AI for Smart Mobility Lab<br>Interdisciplinary Research Center for Smart Mobility and Logistics"
     "<br>Department of Industrial and Systems Engineering<br>Building 22/427<br>"
     "King Fahd University of Petroleum and Minerals<br>Academic Belt Road, Dhahran 31261, Saudi Arabia"),
    ("email", "Email", '<a href="mailto:alaa.rashwan@kfupm.edu.sa">alaa.rashwan@kfupm.edu.sa</a>'),
    ("phone", "Phone", "+966-13-860-3754"),
    ("github", "GitHub", '<a href="https://github.com/ai4smlab" target="_blank" rel="noopener noreferrer">github.com/ai4smlab</a>'),
    ("medium", "Medium publication hub", '<a href="https://medium.com/ai4sm" target="_blank" rel="noopener noreferrer">medium.com/ai4sm</a>'),
    ("youtube", "YouTube channel", '<a href="https://www.youtube.com/@AI4SM_lab" target="_blank" rel="noopener noreferrer">youtube.com/@AI4SM_lab</a>'),
    ("users", "Agentic AI @ KFUPM community", '<a href="https://agenticaikfupm.github.io/" target="_blank" rel="noopener noreferrer">agenticaikfupm.github.io</a>'),
    ("web", "Director", '<a href="https://alaakhamis.org/" target="_blank" rel="noopener noreferrer">alaakhamis.org</a>'),
]


# ---------------------------------------------------------------- builders

def _links(links, icon):
    return '<div class="pub__links">%s</div>' % "".join(
        '<a href="%s" target="_blank" rel="noopener noreferrer">%s%s</a>' % (url, icon(ic), label)
        for ic, url, label in links)


def _person(photo, name, role, links, icon, contain=False):
    social = "".join(
        '<a href="%s" target="_blank" rel="noopener noreferrer" aria-label="%s of %s">%s</a>'
        % (url, ic, name, icon(ic)) for ic, url in links)
    cls = " person__photo--contain" if contain else ""
    return ('<article class="person">'
            '<img class="person__photo%s" src="%s" alt="%s" loading="lazy">'
            '<h3>%s</h3><p>%s</p><div class="social">%s</div></article>'
            % (cls, photo, name, name, role, social))


def _project(img, title, paras, funder, duration, video=None, topics=None, index=None):
    media = '<img src="%s" alt="%s" loading="lazy">' % (img, title)
    if video:
        media = ('<a href="%s" target="_blank" rel="noopener noreferrer" '
                 'aria-label="Watch: %s">%s</a>' % (video, title, media))
    tags = []
    if funder:
        tags.append('<span class="tag"><strong>Funding</strong> %s</span>' % funder)
    if duration:
        tags.append('<span class="tag"><strong>Duration</strong> %s</span>' % duration)
    if topics:
        tags.append('<span class="tag">%s</span>' % topics)
    if video:
        tags.append('<span class="tag tag--accent">Video</span>')
    meta = '<div class="project__meta">%s</div>' % "".join(tags) if tags else ""
    body = "".join("<p>%s</p>" % p for p in paras)
    return ('<article class="project"><div class="project__index">%s</div>'
            '<div class="project__media">%s</div>'
            '<div class="project__body"><h3>%s</h3>%s%s</div></article>'
            % ("%02d" % index if index else "", media, title, body, meta))


def pages(page_header, section, icon, social_html):
    out = []

    # ---------------------------------------------------------------- home
    pillars = "".join(
        '<article class="pillar"><div class="pillar__num">%02d</div><h3>%s</h3><p>%s</p></article>'
        % (n + 1, t, b) for n, (t, b) in enumerate(PILLARS))
    featured = "".join(
        '<article class="card"><div class="card__num">%02d</div><h3>%s</h3><p>%s</p>'
        '<a class="link-more" href="research.html">Project details</a></article>'
        % (n + 1, t, paras[0][:180].rsplit(" ", 1)[0] + "...")
        for n, (_, t, paras, _, _) in enumerate(CURRENT_PROJECTS[:3]))
    latest = "".join("<li>%s</li>" % body for _, body, _ in NEWS[:5])

    home = """<section class="hero">
  <div class="wrap">
    <div class="hero__grid">
      <div class="hero__body">
        <p class="hero__kicker">Interdisciplinary Research Center for Smart Mobility and Logistics</p>
        <h1>AI at the intersection of <em>mobility</em> systems and services</h1>
        <p class="hero__lead">
          The future of mobility is people-centric, software-defined, connected, and electric. Our
          mission is to advance transformative innovations that prioritize user experience, enhance
          connectivity, and drive sustainable electrification.
        </p>
        <p class="hero__lead">
          By integrating cutting-edge research with interdisciplinary collaboration, we create
          mobility solutions that empower individuals, foster global connectivity, and contribute to
          a cleaner, smarter, and more inclusive world.
        </p>
        <div class="actions">
          <a class="btn btn--primary" href="research.html">Explore our research
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
          </a>
          <a class="btn btn--ghost" href="join.html">Open positions</a>
        </div>
        <div style="margin-top:30px">%s</div>
      </div>
    </div>
  </div>
</section>

%s%s%s%s""" % (
        social_html(),
        section("01", "What is smart mobility?",
                '<div class="prose" style="padding:0"><p>Smart mobility is a wide umbrella for '
                'different systems and services that meet various end-user needs without compromising '
                'the collective good of society and the environment. These systems and services are '
                'built on advanced technologies such as artificial intelligence, connectivity, and '
                'electrification, alongside innovative business models like the digital economy, '
                'servitization, the sharing economy, the gig economy, the experience economy, and the '
                'circular economy.</p><p>The AI4SM Lab is part of the '
                '<a href="https://ri.kfupm.edu.sa/irc-sml" target="_blank" rel="noopener noreferrer">'
                'Interdisciplinary Research Center for Smart Mobility and Logistics</a> at KFUPM. Our '
                'research sits at the intersection of AI and mobility systems, services, and business '
                'models.</p></div>',
                wrap="wrap wrap--narrow"),
        section("02", "Research pillars", '<div class="pillars">%s</div>' % pillars, alt=True,
                lead="Three connected threads run through everything the lab builds."),
        section("03", "Active projects", '<div class="cards">%s</div>' % featured,
                lead="Funded research currently running in the lab.",
                more=("research.html", "All projects")),
        section("04", "Latest news", '<ul class="news-list">%s</ul>' % latest, alt=True,
                more=("news.html", "All news")),
    )
    out.append(("index.html", "AI for Smart Mobility Lab | KFUPM",
                "The AI for Smart Mobility (AI4SM) Lab at KFUPM researches AI for mobility systems, "
                "services, and business models: software-defined vehicles, agentic AI, seamless "
                "integrated mobility, and last-mile delivery.",
                home, ""))

    # ------------------------------------------------------------ research
    current = "".join(_project(i, t, p, f, d, index=n + 1)
                      for n, (i, t, p, f, d) in enumerate(CURRENT_PROJECTS))
    past = "".join(_project(i, t, p, f, d, video=v, topics=tp, index=n + 1)
                   for n, (i, v, t, p, f, d, tp) in enumerate(PAST_PROJECTS))
    unis_js = ",\n      ".join(
        '{ name: "%s", coords: [%s, %s], url: "%s" }' % (n.replace('"', ""), a, b, u)
        for n, a, b, u in COLLABORATOR_UNIS)
    map_js = """<div id="map" role="img" aria-label="World map of AI4SM Lab partner universities"></div>
<script>
  (function () {
    var universities = [
      %s
    ];
    var map = L.map('map', { scrollWheelZoom: false });
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
      attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);
    var bounds = [];
    universities.forEach(function (u) {
      L.marker(u.coords).addTo(map).bindPopup(
        '<b>' + u.name + '</b><br><a href="' + u.url + '" target="_blank" rel="noopener">' + u.url + '</a>');
      bounds.push(u.coords);
    });
    map.fitBounds(bounds, { padding: [30, 30] });
  })();
</script>""" % unis_js

    research = (page_header("Research",
                            "Driving innovation for sustainable, inclusive, and safe mobility.")
                + section("01", "Current projects", '<div class="projects">%s</div>' % current)
                + section("02", "Samples of previous projects", '<div class="projects">%s</div>' % past, alt=True)
                + section("03", "Research collaborators", map_js,
                          lead="We collaborate with partner universities and research groups worldwide."))
    out.append(("research.html", "Research | AI for Smart Mobility Lab",
                "Funded research projects at the AI4SM Lab: connected and automated vehicle safety, "
                "SDV contextual observability, seamless integrated mobility, and eco-efficient "
                "last-mile delivery.",
                research, LEAFLET))

    # ---------------------------------------------------------------- team
    pi_links = [("linkedin", "https://www.linkedin.com/in/alaakhamis/"),
                ("scholar", "https://scholar.google.ca/citations?user=btM72xsAAAAJ&hl=en"),
                ("researchgate", "https://www.researchgate.net/profile/Alaa-Khamis"),
                ("amazon", "https://amazon.com/author/alaakhamis"),
                ("github", "https://github.com/Dr-AlaaKhamis"),
                ("medium", "https://medium.com/@alaakhamis"),
                ("web", "https://alaakhamis.org/"),
                ("email", "mailto:alaa.rashwan@kfupm.edu.sa")]
    pi_social = "".join(
        '<a href="%s"%s aria-label="%s">%s</a>'
        % (u, "" if u.startswith("mailto:") else ' target="_blank" rel="noopener noreferrer"', ic, icon(ic))
        for ic, u in pi_links)
    lead = """<div class="lead">
  <img src="images/AlaaKhamis.png" alt="Portrait of Dr. Alaa Khamis">
  <div>
    <h3>Dr. Alaa Khamis</h3>
    <p class="lead__role">Director and Principal Investigator</p>
    <p>Department of Industrial and Systems Engineering, and Interdisciplinary Research Center for
       Smart Mobility and Logistics (SML), College of Computing and Mathematics, King Fahd University
       of Petroleum and Minerals.</p>
    <p>Formerly AI and Smart Mobility Technical Leader at General Motors. Founding Chair of the IEEE
       Intelligent Transportation Systems Society Saudi Arabia Chapter.</p>
    <div class="social">%s</div>
  </div>
</div>""" % pi_social

    researchers = "".join(_person(p, n, r, l, icon, contain=p.endswith("AI4SM_lab.png"))
                          for p, n, r, l in RESEARCHERS)
    researchers += ('<article class="vacancy"><h3>Postdoctoral fellows</h3><p>2 open positions</p>'
                    '<a class="btn btn--primary" href="join.html">Join us</a></article>'
                    '<article class="vacancy"><h3>PhD and MSc students</h3><p>4 open positions</p>'
                    '<a class="btn btn--primary" href="join.html">Join us</a></article>')
    collabs = "".join(_person(p, n, r, l, icon, contain=p in ("images/OTU.png", "images/SusRobotics.png"))
                      for p, n, r, l in COLLABORATORS)

    team = (page_header("Team", "The people behind the lab.")
            + section("01", "Faculty", lead)
            + section("02", "Researchers", '<div class="team-grid">%s</div>' % researchers, alt=True)
            + section("03", "Collaborators", '<div class="team-grid">%s</div>' % collabs))
    out.append(("team.html", "Team | AI for Smart Mobility Lab",
                "Faculty, researchers, students, and collaborators of the AI for Smart Mobility Lab "
                "at KFUPM.", team, ""))

    # ---------------------------------------------------------- facilities
    facs = "".join(
        '<section class="facility"><div class="facility__media">'
        '<img src="%s" alt="%s" loading="lazy"></div>'
        '<div><div class="facility__num">%02d</div><h3>%s</h3><p>%s</p></div></section>'
        % (img, t, n + 1, t, body)
        for n, (img, t, body) in enumerate(FACILITIES))
    facilities = (page_header("Facilities",
                              "Research platforms and computing infrastructure available to the lab.")
                  + '<section class="section"><div class="wrap">%s</div></section>\n' % facs)
    out.append(("facilities.html", "Facilities | AI for Smart Mobility Lab",
                "The AI4SM Lab's automated driving research platform, software-defined vehicle "
                "testbed, SDV prototyping platforms, and high-performance computing workstations.",
                facilities, ""))

    # -------------------------------------------------------- publications
    books = "".join(
        '<article class="book-row"><img src="%s" alt="Cover of %s" loading="lazy">'
        '<div><h3>%s</h3><p class="pub__cite">%s</p>%s</div></article>'
        % (img, t, t, cite, _links(links, icon)) for img, t, cite, links in BOOKS)

    def pub_list(items):
        return "".join(
            '<article class="pub"><p class="pub__cite">%s <em>%s</em>. '
            '<span class="pub__venue">%s</span></p>%s</article>'
            % (authors, title, venue, _links(links, icon))
            for authors, title, venue, links in items)

    hub = """<div class="prose" style="padding:0">
  <p>The AI4SM Lab publishes and maintains the
     <a href="https://medium.com/ai4sm" target="_blank" rel="noopener noreferrer">AI for Smart
     Mobility</a> hub on Medium, a collaborative platform dedicated to exploring AI's transformative
     impact on transportation infrastructure, people mobility, and logistics, featuring diverse use
     cases supported by code and data. Lab code is released on
     <a href="https://github.com/ai4smlab" target="_blank" rel="noopener noreferrer">GitHub</a>.</p>
  <figure><a href="https://medium.com/ai4sm" target="_blank" rel="noopener noreferrer">
    <img src="images/AI4SM.jpg" alt="AI for Smart Mobility publication on Medium"></a></figure>
</div>"""

    publications = (page_header("Publications",
                                "Books, journal articles, and conference papers from the lab.")
                    + section("01", "Books", books)
                    + section("02", "Journal articles", pub_list(JOURNALS), alt=True)
                    + section("03", "Conference papers", pub_list(CONFERENCES))
                    + section("04", "Knowledge sharing hub", hub, alt=True, wrap="wrap wrap--narrow"))
    out.append(("publications.html", "Publications | AI for Smart Mobility Lab",
                "Books, journal articles, and conference papers published by the AI for Smart "
                "Mobility Lab at KFUPM.", publications, ""))

    # --------------------------------------------------------------- talks
    rows = []
    for title, venue, date, link in TALKS:
        label = ('<a href="%s" target="_blank" rel="noopener noreferrer">%s</a>' % (link, title)
                 if link else title)
        slides = ('<div class="pub__links"><a href="%s" target="_blank" rel="noopener noreferrer">'
                  '%sSlides</a></div>' % (link, icon("slides"))) if link and link.endswith(".pdf") else ""
        rows.append('<article class="pub"><p class="pub__cite"><em>%s</em><br>'
                    '<span class="pub__venue">%s &middot; %s</span></p>%s</article>'
                    % (label, venue, date, slides))
    talks = (page_header("Talks", "Keynotes, seminars, and tutorials given by the lab.")
             + section("01", "Recent talks", "".join(rows), wrap="wrap wrap--narrow"))
    out.append(("talks.html", "Talks | AI for Smart Mobility Lab",
                "Keynote speeches, seminars, and tutorials given by the AI for Smart Mobility Lab.",
                talks, ""))

    # ---------------------------------------------------------------- news
    items = []
    for year, body, media in NEWS:
        fig = ('<figure><img src="%s" alt="%s" loading="lazy"></figure>'
               % media) if media else ""
        items.append('<article class="news-entry" data-item><span class="tag">%s</span>'
                     '<div class="news-entry__body">%s%s</div></article>' % (year, body, fig))
    toolbar = """<div class="toolbar" data-filter-root="#news-list">
  <div class="wrap">
    <div class="toolbar__inner">
      <div class="search">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
        <input id="news-search" type="search" placeholder="Search news and events..." aria-label="Search news and events" autocomplete="off">
      </div>
      <span class="filter-status" role="status"></span>
    </div>
  </div>
</div>
"""
    news = (page_header("News and Events", "Papers, awards, appointments, and lab announcements.")
            + toolbar
            + '<div class="prose"><div class="wrap wrap--narrow"><div id="news-list"><ul>%s</ul>'
              '<p class="empty-state is-hidden">No items match that search.</p></div></div></div>\n'
              % "".join(items))
    out.append(("news.html", "News and Events | AI for Smart Mobility Lab",
                "Recent news, papers, awards, and announcements from the AI for Smart Mobility Lab "
                "at KFUPM.", news, ""))

    # ---------------------------------------------------------------- join
    toc = "".join('<li><a href="#%s">%s</a></li>' % (a, t) for a, t, _, _, _, _, _, _ in POSITIONS)
    blocks = []
    for anchor, title, track, intro, resp, req, pref, offer in POSITIONS:
        parts = ['<section class="position" id="%s">' % anchor,
                 '<span class="position__track">%s</span>' % track,
                 "<h2>%s</h2>" % title,
                 "<p>%s</p>" % intro,
                 "<h4>Key responsibilities</h4><ul>%s</ul>" % "".join("<li>%s</li>" % r for r in resp),
                 "<h4>Required qualifications</h4><ul>%s</ul>" % "".join("<li>%s</li>" % r for r in req),
                 "<h4>Preferred qualifications</h4><ul>%s</ul>" % "".join("<li>%s</li>" % r for r in pref)]
        if offer:
            parts.append("<h4>What we offer</h4><ul>%s</ul>" % "".join("<li>%s</li>" % o for o in offer))
        parts.append("</section>")
        blocks.append("".join(parts))

    join_body = """<div class="prose">
  <div class="wrap wrap--narrow">
    <p>We always welcome inquiries from enthusiastic undergraduate and graduate researchers eager to
       contribute to our work. To explore potential alignment with the lab's focus, we encourage you
       to review the active projects on our <a href="research.html">Research</a> page.</p>
    <nav class="toc" aria-label="Available positions">
      <h2>Available positions</h2>
      <ol>%s</ol>
    </nav>
%s
    <div class="callout">
      <h2>How to apply</h2>
      <p>Join us to contribute to the future of sustainable mobility. For PhD and MSc positions,
         applications should be submitted through the
         <a href="https://cgis.kfupm.edu.sa/" target="_blank" rel="noopener noreferrer">College of
         Graduate and Interdisciplinary Studies</a> at KFUPM. For postdoctoral positions, please
         complete this <a href="https://forms.gle/ZqkoZ7awBw6StHbcA" target="_blank" rel="noopener noreferrer">application
         form</a>. Only shortlisted candidates will be contacted for an interview.</p>
    </div>
  </div>
</div>
""" % (toc, "\n".join(blocks))
    join = page_header("Join the Lab", "Six open positions across our two funded research tracks.") + join_body
    out.append(("join.html", "Join the Lab | AI for Smart Mobility Lab",
                "Open postdoctoral, PhD, and MSc positions at the AI for Smart Mobility Lab at KFUPM "
                "in software-defined vehicles and seamless integrated mobility.", join, ""))

    # ------------------------------------------------------------- contact
    cards = "".join(
        '<div class="contact__item"><h3>%s%s</h3><p>%s</p></div>' % (icon(ic), label, body)
        for ic, label, body in CONTACT)
    contact = (page_header("Contact and Resources", "Where to find us and how to follow the lab's work.")
               + '<section class="section"><div class="wrap"><div class="contact">%s</div></div></section>\n' % cards)
    out.append(("contact.html", "Contact | AI for Smart Mobility Lab",
                "Contact details and online resources for the AI for Smart Mobility Lab at KFUPM.",
                contact, ""))

    # ----------------------------------------------------------------- 404
    nf = (page_header("This page does not exist", "The link may be out of date, or the page may have "
                      "moved when the site was rebuilt.", label="Error 404")
          + '<div class="prose"><div class="wrap wrap--narrow"><p>Try one of these instead:</p><ul>'
            '<li><a href="index.html">Home</a></li>'
            '<li><a href="research.html">Research</a> &middot; <a href="team.html">Team</a> &middot; '
            '<a href="facilities.html">Facilities</a></li>'
            '<li><a href="publications.html">Publications</a> &middot; <a href="talks.html">Talks</a> '
            '&middot; <a href="news.html">News</a></li>'
            '<li><a href="join.html">Join the lab</a> &middot; <a href="contact.html">Contact</a></li>'
            '</ul></div></div>\n')
    out.append(("404.html", "Page not found | AI for Smart Mobility Lab",
                "The page you were looking for could not be found.", nf, ""))

    return out
