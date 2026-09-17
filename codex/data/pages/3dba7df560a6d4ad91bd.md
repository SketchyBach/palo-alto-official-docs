---
url: https://docs.paloaltonetworks.com/content/techdocs/en_US/panorama/getting-started/panorama-overview/panorama-commit-validation-and-preview-operations.html
fetched_at: 2026-09-16T12:47:06Z
source: palo-alto-main
---

# Panorama Commit, Validation, and Preview Operations Clear

Updated on 

 Thu Jul 16 11:23:55 PDT 2026 

 Focus 

 Home 

 Panorama 

 Panorama Overview 

 Panorama Commit, Validation, and Preview Operations 

 Download PDF 

 Panorama 

 Panorama Commit, Validation, and Preview Operations 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Panorama Docs 

 Getting Started 

 Administration 

 New Features 

 Previous 

 Administrative Authentication 

 Next 

 Plan Your Panorama Deployment 

 Panorama Commit, Validation, and Preview Operations 

 Where Can I Use This? What Do I Need? 

 NGFW (Managed by Panorama) 

 No prerequisites needed 

 When you are ready to activate changes that you made to the candidate configuration on Panorama
 or to push changes to the devices that Panorama manages (firewalls, Log Collectors, and
 WildFire appliances and appliance clusters), you can Preview, Validate, or Commit Configuration
 Changes . For example, if you add a Log Collector to the Panorama
 configuration, firewalls cannot send logs to that Log Collector until you commit the
 change to Panorama and then push the change to the Collector Group that contains the Log
 Collector. 

 You can filter changes by administrator or location and
then commit, push, validate, or preview only those changes. The
location can be specific device groups, templates, Collector Groups, Log
Collectors, shared settings, or the Panorama management server. 

 When you commit changes, they become part of the running configuration. Changes that you haven’t
 committed are part of the candidate configuration. Panorama queues commit requests so
 that you can initiate a new commit while a previous commit is in progress. Panorama
 performs the commits in the order they are initiated but prioritizes auto-commits that
 are initiated by Panorama (such as FQDN refreshes). However, if the queue already has
 the maximum number of administrator-initiated commits (10), you must wait for Panorama
 to finish processing a pending commit before initiating a new one. You can Use the Panorama Task Manager ( 

 ) to cancel pending commits or to see details
 about commits that are pending, in progress, completed, or failed. To check which
 changes a commit will activate, you can run a commit preview. 

 When you initiate a commit, Panorama checks the validity of the
changes before activating them. The validation output displays conditions
that block the commit (errors) or that are important to know (warnings).
For example, validation could indicate an invalid route destination
that you need to fix for the commit to succeed. The validation process
enables you to find and fix errors before you commit (it makes no
changes to the running configuration). This is useful if you have
a fixed commit window and want to be sure the commit will succeed
without errors. 

 When you preview your configuration commit, any configuration object added between
 existing any other existing object is displayed as a modified configuration object
 rather than an added configuration object. For example,
 Address1 and Address2 are
 existing Address objects. A Panorama admin later creates
 Address3 and adds the Address object between
 Address1 and Address2 .
 When the Panorama admin goes to preview the configuration changes,
 Address3 is displayed as a modified configuration
 object. 

 Automated commit recovery is enabled by default, allowing the
managed firewalls to locally test the configuration pushed from
Panorama to verify that the new changes do not break the connection
between Panorama and the managed firewall. If the committed configuration
breaks the connection between Panorama and a managed firewall then
the firewall automatically fails the commit and the configuration
is reverted to the previous running configuration and the Shared
Policy or Template Status ( Panorama Managed Devices Summary )
gets out of sync depending on which configuration objects were pushed.
Additionally, the managed firewalls test their connection to Panorama
every 60 minutes and if a managed firewall detects that it can no
longer successfully connect to Panorama then it reverts its configuration
to the previous running configuration. 

 For details on candidate and running configurations, see Manage Panorama and Firewall Configuration
 Backups . 

 To prevent multiple administrators from making configuration changes during concurrent sessions,
 see Manage Locks for Restricting Configuration
 Changes . 

 When
pushing configurations to managed firewalls, Panorama pushes the
running configuration. Because of this, Panorama does not let you
push changes to managed firewalls until you first commit the changes
to Panorama. 

 Previous 

 Administrative Authentication 

 Next 

 Plan Your Panorama Deployment
