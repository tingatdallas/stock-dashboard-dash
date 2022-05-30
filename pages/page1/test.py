from dash import html, dcc
import dash_bootstrap_components as dbc
from dash import Input, Output, callback
from dash.dependencies import Input, Output


from datetime import datetime
import pandas as pd
import yfinance as yf
import pandas_ta as ta
#import stock_pandas as spd
#import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from yahoo_fin.stock_info import *
from yahoo_fin.options import *
from yahoo_fin import news

'''
df2=get_options_chain('nflx')
df=get_day_most_active()
print(df,df.columns,df2)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

dict1=get_quote_data('tsla')
df=pd.DataFrame.from_dict(dict1,orient='index')
df=df[df.index.isin(['regularMarketChange',
                     'regularMarketChangePercent', 'regularMarketPrice',
                     'regularMarketDayRange',
                     'regularMarketVolume',
                     'priceToBook', 'averageAnalystRating',
                     'averageDailyVolume3Month', 'averageDailyVolume10Day',
                     'fiftyTwoWeekRange', 'trailingPE',
                     'epsTrailingTwelveMonths', 'epsForward',
                     'epsCurrentYear', 'priceEpsCurrentYear', 'sharesOutstanding',
                     'marketCap', 'forwardPE', 'symbol']
                    )]
#print(df.rename(columns={0:'Value'}))
df3=get_stats_valuation('tsla')
ls=df3.columns[:2]
df3=df3[ls].rename(columns={ls[0]:'unnamed',ls[1]:'Value'})
df3=df3.set_index('unnamed')
df4=get_cash_flow('tela', yearly = True)

#print(df4,df4.columns)
#print(get_earnings('tsla')['yearly_revenue_earnings'])
#print(get_earnings_history('tsla'))
#print(get_income_statement('tsla', yearly = True))
print('start')
'''
print(get_financials('tsla', yearly = True, quarterly = True).keys())
df5=get_financials('tsla', yearly = True, quarterly = True)['yearly_balance_sheet']
print(df5.index)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

dict_item= \
    {
        'intangibleAssets':'intangibleAssets',
        'capitalSurplus':'Capital Surplus',
        'totalLiab':'Total Liab',
        'totalStockholderEquity':'Total Stock holder Equity',
        'minorityInterest':'Minority Interest',
        'otherCurrentLiab':'Other Current Liab',
        'totalAssets':'Total Assets',
        'commonStock':'Common Stock',
        'otherCurrentAssets':'Other Current Assets',
        'retainedEarnings':'Retained Earnings',
        'otherLiab':'Other Liab',
        'Good Will':'goodWill',
        'treasuryStock':'Treasury Stock',
        'otherAssets':'otherAssets',
        'cash':'Cash',
        'totalCurrentLiabilities':'Total Current Liabilities',
        'shortLongTermDebt':'Short Long-Term Debt',
        'otherStockholderEquity':'Other Stock holder Equity',
        'propertyPlantEquipment':'Property Plant Equipment',
        'totalCurrentAssets':'Total Current Assets',
        'netTangibleAssets':'Net Tangible Assets',
        'shortTermInvestments':'Short Term Investments',
        'netReceivables':'Net Receivables',
        'longTermDebt':'Long Term Debt',
        'inventory':'Inventory',
        'accountsPayable':'Accounts Payable',
        'longTermInvestments':'Long Term Investments'
    }

for key, value in dict_item.items():
    print(f'dcc.Tab(label="{value}", value="{key}",style=tab_style, selected_style=tab_selected_style),')

'''
'intangibleAssets':value='intangibleAssets',
'capitalSurplus':'Capital Surplus', 
'totalLiab':'Total Liab',
'totalStockholderEquity':'Total Stock holder Equity', 
'minorityInterest':'Minority Interest', 
'otherCurrentLiab':'Other Current Liab', 
'totalAssets':'Total Assets', 
'commonStock':'Common Stock',
'otherCurrentAssets':'Other Current Assets',
'retainedEarnings':'Retained Earnings',
'otherLiab':'Other Liab', 
'Good Will':'goodWill',
'treasuryStock':'Treasury Stock', 
'otherAssets':'otherAssets',
'cash':'Cash',
'totalCurrentLiabilities':'Total Current Liabilities', 
'shortLongTermDebt':'Short Long-Term Debt', 
'otherStockholderEquity':'Other Stock holder Equity', 
'propertyPlantEquipment':'Property Plant Equipment', 
'totalCurrentAssets':'Total Current Assets', 
'netTangibleAssets':'Net Tangible Assets', 
'shortTermInvestments':'Short Term Investments', 
'netReceivables':'Net Receivables', 
'longTermDebt':'Long Term Debt', 
'inventory':'Inventory', 
'accountsPayable':'Accounts Payable', 
'longTermInvestments':'Long Term Investments', 
'''

'''
'researchDevelopment', 'effectOfAccountingCharges', 'incomeBeforeTax',
       'minorityInterest', 'netIncome', 'sellingGeneralAdministrative',
       'grossProfit', 'ebit', 'operatingIncome', 'otherOperatingExpenses',
       'interestExpense', 'extraordinaryItems', 'nonRecurring', 'otherItems',
       'incomeTaxExpense', 'totalRevenue', 'totalOperatingExpenses',
       'costOfRevenue', 'totalOtherIncomeExpenseNet', 'discontinuedOperations',
       'netIncomeFromContinuingOps', 'netIncomeApplicableToCommonShares'
'''