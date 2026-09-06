---
url: https://cortex-docs.paloaltonetworks.com/demisto-sdk-development-guide/demisto-sdk-guide/demisto-sdk-commands/prepare-content
fetched_at: 2026-09-06T10:39:13Z
source: cortex-platform
---

# prepare-content | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 8 

 Demisto SDK Development Guide 

 Demisto SDK Guide 

 Demisto SDK commands 

 prepare-content 

 Prepare Cortex content files and packs for development, validation, or release workflows. 

 The prepare-content command prepares content to upload to Cortex XSOAR or Cortex XSIAM. If the content item is a pack, prepare-content creates the pack .zip file. If the content item is an integration/script/rule, prepare-content creates the unified YAML file. 

 Note 

 The prepare-content command replaces the unify command. 

 Arguments 

 Argument 

 Description 

 -i , --input 

 The path to the directory of a content pack or a content item where the files reside. 

 -o , --output 

 The path to the directory into which to write the result. 

 -f , --force 

 Forcefully overwrites the preexisting file if one exists. 

 -c , --custom 

 Adds a custom label to the name / display / id of the unified YAML. Only applies to integrations/scripts. 

 -a , --all 

 Runs prepare-content on all content packs. If no output path is given, it dumps the result in the current working path. 

 -g , --graph 

 Whether to use the content graph. 

 --skip-update 

 Whether to skip updating the content graph (used only when graph is true ). 

 -ini , --ignore-native-image 

 Whether to ignore the addition of the nativeimage key to the YAML of a script/integration. 

 -mp , --marketplace 

 The Marketplace the content items are created for, which determines the text used specific to that Marketplace. Default is the XSOAR Marketplace. 

 Examples 

 demisto-sdk prepare-content -i Integrations/MyInt -o Integrations 

 Takes the integration components in the Integrations/MyInt directory and unifies them to a single YAML file that is created in the Integrations directory. 

 demisto-sdk prepare-content -i Scripts/MyScr -o Scripts 

 Takes the script components in the Scripts/MyScr directory and unifies them to a single YAML file that is created in the Scripts directory. 

 demisto-sdk prepare-content -u Integrations/MyInt -c Test 

 Appends to the unified YAML name / script / id a label - Test that prevents conflicts with the uploaded unified YAML and the original integration/script on the server. 

 origin yml: {name: integration} --> unified yml: {name: integration - Test} 

 demisto-sdk prepare-content -i Packs/RBVM/GenericModules/genericmodule-RBVM.json 

 Takes the GenericModule input file genericmodule-RBVM.json , unifies it with its dashboards, and saves the unified file in the same directory as the input file in the Packs/RBVM/GenericModules directory. 

 demisto-sdk prepare-content -i Packs/RBVM/GenericModules/genericmodule-RBVM.json -o Packs/RBVM/ 

 Takes the GenericModule input file genericmodule-RBVM.json , unifies it with its dashboards, and saves the unified file in the given output directory Packs/RBVM . 

 demisto-sdk prepare-content -i Packs/SIEMPack/ParsingRule/MyParsingRule -o Packs/SIEMPack/ParsingRule 

 Takes the parsing rules components (YAML, XIF and JSON) from the ParsingRule/MyParsingRule directory and unifies them into a single YAML file that is created in the ParsingRule directory. 

 Previous pre-commit 

 Next run 

 Last updated 3 days ago 

 Was this helpful?
