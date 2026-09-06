---
url: https://cortex-docs.paloaltonetworks.com/python-development-quick-start-guide/cortex-xsoar-python-development-quick-start-guide/development-tools-and-resources/cortex-xsoar-automation-scripts/close-an-investigation
fetched_at: 2026-09-06T10:50:54Z
source: cortex-platform
---

# Close an Investigation | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Python Development Quick Start Guide 

 Cortex XSOAR Python Development Quick Start Guide 

 Development Tools and Resources 

 Cortex XSOAR Automation Scripts 

 Close an Investigation 

 Example automation script for closing an investigation in Cortex XSOAR. 

 At the end of an investigation, you may need to take certain steps before closing it. 

 This example creates an automation with two mandatory arguments, reason and notes for closing an open investigation. The reason argument is a list of the four standard investigation close reasons used in Cortex XSOAR: Resolved, False Positive, Duplicate, and Other. 

 Note 

 For list options, no spaces are allowed. 

 Create an automation and use the Settings button to add the mandatory arguments reason and notes . 

 cortex-xsoar-automation-close-investigation.png 

 Use the basic automation template to create the following code. 

 Since there are two arguments, return the entire arguments dictionary in a single call with args = demisto.args() . 

 Compare the reason argument and look up the proper value from a close reason dictionary. 

 Replace all spaces in the reason argument and test if it exists in the map. If not, raise an exception, otherwise retrieve the notes argument. The investigation ID is needed for the close investigation command and is found with the demisto.incident() function that returns the incident fields as a dictionary. Only the investigation id is required to close an investigation. 

 To close the investigation, the demisto.executeCommand() function is called with the closeInvestigation command and the options passed as a dictionary. 

 Ask Copy 

 closeMap = { 
 'Resolved': "Resolved", 
 'FalsePositive':"False Positive", 
 'Duplicate': "Duplicate", 
 'Other': "Other" 
 } 

 def main(): 
 try: 
 args = demisto.args() 
 closeReason = args['reason'].replace(" ", "") 
 if closeReason in closeMap: 
 closeNotes = args['notes'] 
 id = demisto.incident()['id'] 
 demisto.executeCommand("closeInvestigation", { 
 'id': id, 
 'closeReason': closeMap[closeReason], 
 'closeNotes': closeNotes 
 }) 
 else: 
 raise Exception("Invalid close reason = " + 
 args['reason'] 
 ) 
 except Exception as ex: 
 demisto.error(traceback.format_exc()) 
 return_error("Failed to close investigation: " + 
 str(ex) 
 ) 

 if __name__ in ("__main__", "__builtin__", "builtins"): 
 main() 

 Save the completed automation and run it in the War Room of an open incident to test it. 

 Previous Set an Incident Field 

 Next Query the Audit Trail 

 Last updated 1 month ago 

 Was this helpful?
