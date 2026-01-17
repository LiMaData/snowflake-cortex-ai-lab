# 🔍 Cortex Search Tool Configuration

> **Purpose**: Template for searching unstructured marketing assets (Guidelines, Briefs, Strategy).

---

## Tool Setup in Snowsight

**Location**: AI&ML → Agents → [SFMC_EMAIL_ANALYTICS_AGENT] → Edit → Tools → Add Cortex Search Services

| Setting | Value |
|---------|-------|
| Cortex Search Service | `DEV_MARCOM_DB.APP_DIRECTMARKETING.MARKETING_DOCS_SEARCH` |
| ID Column | `CHUNK_ID` |
| Title Column | `DOCUMENT_NAME` |
| Name | `Marketing_Knowledge_Base` |

---

## Tool Description

Copy this into the **Description** field:

```text
Searches through marketing strategy documents, campaign guidelines, brand standards, and program briefs for SFMC email marketing.

**Use this tool when the user asks about:**
- Brand guidelines (voice, tone, logo usage)
- Campaign strategy or program definitions
- Best practices for email design and CTAs
- Historical campaign reports (PDF/DOCX)
- Legal requirements or compliance for specific markets

**Available content includes:**
- Marketing Program Playbooks
- Brand Identity Guidelines
- Regulatory compliance documents per market
- PDF summaries of industry benchmarks

**Do NOT use this tool for:**
- Querying live performance numbers or KPIs (use Direct_Marketing_Analytics)
- Calculating YTD/YoY trends
- Comparing sends or opens across markets
```

---

## Alternative Descriptions

### Short Version
```text
Search marketing playbooks, brand guidelines, and campaign strategy documents for qualitative context.
```

### Detailed Version
```text
Semantic search over marketing unstructured data:
- Content: Strategy briefs, playbooks, guidelines.
- Searchable Metadata: Document type, Market, Program Name.
- Use Case: Identifying "How" or "Why" behind campaign performance, vs "What" (which is in Analyst).
```
