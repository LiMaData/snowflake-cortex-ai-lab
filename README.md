# ❄️ Building Agentic AI Applications - Cortex AI Lab

**Welcome!** This project contains everything you need to build intelligent AI agents on Snowflake that combine structured analytics (SQL) with unstructured document search (RAG).

## 🚀 Quick Start Guide

### 1. Environment Setup
*   **Credentials**: Ensure you have your `SNOWFLAKE_ACCOUNT`, `USER`, and `PASSWORD`.
*   **Verification**: Run the connection test script:
    ```powershell
    python tests/test_connection.py
    ```

### 2. Prepare Your Workspace
*   **Run Setup SQL**: Open `setup.sql` in Snowsight or your IDE and execute it to create your schema (`PLAYGROUND_LM.CORTEX_ANALYTICS_ORCHESTRATOR`).
*   **Upload Data**: Upload PDF/Image files to the `@docs` stage.

### 3. Deploy Semantic Model
We have an automated script to deploy your semantic model.
```powershell
python scripts/deploy_semantic_model.py
```
This will:
1.  Check/Create `semantic_models` stage.
2.  Upload `config/semantic.yaml`.
3.  Create/Update the `SFMC_EMAIL_PERFORMANCE` semantic model object.

### 4. Configure Your Agent (in Snowsight)
Go to **AI & ML** → **Agents** → Create Agent. Use the following configurations:

| Section | Configuration | Source File |
|---------|---------------|-------------|
| **Orchestration** | Instructions | `config/agents/orchestration/default.md` |
| **Response** | Instructions | `config/agents/response/default.md` |
| **Tool: Sales_Data** | Description | `config/agents/tools/cortex_analyst.md` |
| **Tool: Docs** | Description | `config/agents/tools/cortex_search.md` |

---

## 🔄 Development Workflow (Automated vs. Manual)

| Component | Status | How to Update |
|-----------|--------|---------------|
| **Semantic Model** | ✅ **Automated** | Edit `config/semantic.yaml` → Run `python scripts/deploy_semantic_model.py`. This updates the object in Snowflake automatically. |
| **Agent Instructions** | ✋ **Manual** | **Cannot be automated via IDE**. Best Practice is to edit the `.md` files in `config/agents/` to track changes in Git, then **Copy-Paste** the content into the Snowsight UI. |
| **Tool Descriptions** | ✋ **Manual** | Similar to instructions, these must be pasted into the Tool settings in Snowsight. |

---

## 📂 Project Structure

```text
├── config/                     # Configuration Templates
│   ├── semantic.yaml           # Data Model Definition (Edit this!)
│   ├── agents/                 # Agent Instruction Templates
│   │   ├── orchestration/      # How the agent thinks
│   │   ├── response/           # How the agent talks
│   │   └── tools/              # Tool descriptions
│
├── scripts/                    # Automation Scripts
│   ├── deploy_semantic_model.py  # Deploys your Semantic Model
│   └── inspect_agent.py        # Inspects Agent objects (read-only)
│
├── tests/                      # Verification Scripts
│   └── test_connection.py      # verify your .env credentials
│
├── participant-setup/          # Guide & Setup SQL
│   ├── PARTICIPANT_GUIDE.md    # Detailed Step-by-Step Tutorial
│   └── setup.sql               # Database Initialization Script
```

---

## 🛠️ Configuration Detail

### Agent Behavior
*   **Orchestration**: Defines *when* to use which tool (e.g., "Use Analyst for sales numbers, Search for strategy docs").
    *   *See `config/agents/orchestration/examples.md` for variations like "Executive" vs "Technical" styles.*
*   **Response**: Defines tone and format (e.g., "Always use charts", "Be concise").

### Semantic Model
*   **File**: `config/semantic.yaml`
*   **Purpose**: Maps your Snowflake tables (`FACT_SALES`, `DIM_CUSTOMER`) to natural language concepts.
*   **Edit this file** to add new metrics, synonyms, or verified queries.
*   **Deploy**: Always run `python scripts/deploy_semantic_model.py` after editing.

---

## ❓ Troubleshooting

**Connection Failed?**
*   Check your `.env` file matches your Snowflake credentials.
*   Ensure you are using the correct Account URL.

**Agent not answering correctly?**
*   **Structured Data**: Check `semantic.yaml` for missing synonyms.
*   **Unstructured Data**: Check `cortex_search.md` tool description to ensure the agent knows what's in the docs.

**Deployment Error?**
*   Ensure the schema `PLAYGROUND_LM.CORTEX_ANALYTICS_ORCHESTRATOR` exists.
*   Check that your user has permissions to CREATE STAGE and CREATE SEMANTIC MODEL.

---
*Maintained by the Cortex AI Lab Team*
