---
url: https://docs.paloaltonetworks.com/prisma-access-agent/user-guide/configure-forwarding-profiles-to-manage-agent-traffic
fetched_at: 2026-08-13T17:22:37Z
source: palo-alto-main
---

# Set Up Forwarding Profiles to Manage Agent Traffic Clear

Set Up Forwarding Profiles to Manage Agent Traffic 

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

 Set Up Forwarding Profiles to Manage Agent Traffic 

 Updated on 

 Wed Jul 01 22:45:41 PDT 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Access Agent Docs 

 Administration 

 User Guide 

 Release Notes 

 New Features 

 Updated on 

 Wed Jul 01 22:45:41 PDT 2026 

 Focus 

 Home 

 Prisma Access Agent 

 Prisma Access Agent User Guide 

 Set Up Forwarding Profiles to Manage Agent Traffic 

 Download PDF 

 Prisma Access Agent 

 Set Up Forwarding Profiles to Manage Agent Traffic 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Prisma Access Agent Docs 

 Administration 

 User Guide 

 Release Notes 

 New Features 

 Set Up Forwarding Profiles to Manage Agent Traffic 

 Provide
 consistent security for internet, SaaS, and private app access across locations, using
 traffic forwarding rules to optimize traffic routing and policy enforcement. 

 Where Can I Use This? What Do I Need? 

 Prisma Access (Managed by Strata Cloud Manager) 

 Prisma Access (Managed by Panorama) 

 NGFW (Managed by Panorama) 

 Check the prerequisites for the deployment you're
 using 

 Contact your Palo Alto Networks account representative to
 activate the Prisma Access Agent feature 

 Forwarding profiles provide a seamless end-to-end security solution for consistent
 access to internet, SaaS, and private applications for your users under varying
 conditions. This feature enables always-on security for internet access from any
 location and on-demand security for private apps based on user presence (remote or
 on-premises). 

 To effectively configure and use forwarding profiles, you will need to understand
 several key components: 

 Forwarding Profiles 

 Forwarding profiles contain a set of rules that define how to direct traffic based on
 various criteria. Once you set up the forwarding profiles, you can assign them to
 users or user groups in the Agent Settings page. These forwarding
 profiles allow you to create a comprehensive traffic management strategy tailored to
 your organization's needs. 

 Traffic Forwarding Rules 

 Traffic forwarding rules within forwarding profiles consist of several important
 elements. Traffic that matches a rule is steered according to the traffic forwarding
 specifications. 

 ( macOS and Windows agents only ) ( Strata Cloud Manager Managed Prisma Access ) User
 Location : You can specify rules based on whether users
 are remote or on-premises, using methods like Internal Host Detection
 (IHD) or source IP addresses. 

 If enabled, the Internal Host Detection setting in the agent app settings takes precedence over
 the Internal Host Detection setting in forwarding profiles. Unlike
 the Internal Host Detection setting in the agent app settings, the
 Internal Host Detection rules in forwarding profiles don't suppress
 the tunnel. 

 Traffic Objects : You can define the criteria for
 traffic handling based on traffic objects. This includes applications,
 destinations, and traffic types, such as network traffic and DNS
 traffic.
 (Applications do not
 apply to agents on iOS, Android, and ChromeOS.) 

 Connectivity Options : For each rule, you can
 choose how to route the traffic. Options include: 
 Direct —Allows traffic to go straight to
 its destination. Selecting Direct will
 bind the traffic to the physical adapter on the endpoint rather
 than the tunnel. 

 Block —Blocks traffic at the endpoint 

 Bypass —Ignores specific traffic to
 enabling third-party agents to handle designated connections (macOS and Windows agents only) 

 Best Available - Fail Safe —Routes traffic
 through the tunnel to the nearest gateway for inspection and
 policy enforcement but block access if the user can't connect to
 the tunnel or the traffic type is unsupported (macOS and Windows agents only) 

 Best Available - Fail Open —Routes traffic
 through the tunnel to the nearest gateway for inspection and
 policy enforcement but allow access even if the user can’t
 connect to the tunnel or the traffic type is unsupported 

 You can also customize your own connectivity option to direct traffic to
 the tunnel, the proxy (if enabled), or fallback to Advanced DNS
 Security Resolver if the tunnel is down. (Proxy and ADNS
 Resolver support are available only for macOS and Windows agents.) 

 ( macOS and Windows agents only ) Fallback Behavior : For rules using custom
 connectivity options, you can set the fallback behavior when the primary
 connection is unavailable: 
 Block —Blocks all traffic when the tunnel
 is down or for unsupported traffic types 

 Direct —Allows traffic to go directly to
 its destination when the tunnel is down or for unsupported
 traffic types 

 For agents on iOS,
 Android, and ChromeOS, the fallback behavior is defined by the mobile
 device management (MDM) configuration. 

 Predefined Rules —The system includes predefined forwarding rules for
 common scenarios, such as: 

 ( macOS and Windows agents only ) Video Streaming —Directs network traffic
 from video streaming apps such as YouTube and Netflix outside the
 tunnel (direct connectivity) 

 Default —Sends all DNS and network traffic
 through the tunnel to Prisma Access for inspection 

 How Forwarding Profiles Work 

 When Prisma Access Agent receives a connection request, it evaluates the
 forwarding rules in your forwarding profile in priority order. The agent matches
 the connection against each rule's criteria including destination addresses,
 source applications, traffic types, and user location. When all criteria in a
 rule match, the agent applies that rule's connectivity method to route the
 traffic. If a rule does not match, the agent continues evaluating subsequent
 rules until it finds a match or reaches the default rule. 

 Before you begin to configure
 forwarding profiles for Prisma Access Agent on Windows endpoints, refer to Windows Forwarding Profiles Considerations . 

 On Prisma Access Agent and GlobalProtect coexistence
 tenants, Prisma Access Agents will use forwarding profiles to manage traffic
 forwarding rules, while GlobalProtect will continue to use existing split tunnel configuration on GlobalProtect
 gateways . 

 Strata Cloud Manager 

 Panorama 

 Set Up Forwarding Profiles (Strata Cloud Manager Managed Deployments) 

 Provide
 consistent security for internet, SaaS, and private app access across locations, using
 traffic forwarding rules to optimize traffic routing and policy enforcement. 

 To configure forwarding profiles on Prisma Access (Managed by Strata Cloud Manager) deployments, complete the
 following steps: 

 Navigate to the Forwarding Profiles page from Strata Cloud Manager . 

 Select Configuration NGFW and Prisma Access Configuration Scope Mobile Users Container Mobile Users . 

 Edit the settings in the Forwarding Profiles
 Setup section by selecting the gear icon. 

 ( macOS and Windows agents only ) Set up User Locations if you want to specify the
 location that a forwarding rule applies to. You can specify Internal Host
 Detection to apply the rule to users connected to your internal network, or
 specify source IP addresses for external locations like branch offices. 

 User location detection occurs automatically when the agent loads a new
 forwarding profile, when you manually import a profile, or when network
 changes occur such as switching WiFi networks or changing IP addresses. The
 agent uses Internal Host Detection or source IP address matching to
 determine the current location, then applies the appropriate forwarding
 rules for that location. 

 If enabled, the Internal Host Detection setting in the agent app settings takes precedence over
 the Internal Host Detection setting in forwarding profiles. Unlike
 the Internal Host Detection setting in the agent app settings, the
 Internal Host Detection rules in forwarding profiles don't suppress
 the tunnel. 

 In the Forwarding Profiles Setup page, select User Locations Add User Location . 

 Enter a meaningful Name for the user location
 that you want to add. 

 Select Internal Host Detection for users on the
 internal corporate network, or select IP
 Addresses to steer traffic based on private IP
 addresses. 

 Internal Host Detection —Specify the
 IP Address and
 FQDN for your internal network.
 Only IPv4 addresses are supported. 

 If enabled, the Internal Host Detection setting in the agent app settings takes precedence over
 the Internal Host Detection setting in forwarding profiles. Unlike
 the Internal Host Detection setting in the agent app settings, the
 Internal Host Detection rules in forwarding profiles don't suppress
 the tunnel. 

 IP Addresses —Provide one or more
 source IP addresses of endpoints. You must enter specific
 IPv4 addresses. You can also enter a subnet (using CIDR
 notation), such as 192.168.1.0/24 . 

 The source IP address here is the IP address assigned to
 the endpoints and not the egress IP address. 

 Save the user location settings. 

 ( macOS, Windows, and Linux agents only ) Set up Source
 Applications if you want to steer traffic based on the
 application name. 

 In the Forwarding Profiles Setup page, select Source Applications Add Source Application . 

 Enter a meaningful Name for the application that
 you want to add. 

 Click + in the
 Applications table and enter the complete
 path of the application. You can add one or more applications to the
 table. 

 You will select these applications when setting up the forwarding
 rules in a forwarding profile. For example, to exclude application
 traffic, select Direct connectivity when
 configuring the forwarding rule. Traffic from these applications
 will be sent through the physical adapter on the endpoints rather
 than the tunnel (the virtual adapter). If you choose to include
 application traffic, select Best Available - Fail
 Safe (macOS and Windows agents only),
 Best Available - Fail Open , or your own
 configured connectivity option when configuring the forwarding
 rule. 

 For example, to manage traffic from the Zoom application, add the
 following complete paths: 
 Windows endpoints:
 %AppData%\Roaming\Zoom\bin\Zoom.exe 

 macOS endpoints:
 /Applications/zoom.us.app/Contents/MacOS/zoom.us 

 Wildcard Character Support 

 ( macOS, Windows, and Linux agents only ) For
 applications with dynamic installation locations, you can use
 the asterisk (*) as a wildcard character to replace exactly one
 directory component in the path. You can include multiple
 wildcards throughout the path to handle various scenarios such
 as version-specific directories, user-specific installations, or
 architecture-dependent locations. To account for changing
 version numbers or user directories, you can place wildcards in
 the middle or end of a path (when you need to match any
 executable within a specific directory). 

 Each wildcard must be a single asterisk (*) that occupies an
 entire directory component; double asterisks (**) are not
 supported. A wildcard cannot be combined with other characters
 within the same component. The
 path must begin with a valid root directory on macOS or
 Linux, or a drive letter on Windows, so you cannot start the
 path with a wildcard character. 

 Valid Examples 

 /abc/v1/app 

 /*/bin/curl 

 /opt/*/Cellar/*/*/bin/wget 

 C:\Windows\System32\* 

 C:\Users\*\AppData\Roaming\Zoom\bin\* 

 Invalid Examples 

 C:\Users\xyz\AppData\Roaming\Zoom\bin\zoom* 
 — wildcard combined with other characters in the same
 component 

 */bin/curl — path starts with a
 wildcard 

 C:\Users\**\AppData\Roaming\Zoom\bin\zoom.exe 
 — double asterisk ( ** ) is not a valid
 wildcard pattern 

 /abc/**/xyz/app — double asterisk
 ( ** ) is not a valid wildcard
 pattern 

 If any path in the list is invalid — including paths that use
 unsupported wildcard patterns such as ** —
 the agent rejects the rule and traffic falls through to the
 Default profile, even if other paths
 in the list are valid. 

 Wildcard support for source application paths is not
 available on Arch Linux ARM64. On Arch Linux ARM64, Prisma Access Agent cannot identify which application
 generated a given traffic flow, so source application rules
 — including those that use wildcards — do not apply. Use
 destination-based rules on Arch Linux ARM64 endpoints.
 Wildcard support for source application paths works as
 expected on Arch Linux x86_64 endpoints. 

 Wildcard support for source application paths on Linux
 requires Prisma Access Agent 26.2.2 or later. On Linux
 endpoints running 26.2.1, source application rules require
 the complete real path of the application and wildcard
 characters are not supported — use destination-based rules
 for applications with variable paths on those endpoints. 

 If you have a list of applications in a text file in comma-separated
 values format (.csv), you can Upload .csv
 File . 

 Save the source application. 

 Repeat these steps to add more source applications. 

 Set up Destinations if you want to create a split tunnel
 based on the destination domain or access routes. 

 On Windows endpoints,
 Prisma Access Agent supports UDP traffic steering to IP-based
 destinations and source app-based rules only. Forwarding profile rules
 that use FQDN or domain-based destination objects don't apply to UDP
 traffic on Windows endpoints. 

 In the Forwarding Profiles Setup page, select Destinations Add Destination . 

 Prisma Access Agent also offers predefined
 destination domains, such as Okta SAML Authentication
 Domains , Azure SAML Authentication
 Domains , Microsoft Client Authentication
 Domains , and Video Traffic so
 that you can easily create forwarding rules for these destination
 domains. 

 Enter a meaningful Name for the destination that
 you want to add. 

 Add a destination by specifying the domain name, access route, or
 both. 

 ( macOS, Windows, and Linux agents only ) To add a
 destination domain, click + in the
 FQDNs table and enter the FQDN for
 the destination domain. You can optionally add a port. If you
 don't specify a port, all ports for the specified domain are
 subjected to the forwarding rule. You can add one or more
 domains for traffic management. 

 You can enter alphanumeric characters for the FQDN. You
 can also specify a wildcard domain by including a
 wildcard character (*) in the FQDN. However, the
 wildcard must appear only once and must be the first
 character of the string, and a period must follow the
 wildcard. 

 The following are valid FQDN examples: 
 example.com (exact
 domain) 

 *.local (wildcard
 domain) 

 The following FQDN examples are not valid: 
 .example.com (missing
 characters before the first period) 

 *example.com (missing
 period after the wildcard) 

 my*.example.* (only one
 wildcard allowed and it must appear at the start
 of the string) 

 *.example.*.com (wildcard
 not allowed in middle of string) 

 Prisma Access Agent will check whether your FQDN entry is
 valid or not. For invalid domain inputs, the
 " Invalid FQDN format "
 message appears. 

 If you add a port, the port can only contain positive
 numbers. The range is 1-65535. 

 You will select these destinations when setting up the
 forwarding rules in a forwarding profile. For example, to
 exclude traffic based on the domain name, select
 Direct connectivity when
 configuring the forwarding rule. Traffic from the domain
 will be sent through the physical adapter on the endpoints
 rather than the tunnel (the virtual adapter). If you choose
 to include traffic based on the domain name, select
 Best Available - Fail Safe (macOS
 and Windows agents only), Best Available - Fail
 Open , or your own configured connectivity
 option when configuring the forwarding rule. Traffic from
 the domain is routed to Prisma Access, even if it meets the
 excluded traffic criteria. 

 To add an access route, click + in the
 IP Addresses table and enter a
 destination subnet. You can add one or more access routes for
 traffic management. 
 ( macOS and Windows agents only ) For IPv6 addresses, you can enter: 
 Single IPv6 addresses using standard notation (for
 example, 2001:0db8:85a3:: ) 

 IPv6 subnets using CIDR notation (for example,
 2001:0db8:85a3::/48 ) 

 For IPv4 addresses, you can a wildcard character (*) in
 the IP address, but the wildcard must not appear in the
 middle of the IP address. Once a wildcard is used, all
 the following octets must also be wildcards. 

 The following are some examples of valid IPv4
 addresses: 
 1.2.3.4 (exact IP
 address) 

 1.4.3.* (wildcard IP
 address) 

 1.*.*.* 

 *.*.*.* (full wildcard IP
 address) 

 1.2.3.4/32 (exact IP
 address followed by CIDR) 

 The following are examples of an invalid IPv4 address: 
 1.2.3.300 (each byte must
 be 0-255) 

 3.3.3.3/255.255.255.256 
 (invalid subnet mask) 

 Prisma Access Agent will check whether your IP address
 entry is valid or not. For invalid inputs, a message
 appears indicating that the IP address is not valid. 

 In some cases (such as
 1.2.*.4 and
 7.7.7.7/33 ), the
 configuration validator will allow the entry, but the
 agent will ultimately reject it because the entry does
 not adhere to a supported format. In this case, the
 agent will reject the forwarding profile rule and fall
 back to the fail-safe mode, forwarding all traffic to
 the
 tunnel. 

 If you don't include or exclude routes or applications,
 every request is routed through the tunnel. Also, all
 traffic is inspected and subjected to policy enforcement
 whenever users connect to Prisma Access. 

 When you
 define split tunnel traffic to exclude access routes (by
 selecting Direct connectivity in the
 forwarding rule), these routes are sent through the physical
 adapter on the endpoint instead of being sent through the
 virtual adapter (the tunnel). This way, you can send
 latency-sensitive or high-bandwidth traffic outside of the
 tunnel, while all other traffic is routed through the tunnel
 for inspection and policy enforcement by the
 gateway. 

 When you define split tunnel traffic to
 include access routes (by selecting Best
 Available - Fail Safe 
 (macOS and Windows agents only) , Best Available - Fail Open , or
 your own configured connectivity option in the forwarding
 rule), the gateway pushes these routes to the remote users’
 endpoints to specify what traffic these endpoints can send
 through the tunnel. 

 Specify exclude routes that are
 more specific than include routes; otherwise, you might
 exclude more traffic than intended. 

 If you have a
 list of IP addresses in a text file in
 .csv format, you can
 Upload .csv File . 

 Save the destinations. 

 Repeat these steps to add more destinations. 

 Set up Connectivity options to direct traffic based on
 the connectivity method. 

 Prisma Access Agent provides predefined connectivity
 options when users are using the best available location but the tunnel and
 proxy (if enabled) are not available or the traffic type is unsupported
 (such as IPv6 traffic). 
 ( macOS and Windows agents only ) Best Available - Fail Safe —Connect to
 the nearest gateway or Prisma Access location but block access if
 the user can’t connect to the tunnel and proxy (when enabled) or the
 traffic type is unsupported, such as proxy-only UDP traffic. 

 Best Available - Fail Open —Connect to the
 nearest gateway or Prisma Access location but allow access even if
 the user can’t connect to the tunnel and proxy (when enabled) or the
 traffic type is unsupported, such as proxy-only UDP traffic. 

 To set up a custom connectivity option: 

 In the Forwarding Profiles Setup page, select Connectivity Add Connectivity . 

 Enter a meaningful Name for the connectivity
 option you want to add. 

 ( Strata Cloud Manager only) Select Type Prisma Access Agent . 

 Configure the Connectivity Methods . By default,
 only the Tunnel connectivity method is enabled,
 but you can also send traffic to a proxy or send DNS traffic to Advanced
 DNS Security Resolver as a fallback connection if the tunnel
 is disconnected (macOS and Windows agents only) . 

 Tunnel —Directs traffic through the
 tunnel 

 ( macOS and Windows agents only ) Proxy —Directs traffic to the
 proxy 

 ( macOS and Windows agents only ) ADNS —Directs DNS traffic to
 Advanced DNS Security Resolver if the tunnel is disconnected.
 You can enable ADNS only if
 Tunnel is enabled. 

 ( macOS and Windows agents only ) Usage: 

 To direct internet traffic only through the tunnel, enable
 Tunnel and disable
 Proxy . 

 To direct internet traffic only to the proxy, disable
 Tunnel and enable
 Proxy . 

 To direct internet traffic to the proxy only when the tunnel is
 disconnected or unavailable, enable both 
 Tunnel and Proxy .
 Prisma Access Agent will send traffic through the tunnel, and if
 the tunnel becomes disconnected, will send traffic to the
 proxy. 

 To direct DNS traffic to Advanced DNS Security Resolver in the
 event the tunnel gets disconnected, enable both
 Tunnel and
 ADNS . 

 ( macOS and Windows agents only ) Select a Fallback behavior if the user is not
 connected using the specified connectivity method. You can prevent
 access ( Block ) or allow access
 ( Direct ). 

 For agents on iOS,
 Android, and ChromeOS, the fallback behavior is defined by the mobile
 device management (MDM) configuration. 

 Save your connectivity settings. 

 Repeat these steps to add more connectivity settings. 

 Create a forwarding profile that allows or excludes traffic based on the source
 applications, user location, destination, or connectivity options that you
 defined. 

 From the Forwarding Profiles Setup page, add a forwarding
 profile. 

 Select Forwarding Profiles Add Forwarding Profile Prisma Access Agent . 

 Enter a meaningful Name for the forwarding
 profile. 

 Add one or more forwarding rules. 

 The Forwarding Rules table shows the rules
 that make up the forwarding profile. By default, all forwarding
 profiles contain the following rules: 
 ( macOS and Windows agents only ) The Video Streaming forwarding
 rule, which sends all network traffic from video streaming
 apps outside the tunnel (direct connectivity). By excluding
 lower risk video streaming traffic (such as YouTube and
 Netflix) from the tunnel, you can decrease bandwidth
 consumption on the gateway. 

 The Default forwarding rule, which
 sends all DNS and network traffic through the tunnel. Any
 new rules that you add are placed above the default rule.
 You cannot delete or move the default forwarding rule, but
 you can disable it or change its
 Connectivity setting. 

 An implicit forwarding rule for basic endpoint connectivity
 that allows traffic such as DHCP, loopback, Prisma Access Agent Endpoint Manager, ADEM, and Remote Browser Isolation
 (RBI) traffic. The implicit forwarding rule is
 not displayed and cannot be changed. 

 For macOS, Windows, and Linux agents, traffic forwarding rules are
 applied from the top down in the forwarding profile. This means that
 when Prisma Access Agent receives a connection request, it evaluates
 the forwarding rules from the top to the bottom of the Forwarding
 Rules table. The agent matches the connection against each rule's
 criteria. When all criteria in a rule match, the agent applies that
 rule's connectivity method to route the traffic. If a rule does not
 match, the agent continues evaluating the next rule in the table
 until it finds a match or reaches the default rule. Therefore,
 configure the forwarding profile in a top-down manner, such as
 configuring the most specific rules first and the least specific
 rules last. 

 For mobile agents such
 as iOS, Android, and ChromeOS, rules will be consolidated top-down
 based on the destination to determine the access route for traffic
 forwarding. 

 Enter the specifications for the forwarding rule. 

 Enable the rule. 

 Enter a meaningful Name for the
 rule. 

 ( macOS, Windows, and Linux agents only ) Select a
 Source Application that you defined
 previously. If you select Any , the
 forwarding rule will apply to traffic from any source
 applications. 
 The rule will match only if the specified
 source application makes the connection. 

 ( macOS and Windows agents only ) ( Prisma Access Agent 26.2 ) Select a
 User Location . If you did not set up
 a user location or if you allow the rule to match any user
 location, select Any . 
 The rule will
 match only if an endpoint is connected to the specified user
 location. 

 For Prisma Acces Agents earlier than version
 26.2, any forwarding rules with a user location setting
 other than Any will be disabled by
 the Endpoint Manager. Running the pacli traffic
 logs command will show the verdict:

 [rule name]- disabled, The agent does not support user location 

 Select a Destination . If you select
 Any , the forwarding rule will apply
 to traffic from any destination domain or IP address. 
 The rule
 will match only if the traffic matches the specified
 destination domain or IP address. 

 On Windows endpoints,
 Prisma Access Agent supports UDP traffic steering to IP-based
 destinations and source app-based rules only. Forwarding profile rules
 that use FQDN or domain-based destination objects don't apply to UDP
 traffic on Windows endpoints. 

 Select a Connectivity option that you
 configured, or select one of the following predefined
 connectivity options to handle traffic that matches the selected
 user location, application, or destination: 
 Direct —Sends the matching traffic
 outside of the tunnel. All matching traffic is sent
 directly to the physical adapter on the endpoint without
 inspection. 

 Block —Blocks all matching traffic
 at the endpoint. 

 ( macOS and Windows agents only ) Bypass — Bypasses the
 matching traffic to allow third-party agents on
 endpoints to process the connections if they
 are active and configured to handle the designated
 traffic. If no third-party agent is present or
 configured to handle the traffic, the system sends the
 traffic to the tunnel (if present) or directly to its
 destination if the tunnel is not present. 

 ( macOS and Windows agents only ) Best Available - Fail
 Safe —Connects to the nearest gateway or
 Prisma Access location but blocks all matching traffic
 when the tunnel and proxy (if configured) are down or
 for unsupported traffic types. 

 Best Available - Fail
 Open —Connects to the nearest gateway or
 Prisma Access location but allows the matching traffic
 to go directly to its destination when the tunnel and
 proxy (if configured) are down or for unsupported
 traffic types. 

 Select the Traffic Type : 
 Specify
 whether to use split DNS to allow users to direct their DNS
 queries for applications and resources over the tunnel or
 outside the tunnel in addition to network traffic. 

 DNS —Includes or excludes rules
 that are applied only to DNS traffic and not to network
 application traffic. All network application traffic
 goes through the tunnel regardless of the split tunnel
 based on the destination domain that you specified for
 inclusions or exclusions. 

 DNS + Network Traffic —Ensures
 that the split tunnel based on the destination domain
 you specified for inclusions or exclusions are applied
 to the DNS traffic and the associated network
 application traffic for that domain. 

 Network Traffic —Includes or
 excludes rules that are applied only to network
 application traffic and not to DNS traffic. All DNS
 traffic goes through the tunnel regardless of the split
 tunnel based on the destination domain that you
 specified for inclusions or exclusions. 

 For Windows agents, the DNS + Network
 Traffic split tunnel option is not
 supported for source application-based split tunnel
 rules . If you set up split tunneling to include
 or exclude traffic from the tunnel based on application
 names and select DNS + Network
 Traffic , DNS query packets for excluded
 and included apps will not honor the split tunnel
 rule. 

 Click Add to save the forwarding rule. 

 The rule is added to the Forwarding Rules table. You can add multiple
 rules to the forwarding profile. 

 In the Forwarding Rules table, adjust the priority of the rules in a
 top-down manner, such that the most specific rules go first and the
 least specific rules go last in the table. You can select the checkbox
 next to a rule and select Move Up or
 Move Down . 

 ( macOS and Windows agents only ) Configure the Traffic Enforcement options to determine
 how you want traffic to be enforced. 

 Block outbound LAN access when connected to the
 tunnel —When enabled, the agent blocks direct access to
 the local network when the agent is connected to the tunnel. 
 Blocking
 access to your local network causes all
 traffic from being sent to
 the local adapter. In addition, your users won't be able to access
 resources on the local subnet, such as printers. Split tunnel
 traffic based on access route, destination domain, and application
 still works as expected. 

 If you disable this option, your end
 users can access local resources without requiring them to first
 connect to Prisma Access using the Prisma Access Agent . The default
 setting is disabled. 

 Block inbound access when connected to the
 tunnel —When enabled, the agent blocks all inbound
 connections from the tunnel. The default setting is disabled. 

 Block Non-TCP and Non-UDP based traffic when connected
 to tunnel —When enabled, the agent blocks all non-TCP and
 non-UDP traffic including ICMP, GRE, IGMP, and IPSec protocols while
 connected to the tunnel. TCP and UDP traffic steering will adhere to the
 forwarding rules configured above. The default is disabled. 
 For
 details, refer to Configure Traffic Enforcement for Non-TCP and Non-UDP Protocols . 

 Allow ICMP for troubleshooting —When enabled,
 the agent blocks all non-TCP and non-UDP traffic except ICMP. This
 configuration allows ICMP traffic while blocking all other Layer 3
 protocols like GRE and IPSec. This option is available only if you
 enable Block Non-TCP and Non-UDP based traffic when connected
 to tunnel . The default is disabled. 

 Save your forwarding profile. 

 Push the configuration by selecting Push Config Push . This action will make your forwarding profile available for
 selection in the Agent Settings page. 

 Set Up Forwarding Profiles (Panorama Managed Deployments) 

 Provide
 consistent security for internet, SaaS, and private app access across locations, using
 traffic forwarding rules to optimize traffic routing and policy enforcement. 

 You can configure forwarding profiles for macOS, Windows, or Linux agents in Prisma Access (Managed by Panorama) and NGFW (Managed by Panorama) deployments. 

 Complete the following steps: 

 Navigate to the Prisma Access Agent setup. 

 Prisma Access (Managed by Panorama) 
 From the Cloud Services plugin in Panorama,
 select Panorama Cloud Services Prisma Access Agent Launch Prisma Access Agent . 

 NGFW (Managed by Panorama) 
 Log in to Strata Cloud Manager as
 the administrator. 

 Select Configuration Forwarding Profiles . 

 ( macOS, Windows, and Linux agents only ) Set up Source
 Applications if you want to steer traffic based on the
 application name. 

 Select Source Applications Add Source Application . 

 Enter a meaningful Name for the application that
 you want to add. 

 Click + in the Source
 Applications table and enter the complete path of the
 application. You can add one or more applications to the table. 

 You will select these applications when setting up the forwarding
 rules in a forwarding profile. To exclude application traffic,
 select Direct connectivity when configuring
 the forwarding rule. Prisma Access Agent sends these applications
 through the physical adapter on the endpoints rather than the tunnel
 (the virtual adapter). If you choose to include application traffic,
 select the Best Available - Fail Safe 
 (macOS and Windows agents only) , Best Available - Fail Open , or your own
 configured connectivity option when configuring the forwarding
 rule. 

 For example, to manage traffic from the Zoom application, add the
 following complete paths: 
 Windows endpoints:
 %AppData%\Roaming\Zoom\bin\Zoom.exe 

 macOS endpoints:
 /Applications/zoom.us.app/Contents/MacOS/zoom.us 

 Wildcard Character Support 

 ( macOS, Windows, and Linux agents only ) For
 applications with dynamic installation locations, you can use
 the asterisk (*) as a wildcard character to replace exactly one
 directory component in the path. You can include multiple
 wildcards throughout the path to handle various scenarios such
 as version-specific directories, user-specific installations, or
 architecture-dependent locations. To account for changing
 version numbers or user directories, you can place wildcards in
 the middle or end of a path (when you need to match any
 executable within a specific directory). 

 Each wildcard must be a single asterisk (*) that occupies an
 entire directory component; double asterisks (**) are not
 supported. A wildcard cannot be combined with other characters
 within the same component. The
 path must begin with a valid root directory on macOS or
 Linux, or a drive letter on Windows, so you cannot start the
 path with a wildcard character. 

 Valid Examples 

 /abc/v1/app 

 /*/bin/curl 

 /opt/*/Cellar/*/*/bin/wget 

 C:\Windows\System32\* 

 C:\Users\*\AppData\Roaming\Zoom\bin\* 

 Invalid Examples 

 C:\Users\xyz\AppData\Roaming\Zoom\bin\zoom* 
 — wildcard combined with other characters in the same
 component 

 */bin/curl — path starts with a
 wildcard 

 C:\Users\**\AppData\Roaming\Zoom\bin\zoom.exe 
 — double asterisk ( ** ) is not a valid
 wildcard pattern 

 /abc/**/xyz/app — double asterisk
 ( ** ) is not a valid wildcard
 pattern 

 If any path in the list is invalid — including paths that use
 unsupported wildcard patterns such as ** —
 the agent rejects the rule and traffic falls through to the
 Default profile, even if other paths
 in the list are valid. 

 Wildcard support for source application paths is not
 available on Arch Linux ARM64. On Arch Linux ARM64, Prisma Access Agent cannot identify which application
 generated a given traffic flow, so source application rules
 — including those that use wildcards — do not apply. Use
 destination-based rules on Arch Linux ARM64 endpoints.
 Wildcard support for source application paths works as
 expected on Arch Linux x86_64 endpoints. 

 Wildcard support for source application paths on Linux
 requires Prisma Access Agent 26.2.2 or later. On Linux
 endpoints running 26.2.1, source application rules require
 the complete real path of the application and wildcard
 characters are not supported — use destination-based rules
 for applications with variable paths on those endpoints. 

 Create the source application. 

 Repeat these steps to add more source applications. 

 Set up Destinations if you want to create a split tunnel
 based on the destination domain or access routes. 

 On Windows endpoints,
 Prisma Access Agent supports UDP traffic steering to IP-based
 destinations and source app-based rules only. Forwarding profile rules
 that use FQDN or domain-based destination objects don't apply to UDP
 traffic on Windows endpoints. 

 Select Destinations Add Destination . 

 Prisma Access Agent also offers predefined
 destination domains, such as Okta SAML Authentication
 Domains , Azure SAML Authentication
 Domains , Microsoft Client Authentication
 Domains , and Video Traffic so
 that you can easily create forwarding rules for these destination
 domains. 

 Enter a meaningful Name for the destination that
 you want to add. 

 Add a destination by specifying the domain name, access route, or
 both. 

 ( macOS, Windows, and Linux agents only ) To add a
 destination domain, click + in the
 FQDNs table and enter the FQDN for
 the destination domain. You can optionally add a port. If you
 don't specify a port, all ports for the specified domain are
 subjected to the forwarding rule. You can add one or more
 domains for traffic management. 

 You can enter alphanumeric characters for the FQDN. You
 can also specify a wildcard domain by including a
 wildcard character (*) in the FQDN. However, the
 wildcard must appear only once and must be the first
 character of the string, and a period must follow the
 wildcard. 

 The following are valid FQDN examples: 
 example.com (exact
 domain) 

 *.local (wildcard
 domain) 

 The following FQDN examples are not valid: 
 .example.com (missing
 characters before the first period) 

 *example.com (missing
 period after the wildcard) 

 my*.example.* (only one
 wildcard allowed and it must appear at the start
 of the string) 

 *.example.*.com (wildcard
 not allowed in middle of string) 

 Prisma Access Agent will check whether your FQDN entry is
 valid or not. For invalid domain inputs, the
 " Invalid FQDN format "
 message appears. 

 If you add a port, the port can only contain positive
 numbers. The range is 1-65535. 

 You
 will select these destinations when setting up the
 forwarding rules in a forwarding profile. To exclude traffic
 based on the domain name, select
 Direct connectivity when
 configuring the forwarding rule. Prisma Access Agent will
 send traffic from the domain through the physical adapter on
 the endpoints rather than the tunnel (the virtual adapter).
 If you choose to include traffic based on the domain name,
 select the Best Available - Fail Safe 
 (macOS and Windows agents only) , Best Available - Fail Open , or
 your own configured connectivity option when configuring the
 forwarding rule. Traffic from the domain is routed to Prisma
 Access, even if it meets the excluded traffic criteria.

 To add an access route, click + in the
 IP Addresses table and enter a
 destination subnet. You can add one or more access routes for
 traffic management. 
 ( macOS and Windows agents only ) For IPv6 addresses, you can enter: 
 Single IPv6 addresses using standard notation (for
 example, 2001:0db8:85a3:: ) 

 IPv6 subnets using CIDR notation (for example,
 2001:0db8:85a3::/48 ) 

 For IPv4 addresses, you can a wildcard character (*) in
 the IP address, but the wildcard must not appear in the
 middle of the IP address. Once a wildcard is used, all
 the following octets must also be wildcards. 

 The following are some examples of valid IPv4
 addresses: 
 1.2.3.4 (exact IP
 address) 

 1.4.3.* (wildcard IP
 address) 

 1.*.*.* 

 *.*.*.* (full wildcard IP
 address) 

 1.2.3.4/32 (exact IP
 address followed by CIDR) 

 The following are examples of an invalid IPv4 address: 
 1.2.3.300 (each byte must
 be 0-255) 

 3.3.3.3/255.255.255.256 
 (invalid subnet mask) 

 Prisma Access Agent will check whether your IP address
 entry is valid or not. For invalid inputs, a message
 appears indicating that the IP address is not valid. 

 In some cases (such as
 1.2.*.4 and
 7.7.7.7/33 ), the
 configuration validator will allow the entry, but the
 agent will ultimately reject it because the entry does
 not adhere to a supported format. In this case, the
 agent will reject the forwarding profile rule and fall
 back to the fail-safe mode, forwarding all traffic to
 the
 tunnel. 

 If
 you don't include or exclude routes or applications, every
 request is routed through the tunnel (without a split
 tunnel). Also, all traffic is inspected and subjected to
 policy enforcement whenever users connect to Prisma
 Access. 

 When you define split tunnel traffic to
 exclude access routes (by selecting
 Direct connectivity in the
 forwarding rule), Prisma Access Agent sends these routes
 through the physical adapter on the endpoint instead of
 being sent through the tunnel via the virtual adapter (the
 tunnel). By excluding split tunnel traffic by access routes,
 you can send latency-sensitive or high-bandwidth traffic
 outside of the tunnel, while all other traffic is routed
 through the tunnel for inspection and policy enforcement by
 the gateway. 

 When you define split tunnel traffic to
 include access routes (by selecting Best
 Available - Fail Safe 
 (macOS and Windows agents only) , Best Available - Fail Open , or
 your own configured connectivity option in the forwarding
 rule), the gateway pushes these routes to the remote users’
 endpoints to specify what traffic these endpoints can send
 through the tunnel. 

 Specify exclude routes that are
 more specific than include routes; otherwise, you might
 exclude more traffic than intended. For example: 

 Create the destinations. 

 Repeat these steps to add more destinations. 

 Set up Connectivity options to direct traffic based on
 the connectivity method. 

 In the Forwarding Profiles Setup page, select Connectivity Add Connectivity . 

 Prisma Access Agent also offers predefined
 connectivity options when users are using the best available
 location but the tunnel and proxy (if enabled) are not available or
 the traffic type is unsupported (such is IPv6 traffic). 
 ( macOS and Windows agents only ) Best Available - Fail
 Safe —Connect to the nearest gateway or Prisma
 Access location but block access if the user can’t connect
 to the tunnel and proxy (when enabled) or the traffic type
 is unsupported, such as proxy-only UDP traffic. 

 Best Available - Fail Open —Connect to
 the nearest gateway or Prisma Access location but allow
 direct access even if the user can’t connect to the tunnel
 and proxy (when enabled) or the traffic type is unsupported,
 such as proxy-only UDP traffic. 

 Enter a meaningful Name for the connectivity
 option you want to add. 

 Configure the Connectivity Methods . By default,
 only the Tunnel connectivity method is enabled,
 but you can also send traffic to a proxy by
 enabling Proxy 
 (macOS and Windows agents only) . 

 To direct internet traffic only through the tunnel, enable
 Tunnel and disable
 Proxy . 

 To direct internet traffic only to the proxy, disable
 Tunnel and enable
 Proxy . 

 To direct internet traffic to the proxy only when the tunnel is
 disconnected or unavailable, enable both 
 Tunnel and Proxy .
 Prisma Access Agent will send traffic through the tunnel, and if
 the tunnel becomes disconnected, will send traffic to the
 proxy. 

 ( macOS and Windows agents only ) Select a Fallback behavior if the user isn’t
 connected using the specified connectivity method. You can prevent
 access ( Block ) or allow access
 ( Direct ). The default is
 Direct . 

 Create your connectivity settings. 

 Repeat these steps to add more connectivity settings. 

 Create a forwarding profile that allows or excludes traffic based on the source
 applications, destination, or connectivity options that
 you defined. 

 From the Forwarding Profiles page, select Forwarding Profiles Add Forwarding Profile . 

 Enter a meaningful Name for the forwarding
 profile. 

 Click Add Rule to add one or more forwarding
 rules. 

 The Forwarding Rules table shows the rules
 that make up the forwarding profile. By default, all forwarding
 profiles contain the following rules: 
 ( macOS and Windows agents only ) The Video Streaming forwarding
 rule, which sends all network traffic from video streaming
 apps outside the tunnel (direct connectivity). By excluding
 lower risk video streaming traffic (such as YouTube and
 Netflix) from the tunnel, you can decrease bandwidth
 consumption on the gateway. 

 The Default forwarding rule, which
 sends all DNS and network traffic through the tunnel. Any
 new rules that you add are placed above the default rule.
 You can’t delete or move the default forwarding rule, but
 you can disable it or change its
 Connectivity setting. 

 An implicit forwarding rule for basic endpoint connectivity
 that allows traffic such as DHCP, loopback, Prisma Access Agent management plane, ADEM, and Remote Browser Isolation
 (RBI) traffic. The implicit forwarding rule isn’t
 displayed and can’t be changed. 

 The traffic forwarding rules are applied from the top down in the
 forwarding profile. This means that when Prisma Access Agent 
 receives a connection request, it evaluates the forwarding rules
 from the top to the bottom of the Forwarding Rules table. The agent
 matches the connection against each rule's criteria. When all
 criteria in a rule match, the agent applies that rule's connectivity
 method to route the traffic. If a rule does not match, the agent
 continues evaluating the next rule in the table until it finds a
 match or reaches the default rule. Therefore, configure the
 forwarding profile in a top-down manner, such as configuring the
 most specific rules first and the least specific rules last. 

 Traffic forwarding rules are applied from the top down in the
 forwarding profile. Therefore, configure the forwarding profile in a
 top-down manner, such as configuring the most specific rules first
 and the least specific rules last. 

 Enter the specifications for the forwarding rule. 

 Enter a Name for the rule. 

 Select a Source Application that you
 defined previously. If you select Any ,
 the forwarding rule will apply to traffic from any source
 applications. 
 The rule will match only if the specified
 source application makes the connection. 

 Select a Destination . If you select
 Any , the forwarding rule will apply
 to traffic from any destination domain or IP address. 
 The rule
 will match only if the connection destination matches the
 specified destination domain or IP address. 

 On Windows endpoints,
 Prisma Access Agent supports UDP traffic steering to IP-based
 destinations and source app-based rules only. Forwarding profile rules
 that use FQDN or domain-based destination objects don't apply to UDP
 traffic on Windows endpoints. 

 Select a Connectivity option that you
 configured, or select one of the following predefined
 connectivity options: 
 Direct —Sends the traffic outside
 of the tunnel. All traffic for the selected application
 or destination is sent directly to the physical adapter
 on the endpoint without inspection. 

 Block —Blocks traffic at the
 endpoint. 

 ( macOS and Windows agents only ) Bypass — Bypasses the
 matching traffic to allow third-party agents on
 endpoints to process the connections if they
 are active and configured to handle the designated
 traffic. If no third-party agent is present or
 configured to handle the traffic, the system sends the
 traffic to the tunnel (if present) or directly to its
 destination if the tunnel is not present. 

 ( macOS and Windows agents only ) Best Available - Fail
 Safe —Connects to the nearest gateway or
 Prisma Access location but blocks all traffic when the
 tunnel is down or for unsupported traffic types. 

 Best Available - Fail
 Open —Connects to the nearest gateway or
 Prisma Access location but allows traffic to go directly
 to its destination when the tunnel is down or for
 unsupported traffic types. This is the default. 

 Select the Traffic Type : 
 Specify
 whether to use split DNS to allow users to direct their DNS
 queries for applications and resources over the tunnel or
 outside the tunnel in addition to network traffic. 

 DNS —Includes or excludes rules
 that are applied only to DNS traffic and not to network
 application traffic. All network application traffic
 goes through the tunnel regardless of the split tunnel
 based on the destination domain that you specified for
 inclusions or exclusions. 

 DNS + Network Traffic —Ensures
 that the split tunnel based on the destination domain
 you specified for inclusions or exclusions are applied
 to the DNS traffic and the associated network
 application traffic for that domain. This is the
 default. 

 Network Traffic —Includes or
 excludes rules that are applied only to network
 application traffic and not to DNS traffic. All DNS
 traffic goes through the tunnel regardless of the split
 tunnel based on the destination domain that you
 specified for inclusions or exclusions. 

 For Windows agents, the DNS + Network
 Traffic split tunnel option is not
 supported for source application-based split tunnel
 rules . If you set up split tunneling to include
 or exclude traffic from the tunnel based on application
 names and select DNS + Network
 Traffic , DNS query packets for excluded
 and included apps will not honor the split tunnel
 rule. 

 Click Add to save the forwarding rule. 

 In the Forwarding Rules table, adjust the priority of the rules in a
 top-down manner, such that the most specific rules go first and the
 least specific rules go last in the table. You can select the checkbox
 next to a rule and select Move Up or
 Move Down . 

 ( macOS and Windows agents only ) Configure the Traffic Enforcement options to determine
 how you want traffic to be enforced. 

 Block outbound LAN access when connected to the
 tunnel —When enabled, the agent blocks direct access to
 the local network when the agent is connected to the tunnel. 
 Blocking
 access to your local network causes all
 traffic from being sent to
 the local adapter. In addition, your users won't be able to access
 resources on the local subnet, such as printers. Split tunnel
 traffic based on access route, destination domain, and application
 still works as expected. 

 If you disable this option, your end
 users can access local resources without requiring them to first
 connect to Prisma Access using the Prisma Access Agent . The default
 setting is disabled. 

 Block inbound access when connected to the
 tunnel —When enabled, the agent blocks all inbound
 connections from the tunnel. The default setting is disabled. 

 Create your forwarding profile. 

 Push the configuration by selecting Push Config Push . This action will make your forwarding profile available for
 selection in the Prisma Access Agent Setup page. 

 On This Page 

 Activation & Onboarding 

 Strata Cloud Manager 

 Activate a License or Product 

 Cloud Identity Engine 

 Strata Logging Service 

 Device Associations 

 Hub 

 Identity and Access Management 

 Tenant Management 

 SASE 

 Prisma Access 

 Strata Multitenant Cloud Manager 

 AI-Powered ADEM 

 Prisma Access Monitoring and Visibility 

 Prisma SD-WAN 

 ION Devices 

 Next-Generation CASB 

 Cloud-Delivered Security Services 

 Advanced WildFire 

 Advanced URL Filtering 

 Advanced Threat Prevention 

 Advanced DNS Security 

 Device Security 

 Enterprise DLP 

 SaaS Security 

 Network Security 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Prisma Access Agent 

 Next-Generation Firewall 

 Administration 

 Prisma Access 

 Panorama 

 Strata Cloud Manager 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
