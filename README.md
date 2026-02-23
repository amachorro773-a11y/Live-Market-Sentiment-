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

## Market Sentiment Pulse
- A raw sentiment is volatile, so with many sentiments rolling in we use the moving average to gauge the long-term vibe of the market.
## Sentiment vs. Relevance
This scatter plot categorizes every news article based on two critical dimensions: how intense the sentiment is (X-axis) and how relevant the article is to the specific ticker (Y-axis).
- The "Market Movers" (Top Right/Left): These represent high-relevance articles with strong bullish (green) or bearish (red) sentiment.      These are the primary drivers for the Top 5 Headlines sheet and represent the most actionable data points in the pipeline.
- The "High-Volume Noise" (Bottom Cluster): The dense cluster along the 0.0 relevance line shows articles that may mention a ticker but      aren't focused on it. By identifying this cluster, the dashboard successfully filters out "ticker-tagging" noise that would otherwise      skew the average sentiment score.
- Neutral/General News (Center Cluster): Articles falling near the $0.0$ sentiment mark provide a baseline of general market updates,        showing stability rather than volatility.
## Market Vibe Gauge
- Shows the distribution of Bearish vs. Bullish news counts, as well as neutral news. This provides a quick "health check" of the current
  news volume
## Top 5 Headlines
- Provides the root cause for any spikes or dips seen in the Pulse timeline, allowing stakeholders to immediately identify the event.
  Demonstrated by displaying the most relevant news in a text table.



