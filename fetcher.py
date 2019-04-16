import sqlite3
from tickers import Tickers
import time
from datetime import datetime
from iex import Stock
import os
import sys

class Fetcher:
    """
    A simple fetcher class
    """
    def __init__(self, db, time_limit):
        """
        initalizes a fetcher object with database name, and time_limit given db and time_limit. also 
        initalizes object with empty tickers list.
        given Fetcher object fetcher, you can access these attributes with
        fetcher.db, fetcher.time_limit and fetcher.tickers
        """
        self.db = str(db)
        self.time_limit = int(time_limit)
        self.tickers = []

    def read_tickers(self):
        """
        reads all tickers from 'Ticker.txt' and writes them to Fetcher instance, fetcher, fetcher.tickers where
        tickers is a list
        """
        with open('tickers.txt') as f:
            for line in f:
                self.tickers.append(line.strip())

    def create_db(self):
        """
        creates database named after Fetcher instance, fetcher, fetcher.db value
        """
        conn = sqlite3.connect(self.db)
        c = conn.cursor()
        print("Opened database successfully")

        c.execute('''CREATE TABLE IF NOT EXISTS STOCKDATA
            (TIME TEXT, TICKER TEXT, LOW FLOAT, HIGH FLOAT, OPEN FLOAT, CLOSE FLOAT, PRICE FLOAT, VOLUME INT)''')
        print("Table created successfully")
        conn.commit()
        conn.close()
    
    def update_stock_info(self,ticker):
        """
        updates stock information in database for argument ticker
        """    
    
        want = ['low', 'high', 'open', 'close', 'latestPrice', 'latestVolume']

        sys.stdout = open(os.devnull, 'w')
        updatedInfo = Stock(ticker).quote()
        sys.stdout = sys.__stdout__

        thevalues = {key:value for key, value in updatedInfo.items() if key in want}
    
        detime = time.strftime("%H:%M")
        
        conn = sqlite3.connect(self.db)
        c = conn.cursor()
        
        print("Opened database successfully")
        print(f"the values to insert...\n{thevalues}")
        print(type(thevalues['latestVolume']))
        c.execute("INSERT INTO STOCKDATA VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (detime, ticker, thevalues['low'], thevalues['high'], thevalues['open'], thevalues['close'], thevalues['latestPrice'], thevalues['latestVolume']))
       

        conn.commit()
        conn.close()

    def fetch_all_data(self):
        """
        calls update_stock_info() for all tickers. 
        this will run for specified time period time_lim (in secs)
        """
        for ticker in self.tickers:
            self.update_stock_info(ticker)

if __name__ == "__main__":
    fetcher = Fetcher("stocks_now.db", 60) 
    fetcher.read_tickers()
    fetcher.create_db()


    fetcher.fetch_all_data()
