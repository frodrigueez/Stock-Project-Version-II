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
        self.db = str(db)
        self.time_limit = int(time_limit)

    def create_db(self):
        conn = sqlite3.connect(self.db)
        c = conn.cursor()
        print("Opened database successfully")

        c.execute('''CREATE TABLE STOCKDATA
            (TIME TEXT, TICKERID TEXT PRIMARY KEY, LOW INT, HIGH INT, OPEN INT, CLOSE INT, PRICE INT, VOLUME INT)''')
        print("Table created successfully")
        conn.commit()
        conn.close()
    
    def update_stock_info(self,ticker):
    #"""
    #updates stock information in database for argument ticker
    #"""    
        
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
        #c.execute("INSERT INTO STOCKDATA (TIME, TICKERID, LOW, HIGH, OPEN, CLOSE, PRICE, VOLUME) VALUES (detime, ticker, thevalues['low'], thevalues['high'], thevalues['open'], thevalues['close'], thevalues['latestPrice'], thevalues['latestVolume'])")

        conn.commit()
    #def fetch_all_data():
    #"""
    #calls update_stock_info() for all tickers. 
    #this will run for specified time period time_lim (in secs)
    #"""
        
if __name__ == "__main__":
    fetcher = Fetcher("stocks_now.db", 60) 
    fetcher.create_db()
    fetcher.update_stock_info('YI')
