import dash_bootstrap_components as dbc
from dash import Input, Output, callback, Dash, html, dcc
from yahoo_fin.stock_info import *
import pandas as pd


table1=dbc.Col(id='table1',xs=12, sm=12, md=12, lg=3, xl=3,style={'margin-top':'0.22rem'})

@callback (Output('table1','children'),Input('intermediate-value', 'data'))
def summary(data):
    dict1=get_stats(data)
    df1=pd.DataFrame.from_dict(dict1)
    df1.set_index('Attribute',inplace=True)
    df1=df1[df1.index.isin([
                         'Shares Outstanding 5',
                         'Revenue (ttm)',
                         'Quarterly Revenue Growth (yoy)',
                         'Quarterly Earnings Growth (yoy)',

                         ])]

    dict2=get_quote_data(data)
    df2=pd.DataFrame.from_dict(dict2,orient='index')
    df2=df2[df2.index.isin([
                     'regularMarketChangePercent', 'regularMarketPrice',
                     'regularMarketDayRange','fiftyTwoWeekRange',
                     'epsTrailingTwelveMonths', 'epsForward',]
                    )]
    df2.rename(columns={0:'Value'},inplace=True)

    df3=get_stats_valuation(data)
    ls=df3.columns[:2]
    df3=df3[ls].rename(columns={ls[0]:'unnamed',ls[1]:'Value'})
    df3=df3.set_index('unnamed')
    df3=df3[df3.index.isin(['Market Cap (intraday)' ,'Trailing P/E' ,'Forward P/E',
                            'PEG Ratio (5 yr expected)','Price/Sales (ttm)','Price/Book (mrq)']
                           )]

    df_concat=pd.concat([df1,df2,df3])
    df_concat.rename_axis([f'{data.upper()}'],inplace=True)

    df_concat.rename(index={'Shares Outstanding 5':'Shares Outstanding','epsTrailingTwelveMonths':'EPS(ttm)',
                            'epsForward':"EPS (fwd)",'regularMarketChangePercent':'Percent Change (intraday)',
                            'regularMarketPrice':'Current Price', 'regularMarketDayRange':"Day Range", 'fiftyTwoWeekRange':"52-week Range"},inplace=True)

    df_concat=df_concat.reindex(['Current Price','Day Range','Percent Change (intraday)', '52-week Range', 'EPS(ttm)', 'EPS (fwd)',
                                 'Trailing P/E','Forward P/E','PEG Ratio (5 yr expected)', 'Price/Sales (ttm)', 'Price/Book (mrq)','Revenue (ttm)',
                                 'Quarterly Revenue Growth (yoy)','Quarterly Earnings Growth (yoy)','Market Cap (intraday)', 'Shares Outstanding'])

    df_concat.iloc[2,0]=str(round(df_concat.iloc[2,0],2))+' %'

    return dbc.Table.from_dataframe(df_concat,striped=True, bordered=True, color='primary',hover=True, index=True,size='sm')


'''
    #print(df_concat.index)

print(df_concat)
df_price=df_concat[df_concat.index.isin(['regularMarketChange', 'regularMarketChangePercent',
                                         'regularMarketPrice', 'regularMarketDayRange', 'regularMarketVolume',
                                         'fiftyTwoWeekRange','symbol']
                                        )]
df_fundamental=df_concat[~df_concat.index.isin(['regularMarketChange', 'regularMarketChangePercent',
                                                'regularMarketPrice', 'regularMarketDayRange', 'regularMarketVolume',
                                                'fiftyTwoWeekRange','symbol']
                                               )]
print(df_price,df_fundamental)

'''