---
url: https://docs.paloaltonetworks.com/advanced-wildfire/wildfire-appliance/wildfire-appliance-overview/wildfire-hybrid-cloud
fetched_at: 2026-09-15T15:08:05Z
source: palo-alto-main
---

# WildFire Hybrid Cloud Clear

Updated on 

 Mar 2, 2026 

 Focus 

 Home 

 Advanced WildFire Powered by Precision AI™ 

 WildFire Appliance Overview 

 WildFire Hybrid Cloud 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Advanced WildFire Powered by Precision AI™ 

 WildFire Hybrid Cloud 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Advanced WildFire 

 Administration 

 Appliance 

 Previous 

 WildFire Private Cloud 

 Next 

 WildFire Appliance Interfaces 

 WildFire Hybrid Cloud 

 Where Can I Use
This? What Do I Need? 

 WildFire Appliance 

 WildFire License 

 A firewall in a WildFire hybrid cloud deployment can forward
certain samples to one of the Palo Alto Networks-hosted WildFire
public clouds and other samples to a WildFire private cloud hosted
by a WildFire appliance. A WildFire hybrid cloud deployment allows
the flexibility to analyze private documents locally and inside
your network, while the WildFire public cloud analyzes files from
the Internet. For example, forward Payment Card Industry (PCI) and
Protected Health Information (PHI) data exclusively to the WildFire
private cloud for analysis, while forwarding Portable Executables
(PEs) to the WildFire public cloud for analysis. In a WildFire hybrid
cloud deployment, offloading files to the public cloud for analysis
allows you benefit from a prompt verdict for files that have been
previously processed in the WildFire public cloud, and also frees
up the WildFire appliance capacity to process sensitive content.
Additionally, you can forward certain file types to the WildFire
public cloud that are not currently supported for WildFire appliance
analysis, such as Android Application Package (APK) files. 

 In a WildFire hybrid cloud deployment, there might be some cases
where a single file matches your criteria for both public cloud
analysis and private cloud analysis; in these cases, the file is
submitted only to the private cloud for analysis as a cautionary
measure. 

 To set up hybrid cloud forwarding, see Forward Files For WildFire Appliance Analysis . 

 Previous 

 WildFire Private Cloud 

 Next 

 WildFire Appliance Interfaces
