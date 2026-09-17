---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/pan-os/11-1/pan-os-admin/quality-of-service.html
fetched_at: 2026-09-16T12:58:11Z
source: palo-alto-main
---

# Quality of Service Clear

Updated on 

 Wed Sep 24 10:44:45 PDT 2025 

 Focus 

 Home 

 Network Security 

 Quality of Service 

 Download PDF 

 Network Security 

 Quality of Service 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Network Security Docs 

 Security Policy 

 IPsec VPN 

 Decryption 

 Device-ID 

 Quantum Security 

 Quality of Service 

 Previous 

 Generate a Quantum-Safe Security Report 

 Next 

 Prioritize Network Traffic using QoS 

 Quality of Service 

 QoS allows granular control over traffic classes, optimizing
 performance for latency-sensitive applications and aligning resource allocation with
 organizational priorities.

 Where Can I Use This? What Do I Need? 

 NGFW 

 No separate license required for QoS when using NGFWs 

 Quality of Service (QoS) is a set of technologies that work on a network to guarantee its
 ability to dependably run high-priority applications and traffic under limited network
 capacity. QoS technologies accomplish this by providing differentiated handling and
 capacity allocation to specific flows in network traffic. This enables the network
 administrator to assign the order in which traffic is handled, and the amount of
 bandwidth afforded to traffic. 

 QoS enables you to prioritize and manage network traffic to ensure critical applications
 and services receive the necessary bandwidth and resources. 

 Palo Alto Networks Application Quality of Service (QoS) provides basic QoS applied to
 networks and extends it to provide QoS to applications and users. 

 With QoS on PAN-OS, you can optimize network performance by defining QoS policies that
 classify traffic into different service classes, each with its own priority level and
 bandwidth allocation. QoS is especially useful in environments where network congestion
 can impact business-critical applications or where certain types of traffic require
 preferential treatment. You can leverage QoS to ensure that latency-sensitive
 applications like voice and video conferencing maintain high quality, while less
 time-sensitive traffic is appropriately managed. QoS policies allow you to match traffic
 based on various criteria such as applications, zones, addresses, users, and DSCP
 values, giving you granular control over how different types of network traffic are
 treated. By implementing QoS, you can improve overall network efficiency, enhance user
 experience for critical services, and align network resource allocation with your
 organization's priorities. With QoS, you can maximize the value of your existing network
 infrastructure while ensuring that your most important traffic always gets through, even
 during periods of high network utilization. 

 Use the Palo Alto Networks product comparison tool to view the QoS
 features supported on your firewall model. Select two or more product models and click
 Compare Now to view QoS feature support for each model (for
 example, you can check if your firewall model supports QoS on subinterfaces and if so,
 the maximum number of subinterfaces on which QoS can be enabled). 

 QoS on Aggregate Ethernet (AE) interfaces is supported on PA-7000 Series, PA-5400 Series,
 PA-5200 Series, PA-3400 Series, PA-3200 Series, PA-1400 Series, and PA-400 Series
 firewalls. 

 Previous 

 Generate a Quantum-Safe Security Report 

 Next 

 Prioritize Network Traffic using QoS
