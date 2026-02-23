# Project Background
As a person new to investing, I wanted to make sure that I was making the right purchases on the "best" or most "reliable" stock. 
Being new to this field of investing, I wanted to create this project to learn more about stocks and thier behaviors, while creating a useful tool to
make the right stock purchases.\
This project reviews **real time shifts in the overall sentiment for stock prices in the technology sector, tracking market trends for specific tickers such as AAPL (Apple Inc. Stock).**
## What does this mean?
A sentiment is the overall attitude, mood, or psychology of investors toward a particular stock or the financial market as a whole, reflecting whether they are optimistic ("bullish") or pessimistic ("bearish"). 
It acts as a driving force behind supply and demand, influencing price movements independent of fundamental, intrinsic value.
## Why does this matter?
- I noticed how tedious and time-consuming it can be to manually look at these observations, as it can be slightly inconvineient to refresh a page to check for updates, and/or
  making your own observations by looking at the market history for the past week.
  I wanted something slightly more convinent for myself, something that shows me the market history.
- So I created an end to end python piplines that pulls, processes, and pushes data onto a live dashboard.

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

# Executive Summary
This **Market Sentiment Intelligence Dashboard** is an end-to-end data solution that transforms raw financial news into actionable insights.\
By automating data extraction via the **Alpha Vantage API** and leveraging a **Python-to-Tablea**u pipeline, the project quantifies market volatility and trend stability, as well as a **real-time 'Market Pulse,'** surfacing the **Top 5 most impactful headlines** to explain the root causes of sentiment shifts and identifying the most **bullish market signals** driving the news cycle. 
(Updated version in link below)


<img width="649" height="859" alt="Dashboard 1 (2)" src="https://github.com/user-attachments/assets/dd482a92-2813-479e-8a20-bd99c48c6a01" />




Check out the live dashboard here: [Live Tableau Dashboard](https://public.tableau.com/shared/2ZS43KD5C?:display_count=n&:origin=viz_share_link)

## Sentiment Pulse
A dual-axis time series plot featuring raw sentiment data points (orange) overlaid with a Moving Average line (blue).
- This chart identifies market momentum. While individual articles create significant "noise" (vertical spread), the moving average          smooths out the volatility to reveal the sustained trend of market opinion over several days.
- Helps distinguish between a single bad headline and a systemic shift in market sentiment. For example, you can see if a cluster of         bearish news is starting to drag the long-term trend line downward.
  
## Sentiment vs. Relevance
This scatter plot categorizes every news article based on two critical dimensions: how intense the sentiment is (X-axis) and how relevant the article is to the specific ticker (Y-axis).
- The "Market Movers" (Top Right/Left): These represent high-relevance articles with strong bullish (green) or bearish (red) sentiment.      These are the primary drivers for the Top 5 Headlines sheet and represent the most actionable data points in the pipeline.
- The "High Volume Noise" (Bottom Cluster): The dense cluster along the 0.0 relevance line shows articles that may mention a ticker but      aren't focused on it. By identifying this cluster, the dashboard successfully filters out "ticker-tagging" noise that would otherwise      skew the average sentiment score.
- Neutral/General News (Center Cluster): Articles falling near the $0.0$ sentiment mark provide a baseline of general market updates,        showing stability rather than volatility.

## Top 5 Headlines
A dynamic text table sorted by the highest absolute sentiment scores.
- This is the dashboard’s "Root Cause Analysis" tool. It provides the qualitative context, the actual stories, behind the quantitative       spikes seen in the Pulse chart.
- By surfacing specific titles (like Bolt Data, Uber, or Garmin), it allows you to verify if a sentiment spike is driven by a sector-wide    event or a specific company's earnings report or product launch.
  
## Market Vibe Gauge
A pie chart showing the percentage breakdown of Bearish, Bullish, and Neutral sentiment, accompanied by a volume bar.
- Provides an immediate "At a Glance" health check of the total news volume. It answers the question on whether the current market           environment is predominantly positive, negative, or just noisy.
- The "Neutral" slice often represents the "Market Noise" identified in your Relevance chart. A growing "Bearish" or "Bullish" slice         indicates a strong consensus is forming in the financial media, which often precedes higher trading volatility.
  



f
