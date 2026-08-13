---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/administration/get-started-with-prisma-sd-wan/site-summary-dashboard
fetched_at: 2026-08-13T17:27:33Z
source: palo-alto-main
---

# Site Summary Dashboard Clear

Site Summary Dashboard 

 Home 

 EN

 Location 

 Documentation Home 

 Palo Alto Networks 

 Support 

 Live Community 

 Knowledge Base 

 >

 Strata Copilot

 Site Summary Dashboard 

 Updated on 

 Aug 10, 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma SD-WAN Docs 

 Activation & Onboarding 

 Administration 

 CloudBlades 

 Select a Document 

 CloudBlade Integrations 

 CloudBlades Integration with Prisma Access 

 Deployment 

 Incidents & Alerts 

 Reference 

 Release Notes 

 Select a Document 

 ION 6.8 

 ION 6.6 

 ION 6.5 

 ION 6.4 

 ION 6.3 

 ION 6.1 

 ION 5.6 

 Prisma SD-WAN Controller 

 Prisma SD-WAN On-Premises Controller 

 Prisma SD-WAN CloudBlades 

 Prisma Access CloudBlade Cloud Managed 

 Prisma Access CloudBlade Panorama Managed 

 New Features 

 Updated on 

 Aug 10, 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Prisma SD-WAN Administrator’s Guide 

 Get Started with Prisma SD-WAN 

 Site Summary Dashboard 

 Download PDF 

 Prisma SD-WAN 

 Site Summary Dashboard 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma SD-WAN Docs 

 Activation & Onboarding 

 Administration 

 CloudBlades 

 Select a Document 

 CloudBlade Integrations 

 CloudBlades Integration with Prisma Access 

 Deployment 

 Incidents & Alerts 

 Reference 

 Release Notes 

 Select a Document 

 ION 6.8 

 ION 6.6 

 ION 6.5 

 ION 6.4 

 ION 6.3 

 ION 6.1 

 ION 5.6 

 Prisma SD-WAN Controller 

 Prisma SD-WAN On-Premises Controller 

 Prisma SD-WAN CloudBlades 

 Prisma Access CloudBlade Cloud Managed 

 Prisma Access CloudBlade Panorama Managed 

 New Features 

 Previous 

 Device Activity Dashboard 

 Next 

 Prisma SD-WAN Predictive Analytics Dashboard 

 Site Summary Dashboard 

 The Site Summary dashboard provides branch site metrics including network health, circuit connectivity, device status, application utilization, and media performance for Prisma SD-WAN sites. 

 Where Can I Use
 This? What Do I Need? 

 Prisma SD-WAN (Managed by Strata Cloud Manager ) 

 Prisma SD-WAN 

 Starting with release 5.6.1 the site summary dashboard provides an information-rich
 display of branch-related metrics. These include new metrics such as network health as
 well as existing network, device and application metrics. 

 Select Configuration Prisma SD-WAN Branch Sites , select a site from the listed branch sites, then select the
 Site Summary tab to view the Site
 Summary widget. 

 Alternatively, select Insights Branch Sites Prisma SD-WAN to open the Map view.
 Select a site from the branch sites, then select the Site
 Summary tab. 

 The default time range to view the metrics is 3 hours but can be adjusted to
 shorter or longer periods of time depending on the desired scope of
 information. 

 For time ranges longer than 7 days a Network DVR license is required. For
 more information contact your Palo Alto Networks Account Team. 

 Site Health Overview 

 The Site Health Overview widget contains the Current Best
 Health Score and the Overall Site Consumed Bandwidth . Click either
 metric to display its time-series view. 

 The Current Best Health Score metric is determined by the Secure Fabric Link
 with the current highest score. In the time series chart the score is determined in
 any given time sample by the healthiest Secure Fabric Link at the site. This value
 will fluctuate as the health of the underlying network connectivity changes. 

 The Health Score metrics are available to customers with an active WAN
 Clarity or AIOps license. For unlicensed customers a trial preview is
 provided in the Prisma SD-WAN Release 5.6.1. 

 The Autonomous Digital Experience Monitoring (ADEM) for Remote Networks
 agent is delivered natively from the Prisma SD-WAN device
 software. The ADEM for Remote Networks agent provides visibility into cloud
 infrastructure performance, application performance and user traffic
 monitoring. This feature is available if ADEM is
 enabled for a site. 

 Current Overall Consumed Bandwidth 

 The Current Overall Consumed Bandwidth metric displays current
 total bandwidth consumption, ingress and egress bandwidth consumption as a raw value
 and as a percentage of the total available. Upon clicking the tab a time series
 chart of the ingress and egress consumed bandwidth are displayed in reference to the
 total configured bandwidth at the site. 

 The Circuit Connectivity and Health widget displays the name
 of the circuit, its physical connectivity, its tunnel connectivity, tunnel health, a
 time-series graph indicating the best-performing tunnel's health score over a period
 of time, and current consumed bandwidth both in egress/ingress direction. 

 Upon clicking a circuit there are several widgets displayed including Circuit
 Metrics, Insights, and Secure Fabric Connectivity and Health. 

 The Circuit Metrics widget displays the time-series graphs for
 the health score of the best performing tunnel and the circuit bandwidth utilization
 between the configured ingress/egress and the actual ingress/egress over time. 

 The system generates Insights using machine
 learning algorithms. These insights identify conditions such as: 

 Excessive Packet Loss Detected 

 Excessive Latency Detected 

 Bandwidth Upgrade Recommended 

 Configured vs Consumed Bandwidth Mismatch Detected 

 Low Circuit Throughput Detected 

 Insights are available to customers with an active WAN Clarity or AIOps
 license. 

 Secure Fabric Connectivity And Health 

 The Secure Fabric Connectivity And Health widget displays each
 of the Branch to DC Secure Fabric Links along with their respective
 Connectivity status, Health chart, and associated current link
 metrics Packet Loss , Jitter , Latency , and Link MOS . 

 When you click a Secure Fabric Link, the system displays a comprehensive view of link metrics
 in a time-series chart. You can change the time range, selected Secure Fabric link,
 and direction. 

 Circuit Health 

 The Circuit Health widget displays the list of tunnels with
 their name, connectivity details, and health score. It also displays the packet
 loss, jitter, latency, and MOS for the ingress or egress connections. You can also
 see the capacity prediction details at the circuit level. 

 The circuit health score is calculated per path, factoring in
 ingress packet loss, egress packet loss, and round-trip time (RTT).
 The scoring mechanism considers both the circuit's load and its
 baseline for a more precise health assessment. For example,
 a 100Mbps circuit operating without load but experiencing 1%
 packet loss scores differently than the same circuit running at 100%
 load with 2% packet loss. This difference reflects how performance expectations change during increased capacity utilization. 

 Consumed Bandwidth 

 The Consumed Bandwidth widget displays the circuit bandwidth
 utilization and the anomaly between the configured ingress/egress and
 the actual ingress/egress over time. 

 Devices 

 The Devices widget displays the device's name, status,
 software version installed, whether the Admin interface is up, its routing peers,
 the HA status, consumed CPU, and consumed memory data. 

 Additional controller connectivity status for Config and Events, Analytics, and Flows
 is available when you hover over or click the status icon. 

 Possible Device Connection States are: 

 Online: All three connections - Config and Events, Analytics, and Flows are
 online. 

 Partially online: Config and Events online and Analytics, and/or Flows may be
 offline. 

 Offline: All three connections - Config and Events, Analytics, and Flows are
 offline. 

 Top Events by Priority 

 The Top Events by Priority widget displays the top
 events by priority. All events in the selected time range appear regardless
 of status, including Resolved and Acknowledged events. To view all current standing alarms, select View All Site Alarms and Alerts, which displays
 standing alarms regardless of time range. 

 Application Utilization 

 The Application Utilization widget displays
 application utilization at the site during the selected time range. The widget shows total
 application ingress and egress traffic for the time range, along with the top 10
 applications by traffic volume and other traffic. For each
 application, the widget displays total bandwidth utilization, ingress, egress, and percentage of
 total traffic based on bandwidth utilization. Click the ellipses to view flow
 information or time-series utilization data. 

 The Recent Site Audit Logs widget displays the recent
 configuration changes made to the site within the selected time range. To see the
 full list of changes select View All Site Audit Logs. 

 TCP Connection Stats 

 The TCP Connection Stats displays the data related to the TCP
 connection metrics in the selected time range and includes four (4) metrics: 

 Init Success - A successful TCP connection was established 

 Transaction Success - After a successful TCP connection, a successful data
 transaction was observed. 

 Init Failure - A failed attempt to establish a TCP connection 

 Transaction Failure - After a successful TCP connection, a failed data
 transaction was observed. 

 The metrics for all TCP applications are initially displayed but, any one of the top
 10 TCP applications can be selected to more narrowly focus on a specific top
 application. 

 Top Media Audio Performance 

 The Top Media Audio Performance widget displays statistical
 information about the observed Mean Opinion Score for audio traffic at the site. The
 top audio application by traffic volume is automatically selected but, other top 10
 media audio applications can also be selected as needed. The MOS score is measured
 in both the ingress and egress directions. The median value for the selected time
 range is displayed along with a trend indicator to display any observed performance
 changes from the previous time period. The box plot displays the low, 25th
 percentile, median, 75th percentile, and high observed MOS scores. Hover
 over the bar chart to display numeric values. View recent flows for media
 traffic by selecting View Flows. To view detailed time-series media
 performance metrics, select View Media Activity. 

 App Health 

 App Health tracks each instance or service
 associated with a given application on all allowed paths. Statistics are always sent
 for an app/path pair as long as there is active traffic for that pair. In case of
 prolonged inactivity, records for app/path are not sent after 10 minutes of
 inactivity. A refresh record sent every 50 minutes shows the last known state of the
 app/path based on the previously known application health. No metrics are reported
 in the 50 minutes refresh records as there are no new flows. 

 The App Health chart reports are on a per-app basis. Select a
 site and an app to display data on your charts. Select at least one app to view the
 App Health by Path table. The health of the selected
 paths is indicated by color. The Health Events by Prefix 
 table, associated with each application instance or service, displays all the
 transaction or init failures. Refer to the table to understand descriptions of the
 different health states. 

 Legend Description 

 Good Application is reachable on all paths. Indicates all
 prefixes on all paths are reachable. 

 Partially Good One or more instances or services associated with an
 application instance are not reachable on one or more paths.
 Indicates either some paths or some prefixes on a path are
 unreachable. A partially good path is not a cause for concern.
 Multi-origin applications such as Office 365 may display as
 partially good, but still be functioning well. 

 Unreachable All instances or services associated with an
 application are unreachable. Indicates all used paths and prefixes
 on all paths are unreachable. 

 No Data No application data is available as the application
 does not use this path or is not allowed to use this path by its
 policy. Indicates that the application is not in use. 

 App Response Time 

 Prisma SD-WAN uses application response time to determine
 the path a flow may take and confirms that the path adheres to the application SLA.
 Application response time is a combination of Network Transfer
 Time (NTT), Round Trip Time (RTT), and
 Server Response Time SRT) metrics and calculated for a
 flow on each path before a decision is taken to send a flow on that path. These
 metrics reflect in the App Response Time chart. 

 The chart displays detailed information on the application transaction time for each
 prefix within an application. It determines network and server performance for a
 specific application, including information from the moment the client generates a
 request to the time the server receives the response in the cloud or the data
 center. It also takes into account L1 – L3 and L4 – L7 characteristics of an
 application, including end-to-end performance rather than just latency, jitter, and
 packet drops for an application. 

 App Response Time chart reports on a per-app basis. Select at
 least one app to view the App Response Time by Path table.
 The health of the selected paths are indicated by color. You can view specific
 Health Events table associated with each application
 instance or service with transaction or init failures. Refer to the above App Health to understand descriptions on the
 different health states. 

 Using NTTn, RTT, SRT, and UDP-TRT metrics, this chart provides information on the
 source of an under performing application. 

 Network Transfer Time (NTTn) —The measure of network
 congestion. The amount of time it takes to transfer incoming data from an
 external server to a local client. 

 Round Trip Time (RTT) —The measure of network latency.
 RTT is measured only for TCP flows and defined as the time taken between a
 forward and return related protocol exchange; TCP SYN to SYN-ACK for
 outbound flows, TCP SYN-ACK to ACK for inbound flows and the time between a
 data sequence and ACK of that data sequence. 

 Thus, RTT is measured throughout the life of a flow and not just at the TCP
 establishment. Measuring RTT throughout the flows life allows the system to
 account for TCP proxy devices like WAN optimization in the path, providing a
 more accurate measurement of RTT. 

 Server Response Time —The amount of time it takes for
 the server to start transmitting data after it has acknowledged the client’s
 request. SRT measured for TCP flows only from the time request is received
 to the time the server sends the first response packet. 

 UDP Response Time (UDP-TRT) —The amount of time it
 takes for the server to respond to the UDP transaction request from the time
 the request is received. Currently, UDP-TRT provides information on UDP DNS
 traffic only. 

 Users Mapping 

 The Site summary page displays IP address-to-user mapping information when
 Cloud User ID is enabled. The dashboard shows the IP addresses mapped to users with
 the time stamp of when the entry is created upon user authentication, the duration
 of the validity, and the time when the entry is removed. 

 Previous 

 Device Activity Dashboard 

 Next 

 Prisma SD-WAN Predictive Analytics Dashboard 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Cloud Identity Engine 

 Hub 

 Identity and Access Management 

 Tenant Management 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 FedRAMP 

 Prisma SASE for FedRAMP 

 Hardware Reference 

 ION 1000 

 ION 1200 

 ION 1200-S 

 ION 2000 

 ION 3000 

 ION 3200 and ION 3200H 

 ION 5200 

 ION 7000 

 ION 9000 

 ION 9200 

 Hardware Quick Start Guides 

 ION 1200 

 ION 1200 4G 

 ION 1200 5G 

 ION 1200-S 

 ION 1200-S 4G 

 ION 1200-S 5G 

 ION 3200 

 ION 3200H 

 ION 3200H 5G 

 ION 5200 

 ION 9200 

 Virtual ION Deployment 

 Virtual ION on AWS 

 Virtual ION on Azure 

 Virtual ION on GCP 

 Virtual ION on Alibaba Cloud 

 Virtual ION on KVM for NFV 

 Virtual ION on OCI 

 Virtual ION on VMware 

 Virtual ION on Megaport Virtual Edge 

 Virtual ION on Dell PowerEdge 

 Prisma SD-WAN Integration 

 AWS Cloud-WAN Integration (GRE Connect) 

 AWS Cloud-WAN Integration (Tunnel-less Connect) 

 Checkpoint Integration 

 LiveAction Integration 

 Netskope Integration 

 Symantec Web Security Services Integration 

 Prisma SD-WAN Experts Corner 

 Network Policy 

 QoS Whitepaper 

 Security Architecture Whitepaper 

 External Antennas for ION-C Series 

 Dynamic Path Selection 

 Best Practices 

 Best Practices Library 

 Resources 

 All Products A - Z 

 Compatibility Matrix 

 SASE 

 Administration 

 Prisma SD-WAN 

 Strata Cloud Manager 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
