from fetcher import Fetcher
    
def test___fetcher__():
    fetcher1 = Fetcher('stocks_now1.db', 90)
    fetcher2 = Fetcher('stocks_now2.db', 60)
    assert fetcher1.db == 'stocks_now1.db'
    assert fetcher2.db == 'stocks_now2.db'
    assert fetcher1.time_limit == 90
    assert fetcher2.time_limit == 60
    assert fetcher1.tickers == []
    assert fetcher2.tickers == []

def test_read_tickers():
    fetcher1 = Fetcher('stocks_now1.db', 90)
    fetcher1.read_tickers()
    assert fetcher1.tickers != []
   

#def test_create_db():

#def update_stock_info():
