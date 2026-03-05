# Strategic Market Sentiment Intelligence (MSI) System
Focus Area: Financial Data Analytics – Equity Markets

## Background
Developed a Market Sentiment Intelligence Dashboard built to mirror workflows within a sector-focused equity research team, to improve visibility into real-time sentiment shifts across high-volume technology equities (e.g., AAPL).

## Measurable Business Impact
- **Operational Efficiency:** Automated sentiment aggregation previously requiring manual news review, reducing monitoring time from hours to minutes per session.
- **Latency Reduction:** Enabled near real-time sentiment tracking, replacing outdated weekly review cycles and allowing for faster reaction to market catalysts.
- **Pipeline Optimization:** Consolidated multiple disparate news and API data sources into one automated, single-source-of-truth reporting pipeline.
- **Scalability:** Built a flexible data framework that can be instantly adapted to monitor other sectors (e.g., Healthcare, Energy) simply by changing the API ticker parameters.

# The Business Problem
Monitoring market sentiment manually is inefficient and reactive. Analysts often rely on:
- Periodic news reviews
- Delayed price reactions
- Subjective interpretation of headlines

This creates a latency gap between market-moving news events and actionable insights.

The solution was to build an automated ETL pipeline that extracts financial news, quantifies sentiment and relevance, and delivers real-time visual analytics through an executive-facing dashboard.

## Strategic Solution & Architecture
To solve this, I built a decision-support system.
- **Automated Signal Generation:** Deployed Python scripts interfacing with the Alpha Vantage API to ingest and score live     technology sector news, eliminating manual tracking.
- **Low-Latency Infrastructure:** Engineered a cloud-based data bridge using the Google Sheets API to ensure a persistent,     up-to-date warehouse without heavy overhead.
- **Executive Visualization:** Architected a Tableau dashboard designed strictly for "At-a-Glance" decision-making,            translating complex data into a scannable narrative.

## Tech Stack and Data Structures
- Language: Python (Pandas, Requests)
- API: Alpha Vantage (Market News & Sentiment)
- Storage/Bridge: Google Sheets API (gspread)
- Visualization: Tableau Public
- Data Automation: Github

In Alpha Vantage's "technology" sector, relevant data is formatted into these categories:
<img width="623" height="467" alt="export (4)" src="https://github.com/user-attachments/assets/c1a6ee55-8ed5-4506-8fff-6610e7c9e23c" />




## High Level Overview
<img width="930" height="716" alt="Live_Market drawio" src="https://github.com/user-attachments/assets/db8196ad-0759-4c5b-8b83-d64c268dd92d" />


# MSI Dashboard
The MSI Dashboard is divided into four tactical modules designed to streamline a Financial Analyst's daily workflow:


<img width="649" height="859" alt="Dashboard 1 (2)" src="https://github.com/user-attachments/assets/dd482a92-2813-479e-8a20-bd99c48c6a01" />




