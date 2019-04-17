import sqlite3
from tickers import Tickers
import time
from datetime import datetime
from iex import Stock
import os
import sys

class Query:
    """
    a simple query class
    """
    def __init__(self, db, time, ticker):
        """
        This initalizes a Query object query with database file value,
        time value (which ids the specific minute for which to print data),
        and ticker (which ids the specific ticker for which to print data)
        """
        self.db = str(db)
        self.time = str(time)
        self.ticker = str(ticker)

    def query_ticker(self):
        """
        This function prints the details corresponding to a specific
        time and ticker symbol to the terminal
        """
        conn = sqlite3.connect(self.db)
        c = conn.cursor()
        t=(self.ticker,self.time)
        c.execute("SELECT * FROM STOCKDATA WHERE TICKER = ? AND TIME=?",t)
        print(c.fetchone())
