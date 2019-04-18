
import os.path
import requests
import re
from iex import Stock
from selenium import webdriver
import sys
import os

# fetches the first n valid tickers from the following URL and write tickes in


class Tickers:
    """
    A simple general Tickers class
    """
    def __init__(self, ticker_count):
        """
        Initalizes a Ticker object ticker with provided ticker_count argument
        access this attribute with ticker.ticker_count
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
            if x is not None:
                if i is 1:
                    t = os.path.basename(x.string).upper()
                    t = t[:-3]
                    tickers.append(t)
                if i is 3:
                    i = 0
                    i = i + 1

        ticker_filename = "tickers.txt"

        f = open(ticker_filename, 'w')

        n = 0
        validTickers = []
        for x in tickers:
            if n == int(self.ticker_count):
                break
            else:
                try:
                    sys.stdout = open(os.devnull, 'w')
                    Stock(x).price()
                    sys.stdout = sys.__stdout__
                    validTickers.append(x)
                    n += 1
                    f.write('{0}\n'.format(x))
                except Exception:
                    print("not valid")

        os.remove("./html.txt")
