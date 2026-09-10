---
url: https://cortex-docs.paloaltonetworks.com/playbook-design-guide/playbook-design-guide/configure-a-sub-playbook-loop
fetched_at: 2026-09-06T10:50:51Z
source: cortex-platform
---

# Configure a Sub-playbook Loop | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Playbook Design Guide 

 Playbook Design Guide 

 Cortex XSOAR 6x 

 Configure a Sub-playbook Loop 

 Configure a sub-playbook to run in a loop Cortex XSOAR 6x. 

 Looping uses sub-playbooks to create loops within a parent playbook. When running the loop, the values are calculated based on the context data for the sub-playbook and not the parent playbook. The loop ends when either the sub-playbook uses the last input available or when a specific condition is met, depending on your configuration. 

 In the parent playbook (the task that contains the sub-playbook), configure when to exit the loop by selecting one of the following options: 

 For Each Input : The loop exits automatically, when the last item in the input is executed. 

 If the input is a single item, the sub-playbook runs once, but if the input is a list of items (such as a list of alert IDs), the sub-playbook runs as many times as there are items in the list. Each iteration of the sub-playbook uses the next item in the list as the input. 

 If there are multiple input lists with the same number of items, the sub-playbook runs once for each set of inputs. 

 If there are multiple input lists with different numbers of items, the sub-playbook runs the first set of inputs, followed by the second, third, etc. until the end. For example: 

 Input 

 Value 

 Input x 

 1,2,3,4 

 Input y 

 a,b,c,d 

 Input z 

 9 

 First loop: 1, a, 9 

 Second loop: 2, b, 9 

 Third loop: 3, c, 9 

 Fourth loop: 4, d, 9 

 Built-in or Choose Loop Automation : The loop exits based on a condition. The playbook does not loop through the inputs but takes the inputs as a whole. 

 For an example of a sub-playbook loop, see the following Sub-Playbook Loop Example . 

 Note 

 Consider the following when adding a loop: 

 The maximum number of loops (default is 100). A high number or a high wait time combined with a large number of incidents, may affect performance. 

 Periodically check looping conditions to ensure they are still valid for the data set. 

 When the task's input is an array, it is iterated automatically (no need to define a loop). 

 In the Playbooks page, select the parent playbook that contains the sub-playbook task you want to run as a loop. 

 Click Edit . 

 If the playbook is installed from a content pack, you need to either detach or duplicate the playbook, before editing. 

 Select the task that contains the sub-playbook for which you want to create the loop. 

 Click the Loop tab. 

 Click one of the following options to define when to exit the loop: 

 None : The sub-playbook does not run multiple times. 

 Built-in : Define the following options for the built-in functions: 

 Option 

 Description 

 Exit when 

 Enables you to define when to exit the loop. Click {} and expand the source category. Hover over the required source and click Filter & Transform to the left of the source to manipulate the data. For information about configuring filters and transformers, see Filters and Transformers . 

 Equals 

 Select the operator to define how the values should be evaluated. 

 Max iterations 

 The maximum number of times the loop should run. 

 Sleep 

 The number of seconds to wait between iterations. 

 Cortex XSOAR recommends that you balance between the number of iterations and the number of seconds to wait between iterations so you don't overload the server. 

 For each input : Run the sub-playbook for all defined inputs. Enter the number of seconds to wait between iterations. 

 Choose Loop automation : Select the automation from the dropdown list to define when to exit the loop. The parameters that appear are applicable to the selected automation. 

 Troubleshoot Looping Context Data 

 If using looping in one or more sub-playbooks you may encounter issues with context data appearing in the main playbook. For example: 

 The main playbook (A) runs in a loop which includes sub-playbook (B) 

 Sub-playbook (B) runs in a loop that includes sub-playbook (C) 

 Sub-playbook (C) outputs to context 

 Sub-playbook (B) is set to private and no outputs are defined 

 In this situation the outputs of playbook (C) are exposed at the root-level context (main playbook (A)). To remove the root level context, create a task to delete the context data in the main playbook (A). 

 When sub-playbook B runs a second loop, sometimes the previous results of the first loop are being appended to the results of the second loop, despite the query not returning data as evident by the task results. Context data may appear to return in the follow up task. Consider filtering the results according to the input of the next task. 

 Previous Common Scripts to use in Automations 

 Next Sub-Playbook Loop Example 

 Last updated 6 days ago 

 Was this helpful?
