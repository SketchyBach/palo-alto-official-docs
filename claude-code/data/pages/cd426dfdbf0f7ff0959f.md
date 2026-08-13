---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/administration/prisma-sd-wan-sites-and-devices/use-external-services-for-monitoring/prisma-sd-wan-specific-information-elements
fetched_at: 2026-08-13T17:28:43Z
source: palo-alto-main
---

# Flow Information Elements  Clear

Flow Information Elements 

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

 Flow Information Elements 

 Updated on 

 Mon Aug 10 04:14:37 PDT 2026 

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

 Mon Aug 10 04:14:37 PDT 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Prisma SD-WAN Administrator’s Guide 

 Prisma SD-WAN Sites and Devices 

 Use External Services for Monitoring 

 Flow Information Elements 

 Download PDF 

 Prisma SD-WAN 

 Flow Information Elements 

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

 Configure Global and Local IPFIX Prefixes 

 Next 

 Options Information Elements 

 Flow Information Elements 

 View detailed information for flow information elements in Prisma SD-WAN. 

 Where Can I Use
 This? What Do I Need? 

 Prisma SD-WAN (Managed by Strata Cloud Manager ) 

 Prisma SD-WAN 

 The table below describes the flow information
elements, which are based on the IANA IP Flow Information Export
(IPFIX) entity definitions included at https://www.iana.org/assignments/ipfix/ipfix.xhtml#ipfix-information-elements. 

 Flow Field Information Element ElementId Description Data Type Data Type Semantics 

 APPLICATION_HOST httpRequestHost IANA 460 Identifies the domain name of the application's request
host. Encoded in UTF-8. string 

 APP_DEF_ID applicationId IANA 95 Identifies the flow application ID. octetArray default 

 CONNECTION_BIFLOW_BYTES cgnxBidirectionalOctetDeltaCount 1006 CGNX Specifies the number of octets since the previous report
(if any) in both directions for this flow at the observation point. unsigned64 deltaCounter 

 CONNECTION_BIFLOW_PACKETS cgnxBidirectionalPacketDeltaCount 1007 CGNX Specifies the number of packets since the previous report
(if any) in both directions for this flow at the observation point. unsigned64 deltaCounter 

 CONNECTION_INIT cgnxTcpConnInit 1021 CGNX This boolean flag indicates if a SYN-ACK packet
is seen in response to a SYN packet. 

 unsigned8 flags 

 CONNECTION_NTT The NTT subTemplate contains the
following Information Elements and is exported as part of the flow
when you configure the CONNECTION_NTT flow
field option: 
 cgnxNttMinMilliseconds 

 cgnxNttMaxMilliseconds 

 cgnxNttObservedDeltaCount 

 cgnxNttSumMilliseconds 

 cgnxNttMinMilliseconds 1012 CGNX Specifies the minimum network transfer time
for an application in milliseconds. unsigned32 default 

 cgnxNttMaxMilliseconds 1013 CGNX Specifies the maximum network transfer time
for an application in milliseconds. unsigned32 default 

 cgnxNttObservedDeltaCount 1014 CGNX Specifies the total number of network transfer
time observations for this Flow at the Observation Point. unsigned32 deltaCounter 

 cgnxNttSumMilliseconds 1015 CGNX Specifies the sum of network transfer times
for an application in milliseconds. unsigned32 default 

 CONNECTION_RTT The RTT subTemplate contains the
following Information Elements and is exported as part of the flow
when you configure the CONNECTION_RTT flow
field: 

 cgnxRttMinMilliseconds 

 cgnxRttMaxMilliseconds 

 cgnxRttObservedDeltaCount 

 cgnxRttSumMilliseconds 

 cgnxRttMinMilliseconds 1008 CGNX Specifies the minimum round trip time for an application
in milliseconds. unsigned32 default 

 cgnxRttMaxMilliseconds 1009 CGNX Specifies the maximum round trip time for an application
in milliseconds. unsigned32 default 

 cgnxRttObservedDeltaCount 1010 CGNX Specifies the number of round trip time observations
for this Flow at the Observation Point. unsigned32 deltaCounter 

 cgnxRttSumMilliseconds 1011 CGNX Specifies the sum of round trip times for an application
in milliseconds. unsigned32 default 

 CONNECTION_SRT The SRT subTemplate contains the
following Information Elements and is exported as part of the flow
when you include the CONNECTION_SRT flow
field: 
 cgnxSrtMinMilliseconds 

 cgnxSrtMaxMilliseconds 

 cgnxSrtObservedDeltaCount 

 cgnxSrtSumMilliseconds 

 cgnxSrtMinMilliseconds 1016 CGNX Specifies the minimum server response time
