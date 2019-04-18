from stock import Tickers
import pytest

def test___init__():
    """
    tests correct initalization of ticker object, (ie: correct
    storage of ticker_count for ticker_counts within range)
    """
    ticker = Tickers(100)
    ticker2 = Tickers(110)
    ticker3 = Tickers(1)
    assert ticker.ticker_count == 100
    assert ticker2.ticker_count == 110
    assert ticker3.ticker_count == 1

def test_raises_exception_on_out_of_range_ticker_count():
    """
    tests that IndexError exception does work when trying to initalize a ticker
    object witha ticker count greater than bound 110
    """
    with pytest.raises(IndexError):
        ticker = Tickers(120)

def test_web_crawling():
    """
    tests that selenium properly crawls the provided url
    """
    ticker = Tickers(20)
    assert ticker.save_tickers() == True


#def test_save_tickers():
#    """
#    This will test that the selenium we use to get valid tickers is working properly
#    """
#    ticker = Tickers(100)
#    ticker.save_tickers()
#    file_ticker_count = count_tickers_in_file('tickers.txt')
#    assert ticker_count == 100

#def count_tickers_in_file(fname):
#    """
#    a function to aid in the test_save_tickers
#    it counts the lines (amount of tickers) in generated 'tickers.txt'
#    """
#    with open(fname) as f:
#        for i, l in enumerate(f):
#            pass
#       return i + 1


