import argparse
import os 
import sys

if __name__ == "__main__":
    # process flags
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
    elif args.operation == "Fetcher":
        print(f"instantiate Fetchers class w {args.db} & {args.time_limit}")
    elif args.operation == "Query":
        print(f"instantiate Query class w {args.db} & {args.time} & {args.ticker}")

