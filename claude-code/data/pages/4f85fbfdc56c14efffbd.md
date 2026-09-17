---
url: https://cortex-docs.paloaltonetworks.com/demisto-sdk-development-guide/demisto-sdk-guide/demisto-sdk-commands/update-release-notes
fetched_at: 2026-09-16T08:55:51Z
source: cortex-platform
---

# update-release-notes | Cortex Documentation Portal arrow-up-right-and-arrow-down-left-from-center

For the complete documentation index, see llms.txt . This page is also available as Markdown . 

 Ask 
 On this page 

 Guides 

 Cortex XSOAR 8 

 Demisto SDK Development Guide 

 Demisto SDK Guide 

 Demisto SDK commands 

 update-release-notes 

 Create and update Cortex content release notes with the Demisto SDK. 

 Automatically generates release notes for a given pack and updates the pack_metadata.json version for changed items. 

 This command creates a new release notes file under the ReleaseNotes directory in the given pack in the form of X_Y_Z.md where X_Y_Z is the new pack version. The command automatically bumps the currentVersion found in the pack_metadata.json file. After running this command, add the newly created release notes file to GitHub and add notes under their respective headlines. 

 For a private repository and an unconfigured DEMISTO_SDK_GITHUB_TOKEN , remote files are fetched from the remote branch of the local repository. 

 Arguments 

 Argument 

 Description 

 -i, --input <PACK_PATH> 

 The path of the content pack to generate release notes for. 

 -u, --update-type 

 Optional. If no update_type is defined, the currentVersion is bumped as a revision. Refers to the type of update. Options are: 

 major 

 minor 

 revision 

 documentation (revision) 

 -g, --use-git 

 Uses Git to identify the relevant changed files and updates all release notes in every pack that has changes. Used by default if -i is not set. The -u argument is applied to all changed packs. 

 -f, --force 

 Updates the release notes of a pack even if no changes requiring an update were made. 

 --text 

 Text to add to all release notes files. 

 --pre_release 

 Indicates that this update is for a pre-release version. The currentVersion changes to reflect the pre-release version number. 

 --prev-ver 

 Previous branch or SHA1 commit to run checks against. 

 -v, --version <DESIRED_VERSION> 

 Bumps to a specific version. Cannot be used with -u, --update-type flags. 

 -bc, --breaking-changes 

 Whether a new version contains breaking changes. 

 Examples 

 demisto-sdk update-release-notes -i Packs/HelloWorld -u minor 

 Creates a new Markdown file in the ReleaseNotes folder for the HelloWorld pack and bumps the currentVersion with a minor increment. 

 demisto-sdk update-release-notes -i Packs/HelloWorld -u major 

 Creates a new Markdown file in the ReleaseNotes folder for the HelloWorld pack and bumps the currentVersion with a major increment. 

 demisto-sdk update-release-notes -i Packs/HelloWorld -u revision 

 Creates a new Markdown file in the ReleaseNotes folder for the HelloWorld pack and bumps the currentVersion with a revision increment. 

 demisto-sdk update-release-notes -g -u revision 

 Creates a new Markdown file in the ReleaseNotes folder for all changed packs and bumps the currentVersion with a revision increment. 

 demisto-sdk update-release-notes -i Packs/HelloWorld -u revision --pre_release 

 Creates a new Markdown file in the ReleaseNotes folder for the HelloWorld pack and bumps the currentVersion with a revision increment, appending pre_release to the currentVersion . 

 Previous split 

 Next upload 

 Last updated 14 days ago 

 Was this helpful?
