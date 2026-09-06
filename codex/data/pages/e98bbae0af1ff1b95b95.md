---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.14/customize-cortex-xsoar/customize-and-configure-cortex-xsoar/indicators/indicator-expiration
fetched_at: 2026-09-06T10:42:16Z
source: cortex-platform
---

# Indicator Expiration | 6.14 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.14 

 Customize Cortex XSOAR 

 Customize and Configure Cortex XSOAR 

 Indicators 

 Cortex XSOAR 6.14 

 Indicator Expiration 

 Configure Cortex XSOAR 6.14 indicator expiration statuses, default methods, and retention periods. 

 Indicators can have the Expiration Status field set to Active or Expired, which is determined by the Expiration field. When indicators expire, they still exist in Cortex XSOAR, meaning they are still displayed and you can still search for them. A job that runs daily checks for newly expired indicators and updates the Expiration Status field. 

 Note 

 If an indicator is marked for expiration, the status does not change to expired until the hourly job runs. 

 When indicators expire, the expirationStatus and expiration fields are updated. You can use an indicator field trigger script to take actions based on indicator expiration. 

 You can set the default expiration method for indicators either to never expire or to expire after a specific period of time. The default expiration method is set by the indicator type. For more information, see Indicator Type Profile. 

 This is the hierarchy by which indicators are expired. 

 Method 

 Description 

 Manual 

 A user manually expires the indicator or sets it to never expire. This method overrides all other methods. 

 Automation script 

 Use the expireIndicators command to change the expiration status to Expired for one or more indicators. This script accepts a comma-separated list of indicator values, and supports multiple indicator types. For example, you can set the expiration status for an IP address, domain, and file hash: !expireIndicators value=1.1.1.1,safeurl.com,45356A9DB614ED7161A3B9192E2F318D0AB5AD10 

 (Same in the indicator expiration hierarchy as manual.) 

 Use the !setIndicators command to reset the indicators' expiration value. The parameter's value can either be never or a time in ISO 8601 format. For example, 2006-01-02T15:04:05Z (for UTC time) or 2006-01-02T15:04:05Z07:00 (UTC +7 hours). 

 Examples: 

 !setIndicators indicatorsValues=watson.com expiration=Never 

 !setIndicators indicatorsValues=watson.com expiration=2006-01-02T15:04:05Z 

 Feed integration 

 Some integrations support setting the expiration method on an integration instance level, which overrides the method defined for the indicator type. 

 If a feed's expiration method is set to When removed from the feed, indicators that are removed from the feed immediately expire. Note that if the feed is disabled, its expiration method reverts to that of the indicator type (time-based). 

 Time-based expiration is set according to feed reliability. If the same indicator appears on multiple feeds, the feed with the highest reliability determines the indicator's expiration time. If multiple feeds have the same reliability, the last feed to add or modify the indicator determines its expiration time. 

 Example: 

 An indicator was initially fetched by Feed A, then by Feed B. 

 Both feeds have the same reliability. 

 Feed B's indicators are set to expire When removed from the feed. 

 Feed B is now disabled. 

 After Feed B is disabled, the indicator's expiration method reverts to that of the indicator type (for example, expire after 7 days). However, if Feed A then modifies the indicator (or removes and re-adds it), the expiration method changes back to Feed A's settings. 

 Indicator type 

 The expiration method (interval or never) is defined according to the indicator type, which applies to all indicators of this type. This is the default expiration method for an indicator. 

 Previous Disable Indicator Extraction for Automations or Integrations 

 Next Feed Integrations 

 Last updated 4 days ago 

 Was this helpful?
