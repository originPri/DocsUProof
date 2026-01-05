# How the System Determines Fairness/Legality

## Overview

The Australian Rental Fairness Checker determines whether a rental contract clause is **fair** or **legal** through a multi-layered assessment system based on Australian tenancy legislation.

## Decision-Making Process

### 1. **Rule-Based Validation** (Primary Method)

The system checks specific numeric limits against state legislation:

- **Bond Validation**: 
  - Maximum: 4 weeks of rent (NSW)
  - Legal Basis: Residential Tenancies Act 2010 (NSW) Section 19
  - If bond exceeds 4 weeks → **ILLEGAL**

- **Break Lease Fee Validation**:
  - Maximum: 4 weeks of rent (NSW)
  - Legal Basis: Residential Tenancies Act 2010 (NSW) Section 107
  - If fee exceeds 4 weeks → **ILLEGAL**

- **Rent Increase Validation**:
  - Minimum notice: 60 days (NSW)
  - Maximum frequency: Once per 12 months (NSW)
  - Legal Basis: Residential Tenancies Act 2010 (NSW) Section 42
  - If notice < 60 days or frequency > 12 months → **ILLEGAL**

### 2. **Prohibited Clause Detection**

The system identifies clauses that are explicitly illegal:

- **Absolute pet bans** (unreasonable restrictions)
- **Shifting landlord maintenance responsibilities** to tenant
- **Prohibiting subletting** without reasonable grounds
- **Charging for utilities** that landlord cannot charge (e.g., water without separate meter)
- **Waiver of tenant rights** clauses

### 3. **Unfair Contract Term Assessment**

Based on Australian Consumer Law, the system flags:

- **Excessive penalty clauses** that exceed actual loss
- **Unreasonable restrictions** on tenant rights
- **Automatic forfeiture** clauses
- **Unfair late fees**

### 4. **Risk-Based Flagging**

Uses keyword analysis to identify high-risk language:
- Keywords: "penalty", "forfeit", "prohibited", "automatic increase"
- Flags clauses requiring manual legal review

## Fairness Scores

Each clause receives a fairness score:

- **"fair"**: No issues detected, complies with legislation
- **"questionable"**: High-risk language or concerns, needs review
- **"unfair"**: Violates legislation or contains prohibited terms

## Legal Basis

All rules are derived from:

1. **Residential Tenancies Act 2010 (NSW)** - Primary tenancy legislation
2. **Fair Trading Act 1987 (NSW)** - Consumer protection
3. **Australian Consumer Law** - Unfair contract terms provisions

## Limitations

The current system:

- ✅ Validates specific numeric limits (bond, fees, notice periods)
- ✅ Detects prohibited clause types
- ✅ Flags high-risk language
- ⚠️ Uses keyword matching (not full legal AI analysis)
- ⚠️ Currently only NSW rules (other states are placeholders)
- ⚠️ May miss nuanced legal issues requiring case law interpretation

## How to Improve

To make the system more comprehensive:

1. **Add Real LLM Integration**: Replace keyword matching with actual legal AI
2. **Expand State Rules**: Add comprehensive rules for VIC, QLD, SA, WA, etc.
3. **Add More Clause Types**: Validate maintenance, entry rights, quiet enjoyment, etc.
4. **Case Law Integration**: Include precedents for ambiguous clauses
5. **Semantic Analysis**: Better understanding of clause intent, not just keywords

## Example Assessment

**Input Clause**: "The bond is 6 weeks rent ($3,000)"

**Assessment Process**:
1. Type detected: "bond"
2. Numeric value: 6 weeks
3. Rule check: NSW max = 4 weeks
4. Result: **ILLEGAL** - "Bond of 6 weeks exceeds NSW maximum of 4 weeks"
5. Fairness Score: **"unfair"**

---

*This system provides automated screening but should not replace professional legal advice for complex cases.*

