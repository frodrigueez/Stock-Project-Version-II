from stock import Tickers
import pytest

def test___init__():
    ticker = Tickers(100)
    ticker2 = Tickers(110)
    ticker3 = Tickers(1)
    assert ticker.ticker_count == 100
    assert ticker2.ticker_count == 110
    assert ticker3.ticker_count == 1

def test_raises_exception_on_out_of_range_ticker_count():
    with pytest.raises(IndexError):
        ticker = Tickers(120)

#def test_save_tickers():
#    ticker = Tickers(100)
#    ticker.save_tickers()
#    ticker_count = count_tickers_in_file('tickers.txt')
#    assert ticker_count == 100

def count_tickers_in_file(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
        return i + 1


