Source: https://docs.koi.ai/risk-and-threat-intelligence/findings/index-4/identity-authentication-permissions.md

# Identity & Authentication Permissions

**Severity**

🟡 Medium (5)

**Short Description**

Flags items that request access to user identity or authentication flows. These capabilities may expose session credentials or login behavior, increasing the risk of impersonation, session hijacking, or unauthorized account access.

**Suggestion**

Carefully review the item's permissions and assess whether access to identity and authentication flows is necessary for its intended functionality. Consider removing or replacing the item if the permissions appear excessive or if the item's purpose does not justify such sensitive access.

**Information**

Items requesting access to user identity or authentication flows have the ability to interact with sensitive credential data, session tokens, and login mechanisms. While some items may require these permissions for legitimate purposes such as single sign-on or authentication management, these capabilities can also be exploited by malicious actors to compromise user accounts. When an item has access to authentication flows, it can potentially observe, intercept, or manipulate session credentials and login behavior, creating opportunities for unauthorized access to user accounts and organizational systems.

**Included Permissions**

* cookies
* webAutheticationProxy
* pkcs11
* webRequestAuthProvider
* signedInDevices

**Risks of Identity & Authentication Permissions**

* **Session Hijacking**: The item may capture or manipulate active session tokens, allowing attackers to impersonate legitimate users without needing passwords.
* **Credential Exposure**: Access to authentication flows could expose login credentials, enabling unauthorized account takeover.
* **Account Impersonation**: The item could leverage captured identity information to perform actions on behalf of users, potentially accessing sensitive data or systems.
* **Persistent Unauthorized Access**: Compromised authentication mechanisms can provide ongoing access to user accounts even after password changes.

**Recommended Actions**

1. **Investigate the Item**:
   * **Review Permission Justification**: Determine whether the item's core functionality legitimately requires access to identity and authentication flows.
   * **Evaluate Publisher Trust**: Verify the publisher's reputation and history, particularly regarding handling of sensitive data.
   * **Assess Usage Context**: Identify which users have this item installed and what level of access they have to sensitive systems.
2. **Immediate Action**:
   * **Restrict or Remove**: If the permissions appear excessive or unjustified, remove the item from affected endpoints.
   * **Monitor Activity**: Track the item's behavior for any unusual authentication-related activities or network requests.
   * **Review Access Logs**: Check authentication logs for suspicious login patterns or session anomalies that may indicate exploitation.


---

---
