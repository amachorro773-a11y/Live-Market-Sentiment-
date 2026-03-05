# Strategic Market Sentiment Intelligence (MSI) System
Role: Financial Data Analyst\
Domain: Equity Research & Quantitative Analysis

# Background
Developed a Market Sentiment Intelligence Dashboard built to mirror workflows within a sector-focused equity research team, to improve visibility into real-time sentiment shifts across high-volume technology equities (e.g., AAPL).

# Measurable Business Impact
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

# Strategic Solution & Architecture
To solve this, I built a decision-support system.
- **Automated Signal Generation:** Deployed Python scripts interfacing with the Alpha Vantage API to ingest and score live     technology sector news, eliminating manual tracking.
- **Low-Latency Infrastructure:** Engineered a cloud-based data bridge using the Google Sheets API to ensure a persistent,     up-to-date warehouse without heavy overhead.
- **Executive Visualization:** Architected a Tableau dashboard designed strictly for "At-a-Glance" decision-making,            translating complex data into a scannable narrative.

# Tech Stack and Data Structures
- Language: Python (Pandas, Requests)
- API: Alpha Vantage (Market News & Sentiment)
- Storage/Bridge: Google Sheets API (gspread)
- Visualization: Tableau Public
- Data Automation: Github

In Alpha Vantage's "technology" sector, relevant data is formatted into these categories:
<img width="623" height="467" alt="export (4)" src="https://github.com/user-attachments/assets/c1a6ee55-8ed5-4506-8fff-6610e7c9e23c" />




# High Level Overview
<img width="930" height="716" alt="Live_Market drawio" src="https://github.com/user-attachments/assets/db8196ad-0759-4c5b-8b83-d64c268dd92d" />


# MSI Dashboard
The MSI Dashboard is divided into four tactical modules designed to streamline a Financial Analyst's daily workflow:
<img width="649" height="859" alt="Dashboard 1 (2)" src="https://github.com/user-attachments/assets/dd482a92-2813-479e-8a20-bd99c48c6a01" />




Check out the live dashboard here: [Live Tableau Dashboard](https://public.tableau.com/shared/2ZS43KD5C?:display_count=n&:origin=viz_share_link)

## Market Sentiment Pulse (Momentum Tracking)
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

# Challenges & Lessons Learned
- API Rate Limiting: One of the main hurdles was managing the Alpha Vantage API's free tier limits. I solved this by implementing a "caching" logic in Python, storing the daily news in Google Sheets so Tableau doesn't trigger a new API call every time a user refreshes the dashboard.
  
- Github Actions: I needed the data pipeline to run reliably every day without relying on my local machine's uptime or using local scheduling tools like cron. So I migrated the execution layer to GitHub Actions, configured a .yml workflow to trigger the Python script on a daily schedule, ensuring the Tableau dashboard stays updated automatically.
  
- Github Actions Secrets for Security: To protect my API credentials, I implemented GitHub Actions Secrets. This taught me the importance of environment variable management, allowing the script to fetch and send data (Alpha Vantage and Google Sheets) securely without exposing sensitive API keys in the public repository.
  
- Data Consistency: Since this data-set was a bit unorganized, I had to write custom cleaning functions to handle special characters in headlines and ensure the time_published strings were correctly parsed into a Tableau friendly DateTime format.

- Aggregation Bias: Initially, I used "Sum" for sentiment, which skewed results toward stocks with high news volume. Switching to Moving Averages (AVG) was a key pivot that made the "Market Pulse" a more accurate reflection of actual sentiment trends.
  
- Path Management in CI/CD: When setting this project up for other users, I noticed that I did not create a folder with the needed libraries and dependencies, and decided to add it in towards the end. I learned that moving files into a /src directory requires updating the GitHub Actions workflow paths. This taught me the importance of maintaining alignment between repository structure and automated deployment scripts.

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
