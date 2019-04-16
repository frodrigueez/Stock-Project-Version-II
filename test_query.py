from query import Query


def test___init__():
    query1 = Query('stocks_now1.db', '22:34', 'YI')
    assert query1.db == 'stocks_now1.db'
    assert query1.time == '22:34'
    assert query1.ticker == 'YI'


