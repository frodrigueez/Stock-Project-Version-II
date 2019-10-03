import os.path
import requests
import re
from iex import Stock
from selenium import webdriver
import sys
import os
import sqlite3
import time
from datetime import datetime

class Tickers:
    """
    Write one ticker symbol per line of the file tickers.txt. The number n will be provided to the driver
    as an optional argument and will be at most 110.
    """
    def __init__(self, ticker_count):
        """
        Initalizes a Ticker object ticker with provided ticker_count argument
        access this attribute with ticker.ticker_count

        :type ticker_count : integer

        :param ticker_count : amount of tickers
        """
        if int(ticker_count) <= 110:
            self.ticker_count = int(ticker_count)
        else:
            raise IndexError("ticker_count out of range; must be <= 110")

    def save_tickers(self):
        """
        Uses selenium to crawl webpage and access up to 110 valid tickers using
        price() from iex API to verify validity, then writes them to 'tickers.txt'
        with one ticker per line
        """
        crawled = False
        driver = webdriver.Chrome('./chromedriver')
        link = "http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQrender=download"
        driver.get(link)
        driver.find_element_by_xpath('//*[@id="main_content_lstpagesize"]/option[3]').click()

        link = driver.current_url

        tickers = []
        d = requests.get(link)

        html_file = open('html.txt', 'w')
        html_file.write(d.text)
        html_file = open('html.txt')

        tickerbaselink = "https://www.nasdaq.com/symbol/"
        i = 1
        for line in html_file.readlines():
            x = re.search(tickerbaselink, line)

        crawled = True
        return True

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

        :type db : string

        :param db : name of database

        :type time_limit : string

        :param time_limit : data will be fetched for this amount of time
        """
        self.db = str(db)
        self.time_limit = time_limit
        self.tickers = []
        self.hasDB = False
        self.read_tickers()
        self.create_db()



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

        c.execute('''CREATE TABLE IF NOT EXISTS StockData
            (TIME TEXT, TICKER TEXT, LOW FLOAT, HIGH FLOAT, OPEN FLOAT, CLOSE FLOAT, PRICE FLOAT, VOLUME INT)''')
        self.hasDB = True
        conn.commit()
        conn.close()

    def update_stock_info(self,ticker):
        """
        updates stock information in database for argument ticker

        :type ticker : string

        :param ticker : ticker name
        """

        want = ['low', 'high', 'open', 'close', 'latestPrice', 'latestVolume']

        sys.stdout = open(os.devnull, 'w')
        updatedInfo = Stock(ticker).quote()
        sys.stdout = sys.__stdout__

        thevalues = {key:value for key, value in updatedInfo.items() if key in want}

        detime = time.strftime("%H:%M")

        conn = sqlite3.connect(self.db)
        c = conn.cursor()

        c.execute("INSERT INTO StockData VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (detime, ticker, thevalues['low'], thevalues['high'], thevalues['open'], thevalues['close'], thevalues['latestPrice'], thevalues['latestVolume']))


        conn.commit()
        conn.close()

    def fetch_all_data(self):
        """
        calls update_stock_info() for all tickers.
        this will run for specified time period time_lim (in secs)
        """
        timesup = False
        start_time = time.time()
        elapsed_time = 0
        while elapsed_time < int(self.time_limit):
            for ticker in self.tickers:
                self.update_stock_info(ticker)
            elapsed_time = time.time() - start_time
            if int(self.time_limit)-elapsed_time > 60:
                time.sleep(60)
            else:
                break

        timesup = True
        return timesup

class Query:
    """
    a simple query class
    """
    def __init__(self, db, time, ticker):
        """
        This initalizes a Query object query with database file value,
        time value (which ids the specific minute for which to print data),
        and ticker (which ids the specific ticker for which to print data)

        :type db : string

        :param db : name of database

        :type time : string

        :param time :the specific minute for which to print data

        :type ticker : string

        :param ticker : ticker name
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
        c.execute("SELECT * FROM StockData WHERE TICKER = ? AND TIME=?",t)
        if c.fetchone() is not None:
            print(c.fetchone())
            return True
        else:
            return False
