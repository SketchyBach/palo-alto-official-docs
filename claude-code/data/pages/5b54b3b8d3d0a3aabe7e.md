---
url: https://docs.paloaltonetworks.com/enterprise-dlp/administration/configure-enterprise-dlp/configure-exact-data-matching/supported-edm-data-set-formats
fetched_at: 2026-08-13T15:32:11Z
source: palo-alto-main
---

# Supported EDM Data Set Formats Clear

Supported EDM Data Set Formats 

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

 Supported EDM Data Set Formats 

 Updated on 

 Jul 10, 2026 

 Focus 

 Download PDF 

 Filter

 Expand All 
 | 
 Collapse All 

 Enterprise DLP Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Reference 

 Release Notes 

 New Features by OS Version 

 New Features by Month 

 Updated on 

 Jul 10, 2026 

 Focus 

 Home 

 Enterprise DLP 

 Administration 

 Configure Enterprise DLP 

 Exact Data Matching (EDM) 

 Supported EDM Data Set Formats 

 Download PDF 

 Enterprise DLP 

 Supported EDM Data Set Formats 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Enterprise DLP Docs 

 Activation & Onboarding 

 Getting Started 

 Administration 

 Reference 

 Release Notes 

 New Features by OS Version 

 New Features by Month 

 Previous 

 Exact Data Matching (EDM) 

 Next 

 Set Up the EDM CLI App 

 Supported EDM Data Set Formats 

 Supported source file and data type formats for encrypted Exact Data Matching (EDM)
 datasets. 

 On May 7, 2025 , Palo Alto Networks is introducing new Evidence Storage and Syslog Forwarding service IP
 addresses to improve performance and expand availability for these services
 globally. 

 You must allow these new service IP addresses on your network
 to avoid disruptions for these services. Review the Enterprise DLP 
 Release Notes for more
 information. 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by Panorama or Strata Cloud Manager) 

 Prisma Access (Managed by Panorama or Strata Cloud Manager) 

 Prisma Browser 

 Enterprise Data Loss Prevention (E-DLP) license 

 Review the Supported
 Platforms for details on the required license
 for each enforcement point. 

 Or any of the following licenses that include the Enterprise DLP license 

 Prisma Access CASB license 

 Next-Generation
