import tushare as ts
import pandas as pd
from time import sleep

ts.set_token('6f47214cf72a29b697efeecdb4ac7730223dfe532c958ec61cf312b4')

pro = ts.pro_api()

Tickers = pro.stock_company(exchange='SZSE',fields='ts_code')

df_full = pd.DataFrame(columns=['ts_code', 'trade_date', 'open', 'high', 'low', 'close', 'pre_close','change', 'pct_chg', 'vol', 'amount'])

def progressbar(current_value,total_value,bar_lengh,progress_char): 
    percentage = int((current_value/total_value)*100)                                                # Percent Completed Calculation 
    progress = int((bar_lengh * current_value ) / total_value)                                       # Progress Done Calculation 
    loadbar = "Progress: [{:{len}}]{}%".format(progress*progress_char,percentage,len = bar_lengh)    # Progress Bar String
    print(loadbar, end='\r')

for i,ticker in enumerate(Tickers['ts_code']):
    df_i = pro.daily(ts_code=ticker, start_date='20230101', end_date='20241101')
    sleep(1)
    progressbar(i,len(Tickers['ts_code']),30,'■')
    df_full = pd.concat([df_full,df_i])

df_full = df_full.reset_index()
Tickers.to_csv('Tickers_Final.csv')
df_full.to_pickle('tusharedata.pkl')
