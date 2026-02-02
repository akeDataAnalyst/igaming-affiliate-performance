# 🛡️ iGaming Affiliate Performance & Traffic Integrity Pipeline

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)

---

## Executive Summary

In the high-stakes iGaming industry, marketing budgets are frequently targeted by low-quality traffic, bonus abuse, and automated bot registrations.  
This project delivers an end-to-end analytical pipeline designed to protect marketing margins by continuously evaluating the integrity, ROI, and risk profile of affiliate partners.

By combining financial feature engineering, statistical anomaly detection, and an interactive BI dashboard, the pipeline identifies:

- Bonus Hunters
- Bot-driven registration spikes
- Negative ROI affiliate traffic

This enables stakeholders to reallocate spend away from toxic sources and toward high-LTV (Lifetime Value) channels.

---

## Business Objectives

- Detect and mitigate affiliate fraud & bonus abuse
- Measure true Net Gaming Revenue (NGR) per affiliate
- Identify non-human traffic patterns early
- Enable data-driven affiliate budget reallocation

---

## Key Features

### Dynamic ROI & NGR Tracking
- Real-time calculation of Net Gaming Revenue (NGR)
- Player profitability tracking across multiple markets:
  - UK
  - Brazil
  - India
  - Nigeria

---

### Bonus Abuse “Heatmap” Intelligence
- Custom Bonus-to-Deposit Ratio (BDR) metric
- Instantly flags segments where bonus costs exceed deposits
- Visual heatmaps highlight toxic affiliate–country combinations

---

### Statistical Anomaly Detection (Z-Score)
- Automated detection of bot-driven registration spikes
- Uses standard deviation modeling
- High-risk traffic is flagged for immediate IP and source audit

---

### Interactive Stakeholder Dashboard
- Built with Streamlit
- Multi-dimensional filters:
  - Country
  - Affiliate
- Automated “Red Flag” indicators for rapid decision-making

---

## Strategic Analysis Logic

The pipeline evaluates affiliate health using three analytical layers:

### Bonus-to-Deposit Ratio (BDR)

\[
BDR = \frac{Total\ Bonuses}{Total\ Deposits + 1}
\]

- **BDR > 1.0** → Toxic Segment
- Indicates the house is subsidizing 100%+ of player activity

---

### Traffic Velocity Anomaly (Z-Score)

\[
Z = \frac{x - \mu}{\sigma}
\]

- Measures abnormal spikes in registrations
- Z > 3.0 → Flagged as likely bot activity
- Enables early detection within hours instead of days

---

### Regional Profitability Heatmapping
- Cross-references:
  - Affiliate ID
  - Country Code
- Detects:
  - Localized fraud rings
  - Misconfigured promotions
  - Region-specific performance failures

---
## Business Value & Impact

### Direct Cost Savings
- Identified underperforming affiliates (e.g. `Bonus_Hunter_Site`)
- Detected BDR = 11.08
- Preserved $25,000+ per month in marketing spend

---

### Fraud Mitigation
- Reduced Time-to-Detect bot traffic from days → hours
- Enabled proactive traffic blocking and source auditing

---

### Data-Driven Budget Allocation
- Shift from:
  - Volume-based (CPA)
  - Quality-based (RevShare)
- Visualized true NGR contribution per affiliate

---

## Technical Stack

### Language
- Python 3.9+

### Data Engineering
- Pandas & NumPy — Financial feature engineering & normalization

### Analytics
- SciPy — Z-Score implementation for anomaly detection

### Visualization & UI
- Streamlit — Interactive web-based dashboard
- Matplotlib & Seaborn — Statistical & financial visualizations

---
