#  Snowflake Agent Creation Script (Refined)

> **Agent Name**: `Direct Marketing Analytics Agent`
> **Environment**: `PLAYGROUND_LM.CORTEX_ANALYTICS_ORCHESTRATOR`

---

##  1. Infrastructure Preparation (SQL)
Run this in a Snowflake Worksheet as `SYSADMIN`:

```sql
-- Set context
USE ROLE SYSADMIN;
USE WAREHOUSE TEST;
USE DATABASE PLAYGROUND_LM;
USE SCHEMA CORTEX_ANALYTICS_ORCHESTRATOR;

-- Ensure stages exist (for tools and assets)
CREATE STAGE IF NOT EXISTS SEMANTIC_MODELS DIRECTORY = (ENABLE = TRUE);
CREATE STAGE IF NOT EXISTS SEMANTIC_FILES DIRECTORY = (ENABLE = TRUE);

-- Create Benchmarks Table and Search Service
-- Run content from: scripts/setup_benchmarks.sql
```

---

##  2. Agent Setup Instructions (Manual Steps)

Follow these steps in **AI & ML**  **Agents**:

###  Tab 1: About
*   **Display Name**: `Direct Marketing Analytics Agent`
*   **Description**: `AI-powered analytics agent for Salesforce Marketing Cloud email campaign performance. Query YTD metrics, YoY benchmarks, program performance, and market comparisons using natural language.`
*   **Example Questions**:
    1. `What was the open rate for last month's global eDM campaign?`
    2. `Show me the click-through rate trend for the past six months in Europe`
    3. `How does Germany's email performance compare to the European average?`
    4. `Which campaign achieved the highest engagement in Q3?`
    5. `Compare open rates for France Spain and Italy for the most recent campaign`
    6. `What is Spain's opt-out rate compared to the EU average in Q3?`
    7. `Compare open and click rates for EX30 campaigns in NL versus BE`
    8. `Summarize all markets where the opt-out rate exceeds 0.5%`

###  Tab 2: Tools

#### Tool A: Cortex Analyst (Email_Performance_Analytics)
*   **Add Tool**: Cortex Analyst
*   **Semantic Model**: `PLAYGROUND_LM`  `CORTEX_ANALYTICS_ORCHESTRATOR`  `@SEMANTIC_MODELS/marketing_semantic_model.yaml`
*   **Name**: `Email_Performance_Analytics`
*   **Warehouse**: `TEST`
*   **Description**: (Copy from `config/agents/tools/cortex_analyst.md`)
    > Analyzes SFMC (Salesforce Marketing Cloud) email marketing performance data. Use this tool to query core campaign metrics and calculate marketing KPIs across different dimensions.

#### Tool B: Cortex Search (Benchmark_Intelligence_Base)
*   **Add Tool**: Cortex Search Services
*   **Cortex Search Service**: `DEV_MARCOM_DB`  `APP_DIRECTMARKETING`  `CORTEX_SFMC_BENCHMARK_SEARCH`
*   **ID Column**: `BENCHMARK_ID`
*   **Title Column**: `METRIC_NAME`
*   **Name**: `Benchmark_Intelligence_Base`
*   **Description**: (Copy from `config/agents/tools/cortex_search.md`)
    > Searches through industry benchmarks, performance standards, and campaign threshold guidelines for SFMC email marketing.
*   **Attributes Available**: `METRIC_NAME`, `EMAIL_TYPE`, `STATUS`, `INDUSTRY`, `YEAR_PERIOD`
*   **Setup Source**: Ensure you have executed `scripts/setup_benchmarks.sql` first to create the service.

###  Tab 3: Orchestration
*   **Model**: `Claude Sonnet 4.5`
*   **Time Limit**: `300 seconds`
*   **Token Limit**: `4000 tokens`

#### Orchestration Instructions
(Copy full text from [`config/agents/orchestration/instructions_default.md`](config/agents/orchestration/instructions_default.md))

#### Response Instructions
(Copy full text from [`config/agents/orchestration/response_default.md`](config/agents/orchestration/response_default.md))

###  Tab 4: Access
*   **Owner**: `LIMA`
*   **Roles & Permissions**:
    1.  `CLD-SNOWFLAKE-DEV-MARCOM-APP-DIRECTMARKETING-ETL-SG`: **Ownership / Full Access** (AI Dev / Data Eng)
    2.  `CLD-SNOWFLAKE-DEV-MARCOM-APP-DIRECTMARKETING-ANALYST-SG`: **Usage & Monitor** (Market Analyst)
    3.  `CLD-SNOWFLAKE-PROD-MARCOM-APP-DIRECTMARKETING-ANALYST-SG`: **Usage Only** (Business Stakeholder)

####  How to Configure
In the **Access** tab in Snowsight:
1. Click **+ Add role**
2. Add the relevant Account Roles listed above.
3. Assign the appropriate permission levels.

---

##  3. Validation Command
Once the agent is created, you can test it directly in a worksheet:

```sql
-- Conceptual test (Syntax varies by account availability)
SELECT SNOWFLAKE.CORTEX.AGENT_ANSWER(
    'PLAYGROUND_LM.CORTEX_ANALYTICS_ORCHESTRATOR.Direct_Marketing_Analytics_Agent',
    'What was the average open rate last month?'
);
```
