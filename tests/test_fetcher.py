from stock import Fetcher 

def test___fetcher__():
    fetcher1 = Fetcher('stocks_now1.db', 90)
    fetcher2 = Fetcher('stocks_now2.db', 60)
    assert fetcher1.db == 'stocks_now1.db'
    assert fetcher2.db == 'stocks_now2.db'
    assert fetcher1.time_limit == 90
    assert fetcher2.time_limit == 60
    assert fetcher1.tickers != []
    assert fetcher2.tickers != []

def test_read_tickers():
    fetcher1 = Fetcher('stocks_now1.db', 90)
    fetcher1.read_tickers()
    assert fetcher1.tickers != []
   

def test_create_db():
    fetcher1 = Fetcher('stocks_now3.db', 300)
    assert fetcher1.hasDB == True
    
#def test_update_stock_info():
#fetcher1 = Fetcher('stocks_now3.db', 300)
#    assert 

def test_fetch_all_data():
    """
    will test fetch all data by ensuring the boolean variable that signals 
    fetch_all_data has run for the correct amount of time is True, signifying 
    the function ran as it should
    """
    fetcher1 = Fetcher('stocks_now3.db', 130)
    assert fetcher1.fetch_all_data() == True

def count_tickers_in_file(fname):
    """
    a function to aid in the test_update_stock_info() and test_fetch_all_data()
    it counts the lines, entries, in generated .db file
    """
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
        return i + 1


