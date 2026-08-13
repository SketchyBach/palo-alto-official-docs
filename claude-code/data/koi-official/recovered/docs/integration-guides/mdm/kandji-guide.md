Source: https://docs.koi.ai/integration-guides/mdm/kandji-guide.md

# Kandji Guide

This document provides step-by-step instructions on integrating **Koi** into your environment with [Kandji](https://support.kandji.io/kb/certificate-library-item).

## Configuration Guide

**Prerequisites**

* Access to the Kandji management dashboard.
* The configuration script provided by Koi.
* Internet access from managed devices.

**Integrations Steps**

1. Log in to Kandji's admin dashboard
2. In the sidebar, navigate to **LIBRARY**
3. In the top right corner, click the **Add Library Item** button
4. Search for the **Custom Scripts** component. Select it, then click **Add and configure** at the bottom right.
5. *Configuring the library*
   1. Add *title* to the component (eg: Koi Security)
   2. In the *Execution Frequency* section, select **Run every 15 minutes**
   3. inside *Script Details* -> *Audit Script*, paste the **Koi MDM script** provided to you
6. Press **Save** on the bottom right
7. Add the recent created *library* you created, into a **Blueprint** in order to apply the MDM script to the devices


---

---