Check out the live dashboard here: [Live Tableau Dashboard](https://public.tableau.com/shared/2ZS43KD5C?:display_count=n&:origin=viz_share_link)

## Sentiment Pulse (Momentum Tracking)
A dual-axis time series plot featuring raw sentiment data points (orange) overlaid with a Moving Average line (blue).
- This chart identifies market momentum. While individual articles create significant "noise" (vertical spread), the moving average          smooths out the volatility to reveal the sustained trend of market opinion over several days.
- Helps distinguish between a single bad headline and a systemic shift in market sentiment. For example, you can see if a cluster of         bearish news is starting to drag the long-term trend line downward.
  
## Sentiment vs. Relevance (Signal to Noise Ratio)
This scatter plot categorizes every news article based on two critical dimensions: how intense the sentiment is (X-axis) and how relevant the article is to the specific ticker (Y-axis).
- The "Market Movers" (Top Right/Left): These represent high-relevance articles with strong bullish (green) or bearish (red) sentiment.      These are the primary drivers for the Top 5 Headlines sheet and represent the most actionable data points in the pipeline.
- The "High-Volume Noise" (Bottom Cluster): The dense cluster along the 0.0 relevance line shows articles that may mention a ticker but      aren't focused on it. By identifying this cluster, the dashboard successfully filters out ticker noise that would skew the average sentiment score.
- Neutral/General News (Center Cluster): Articles falling near the $0.0$ sentiment mark provide a baseline of general market updates,        showing stability rather than volatility.
  
## Market Vibe Gauge (Macro Sector Health)
A pie chart showing the percentage breakdown of Bearish, Bullish, and Neutral sentiment, accompanied by a volume bar.
- Provides an immediate "At-a-Glance" health check of the total news volume. It answers whether the current market environment               is predominantly positive, negative, or noisy.
- The "Neutral" slice often represents the "Market Noise" found in the Relevance chart. A growing "Bearish" or "Bullish" slice         indicates a strong consensus is forming in the financial media, which often means higher trading volatility.
  
## Top 5 Headlines (Root Cause Analysis)
A dynamic text table sorted by the highest absolute sentiment scores.
- It provides the context behind the quantitative spikes seen in the Pulse chart.
- By surfacing specific titles (like Bolt Data, Uber, or Garmin), it allows you to verify if a sentiment spike is driven by a sector-wide    event or a specific company's earnings report or product launch.

# Analytical Applications
This dashboard supports:
- Sector rotation analysis
- Earnings season monitoring
- Event-driven trade validation
- Volatility forecasting
- Short-term momentum strategy confirmation

The system is designed to complement technical price analysis and volume metrics rather than replace them.

# System Constraints and Solutions
API Rate Limiting (Alpha Vantage Free Tier)
The API’s rate limits created instability in repeated dashboard refreshes.
Solution:
- Implemented a caching layer using Google Sheets as a lightweight data store, reducing redundant API calls and stabilizing the reporting layer.
Impact:
- Improved reliability and reduced external API dependency during user interactions.

CI/CD Automation (GitHub Actions)
Local scheduling (cron) was not scalable.\
Solution:
- Migrated execution to GitHub Actions with a scheduled .yml workflow to trigger daily pipeline runs.
Impact:
- Created a fully automated, cloud-based execution layer independent of local uptime.

Credential Security
Public repositories posed a risk of API key exposure.\
Solution:
- Implemented GitHub Actions Secrets and environment variables for secure credential injection.
Impact:
- Established secure DevOps practices aligned with production standards.

Data Normalization & Cleaning
Raw API data contained inconsistent formatting and non-standard timestamps.\
Solution:
- Built custom preprocessing functions to normalize special characters and convert timestamps into Tableau-compatible DateTime format.
Impact:
- Ensured consistent aggregation and visualization accuracy.

Aggregation Bias Correction
Initial sentiment aggregation used SUM, which overweighted high-news-volume tickers.\
Solution:
- Transitioned to moving averages (AVG smoothing) to better represent sustained sentiment trends rather than volume spikes.
Impact:
- Improved signal reliability and reduced statistical distortion.

Repository & Deployment Alignment
Refactoring into a /src directory initially broke CI workflow paths.\
Solution:
- Updated GitHub Actions path references and standardized repository structure.
Impact:
- Reinforced understanding of dependency management and CI/CD integration discipline.

# How to Use This Repo
To reproduce this pipeline or explore the data processing logic, follow the steps below:

1. Prerequisites
- Python 3.x installed.
- An Alpha Vantage API Key (Free tier).
- A Google Cloud Service Account with access to the Google Sheets API.

2. Installation & Setup\
Clone the repository and install the necessary dependencies:
````
git clone https://github.com/amachorro773-a11y/Live-Market-Sentiment-.git
cd your-repo-name
pip install -r requirements.txt\ 
````
NOTE: View the requirements.txt file for the full list of libraries (Pandas, GSpread, Requests, etc.).

3. Repository Structure
- /src: Contains the core Python scripts, including the main data extraction and transformation logic.
- /.github/workflows: Contains the .yml file for the GitHub Actions automation.
- /data: (Optional) Sample CSV outputs or historical logs.

4. Running the Pipeline\
To trigger a manual run of the data fetch:
````
python src/extract.py
````
(Ensure your environment variables for API keys and Google credentials are set up in your .env file or GitHub Secrets.)
