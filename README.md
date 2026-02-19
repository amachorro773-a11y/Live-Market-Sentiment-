# Project Background
As a person new to investing, I wanted to make sure that I was making the right purchases on the "best" or most "reliable" stock. 
Being new to this field of investing, I wanted to create this project to learn more about stocks and thier behaviors, while creating a useful tool to
make the right stock purchases.
This project reviews real time shifts in the overall sentiment for stock prices in the technology sector, tracking market trends for specific tickers such as AAPL (Apple Inc. Stock).
## What does this mean?
A sentiment is the overall attitude, mood, or psychology of investors toward a particular stock or the financial market as a whole, reflecting whether they are optimistic ("bullish") or pessimistic ("bearish"). 
It acts as a driving force behind supply and demand, influencing price movements independent of fundamental, intrinsic value.
## Why does this matter?
- I noticed how tedious and time-consuming it can be to manually look at these observations, as it can be slightly inconvineient to refresh a page to check for updates, and/or
  making your own observations by looking at the market history for the past week.
  I wanted something slightly more convinent for myself as person new to this field of investing.
- So I created an end to end python piplines that pulls, processes, and pushes data onto a live dashboard.

# Tech Stack and Data Structures
Language: Python (Pandas, Requests)
API: Alpha Vantage (Market News & Sentiment)
Storage/Bridge: Google Sheets API (gspread)
Visualization: Tableau Public
Data Automation: Github

In Alpha Vantage's "technology" sector. relevant data is formatted into these categories:
<img width="623" height="467" alt="export (4)" src="https://github.com/user-attachments/assets/c1a6ee55-8ed5-4506-8fff-6610e7c9e23c" />




# High Level Overview
<img width="930" height="716" alt="Live_Market drawio" src="https://github.com/user-attachments/assets/db8196ad-0759-4c5b-8b83-d64c268dd92d" />

