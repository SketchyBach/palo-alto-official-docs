---
url: https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/cli-pipeline-code-snippets/jenkins
fetched_at: 2026-09-06T10:11:27Z
source: cortex-platform
---

# Jenkins | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center shield-alt shield-alt

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex Cloud 

 Application Security 

 Application Security 

 Onboard data sources 

 CLI pipeline code snippets 

 Jenkins 

 Configure Cortex CLI code scanning in Jenkins. 

 ARM64 

 AMD64 

 Ask Copy 

 pipeline { 
 agent { 
 docker { 
 // Replace with a suitable image or executor 
 image ' cimg/node:22.17.0 ' 
 args ' -u root ' 
 } 
 } 
 environment { 
 CORTEX_API_KEY = credentials ( ' CORTEX_API_KEY ' ) 
 CORTEX_API_KEY_ID = credentials ( ' CORTEX_API_KEY_ID ' ) 
 CORTEX_API_URL = ' <your_cortex_api_url> ' 
 } 
 stages { 
 stage ( ' Checkout Repository ' ) { 
 steps { 
 git branch : ' main ' , url : ' this-is-repository-url-example ' 
 stash includes : ' **/* ' , name : ' source ' 
 } 
 } 
 stage ( ' Install Dependencies ' ) { 
 steps { 
 sh ''' 
 apt update 
 apt install -y curl jq git 
 ''' 
 } 
 } 
 stage ( ' Download cortexcli ' ) { 
 steps { 
 script { 
 def response = sh ( script : """ 
 curl --location ' ${ env.CORTEX_API_URL } /public_api/v1/unified-cli/releases/download-link?os=linux&architecture=arm64' \ 
 --header 'Authorization: ${ env.CORTEX_API_KEY } ' \ 
 --header 'x-xdr-auth-id: ${ env.CORTEX_API_KEY_ID } ' \ 
 --silent 
 """ , returnStdout : true ) . trim () 
 def downloadUrl = sh ( script : """ echo ' ${ response } ' | jq -r '.signed_url' """ , returnStdout : true ) . trim () 
 sh """ 
 curl -o cortexcli ' ${ downloadUrl } ' 
 chmod +x cortexcli 
 ./cortexcli --version 
 """ 
 } 
 } 
 } 
 stage ( ' Run Scan ' ) { 
 steps { 
 script { 
 unstash ' source ' 
 // Replace the repo-id with your repository like: owner/repo 
 sh """ 
 ./cortexcli \ 
 --api-base-url " ${ env.CORTEX_API_URL } " \ 
 --api-key " ${ env.CORTEX_API_KEY } " \ 
 --api-key-id " ${ env.CORTEX_API_KEY_ID } " \ 
 code scan \ 
 --directory "\$(pwd)" \ 
 --repo-id <REPLACE WITH REPO_OWNER/REPO_NAME> \ 
 --branch <REPLACE WITH BRANCH> \ 
 --source "JENKINS" \ 
 --create-repo-if-missing 
 """ 
 } 
 } 
 } 
 } 
 } 

 Previous GitLab Runner 

 Next Onboard private package registries 

 Last updated 1 month ago 

 Was this helpful?
