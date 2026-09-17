---
url: https://docs.paloaltonetworks.com/advanced-url-filtering/administration/troubleshooting/incorrect-categorization
fetched_at: 2026-09-15T15:08:04Z
source: palo-alto-main
---

# Incorrect Categorization Clear

Updated on 

 Thu Jul 30 19:58:44 PDT 2026 

 Focus 

 Home 

 Advanced URL Filtering 

 Troubleshooting 

 Incorrect Categorization 

 Download PDF 

 English 

 日本語 (Japanese) 

 中文 (Chinese Simplified) 

 繁體中文 (Chinese Traditional) 

 Español (Spanish) 

 Français (French) 

 Advanced URL Filtering 

 Incorrect Categorization 

 Table of Contents 

 Filter

 Expand All 
 | 
 Collapse All 

 Advanced URL Filtering 

 Administration 

 Previous 

 URLs Classified as Not-Resolved 

 Next 

 Troubleshoot Website Access Issues 

 Incorrect Categorization 

 If you believe a website has been incorrectly categorized,
follow these steps to verify the URL category and request a URL
category change, if necessary. 

 Where can I use
this? What do I need? 

 NGFW (Managed by PAN-OS or Panorama) 

 Advanced URL
 Filtering license (or a legacy URL filtering
 license) 

 Note: Legacy URL filtering licenses are
 discontinued, but active legacy licenses are still
 supported. 

 Sometimes you may come across a URL that you
believe is categorized incorrectly. Use the following workflow to
determine the URL categorization for a site and request a category
change, if appropriate. 

 Verify the category in the dataplane by running
the following command: 

 show running url <URL> 

 For
example, to view the category for the Palo Alto Networks website,
run the following command: 

 show running url paloaltonetworks.com 

 If
the URL stored in the dataplane cache has the correct category (computer-and-internet-info
in this example), then the categorization is correct and no further
action is required. If the category is not correct, continue to
the next step. 

 Verify if the category in the management plane by running
the command: 

 test url-info-host <URL> 

 For
example: 

 test url-info-host paloaltonetworks.com 

 If
the URL stored in the management plane cache has the correct category, remove
the URL from the dataplane cache by running the following command: 

 clear url-cache url <URL> 

 The
next time the firewall requests the category for this URL, the request
will be forwarded to the management plane. This will resolve the
issue and no further action is required. If this does not solve
the issue, go to the next step to check the URL category on the
cloud systems. 

 Verify the category in the cloud by running the following command: 

 test url-info-cloud <URL> 

 If the URL stored in the cloud has the correct category,
remove the URL from the dataplane and the management plane caches. 

 Run the following command to delete a URL from the dataplane cache: 

 clear url-cache url <URL> 

 Run
the following command to delete a URL from the management plane cache: 

 delete url-database url <URL> 

 The
next time the firewall queries for the category of the given URL,
the request will be forwarded to the management plane and then to
the cloud. This should resolve the category lookup issue. If problems
persist, see the next step to submit a categorization change request. 

 To submit a change request from the web interface, go
to the URL log and select the log entry for the URL you would like
to have changed. 

 Click the Request Categorization change link
and follow instructions. You can also request a category change
from Palo Alto Networks Test A Site website by
searching for the URL and then clicking the Request Change icon.
To view descriptions of each category, refer to Predefined URL
Categories . 

 If your change request is approved, you will receive an
email notification. You then have two options to ensure that the
URL category is updated on the firewall: 

 Wait until
the URL in the cache expires and the next time the URL is accessed
by a user, the new categorization update will be put in the cache. 

 Run the following command to force an update in the cache: 

 request url-filtering update url <URL> 

 Previous 

 URLs Classified as Not-Resolved 

 Next 

 Troubleshoot Website Access Issues
