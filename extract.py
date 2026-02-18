import requests
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine

import gspread #to export clean data to google sheets
from gspread_dataframe import set_with_dataframe
import os
import json
from oauth2client.service_account import ServiceAccountCredentials

######################### EXTRACTING ##########################
#API_KEY = 'BDSGBX4SP58TL7X9'
#SYMBOL = 'AAPL'
API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY', 'BDSGBX4SP58TL7X9')
SYMBOL = 'AAPL'
#pulling latest news for "technology" in Alpha Vantage
def fetch_market_sentiment(topic='technology'):
   url = f'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&topics={topic}&apikey={API_KEY}'
   response = requests.get(url)
    

   if response.status_code == 200:
       data = response.json()
       articles = data.get('feed', []) #Alpha Vantage return 'feed'
       return articles
   else:
       print(f"Error: {response.status_code}") #edge case where file not found
       return []
#raw_data = fetch_market_sentiment()

##TRANSFORMING DATA
class NewsProcessor:
    def __init__(self, raw_feed):
        self.raw_feed = raw_feed
        self.cleaned_data = []
       

    def process(self):
        for item in self.raw_feed:
            #Alpha Vantage has sentiment labels and score already
            #we want HIGH RELEVANCE items ONLY
            processed_item = { 
                'title': item.get('title'),
                'time_published': self._parse_date(item.get('time_published')),
                'sentiment_score': float(item.get('overall_sentiment_score', 0)),
                'relevance': self._get_ticker_relevance(item, 'AAPL')
            }
            self.cleaned_data.append(processed_item)
        return pd.DataFrame(self.cleaned_data)
        
    def _parse_date(self, date_str):
        return datetime.strptime(date_str, '%Y%m%dT%H%M%S') 
    
    def _get_ticker_relevance(self, item, ticker):
        #helper to find specifies ticker relevance in 'ticker_sentiment' list
        for t in item.get('ticker_sentiment', []):
            if t.get('ticker') == ticker:
                return float(t.get('relevance_score', 0))
        return 0.0
            

##Uploading cleaned data onto PostgreSQL 
#get url uplodad database (db) onto cloud
DB_URL = "postgresql://postgres:FOEjTNx9ovDLUtYf@db.aeygshohlxdyncevzuus.supabase.co:5432/postgres"

engine = create_engine(DB_URL)   


################ Uploading cleaned data onto google sheets ###################

"""
def push_to_sheets(df, sheet_id="1vEtAH5aV-sNLd4mZo4xt2E2OJ7Dc2urwHJLYGNZM2lg"):
    # Explicitly define the scopes
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]
    
    # Authenticate with explicit scopes
    gc = gspread.service_account(filename='service_account.json', scopes=scopes)
    sh = gc.open_by_key(sheet_id)
    worksheet = sh.get_worksheet(0)

    print(f"📍 Writing to Spreadsheet: {sh.title} | Tab: {worksheet.title}")
    print(f"📊 Rows received for upload: {len(df)}") 
    
    existing_records = worksheet.get_all_records()
    existing_titles = {row['title'] for row in existing_records} if existing_records else set()
    new_data_df = df[~df['title'].isin(existing_titles)]

    print(f"✨ New unique rows to add: {len(new_data_df)}") # NEW
    if not new_data_df.empty:
        # Convert Timestamps to strings so JSON can handle them
        # This formats it as '2026-02-12 22:51:45'
        new_data_df['time_published'] = new_data_df['time_published'].dt.strftime('%Y-%m-%d %H:%M:%S')
        
        # Now send the data
        worksheet.append_rows(new_data_df.values.tolist())
        print("🚀 Data successfully sent to Google Sheets!")
"""

### NEW PUSH TO SHEETS #####
def push_to_sheets(df, sheet_id="1vEtAH5aV-sNLd4mZo4xt2E2OJ7Dc2urwHJLYGNZM2lg"):
    scopes = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
    
    # 2. AUTHENTICATION: Check for GitHub Secret 'GOOGLE_CREDENTIALS'
    creds_json = os.getenv('GOOGLE_CREDENTIALS')
    
    if creds_json:
        # If on GitHub, use the Secret string
        creds_dict = json.loads(creds_json)
        creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scopes=scopes)
        gc = gspread.authorize(creds)
    else:
        # If on your Mac, use the 'service_account.json' file
        gc = gspread.service_account(filename='service_account.json', scopes=scopes)

    sh = gc.open_by_key(sheet_id)
    worksheet = sh.get_worksheet(0)

    print(f"📍 Writing to Spreadsheet: {sh.title}")
    
    existing_records = worksheet.get_all_records()
    
    # 3. DEDUPLICATION: Safe .get() prevents the 'KeyError' crash
    existing_titles = {row.get('title') for row in existing_records if row.get('title')} if existing_records else set()
    
    new_data_df = df[~df['title'].isin(existing_titles)]

    print(f"✨ New unique rows to add: {len(new_data_df)}") 
    if not new_data_df.empty:
        new_data_df['time_published'] = new_data_df['time_published'].dt.strftime('%Y-%m-%d %H:%M:%S')
        worksheet.append_rows(new_data_df.values.tolist())
        print("🚀 Data successfully sent to Google Sheets!")





########################## MAIN ###########################
def main():
    # 1. Fetch the data
    print("🔍 Fetching news...")
    raw_news = fetch_market_sentiment('technology')
    
    if not raw_news:
        print("❌ No data fetched. Check your API key or wait a minute.")
        return # Stop here if there's no data

    # 2. Process the data
    print("⚙️ Processing news...")
    processor = NewsProcessor(raw_news)
    df = processor.process() # Now 'df' is defined!

    # 3. Upload the data
    print("☁️ Syncing to Google Sheets...")
    push_to_sheets(df)
    print("🚀 Complete! Check your Google Sheet.")

if __name__ == "__main__":
    main()

