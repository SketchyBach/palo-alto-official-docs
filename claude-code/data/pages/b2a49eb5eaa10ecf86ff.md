---
url: https://cortex-docs.paloaltonetworks.com/xsoar-6-administrator-guide/6.13/reference-docs/reference/server-configurations/users-and-roles-server-configurations
fetched_at: 2026-09-06T10:46:26Z
source: cortex-platform
---

# Users and Roles Server Configurations | 6.13 | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 6 

 Cortex XSOAR 6 Administrator Guides 

 6.13 

 Reference Docs 

 Reference 

 Server Configurations 

 Cortex XSOAR 6.13 

 Users and Roles Server Configurations 

 Review user and role server configurations in Cortex XSOAR 6.13. 

 Key 

 Description 

 Default 

 builtin.commands.hidden.clearUsersData 

 Set to false to run the clearUserData command in the CLI and playbook. 

 true 

 clear.users.data.job.enabled 

 Set to true to clear the user's data. 

 false 

 clear.users.data.job.time 

 Sets the time to run in Cron format to clear the users data. Default is every Sunday at 12AM. For example to run every minute, enter */1 * * * * . 

 0 0 * * SUN 

 clear.users.data.job.userslist 

 The name of the list that you need to create to remove users data after you have deleted the user. 

 N/a 

 clear.users.data.job.clear.list 

 Set to true to delete the list after the data is cleared. 

 false 

 clear.users.data.job.username 

 The name of the replacement user. 

 admin 

 server.mask.git.commits 

 Set to true to remove the users data from the git commit version that the user created (version control). 

 false 

 ExpireAfter 

 The number of the unit you want to expire in a password policy. For example, 4 hours, 4 days, etc. Numeric settings are disabled with a 0 value. For more information, see Default Password Policy Keys . 

 0 

 ExpireUnit 

 The unit for a password policy to expire. Values are month , week , and day . For more information, see Default Password Policy Keys . 

 month 

 MaxFailedLoginAttempts 

 How many attempted logins within one minute for a password policy. For example, 10 failed logins within one minute. For more information, see Default Password Policy Keys . 

 10 

 MinDigitsOrSymbols 

 The minimum digits or symbols for a password policy. For more information, see Default Password Policy Keys . 

 1 

 MinLowercaseChars 

 The minimum password length for a password policy. For more information, see Default Password Policy Keys . 

 1 

 MinPasswordLength 

 The minimum password length for a password policy. For more information, see Default Password Policy Keys . 

 8 

 MinUppercaseChars 

 The minimum upper case characters for a password policy. For more information, see Default Password Policy Keys . 

 1 

 PreventRepitition 

 Whether to prevent repetition for a password policy. For more information, see Default Password Policy Keys . 

 true 

 SetUnlockAfterMinutes 

 User unlocks automatically after x minutes (if 0, only an administrator can unlock) for a password policy. For more information, see Default Password Policy Keys . 

 0 

 create.read.only.users 

 Allow read-only users. 

 false 

 Previous System Diagnostics Server Configurations 

 Next War Room Server Configurations 

 Last updated 3 days ago 

 Was this helpful?