CASB for Prisma Access and NGFW (CASB-X) license 

 Data Security license 

 The Exact Data Matching (EDM) CLI app 
 supports CSV and TSV as source files for an encrypted EDM dataset upload to Enterprise Data Loss Prevention (E-DLP) . Before you upload an encrypted EDM dataset to Enterprise DLP , review the supported CSV file, TSV file, and data type
 formatting. 

 Enterprise DLP uses an Exact Match for values that don't follow the supported data type
 format below or data types that have no unique formatting requirements. If a data type
 follows the supported format, Enterprise DLP can match other instances of the data
 type in the scanned file. For example, if you configure a DLP rule to block files that contain the social
 security number 456-12-7890 , Enterprise DLP also matches
 instances of social security numbers formatted as 456 12 7890 and
 456.12.7890 . However, if you configure the DLP rule to block
 files containing the social security number 456127890 , Enterprise DLP only blocks files containing an exact match to this social security
 number. 

 When preparing an EDM dataset for upload, consider the following: 

 Enterprise DLP supports a header row in an EDM dataset. 

 Enterprise DLP supports datasets in CSV and TSV formats. 

 Palo Alto Networks recommends that datasets in CSV format adhere to the RFC-4180
 standard. 

 Palo Alto Networks recommends Atomic columns to ensure accurate matching of
 sensitive data. 

 Atomic columns are columns containing cells that contain a discrete or unique
 Data Type value. For example, in your dataset you have the
 SSN column. One of the cells in this column
 contains the value " 123456789;098765432 ." In this
 example, Enterprise DLP inspects for all incidents of
 123456789;098765432 as a singular SSN rather
 than inspecting for 123456789 and
 098765432 as unique incidents. 

 Enterprise DLP supports up to 50 individual Data Type values in a single
 cell. 

 The Data Types are data values recognized by Enterprise DLP . If a cell has
 more than 50 Data Type values recognized by Enterprise DLP , Enterprise DLP processes only the first 50 values and ignores the remaining
 values. 

 For example, Today is August 02 2020 contains three
 data type values; Today and
 is are Alphabet data types and
 August 02 2020 is a Date data type. 

 Enterprise DLP supports English (Latin script) and Hebrew (Hebrew script) in
 EDM datasets. 

 For Hebrew script, the detection engine supports all 22 letters, including the
 five distinct final form (Sofiot) characters ( ך, ם, ן, ף, ץ ) used at the
 end of words. Although you can include Nikud in Hebrew words, Enterprise DLP will ignore these vowel points in both the EDM dataset and the inspected
 network traffic. While Hebrew script is supported, there are some limitations
 for data formats. 

 Date Processing: Limited to Gregorian numeric dates (for example,
 01/02/2026). Enterprise DLP does not process traditional Hebrew
 calendar formats or dates where the month is written in Hebrew script (for
 example, "1 בפברואר 2026"). 

 Email Addresses: Limited to Latin script. Enterprise DLP does
 not process Email addresses that contain Hebrew characters. 

 Regional Identifiers: Recognition of certain sensitive identifiers,
 such as Social Security Numbers and Driver's License IDs, is currently
 restricted to formats used in the USA. 

 Enterprise DLP supports the following delimiters to separate values in
 scanned files: 

 Caret ( ^ ) 

 Less-than sign ( < ) 

 Greater-than sign ( > ) 

 Pipe ( | ) 

 Semicolon ( ; ) 

 Tab ( \t ) 

 Tilde ( ~ ) 

 Enterprise DLP stops inspecting an EDM dataset when any of the following
 limits is reached first. 

 Limit Default Maximum 

 Columns and rows per dataset 30 columns and 130 million rows 

 Cells per dataset 120 million 

 Cells per tenant (all datasets) 500 million 

 For example, an EDM dataset with 30 columns and 4 million rows (120 million
 cells) is within all limits, as is a dataset with 6 columns and 20 million rows
 (120 million cells). 

 Contact Palo Alto Networks Customer Support to increase
 the maximum number of cells supported for your Enterprise DLP tenant. 

 By request, Enterprise DLP can support up to 1 billion cells per EDM
 dataset and up to 2 billion cells per Enterprise DLP tenant across all
 EDM datasets uploaded to Enterprise DLP . 

 The supported file encoding schemes are UTF-8, UTF-16, ISO-8859-1, and
 US-ASCII. 

 The EDM CLI app removes all punctuation from data contained in the EDM
 dataset. 

 The EDM CLI app supports the following data type formats for EDM datasets. 

 Alphabet and Alphanumeric 

 Format Example 

 Latin script: Numbers, uppercase letters, and
 lowercase letters 

 Hebrew script: Numbers and Hebrew alphabet characters
 (including final forms) 

 ABCDEFG / abcdefg 

 AB123CG / ab123cd 

 אבגדהוז 

 אב123גד 

 כן / לם 

 Bank Routing Number and Bank Account Number 

 Format Example 

 Enterprise DLP requires an exact match for a bank
 routing number and bank account number to render a
 verdict. 

 N/A 

 Brazil CPF 

 Always ensure that the column data format in the source file is set to include
 any leading or ending zeros in the individual ID numbers. For example,
 01234567891 and
 12345678900 . 

 Format Example 

 Unmasked—11 consecutive digits 

 12345678901 

 Nine-digit block with final separator
 ( - or
 /) 

 123456789-01 

 123456789/01 

 Three-part separated with final separator
 ( - or
 /) 

 123.456.789-01 

 123.456.789/01 

 123 456 789-01 

 123 456 789/01 

 Country Name 

 Format Example 

 Enterprise DLP requires an exact match for country names
 to render a verdict. 

 Full country name 

 Country name abbreviation 

 US 

 USA 

 United States 

 United States of America 

 The United States of America 

 מדינת ישראל (State of Israel) 

 ישראל (Israel) 

 Credit Card 

 Format Example 

 Between 13 to 23 digits including dashes (-). 

 4739-5402-9061-0638 

 4739540290610638 

 Currency 

 Enterprise DLP supports inspection of the US Dollar (USD, $), the
 Euro (EUR, €), the New Israeli Shekel (ILS/NIS, ₪), and Generic Number
 values. 

 All currencies support values from 0 to 1 trillion (1,000,000,000). 

 All currencies support negative values. Enterprise DLP matches
 negative values against their absolute counterparts. 

 Enterprise DLP recognizes currency formats when a currency symbol
 or code is within 5 spaces of the beginning of the number. 

 Enterprise DLP treats the following formats as currencies when a
 symbol or code is present. As standalone values, Enterprise DLP 
 treats these as generic numbers. 

 Simple Integer with No Symbol or Code 

 No Symbol or Code with Cents 

 US/UK/Israel Notation with No Symbol or Code 

 Format 

 Example 

 Simple Integer with Symbol 

 $1000, €1000, or ₪1000 

 Simple Integer with Code USD1000, EUR1000, ILS1000, or NIS1000 

 Simple Integer with Symbol and Space $ 1000, € 1000, or 1000 ₪ 

 Simple Integer with Code and Space USD 1000, EUR 1000, ILS 1000, or 1000 NIS 

 Symbol or Code with Cents $1000.00, EUR1000.00, or ₪1000.00 

 Symbol or Code Comma Notation $1,000, EUR1,000, or 1,000 ₪ 

 Comma Notation Symbol or Code with Cents $1,000.00, EUR1,000.00, or 1,000.00 ₪ 

 Symbol or Code European Dot-Comma Notation $1.000,00, €1.000,00, or ₪1.000,00 

 Simple Integer with No Symbol or Code 1000 

 No Symbol or Code with Cents 1000.00 

 US/UK/Israel Notation with No Symbol or Code 1,000.00 

 Date 

 While Hebrew
 script is supported for general text, dates must remain in Gregorian numeric
 formats (for example, DD/MM/YYYY). Traditional Hebrew calendar dates (using
 Hebrew month names or years) are not supported. 

 Enterprise DLP supports spaces, dashes ( - ), slashes
 ( / ), periods ( . ), and any
 combination of these as separators. Enterprise DLP detects
 variations of the formats described below. 

 Enterprise DLP supports 20th and 21st century dates
 only. These are all dates starting on January 1, 1901. 

 Format Example 

 Legend 

 DD —Two-digit day of the month.
 For example, 02 . 

 MMM —Three letter abbreviation
 for month. For example,
 Aug . 

 MM —Two-digit month. For
 example, 12 . 

 YYYY —Four-digit year. For
 example, 2020 . 

 MM-DD-YYYY 

 MM/DD/YYYY 

 MM.DD.YYYY 

 MMM-DD-YYYY 

 MMM/DD/YYYY 

 MMM.DD.YYYY 

 DD-MM-YYYY 

 DD/MM/YYYY 

 DD MM YYYY 

 DD.MM.YYYY 

 DD-MMM-YYYY 

 DD/MMM/YYYY 

 DD MMM YYYY 

 DD.MMM.YYYY 

 YYYY-MM-DD 

 YYYY/MM/DD 

 YYYY.MM.DD 

 YYYY-MMM-DD 

 YYYY/MMM/DD 

 YYYY.MMM.DD 

 12-02-2020 

 12/02/2020 

 12.02.2020 

 Dec-02-2020 

 Dec/02/2020 

 Dec.02.2020 

 02-12-2020 

 02/12/2020 

 02 12 2020 

 02.12.2020 

 02-Dec-2020 

 02/Dec/2020 

 02 Dec 2020 

 02.Dec.2020 

 2020-12-02 

 2020/12/02 

 2020.12-02 

 2020-Dec-02 

 2020/Dec/02 

 2020.Dec.02 

 Ambiguous Dates —An ambiguous date is a date value
 that Enterprise DLP can't explicitly identify or interpret as a discrete
 and specific DD , MM ,
 or YYYY value. For ambiguous dates, Enterprise DLP detects and takes action on all possible interpretations of
 ambiguous dates. When Enterprise DLP encounters an ambiguous year value, it
 only checks for dates in the 20th (19xx) and 21st (20xx) centuries. 

 For example, consider the ambiguous date of
 1/8/1975 . This date can be interpreted as
 January 8th, 1975 or August 1st,
 1975 depending on the country. 

 Common examples of ambiguous dates include: 

 Dates where the year value of the date consists of 2 digits and is
 greater than 32. 

 Check Type : Enterprise DLP checks for every possible
 day/month combination. 

 Example : 2/06/50 

 Dates Enterprise DLP Checks For : 

 Feb 6 1950
