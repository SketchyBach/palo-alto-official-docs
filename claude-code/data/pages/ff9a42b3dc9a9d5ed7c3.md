---
url: https://docs.paloaltonetworks.com/prisma-sd-wan/cloudblades/prisma-access-integrations/configure-site-level-settings-to-onboard-a-site/understand-service-and-data-center-groups
fetched_at: 2026-09-16T07:48:07Z
source: strata-and-sase
---

# Understand Service and Data Center Groups Clear

Updated on 

 Wed Feb 25 08:10:06 PST 2026 

 Focus 

 Home 

 Prisma SD-WAN 

 Prisma SD-WAN CloudBlades Integration with Prisma Access 

 Configure Site-Level Settings to Onboard a Site 

 Understand Service and Data Center Groups 

 Download PDF 

 Prisma SD-WAN 

 Understand Service and Data Center Groups 

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

 Edit Application Policy Network Rules 

 Next 

 Verify Standard VPN Endpoints 

 Understand Service and Data Center Groups 

 Understand mapping of standard services and Prisma SD-WAN data centers
 to allow flexibility when creating network policy rules. 

 Where Can I Use This? What Do I Need? 

 Supported CloudBlades: 

 Prisma Access for Networks (Managed by Panorama) 

 Prisma Access for Networks (Cloud Managed) 

 Prisma SD-WAN 

 Prisma Access 

 Supported Cloud Plugin Versions 

 Prisma Access for Networks (Managed by Panorama) CloudBlade versions 3.x.x and
 later 

 Prisma Access for Networks (Cloud Managed) CloudBlade versions 3.x.x and
 4.x.x 

 Prisma SD-WAN uses mapping of standard services and Prisma SD-WAN data centers to allow flexibility when creating network
 policy rules, while accounting for uniqueness across sites. For example, an
 administrator may want to create a single network policy that directs all HTTP and SSL
 internet bound traffic through the primary Palo Alto Prisma Access for Networks in
 the region if it's available. If not available, it can leverage the backup Palo Alto Prisma Access for Networks in the region. Now, the administrator will have different
 primary and backup Cloud Security Service endpoints based on their geographic location.
 Regardless of the site location, the intent and the policy rules will remain the
 same. 

 This is where the concept of endpoints, groups, and domains come into play. To leverage
 the underlying resources available to an administrator, it's important to understand how
 an endpoint, group, and domain work in the Prisma SD-WAN system. 

 Endpoint—A service endpoint is a label representing a specific location or
 network service. It can be of type Prisma SD-WAN , specifically
 Prisma SD-WAN data centers for data center transit services,
 or of type standard. 

 Group—A service group is a label representing a set of common service endpoint
 types. This Service Group label will be used in network policy rules to express
 intent to allow or force traffic to the defined service endpoints. It can be of
 type Prisma SD-WAN or standard and may contain zero or more
 service endpoints. 

 Domain—A domain is a collection of groups, which can be assigned to a set of
 sites. There can be multiple domains defined, but a site can only be assigned to
 one domain at a time. 

 A site will be able to use only the endpoints configured in a group within a domain
 that is assigned to the site. The same group, however, can be in multiple domains
 with different service endpoints, allowing you to use the same policy across
 different sites utilizing different endpoints. 

 Let us further explore the concept of endpoints, groups, and domains using the following
 illustration. 

 The illustration displays how endpoints added to a group are associated with a domain.
 The domains are then bound to a site, thus mapping standard services or Prisma SD-WAN data centers uniquely for each site. 

 A group, with different endpoints, can be mapped to one or more domains and a domain
 can be mapped to one or more sites. 

 Another example to illustrate the concept is shown. For a customer with sites in North
 America and Europe that has one Prisma SD-WAN -enabled data center in each
 region and has adopted a Palo Alto Prisma Access for Networks within each region,
 with two geographic locations in each region, domain mapping is accomplished as
 follows: 

 The same endpoint can be added to more than one group. Only one active group and one
 backup group can be used in a network policy rule. 

 Previous 

 Edit Application Policy Network Rules 

 Next 

 Verify Standard VPN Endpoints
