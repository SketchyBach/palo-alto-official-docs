Source: https://docs.koi.ai/integration-guides/single-sign-on/sso-saml-jit.md

# SSO Set Up

**Capabilities**

1. User creation and access is managed via your IdP.
2. Group mapping - Map groups to Koi platform's roles to manage users’ permissions in the platform. The current roles are:
   * **Read only** - **View** access to all platforms' sections
   * **Security** - **Full** access to all platform's sections, with exception of the settings page
   * **Admin** - **Full** access to all platform's sections

**Default Authentication**\
By default, user authentication to your tenant is done via a 'magic link' that is sent to authorized users' email address and is accessed through their inbox. The link will expire after 3 minutes and access will remain open for 30 days after using the link.

**How to set up SSO?**

Request SSO set-up link from your Koi customer experience representative, and by following the link, complete the Wizard set up process:

1. From the home page, select **SSO Configuration**

![](https://files.readme.io/37aac6c59d309d39e6cb0245b58587fbe61fd3f9af98a8d53c1b113407f5afad-image.png)

2. Choose your **IdP vendor** and click \***SAML**. You would then be forwarded to the "Service Provider Information" page, and be asked to fill the information according to the relevant vendor.

If you don't find your IdP vendor, use the generic configuration options at the bottom of the screen.

![](https://files.readme.io/67e00e2aefd775880f889a627d22981c31a639ca9073c704e03ae73b282e0c3a-image.png)

3. **User attribute mapping** - you can map attribute names from the IdP (name, email, etc.) to user attributes.

![](https://files.readme.io/29e03f110afe4e5415fc2c90587d464355fe357d029f216bfbc1395ea5534077-image.png)

4. **Group Attribute Mapping** you can add group attribute statements on the same page.

![](https://files.readme.io/3a665574a1b9e52a47949e02a9829baa6665d716d620be215343bb902dea0960-image.png)

5. **Add the Identity Provider information**

![](https://files.readme.io/a9a01827d362177b1cbbe1d6b23d2aa2cd170002e917809c41d036d379da3193-image.png)

6. **Assign Groups**:

![](https://files.readme.io/1afe470f904d98c87f31b7456311f0338b551718cbbe732fbd17fdc52f1843ff-image.png)

7. **SSO Domains** - Specify the approved domains for SSO

![](https://files.readme.io/91c0e10f5304943a00fe811aa894d6f88c130ef60f696e1b31a664a6d2721af2-image.png)

8. **Testing**- Perform the test at the end of the set up wizard. Please send the test results to your customer experience representative.

![](https://files.readme.io/cae7e94459cc439e04f201ec42cec832690325699ca49e6c80192ebced3288fb-image.png)

Once the set up wizard is complete, Koi's team will approve and complete the SSO configuration.


---

---
