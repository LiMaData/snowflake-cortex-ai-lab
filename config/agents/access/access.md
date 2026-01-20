#  Agent Access Control

> **Purpose**: Defines who can access and interact with the Direct Marketing Analytics Agent across Dev and Prod environments.

---

## Roles and Permissions

| Role | Access Level | Description |
|------|--------------|-------------|
| `CLD-SNOWFLAKE-DEV-MARCOM-APP-DIRECTMARKETING-ETL-SG` | **Ownership / Full Access** | AI Developers and Data Engineers. Can develop, edit, and manage the agent. |
| `CLD-SNOWFLAKE-DEV-MARCOM-APP-DIRECTMARKETING-ANALYST-SG` | **Usage & Monitor** | Market Analysts. Can interact with the agent and monitor its performance/logs. |
| `CLD-SNOWFLAKE-PROD-MARCOM-APP-DIRECTMARKETING-ANALYST-SG` | **Usage Only** | Business Stakeholders. Can only use the agent to ask questions. |

---

## Specific User Access

*Primary developer/owner:*
- User: `[LIMA]`
- Access: Owner/Editor

---

##  How to Configure
In the **Access** tab in Snowsight:
1. Click **+ Add role**
2. Add the relevant Account Roles from the table above.
3. Assign the appropriate permission levels (Ownership, Usage & Monitor, or Usage Only).

---

##  Grant Privileges
GRANT USAGE ON AGENT DEV_MARCOM_DB.APP_DIRECTMARKETING.SFMC_EMAIL_ANALYTICS_AGENT TO ROLE "CLD-SNOWFLAKE-DEV-MARCOM-APP-DIRECTMARKETING-ETL-SG";
GRANT OWNERSHIP ON AGENT DEV_MARCOM_DB.APP_DIRECTMARKETING.SFMC_EMAIL_ANALYTICS_AGENT TO ROLE "CLD-SNOWFLAKE-DEV-MARCOM-APP-DIRECTMARKETING-ETL-SG";
GRANT USAGE ON AGENT DEV_MARCOM_DB.APP_DIRECTMARKETING.SFMC_EMAIL_ANALYTICS_AGENT TO ROLE "CLD-SNOWFLAKE-DEV-MARCOM-APP-DIRECTMARKETING-ANALYST-SG";
GRANT MONITOR ON AGENT DEV_MARCOM_DB.APP_DIRECTMARKETING.SFMC_EMAIL_ANALYTICS_AGENT TO ROLE "CLD-SNOWFLAKE-DEV-MARCOM-APP-DIRECTMARKETING-ANALYST-SG";
GRANT USAGE ON AGENT DEV_MARCOM_DB.APP_DIRECTMARKETING.SFMC_EMAIL_ANALYTICS_AGENT TO ROLE "CLD-SNOWFLAKE-PROD-MARCOM-APP-DIRECTMARKETING-ANALYST-SG";