for an application in milliseconds unsigned32 default 

 cgnxSrtMaxMilliseconds 1017 CGNX Specifies the maximum server response time
for an application in milliseconds. unsigned32 default 

 cgnxSrtObservedDeltaCount 1018 CGNX Specifies the number of server response time observations
for this Flow at the Observation Point. unsigned32 deltaCounter 

 cgnxSrtSumMilliseconds 1019 CGNX Specifies the sum of server response times
for an application in milliseconds. unsigned32 default 

 CONNECTION_UDPTRT The TRT subTemplate contains the
following Information Elements and is exported as part of the flow
when you configure the CONNECTION_UDPTRT flow
field: 

 cgnxTrtMinMilliseconds 

 cgnxTrtMaxMilliseconds 

 cgnxTrtObservedDeltaCount 

 cgnxTrtSumMilliseconds 

 cgnxTrtMinMilliseconds 1024 CGNX Specifies the minimum transaction response
time for an application in milliseconds. unsigned32 default 

 cgnxTrtMaxMilliseconds 1025 CGNX Specifies the maximum transaction response
time for an application in milliseconds. unsigned32 default 

 cgnxTrtObservedDeltaCount 1026 CGNX Specifies the number of transaction response
time observations for this Flow at the Observation Point. unsigned32 deltaCounter 

 cgnxTrtSumMilliseconds 1027 CGNX Specifies the sum of transaction response times for
an application in milliseconds. unsigned32 default 

 CONNECTION_UNIFLOW_BYTES octetDeltaCount IANA 1 Identifies the number of octets since the previous report
(if any) in incoming packets for this Flow at the Observation Point. unsigned64 deltaCounter 

 CONNECTION_XACT The XACT subTemplate contains
the following Information Elements and is exported as part of the
flow when you configure the CONNECTION_XACT flow
field: 

 cgnxConnectionTransactionSuccessTotalCount 

 cgnxConnectionTransactionFailureTotalCount 

 cgnxConnectionTransactionSuccessTotalCount 1022 CGNX Specifies the total number of connection transaction success
observations for this Flow at the Observation Point. unsigned32 TotalCounter 

 cgnxConnectionTransactionFailureTotalCount 1023 CGNX Specifies the total number of connection transaction failure
observations for this Flow at the Observation Point. unsigned32 TotalCounter 

 DSCP_MAP cgnxDiffServCodePointMap 1000 CGNX Identifies the Prisma SD-WAN DSCP bitmap observation
for the flow at the interface. unsigned64 flags 

 DSCP_LAST ipDiffservCodePoint IANA 195 Identifies the last observed DSCP value for the
flow. unsigned8 Identifier 

 INTERFACES 
 ingressInterface 

 egressInterface 

 Ingress interface—IANA 10 

 Egress interface—IANA 14 
 Identifies a flow's ingress (where packets
are received) and/or egress interface (where packets are sent) (physical
& logical). The Interface ID exported shall match the SNMP IF
ID. unsigned32 Identifier 

 MEDIA_CODEC cgnxMediaCodecList 1034 CGNX A list of codec identifiers as identified from
the flow. Each codec is represented by an single octet in the list. octetArray Identifier 

 MEDIA_JITTER Identifies the jitter of a media
flow. The Media Jitter subTemplate contains the following Information
Elements and is exported as part of the flow when you configure
the MEDIA_JITTER flow field: 

 cgnxMediaJitterMaxMilliseconds 

 cgnxMediaJitterObservedDeltaCount 

 cgnxMediaJitterSumMilliseconds 

 cgnxMediaJitterMaxMilliseconds 1036 CGNX Specifies the maximum jitter time for an application
in milliseconds. unsigned32 default 

 cgnxMediaJitterObservedDeltaCount 1037 CGNX Specifies the number of jitter time observations
for this Flow at the Observation Point. unsigned64 deltaCounter 

 cgnxMediaJitterSumMilliseconds 1038 CGNX Specifies the sum of jitter times for an application
in milliseconds. unsigned32 default 

 MEDIA_LOSS Identifies the packet loss percentage
of a media flow. The Media Loss subTemplate contains the following
Information Elements and is exported as part of the flow when you
configure the MEDIA_LOSS flow field: 

 cgnxMediaLossMax 

 cgnxMediaLossObservedDeltaCount 

 cgnxMediaLossSum 

 cgnxMediaLossMax 1039 CGNX Specifies the maximum packet loss percentage
for an application. float32 quantity 

 cgnxMediaLossObservedDeltaCount 1040 CGNX Specifies the number of packet loss percentage observations
