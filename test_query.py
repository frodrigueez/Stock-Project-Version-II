from stock import Query

def test___init__():
    """
    tests correct initalization of Query object, including
    correct storage of database name, time and ticker name
    """
    query1 = Query('stocks_now1.db', '22:34', 'YI')
    assert query1.db == 'stocks_now1.db'
    assert query1.time == '22:34'
    assert query1.ticker == 'YI'

def test_query_ticker():
    """
    test that query ticker for an assumed known entry works
    query1 is based on write-up and SHOULD be true, for 
    query2 it assumed that that specific entry will NOT be in 
    database, therefore should be false
    """
    query1 = Query('stocks.db', '16:32', 'YI')
    assert query1.query_ticker() == False
    query2 = Query('stocks_now.db', '12:42', 'YI')
    assert query2.query_ticker() == True
