<!-- KOI source: https://docs.koi.ai/integration-guides/endpoint-integration/deploy-koi-to-your-endpoints/script-package.md -->

> For the complete documentation index, see [llms.txt](https://docs.koi.ai/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.koi.ai/integration-guides/endpoint-integration/deploy-koi-to-your-endpoints/script-package.md).

# Script package

The script package is written in Python. Using Python provides native cross-platform execution, comprehensive built-in modules for system operations, and clear, readable code that security teams can easily review and validate.

### Wrapper Script Layer

The execution begins with platform-specific wrapper scripts that handle OS-level initialization.

#### macOS and Linux - Bash Wrapper

```shell
#!/bin/bash
# Handles environment setup, privilege verification, and Python execution
# Downloads and validates script content (managed mode)
# Executes Python interpreter with proper permissions
```

#### Windows - PowerShell Wrapper

```powershell
# Handles Windows-specific environment setup
# Manages UAC and administrator privilege requirements
# Coordinates WinPython download and execution
```

### Core Python Runtime Environment

#### macOS - System Python Integration

Every Mac comes with Python pre-installed, but it's not always immediately accessible. When the built-in Python isn't available, our script automatically enables it by installing the Xcode Command Line Tools, which activates the system's Python environment. This ensures reliable Python execution without requiring manual intervention or additional software installations.

* Primary: Uses built-in macOS Python (Requires Python 3.8+).
* Fallback: Leverages Xcode Command Line Tools Python if available.
* Advantages: Native integration with macOS system APIs and security model.

#### Linux - Native Python

* Primary: Uses distribution-provided Python installation.
* Compatibility: Works with Python 3.8+ across different distributions (Ubuntu, CentOS, RHEL).
* System Integration: Native access to Linux system calls and package management.
* Lightweight: Minimal overhead using existing system resources.

#### Windows - WinPython Portable

Downloads and uses WinPython - an official, digitally signed, self-contained Python distribution. For organizations that prefer to serve the portable Python from their own servers, this can be configured as described in the Configuration Sets section, supporting air-gapped environments and internal distribution controls.

### Technical Execution Flow

#### 1. System Discovery and Directory Enumeration

```python
def search_dir(os_type, search_params, limit):
    # Efficient file system traversal
    # Platform-specific path handling
    # Configurable search limits for performance
```

* Smart Scanning: Targets specific directories based on platform type.
* Pattern Matching: Uses include/exclude patterns for efficient discovery.
* User Profile Iteration: Scans all local user directories for complete coverage.

#### 2. Network Configuration Deployment

Network configuration deployment is **only relevant if the customer has requested** to perform the integration with this approach and **it is disabled by default**. When network configurations are enabled, the script deploys them before discovery. This step only applies to organizations that choose to integrate network-level monitoring through the script - for customers who prefer to handle network configuration separately or use existing proxy infrastructure, this section is completely skipped and no network settings are modified.

**PAC File Deployment**

```python
def register_pac(user, os_type, pac_url, koi_pac_urls_list):
    if os_type == "Mac":
        # Uses networksetup command for system-wide proxy configuration
    elif os_type == "Linux":
        # Uses gsettings for GNOME desktop environment
    elif os_type == "Windows":
        # Uses Windows Registry for system proxy settings
```

**Hosts File Modification**

PAC files don't natively support device or user grouping - they simply route traffic through proxies without a built-in way to identify which group a device belongs to. To enable group-based policy management, we implement a creative workaround using hosts file modifications. The script creates artificial domain mappings in the hosts file that work with PAC file configurations to generate unique traffic signatures, enabling device grouping and policy management where PAC files don't natively support group identification. The domain is under Koi’s ownership and it is not used.

```python
def set_hosts_entries(entries, tag_comment="# KOI_HOST", hosts_file="/etc/hosts"):
    # Safely modifies system hosts file
    # Automatic tagging for easy identification
```

#### 3. Item Discovery and Cataloging

```python
def run_discovery(user, os_type, settings_obj):
    # Platform-specific discovery methods
    # Extension enumeration with version information
    # Configuration file analysis
    # MCP server detection where applicable
```

* Multi-Platform Support: Handles 15+ different platforms and applications.
* Version Detection: Records specific version numbers for compliance tracking.
* Configuration Analysis: Examines settings files and configurations.
* User Context: Maintains separation between different user profiles.

#### 4. Policy Enforcement and Remediation

```python
def remediate_extensions(user, os_type, extensions_to_remove, settings_obj):
    # Platform-specific removal methods
    # File system cleanup
    # Registry cleaning (Windows)
    # Policy deployment to prevent reinstallation
```

* Complete file removal: Deletes extension files and directories from disk rather than just disabling.
* Platform-specific cleanup: Uses appropriate removal methods for each operating system and application type.
* Registry management: Removes Windows registry entries and deploys enterprise policies to prevent reinstallation.
* Policy enforcement: Configures supported applications to locally block future installation of prohibited extensions.
* User-specific targeting: Handles extensions installed in individual user profiles across multi-user systems.

#### 5. File System Operations

```python
def remediate_vscode_extensions(app, user, os_type, package_names_to_remove):
    # Platform-specific file removal
    # Directory cleanup
    # Symlink handling
    # Permission management
```

* Safe Removal: Comprehensive file and directory cleanup.
* Permission Handling: Manages file permissions and ownership.
* Atomic Operations: Ensures consistent state during file operations.
* Error Recovery: Handles file system errors gracefully.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.koi.ai/integration-guides/endpoint-integration/deploy-koi-to-your-endpoints/script-package.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
