---
url: https://cortex-docs.paloaltonetworks.com/cortex-xsiam-developer-guide/cortex-xsiam-development-guide/testing/debugging
fetched_at: 2026-09-06T10:58:14Z
source: cortex-platform
---

# Debugging | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Reference 

 Developer Docs 

 Cortex XSIAM Developer Guide 

 Cortex XSIAM Development Guide 

 Testing 

 Debugging 

 Cortex XSIAM debugging guidance for logs, War Room, and IDE tools. 

 During the development phase of integrations and scripts, debugging allows you to understand what is happening behind the scenes when your code exhibits unexpected behavior. There are a few strategies that you can implement to debug code in Cortex XSIAM, described in the following sections. 

 Printing to the War Room 

 Seeing your statements in print is often useful when diagnosing issues. To do this, add the following to your integration/script code: 

 Ask Copy 

 error_msg = "Here's your completely broken code" 
 demisto.log(error_msg) 

 This prints the statements in the War Room, for you to review. Remove the error messages when you are done debugging, so that they do not appear in the final code. 

 Debugging using the IDE 

 Sometimes debugging via printing or using the logs is not sufficient. In that case you might want to use the debugger and go through the code line by line or breakpoint by breakpoint. See Debugging configurations for Python Apps in Visual Studio Code . 

 Note 

 We recommend using the Visual Studio Code extension when you are developing content. 

 Python environment 

 Prepare a Python environment with all the base dependencies. Follow the instructions in Set up a local development environment . 

 After the Python environment is prepared, open the integration in a virtual environment using the Cortex XSIAM Visual Studio Code Extension in VS Code. 

 Using demistomock 

 The content repository includes demistomock.py file, which usually appears as the first import in an integration or script: 

 The demistomock module can be used to mock integration configuration, arguments and commands passed. 

 Function 

 Description 

 demisto.params() 

 Returns the connection details inserted into the create instance in the UI. 

 demisto.command() 

 Returns the name of the command you want to run. 

 demisto.args() 

 Returns the arguments for that command. 

 In some cases, you might need to use other functions, and the following guidelines applies to those as well. In the demistomock file we can see a params function defined: 

 This is what is returned if we run the Python file. Instead, we can fill it with the connection credentials needed to connect to our instance. 

 and now commands such as: 

 take their information from there. 

 This is called mocking demisto. 

 Verify that all Cortex XSIAM functions used in the functions we are testing are mocked correctly. Now we can use the debugger from the IDE or ipdb to debug the code as we would any other simple Python file. 

 Previous Test playbooks 

 Next Contributing content 

 Last updated 10 days ago 

 Was this helpful?
