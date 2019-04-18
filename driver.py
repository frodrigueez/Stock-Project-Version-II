import argparse
import os
import sys
from stock import Tickers, Fetcher, Query
def driver():
    """
    a main module that takes the following flags:

    ∗ operation: Values are: ’Fetcher’, ’Ticker’, or ’Query’ Based on the value of this variable, you will
    decide which class you will instantiate and the optional arguments whose values you will need.

    1. For ’Ticker’: Use the optional flag ’ticker count’ to instantiate Tickers class and then call the
    save tickers() function.

    2. For ’Fetcher’: Use the optional flags ’db’ and ’time limit to instantiate Fetcher class and then
    call the fetch all data() function.

    3. For ’Query’: Use the optional flags ’db’ and ’time’ and ’ticker’ to instantiate Query class and
        then call the function to fetch and print data from the database. The data must be printed out
    to the terminal when this operation is used.


    ∗ time: Used by the Query class to identify the specific minute for which to print data. Optional
    argument used only for the Query class.

    ∗ ticker: Used by the Query class to identify the specific ticker for which to print data. Optional
    argument used only for the Query class.

    ∗ time limit: Used by the Fetcher class to identify the length of time in seconds for which to fetch
    data. Optional argument used only for the Fetcher class.

    ∗ db: Used by the Fetcher and Query classes to specify the database file to be used. Optional argument
    used only for the Fetcher and Query classes.

    ∗ ticker count: Used only by the Tickers class to specify the number of valid tickers to be fetched.
    Optional argument only used by Tickers class.

    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--operation", help="values are: 'Fetcher', 'Ticker', 'Query'")
    parser.add_argument("--time", help="used by Query to identify specific minute for which to print data")
    parser.add_argument("--ticker", help="used by Query to identify specific ticker for which to print data")
    parser.add_argument("--time_limit", help="used by Fetcher class to identify the length of time in seconds for which to fetch data")
    parser.add_argument("--db", help="used by Fetcher and Query classes to specify database file to be used")
    parser.add_argument("--ticker_count", help="used by Tickers class to specify number of valid tickers to be fetched")
    args = parser.parse_args()
    if args.operation == "Ticker":
        print(f"instantiate Tickers class w {args.ticker_count}")
        tickers = Tickers(args.ticker_count)
        tickers.save_tickers()
    elif args.operation == "Fetcher":
        print(f"instantiate Fetchers class w {args.db} & {args.time_limit}")
        fetcher = Fetcher(args.db, args.time_limit)
        # call fetch_all_data()
        fetcher.fetch_all_data()
    elif args.operation == "Query":
        print(f"instantiate Query class w {args.db} & {args.time} & {args.ticker}")
        query = Query(args.db, args.time, args.ticker)
        query.query_ticker()
if __name__ == "__main__":
    # process flagser
    driver()