Feb 6 2050
June 2 1950
June 2 2050 

 Dates where the day and year value are ambiguous, or the month and year
 values are ambiguous. 

 Check Type : Enterprise DLP assumes the last pair of numbers
 is the year value and checks for every variation of that date. 

 Example : Feb/06/12 

 Dates Enterprise DLP Checks For : 

 Feb 6 1912
Feb 6 2012 

 Dates where the day, month, and year values are all ambiguous. 

 Check Type : Enterprise DLP assumes the last pair of numbers
 is the year value and checks for every variation of that date. 

 Example : 2/06/12 

 Dates Enterprise DLP Checks For : 

 Feb 6 1912
Feb 6 2012
June 2 1912
June 2 2012 

 Email 

 While Hebrew
 script is supported for general text, only Latin script is supported for Email
 addresses. Enterprise DLP does not process Email addresses that contain
 Hebrew characters. 

 Format Example 

 RFC5322—<emailprefix>@<emaildomain> 

 bill@business.com 

 BILL@BUSINESS.COM 

 BILL@business.com 

 bill@BUSINESS.com 

 First, Middle, Last, and Full Name 

 Format Example 

 Latin script: Uppercase and lowercase letters 

 Hebrew script: Standard and final form (Sofiot)
 characters 

 Bill / bill 

 Bill Smith’s / bill smith’s 

 בנימין (Binyamin — ends in final Nun: ן) 

 יצחק (Yitzchak — ends in standard Qof: ק) 

 IP Address (IPv4 and IPv6) 

 Format Example 

 Enterprise DLP requires an exact match for IPv4 and IPv6
 IP addresses to render a verdict. 

 N/A 

 Medical Record Number 

 Format Example 

 Enterprise DLP requires an exact match for Medical
 Record Numbers to render a verdict. 

 N/A 

 Member ID and Reward ID 

 Format Example 

 Enterprise DLP requires an exact match for Member IDs
 and Reward IDs to render a verdict. 

 N/A 

 Numbers 

 Format Example 

 Enterprise DLP requires an exact match for all numbers
 to render a verdict. 

 Enterprise DLP removes positive signed integers (+) and
 treats the same as a nonsigned integer. Enterprise DLP 
 does not remove negative signed integers (-) to
 differentiate between positive and negative signed integers.

 SI Numbers - 1234, +1234, or -1234 

 Formatted Numbers —9.00 

 Indian Number System —12, 34, 567.89 

 Phone Number 

 Format Example 

 Ten-digit US phone number format only. 

 The EDM CLI app removes the Country code, parentheses
 ( () ),
 dash( - ), space, and periods
 ( . ). 

 8001234567 

 (800)1234567 

 1.800.123.4567 

 +1 (800)123-4567 

 1 800 123 4567 

 +1 800 123 4567 

 +1 800 123-4567 

 1-800-123-4567 

 1 (800) 123-4567 

 (800)123-4567 

 (800) 123 4567 

 800-123-4567 

 Vehicle License Plates 

 Enterprise DLP supports inspection of vehicle license plates for the
 United States and Israel. Enterprise DLP can detect license plates
 containing dashes (ABC-123), or license plates presented as a continuous
 string of characters (ABC123). However, Enterprise DLP does not
 support license plates containing spaces (ABC 123). 

 United States: Supports various state-issued alphanumeric
 patterns, typically consisting of 6 to 7 characters. 

 Israel: Supports standardized 7-digit ( XX-XXX-XX )
 and 8-digit ( XXX-XX-XXX ) numeric patterns. 

 Format Type 

 Example 

 United States Alphanumeric ABC-1234 

 Israel 7-Digit Numeric 12-345-67 

 Israel 8-Digit Numeric 123-45-678 

 USA Driver License 

 Format Example 

 Alphanumeric 

 E1234567 

 e1234567 

 USA Social Security Number 

 Format : 

 Enterprise DLP supports spaces, dashes ( - ), periods
 ( . ) as separators. 

 Format Example 

 XXX-XX-XXXX 

 XXX XX XXXX 

 XXX.XX.XXXX 

 XXXXXXXXX 

 123-45-6789 

 123 45 6789 

 123.45.6789 

 123456789 

 UUID 

 Format Example 

 RFC4122—32 hexadecimal (base-16) digits. If you’re using
 hyphens, the total is 36 digits. 

 123e4567e89b12d3a456426614174000 

 123e4567-e89b-12d3-a456-426614174000 

 Previous 

 Exact Data Matching (EDM) 

 Next 

 Set Up the EDM CLI App 

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

 Next-Generation Firewalls 

 AIOps for NGFW 

 Cloud Management for NGFWs 

 Cloud NGFW for AWS 

 Cloud NGFW for Azure 

 CN-Series 

 Firewalls 

 PAN-OS 

 PAN-OS SD-WAN 

 Service Provider 

 VM-Series 

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

 SaaS Security 

 Endpoints 

 GlobalProtect 

 Visibility & Monitoring 

 Dashboards 

 Incidents and Alerts 

 Reports 

 Autonomous DEM 

 Best Practices 

 Best Practices Library 

 Experts Corner 

 Solutions Docs from Product Experts 

 Administration 

 Cloud-Delivered Security Services 

 Data Filtering 

 Enterprise DLP 

 Concept 

 © 2026 Palo Alto Networks, Inc. All rights reserved.
