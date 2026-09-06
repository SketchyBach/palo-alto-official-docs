---
url: https://cortex-docs.paloaltonetworks.com/demisto-sdk-development-guide/demisto-sdk-guide/demisto-sdk-commands/init
fetched_at: 2026-09-06T10:39:12Z
source: cortex-platform
---

# init | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 8 

 Demisto SDK Development Guide 

 Demisto SDK Guide 

 Demisto SDK commands 

 init 

 Initialize a new Cortex content pack structure with Demisto SDK. 

 Creates a new pack, integration, or script template. 

 Arguments 

 -n, --name 

 The name given to the files and directories of new pack/integration/script being created. 

 --id 

 The ID used for the integration/script YAML file. 

 -o, --output 

 The output directory to which the created object is saved. The default output directory is the current working directory. 

 --integration 

 Create an integration. 

 --script 

 Create a script. 

 --pack 

 Create a pack with its sub directories. 

 -t, --template 

 Create an integration/script based on a specific template. 

 Integration template options: HelloWorld , HelloIAMWorld , FeedHelloWorld . 

 Script template options: HelloWorldScript . 

 -a, --author_image 

 For packs only: The author image path is shown in Marketplace under the PUBLISHER section. The file size should be up to 4Kb and 120x50 pixels. 

 --demisto_mock 

 Copy the demistomock . Relevant for initializing scripts and integrations in a pack. 

 --common-server 

 Copy the CommonServerPython . Relevant for initializing scripts and integrations in a pack. 

 --xsiam 

 Create an Event Collector based on a template, and create matching sub-directories. 

 Notes 

 If integration or script is not set, the command automatically creates a pack, even if pack was not set. 

 If a name is not given, a prompt shows asking for an input. A pack, integration, or script cannot be created without a given name . 

 The name parameter cannot have spaces (' ') in it. 

 If no id is given when an integration or script is created, a prompt will show asking for an input. You can use the name parameter as the id for the YAML file, or provide a different identifier. 

 If activated from the content repository and no output is given, a pack will be created in the Packs directory. 

 If activated from the content repository or within a pack directory and no output is given, an integration will be created in the Integrations directory and a script will be created in the Scripts directory. 

 If no output is given and the command is not activated from the content repo or a pack directory, the pack/integration/script will be created in your current working directory. 

 If a pack was created but no author_image was given - an empty Author_image.png file will be created in the pack root directory. Later when validating the user will be asked to add it manually. 

 The default templates are based on StarterPack/BaseIntegration and StarterPack/BaseScript found in the content repo. 

 If xsiam and integration are set, output is required. 

 Examples 

 demisto-sdk init -n My_Pack 

 Creates a new content pack named My_Pack under the Packs directory in content repository. 

 demisto-sdk init --integration -n MyNewIntegration -o path/to/my/dir 

 Creates a new integration template in a specified directory. In this example, the integration is called myIntegration and is created in the directory Packs/myNewPack/Integrations . 

 demisto-sdk init --script --id "My Script ID" -n MyScript 

 Creates a new script under the Scripts directory. In this example, the new script is named myScript and the YAML file will have the ID My Script ID . 

 demisto-sdk init --pack -n My_Pack -a path/yourAuthorImage.png 

 Creates a new content pack named My_Pack under the Packs directory in the content repository, and adds an author image that will be shown under the PUBLISHER section in the Marketplace. The image file will be created under the pack root directory. 

 demisto-sdk init --pack -n My_Pack --xsiam 

 Creates a new pack named My_Pack under the Packs directory in content report, and adds the relevant empty XSIAM directories under the My_Pack directory. 

 demisto-sdk init --integration -n MyNewIntegration -o path/Packs/My_Pack/Integration --xsiam 

 Creates a new integration named MyNewIntegrationEventCollector within the path/Packs/My_Pack/Integration directory. In addition, creates the relevant folders and files for parsing rules and modeling rules under My_Pack . 

 Previous graph commands 

 Next openapi-codegen 

 Last updated 3 days ago 

 Was this helpful?