for this Flow at the Observation Point. unsigned64 deltaCounter 

 cgnxMediaLossSum Specifies the sum of packet loss percentages for
an application. float32 quantity 

 MEDIA_MOS cgnxMediaMosMin 1042 CGNX Specifies the minimum MOS sample for an application. float32 quantity 

 cgnxMediaMosMax 1043 CGNX Specifies the maximum MOS sample for an application. float32 default 

 cgnxMediaMosObservedDeltaCount 1044 CGNX Specifies the number of MOS observations for
this Flow at the Observation Point. unsigned32 deltaCounter 

 cgnxMediaMosSum 1045 CGNX Specifies the sum of MOS observations for an application. float32 default 

 QOS_QUEUE cgnxQosQueue 1001 CGNX Identifies the QoS queue that the flow is assigned by
the ION device. 

 unsigned8 Identifier 

 RTP_TRANSPORT_TYPE cgnxRtpTransport 1033 CGNX The value of the RTP transport identifier is Prisma
SD-WAN specific and is identified from the flow. 

 unsigned8 Identifier 

 Identifies the minimum and maximum
TCP window size for a flow.The TcpWin subTemplate contains the following
Information Elements and is exported as part of the flow when you
configure the TRANSPORT_TCP_WINDOWSIZE TRANSPORT_TCP_WINDOWSIZE
flow field: 

 cgnxMinTcpWindowSize 

 cgnxMaxTcpWindowSize 

 cgnxMinTcpWindowSize 1003 CGNX The minimum value observed for the TCP window
for the flow. unsigned32 quantity 

 cgnxMaxTcpWindowSize 1004 CGNX The maximum value observed for the TCP window
for the flow. unsigned32 quantity 

 TROUBLESHOOT_DECISION_MAP Specifies the Prisma SD-WAN decision
bitmap observation for the flow at the interface. 
 The information
is encoded in a set of bit fields allocated in 4 octet word groups.
The decision map flags are mapped to bits according to their flag numbers. 
 Single
Decision map subTemplate : Contains the following Information Elements and
is exported as part of the flow when you configure the TROUBLESHOOT_DECISION_MAP flow
field: 

 cgnxDecisionMap 

 Multiple Decision
map subTemplate : The subTemplateList allows a list of Single Decision
Map subTemplate records to be presented. Currently the maximum that may
be presented is 4. 

 cgnxDecisionMap 1048 CGNX Specifies the CloudGenix decision bitmap observation
for this flow at the Observation Point. octetArray flags 

 TROUBLESHOOT_TCP The troubleshoot TCP flags subTemplate
contains the following Information Elements and is exported as part
of the flow when you configure the TROUBLESHOOT_TCP flow
field: 

 cgnxTcpSynDeltaCount 

 cgnxTcpFinDeltaCount 

 cgnxTcpRstDeltaCount 

 cgnxTcpAckDeltaCount 

 cgnxTcpRexmitDeltaCount 

 cgnxTcpOoopDeltaCount 

 The TCP flags, remit and
oop information is combined into a single unified TCP Troubleshoot
subTemplate. 

 cgnxTcpSynDeltaCount 1050 CGNX The number of packets of this Flow with TCP "Synchronize
sequence numbers" (SYN) flag set observed since the last record
for the flow was sent. unsigned32 deltaCounter 

 cgnxTcpFinDeltaCount 1051 CGNX The number of packets of this Flow with TCP
"No more data from sender" (FIN) flag set observed since the last
record for the flow was sent. unsigned32 (Reduced to unsigned8) deltaCounter 

 cgnxTcpRstDeltaCount 1052 CGNX The number of packets of this Flow with TCP
"Reset the connection" (RST) flag set observed since the last record
for the flow was sent. unsigned32 (Reduced to unsigned8) deltaCounter 

 cgnxTcpAckDeltaCount 1053 CGNX The number of packets of this Flow with TCP "Acknowledgement
field significant" (ACK) flag set observed since the last record
for the flow was sent. unsigned32 deltaCounter 

 cgnxTcpRexmitDeltaCount 1046 CGNX unsigned32 deltaCounter 

 cgnxTcpOoopDeltaCount 1047 CGNX Specifies the number of new TCP out of order packet
observations for this TCP Flow at the Observation Point since the
last export record for the flow. unsigned32 deltaCounter 

 WAN-PATH cgnxWanPath 1002 CGNX WAN path identifier unsigned64 Identifier 

 Previous 

 Configure Global and Local IPFIX Prefixes 

 Next 

 Options Information Elements 

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
