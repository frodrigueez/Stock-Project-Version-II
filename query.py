import sqlite3


class Query:
    def __init__(self, db, time, ticker):
        """
        This initalizes a Query object query with database file value, 
        time value (which ids the specific minute for which to print data),
        and ticker (which ids the specific ticker for which to print data)
        """
        self.db = db
        self.time = time
        self.ticker = ticker
    
    def query_ticker(self):
        """
        This function prints the details corresponding to a specific
        time and ticker symbol to the terminal
        """
        conn = sqlite3.connect(self.db)
        c = conn.cursor()
        c.execute('''SELECT * FROM STOCKDATA 
                    WHERE TICKER = 'self.ticker'
                    AND TIME = ?''',self.ticker, self.time)
        print(c.fetchall()) 

if __name__ == "__main__":
    query = Query('stocks_now.db', '12:53', 'YI')        
    query.query_ticker() 
