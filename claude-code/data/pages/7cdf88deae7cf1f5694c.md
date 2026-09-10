---
url: https://cortex-docs.paloaltonetworks.com/cortex-commands-guide/vulnerability-commands
fetched_at: 2026-09-06T11:16:31Z
source: cortex-platform
---

# Vulnerability Commands | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Cortex Commands 

 Cortex Commands Guide 

 Vulnerability Commands 

 getVulnerabilities 

 getVulnerabilityDetails 

 getAffectedSoftware 

 triggerAssetScan 

 uploadVulnerabilityScan 

 getVulnerabilities 

 Returns a list of vulnerabilities based on the provided filter criteria. 

 Arguments 

 Argument Name 

 Description 

 Required 

 limit 

 The maximum number of vulnerabilities to return. Default is 50. 

 Optional 

 page_size 

 The number of vulnerabilities to return per page. When provided, manual pagination is used and 'limit' is ignored. 

 Optional 

 page 

 The page number to return (0-based). When provided, manual pagination is used and 'limit' is ignored. 

 Optional 

 sort_field 

 The field by which to sort the results. Possible values are: PLATFORM_SEVERITY, CVSS_SCORE, EPSS_SCORE, CORTEX_VULNERABILITY_RISK_SCORE, LAST_OBSERVED. Default is LAST_OBSERVED. 

 Optional 

 sort_order 

 The order in which to sort the results. Possible values are: DESC, ASC. Default is DESC. 

 Optional 

 cve_ids 

 A comma-separated list of CVE IDs to filter by. 

 Optional 

 issue_ids 

 A comma-separated list of issue IDs to filter by. 

 Optional 

 cvss_score_gte 

 The minimum CVSS score to filter by. 

 Optional 

 epss_score_gte 

 The minimum EPSS score to filter by. 

 Optional 

 internet_exposed 

 Whether to filter by internet-exposed assets. Possible values are: true, false. 

 Optional 

 exploitable 

 Whether to filter by exploitable vulnerabilities. Possible values are: true, false. 

 Optional 

 has_kev 

 Whether to filter by vulnerabilities that have a Known Exploited Vulnerability (KEV). Possible values are: true, false. 

 Optional 

 affected_softwares 

 A comma-separated list of affected software to filter by. 

 Optional 

 on_demand_fields 

 A comma-separated list of additional fields to retrieve. 

 Optional 

 start_time 

 The start time for filtering according to the issue last-observed time. Supports free-text relative and absolute times. For example: '7 days ago', '2023-06-15T10:30:00Z'. 

 Optional 

 end_time 

 The end time for filtering according to the issue last-observed time. Supports free-text relative and absolute times. For example: '7 days ago', '2023-06-15T10:30:00Z'. 

 Optional 

 severities 

 A comma-separated list of vulnerability issue severities to filter by. Possible values are: info, low, medium, high, critical. 

 Optional 

 assignees 

 A comma-separated list of emails of the users assigned to the vulnerability. Use 'unassigned' for unassigned vulnerabilities or 'assigned' for all assigned vulnerabilities. 

 Optional 

 finding_sources 

 A comma-separated list of finding sources of the vulnerability to filter by. Possible values are: CORTEX_AGENT, CORTEX_AGENTLESS_SCANNER, CORTEX_ATTACK_SURFACE_MANAGEMENT, CORTEX_ATTACK_SURFACE_TESTING, CORTEX_CLI_SCANNER, CORTEX_CONTAINER_REGISTRY_SCANNER, CORTEX_NETWORK_SCANNER, CORTEX_SERVERLESS_FUNCTION_SCANNER, QUALYS, TENABLE. 

 Optional 

 cvrs_gte 

 The minimum risk score assigned to the vulnerability (range 0-100). 

 Optional 

 compensating_controls_effective_coverage 

 A comma-separated list of assessed effectiveness and coverage values of detected compensating controls to filter by. Possible values are: EFFECTIVE, EFFECTIVE_REQUIRES_CONFIGURATION_UPDATE, EFFECTIVE_REQUIRES_CONTENT_UPDATE, EXPLOIT_CONFIRMED, EXPLOIT_UNREACHABLE, NOT_INSTALLED, NO_CONTROLS_FOUND, UNKNOWN_COVERAGE. 

 Optional 

 Outputs 

 Core.VulnerabilityIssue.IssueID string 

 The unique identifier of the vulnerability issue. 

 Core.VulnerabilityIssue.CVEID string 

 The CVE ID of the vulnerability. 

 Core.VulnerabilityIssue.CVEDescription string 

 The description of the CVE. 

 Core.VulnerabilityIssue.AssetName string 

 The name of the affected asset. 

 Core.VulnerabilityIssue.PlatformSeverity string 

 The platform severity of the vulnerability. 

 Core.VulnerabilityIssue.EPSSScore number 

 The EPSS score of the vulnerability. 

 Core.VulnerabilityIssue.CVSSScore number 

 The CVSS score of the vulnerability. 

 Core.VulnerabilityIssue.AssignedTo string 

 The user assigned to the vulnerability. 

 Core.VulnerabilityIssue.AssignedToPretty string 

 The display name of the user assigned to the vulnerability. 

 Core.VulnerabilityIssue.AffectedSoftware unknown 

 The software affected by the vulnerability. 

 Core.VulnerabilityIssue.FixAvailable boolean 

 Whether a fix is available for the vulnerability. 

 Core.VulnerabilityIssue.InternetExposed boolean 

 Whether the affected asset is internet-exposed. 

 Core.VulnerabilityIssue.HasKEV boolean 

 Whether the vulnerability has a Known Exploited Vulnerability (KEV). 

 Core.VulnerabilityIssue.Exploitable boolean 

 Whether the vulnerability is exploitable. 

 Core.VulnerabilityIssue.AssetIDs string 

 The IDs of the affected assets. 

 Core.VulnerabilityIssue.FindingSources string 

 The finding sources of the vulnerability. 

 Core.VulnerabilityIssue.CompensatingControlsDetectedCoverage string 

 The detected coverage of compensating controls. 

 Core.VulnerabilityIssue.CortexVulnerabilityRiskScore number 

 The Cortex vulnerability risk score. 

 Core.VulnerabilityIssue.FixVersions string 

 The versions that fix the vulnerability. 

 Core.VulnerabilityIssue.AssetTypes string 

 The types of the affected assets. 

 Core.VulnerabilityIssue.CompensatingControlsDetectedControls unknown 

 The detected compensating controls. 

 Core.VulnerabilityIssue.ExploitLevel string 

 The exploit level of the vulnerability. 

 Core.VulnerabilityIssue.IssueName string 

 The name of the vulnerability issue. 

 Core.VulnerabilityIssue.PackageInUse boolean 

 Whether the affected package is in use. 

 Core.VulnerabilityIssue.Providers string 

 The providers of the affected asset. 

 Core.VulnerabilityIssue.OSFamily string 

 The operating system family of the affected asset. 

 Core.VulnerabilityIssue.Image string 

 The image of the affected asset. 

 getVulnerabilityDetails 

 Gets vulnerability details by CVE ID. 

 Arguments 

 Argument Name 

 Description 

 Required 

 vulnerability_id 

 The vulnerability ID to retrieve details for. 

 Required 

 Outputs 

 Core.Vulnerability.vulnerabilityID string 

 The unique identifier of the vulnerability (CVE ID). 

 Core.Vulnerability.description string 

 Detailed description of the vulnerability. 

 Core.Vulnerability.cvss.baseScoreMetrics.attackComplexity string 

 The attack complexity required to exploit the vulnerability. 

 Core.Vulnerability.cvss.baseScoreMetrics.attackVector string 

 The attack vector of the vulnerability (e.g., Network, Local). 

 Core.Vulnerability.cvss.baseScoreMetrics.availabilityImpact string 

 The impact on availability if the vulnerability is exploited. 

 Core.Vulnerability.cvss.baseScoreMetrics.confidentialityImpact string 

 The impact on confidentiality if the vulnerability is exploited. 

 Core.Vulnerability.cvss.baseScoreMetrics.integrityImpact string 

 The impact on integrity if the vulnerability is exploited. 

 Core.Vulnerability.cvss.baseScoreMetrics.privilegesRequired string 

 The level of privileges required to exploit the vulnerability. 

 Core.Vulnerability.cvss.baseScoreMetrics.scope string 

 Whether the vulnerability can affect resources beyond its security scope. 

 Core.Vulnerability.cvss.baseScoreMetrics.userInteraction string 

 Whether user interaction is required to exploit the vulnerability. 

 Core.Vulnerability.cvss.score number 

 The CVSS base score. 

 Core.Vulnerability.cvss.scoreSource string 

 The source of the CVSS score. 

 Core.Vulnerability.cvss.severity string 

 The CVSS severity rating (e.g., Critical, High, Medium, Low). 

 Core.Vulnerability.cvss.severitySource string 

 The source of the CVSS severity rating. 

 Core.Vulnerability.cvss.vectorString string 

 The CVSS vector string representation. 

 Core.Vulnerability.cvss.version string 

 The version of the CVSS scoring system used. 

 Core.Vulnerability.epss_score number 

 The probability of exploitability (0-1). 

 Core.Vulnerability.exploitDetails.commercialExploitFound boolean 

 Whether a commercial exploit exists for the vulnerability. 

 Core.Vulnerability.exploitDetails.exploitMaturity string 

 Current state of exploit availability (e.g., weaponized). 

 Core.Vulnerability.exploitDetails.firstReportedThreatActor number 

 The timestamp of the first recorded threat actor activity. 

 Core.Vulnerability.exploitDetails.mostRecentReportedThreatActor number 

 The timestamp of the last recorded threat actor activity. 

 Core.Vulnerability.exploitDetails.publicExploitFound boolean 

 Whether a public exploit exists for the vulnerability. 

 Core.Vulnerability.exploitDetails.reportedExploited boolean 

 Whether the vulnerability has been actively exploited. 

 Core.Vulnerability.exploitDetails.reportedExploitedByBotnets boolean 

 Whether the vulnerability is being leveraged by botnet clusters. 

 Core.Vulnerability.exploitDetails.reportedExploitedByRansomware boolean 

 Whether the vulnerability is used in ransomware campaigns. 

 Core.Vulnerability.exploitDetails.reportedExploitedByThreatActors boolean 

 Whether known threat actors are exploiting this vulnerability. 

 Core.Vulnerability.exploitDetails.weaponizedExploitFound boolean 

 Whether a functional exploit exists in the wild. 

 Core.Vulnerability.fixVersions string 

 The versions that fix the vulnerability. 

 Core.Vulnerability.isKev boolean 

 Whether the vulnerability is listed in the CISA Known Exploited Vulnerabilities catalog. 

 Core.Vulnerability.temporalCvss.confidence string 

 The confidence level of the temporal CVSS score. 

 Core.Vulnerability.temporalCvss.score number 

 The temporal CVSS score. 

 Core.Vulnerability.temporalCvss.vectorString string 

 The temporal CVSS vector string representation. 

 Core.Vulnerability.temporalCvss.version string 

 The version of the CVSS scoring system used for the temporal score. 

 getAffectedSoftware 

 Gets a filtered list of the software affected by one or more vulnerabilities. If no filters are provided, all results are returned. 

 Arguments 

 Argument Name 

 Description 

 Required 

 vulnerability_id 

 Filter by vulnerability ID. Example: CVE-2024-1234. 

 Optional 

 package_name 

 Filter by package name. Example: openssl, curl. 

 Optional 

 cvss_severity 

 Filter by CVSS severity level. Possible values: LOW, MEDIUM, HIGH, CRITICAL. Possible values are: LOW, MEDIUM, HIGH, CRITICAL. 

 Optional 

 cvss_score 

 Filter by CVSS score. Example: 7.5. 

 Optional 

 dist_name 

 Filter by distribution name. Example: ubuntu, debian, rhel. 

 Optional 

 release_version 

 Filter by release version. Example: 22.04, 11, 9. 

 Optional 

 affected_cpu_archs 

 A comma-separated list of CPU architectures to filter by. Example: x86_64,aarch64. 

 Optional 

 affected_versions 

 A comma-separated list of affected software versions to filter by. Example: 1.1.1,1.0.2. 

 Optional 

 sort_field 

 Field to sort results by. Default is cvss_score. Possible values: vulnerability_id, cvss_score, cvss_severity, package_name, distro, release, last_modified. Possible values are: vulnerability_id, cvss_score, cvss_severity, package_name, distro, release, last_modified. Default is cvss_score. 

 Optional 

 sort_order 

 Sort order for results. Default is desc. Possible values: asc, desc. Possible values are: asc, desc. Default is desc. 

 Optional 

 search_from 

 Start offset index of results. Default is 0. Default is 0. 

 Optional 

 search_to 

 End offset index of results. Default is 500. Default is 500. 

 Optional 

 Outputs 

 Core.AffectedSoftware.vulnerability_id string 

 The vulnerability identifier (e.g., CVE ID). 

 Core.AffectedSoftware.cvss_score number 

 The CVSS score of the vulnerability. 

 Core.AffectedSoftware.cvss_severity string 

 The CVSS severity level of the vulnerability. 

 Core.AffectedSoftware.package_name string 

 The name of the affected package. 

 Core.AffectedSoftware.distro string 

 The distribution name. 

 Core.AffectedSoftware.release string 

 The release version. 

 Core.AffectedSoftware.affected_cpu_archs string 

 The affected CPU architectures. 

 Core.AffectedSoftware.affected_versions string 

 The affected software versions. 

 triggerAssetScan 

 Triggers a vulnerability scan for a specific asset. The asset ID is obtained from the assets view. The scanner type should match the asset's finding source (e.g., CORTEX_XDR_AGENT for agent-based findings, CORTEX_XDR_AGENTLESS for agentless findings, CORTEX_NETWORK_SCANNER for network scanner findings). 

 Arguments 

 Argument Name 

 Description 

 Required 

 asset_id 

 The asset ID from the vulnerability management asset view. 

 Required 

 scanner_type 

 The scanner type matching the asset's finding source. Possible values: CORTEX_NETWORK_SCANNER, CORTEX_XDR_AGENT, CORTEX_XDR_AGENTLESS. Possible values are: CORTEX_NETWORK_SCANNER, CORTEX_XDR_AGENT, CORTEX_XDR_AGENTLESS. 

 Required 

 cve_id 

 The CVE identifier (e.g., CVE-2024-1234). Required when scanner_type is CORTEX_NETWORK_SCANNER. 

 Optional 

 scan_target 

 The scan target for CORTEX_XDR_AGENT on Linux endpoints. Possible values: CONTAINER, HOST, IMAGE. Possible values are: CONTAINER, HOST, IMAGE. 

 Optional 

 Outputs 

 Core.AssetScan.AssetID string 

 The asset ID for which the scan was triggered. 

 Core.AssetScan.Message string 

 The response message from the scan trigger. 

 Core.AssetScan.ScanID number 

 The scan ID if available. 

 uploadVulnerabilityScan 

 Upload vulnerability scan results from third-party scanners to Exposure Management and poll for the upload job to complete. 

 Note: This is a polling command. 

 Arguments 

 Argument Name 

 Description 

 Required 

 vendor 

 Vendor name of the scanning tool (e.g., TENABLE, QUALYS) 

 Required 

 product 

 Product name of the scanning tool (e.g., Nessus, Qualys VMDR) 

 Required 

 version 

 Version of the scanning tool 

 Optional 

 assets_json 

 JSON array of assets with vulnerabilities. The JSON schema must match the format required in the API documentation: https://cortex-docs.paloaltonetworks.com/xsiam-api/vulnerability-management/bring-your-own-scanner#post-public_api-vulnerability-management-v1-external-scans-assets . 

 Required 

 interval_in_seconds 

 The polling interval in seconds between each job-status check. Default is 30. 

 Optional 

 timeout_in_seconds 

 The total polling timeout in seconds. Default is 600. 

 Optional 

 Outputs 

 There are no outputs for this command. 

 Previous User Commands 

 Next War Room Commands 

 Last updated 1 month ago 

 Was this helpful?
