"""
 a .py file for tickers module. use python3 tickers.py number_of_tickers
 ticker_filename to execute
"""
import os.path
import requests
import re
from iex import Stock
from selenium import webdriver
import sys
import os

# fetches the first n valid tickers from the following URL and write tickes in
# file tickers.txt
def save_tickers(amountOfTickers):
    driver = webdriver.Chrome('./chromedriver')
    link = "http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQrender=download"
    driver.get(link)
    driver.find_element_by_xpath('//*[@id="main_content_lstpagesize"]/option[4]').click()

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

    if amountOfTickers > 150:
        raise IndexError("n passed to save_tickers out of range. n must be <= 150")
    ticker_filename = sys.argv[2]

    f = open(ticker_filename, 'w')

    n = 0
    validTickers = []
    for x in tickers:
        if n == amountOfTickers:
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

if __name__ == "__main__":
    save_tickers(int(sys.argv[1]))
