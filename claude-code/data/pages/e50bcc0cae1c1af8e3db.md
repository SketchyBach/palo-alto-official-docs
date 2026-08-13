---
url: https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/policy/use-address-object-to-represent-ip-addresses/create-an-address-object
fetched_at: 2026-08-13T17:09:59Z
source: palo-alto-main
---

# Create an Address Object Clear

Create an Address Object 

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

 Create an Address Object 

 Updated on 

 Aug 11, 2025 

 Focus 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 한국어 (Korean) 

 Filter

 Updated on 

 Aug 11, 2025 

 Focus 

 Home 

 PAN-OS 

 Policy 

 Use an Address Object to Represent IP Addresses 

 Create an Address Object 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 한국어 (Korean) 

 Create an Address Object 

 Table of Contents 

 Filter

 Previous 

 Address Objects 

 Next 

 Use Tags to Group and Visually Distinguish Objects 

 Create an Address Object 

 Create an address object to group IP addresses or specify an FQDN, and refer to the
 object in a policy, filter, or other function to avoid specifying IP addresses in multiple
 places. 

 Create Address Objects to represent one or more IP
 addresses and then reference the address objects in one or more policy rules,
 filters, or other firewall functions. If you want to change the set of addresses,
 you change an address object once rather than change multiple policy rules or
 filters, which reduces your operational overhead. 

 Create an address object. 

 Select Objects Addresses and Add an address object by
 Name . The name is case-sensitive, must be
 unique, and can be up to 63 characters (letters, numbers, spaces,
 hyphens, and underscores). 

 Select the Type of address object: 

 IP Netmask —Specify a single IPv4 or IPv6
 address, an IPv4 network with slash notation, or an IPv6 address
 and prefix. For example, 192.168.80.0/24 or 2001:db8:123:1::/64.
 Optionally, click Resolve to see the
 associated FQDN (based on the DNS configuration of the firewall
 or Panorama). To change the address object type from
 IP Netmask to
 FQDN , select the FQDN and click
 Use this FQDN . The
 Type changes to
 FQDN and the FQDN you select appears
 in the text field. 

 IP Range —Specify a range of IPv4
 addresses or IPv6 addresses separated by a hyphen. For example,
 192.168.40.1-192.168.40.255 or
 2001:db8:123:1::1-2001:db8:123:1::22. 

 IP Wildcard Mask —Specify an IP wildcard
 address (IPv4 address followed by a slash and a mask, which must
 begin with a 0). For example, 10.5.1.1/0.127.248.2. A zero
 ( 0 ) in the mask indicates the
 bit being compared must match the bit in the IP address that is
 covered by the zero. A one ( 1 ) in
 the mask (wildcard bit) indicates the bit being compared need
 not match the bit in the IP address covered by the one. 

 FQDN —Specify the domain name. The FQDN
 initially resolves at commit time. The firewall subsequently
 refreshes the FQDN based on the time-to-live (TTL) of the FQDN
 in DNS, as long as the TTL is greater than or equal to the
 Minimum FQDN Refresh Time you
 configure (or the default of 30 seconds). The FQDN is resolved
 by the system DNS server or a DNS proxy object, if a proxy is
 configured. Click Resolve to see the
 associated IP address (based on the DNS configuration of the
 firewall or Panorama). To change the address object type from
 FQDN to IP Netmask, select an IP Netmask and click
 Use this address . The
 Type changes to IP
 Netmask and the IP address you select appears in
 the text field. 

 ( Optional ) Enter one or more Tags to apply to
 the address object. 

 Click OK . 

 Commit your changes. 

 View logs filtered by address object, address group, or wildcard address. 

 For example, select Monitor Logs Traffic to view traffic logs. 

 Select 

 to add a log filter. 

 Select the Address attribute, the
 in Operator, and enter the name of the
 address object for which you want to view logs. Alternatively, enter an
 address group name or a wildcard address, such as
 10.155.3.4/0.0.240.255. 

 Click Apply . 

 View a custom report based on an address object. 

 Select Monitor Manage Custom Reports and select a report that uses a Database such as Traffic
 Log. 

 Select Filter Builder . 

 Select an Attribute such as Address ,
 Destination Address or Source
 Address , select an Operator, and enter the name of the
 address object for which you want to view the report. 

 Use a filter in the ACC to view network activity based on a source IP address
 or destination IP address that uses an address object. 

 Select ACC Network Activity . 

 View the Source IP Activity—For Global Filters ,
 click 

 to add a filter and select one of
 the following: Address or Source Source Address or Destination Destination Address and select an address object. 

 View the Destination IP Activity—For Global
 Filters , click the 

 to add a filter and select one of
 the following: Address or Source Source Address or Destination Destination Address and select an address object. 

 Previous 

 Address Objects 

 Next 

 Use Tags to Group and Visually Distinguish Objects 

 On This Page 

 PAN-OS 

 Next-Generation Firewall 

 Policy 

 11.1 

 Network Security 

 11.1 & Later 

 Administration 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
