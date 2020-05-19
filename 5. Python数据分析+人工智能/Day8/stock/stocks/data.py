import tushare as ts


# 全部股票列表
def stock_all_data(code):
    if code is None:
        df = ts.get_stock_basics()
    return df

# 实时数据
def stock_now_all(code):
    df = ts.get_realtime_quotes(code)
    return df


# k线数据
def stock_k_data(code):
    df = ts.get_hist_data(code)
    return df