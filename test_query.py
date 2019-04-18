from stock import Query

def test___init__():
    query1 = Query('stocks_now1.db', '22:34', 'YI')
    assert query1.db == 'stocks_now1.db'
    assert query1.time == '22:34'
    assert query1.ticker == 'YI'

def test_query_ticker():
    #query1 = Query('stocks.db', '16:32', 'YI')
    #assert query1.query_ticker == True
    query2 = Query('stocks_now.db', '12:42', 'YI')
    assert query2.query_ticker() == True
