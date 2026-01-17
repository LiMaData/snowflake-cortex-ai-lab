# 🤖 Agent Configuration

This folder contains configuration templates for Cortex Agents in Snowflake Intelligence.

## 📁 Folder Structure

```
agents/
├── README.md                    # This file
├── orchestration/               # How the agent thinks and uses tools
│   ├── default.md               # Default orchestration instructions
│   └── examples.md              # Example variations
├── response/                    # How the agent responds to users
│   ├── default.md               # Default response instructions
│   └── examples.md              # Example variations
└── tools/                       # Tool descriptions and configurations
    ├── cortex_analyst.md        # Cortex Analyst tool config
    └── cortex_search.md         # Cortex Search tool config
```

## 🔧 How to Use

1. **Choose your configuration** from the templates below
2. **Copy the instructions** when creating your agent in Snowsight
3. **Customize** based on your specific use case

## 📍 Where to Apply in Snowsight

When editing your agent in **AI&ML → Agents → [SFMC_EMAIL_ANALYTICS_AGENT] → Edit**:

| Config Type | Location in Snowsight |
|-------------|----------------------|
| Orchestration Instructions | Orchestration → Instructions |
| Response Instructions | Orchestration → Response Instructions |
| **Semantic Model/View** | Tools → Cortex Analyst → Semantic View |
| Tool Descriptions | Tools → [Tool Name] → Description |

## 🎯 Quick Reference

- **Semantic Model**: The YAML or View that defines your data structure (Tables, Columns, Joins).
- **Orchestration**: Controls *how* the agent thinks, plans, and uses tools.
- **Response**: Controls *how* the agent formats and presents answers.
- **Tool Descriptions**: Help the agent understand *when* to use each tool.

## 📚 Related Files

- [`../semantic.yaml`](../semantic.yaml) - Semantic model for Cortex Analyst
- [`../../participant-setup/PARTICIPANT_GUIDE.md`](../../participant-setup/PARTICIPANT_GUIDE.md) - Full setup guide
