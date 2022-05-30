from dash import html, dcc
import dash_bootstrap_components as dbc
from dash import Input, Output, callback
from dash.dependencies import Input, Output


from datetime import datetime
import pandas as pd
import numpy as np
import yfinance as yf
import pandas_ta as ta
#import stock_pandas as spd
#import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots



style_input={'width':'14rem','height':'2rem','border':'1px solid',
                'border-radius':'10px','border-color':'green','background':'#F5F5F5'}

style_dropdown1={'width':'14rem','height':'2rem','border':'5px dash',
                'border-radius':'10px','border-color':'green','background':'#7FFFD4'}

style_dropdown2={'width':'14rem','height':'2rem','border':'5px dash',
                'border-radius':'10px','border-color':'green','background':'#AFEEEE'}


layout_daily=dbc.Col([
            html.H5("Stock Price & Return",
                        className='text-center md-4'),
            
            html.Div([
                
                   dbc.Label('Enter Ticker:',className='text-center mb-3'),
                   dcc.Input(id='ticker4',
                      placeholder='Enter ticker like tsla, aapl',
                      value='tsla',className='text-center text-primary md-4'
                      ,style=style_input)]
                      ,style={'display': 'flex','justify-content':'center','gap':'2.3rem'},
                
            ),
            html.Div([
            dbc.Label('Choose Period: ',className='text-center success mb-3'),
            dcc.Dropdown(
                id='period4',
                options=[
                    {'label':'1d','value':'1d'},
                    {'label':'5d','value':'5d'},
                    {'label':'1mo','value':'1mo'},
                    {'label':'3mo','value':'3mo'},
                ],
                value='5d',placeholder='period',className='text-primary mb-4',
                style=style_dropdown1,
            ),],style={'display': 'flex','justify-content':'center','gap':'1rem'}),

            html.Div([
            dbc.Label('Choose Interval: ',className='text-center success mb-3'),
            dcc.Dropdown(
                id='interval4',
                options=[
                    {'label':'1m','value':'1m'},
                    {'label':'2m','value':'2m'},
                    {'label':'5m','value':'5m'},
                    {'label':'15m','value':'15m'},
                    {'label':'30m','value':'30m'},
                    {'label':'60m','value':'60m'},
                ],
                value='15m',placeholder='interval',className='text-primary mb-4',
                style=style_dropdown2,
            ),],style={'display': 'flex','justify-content':'center','gap':'0.75rem'}),

            dcc.Graph(id='display-graphic7', figure={})
        ],# width={'size':5, 'offset':1, 'order':1},
            xs=12, sm=12, md=12, lg=6, xl=6,style={'border':'6px solid SeaShell','padding-top':'0.5rem'}
        )


@callback(
    Output('display-graphic7', 'figure'),
    Input('ticker4', 'value'),
    Input('period4','value'),
    Input('interval4','value'),
)

def update_graph(input1,input2,input3): # Plot candlestick price

    def add_ema_vwap(stock_ticker,periods,intervals):# add ema, vwamp. Parameters:stock ticker,interval
        df=yf.download(tickers=stock_ticker,period=periods,interval=intervals)

        df.reset_index(inplace=True)
        df.rename(columns={'Date':'Datetime'},inplace=True)
        df['Return']=10*(df['Close']-df['Close'].iloc[0])/df['Close'].iloc[0]
        return df

    df=add_ema_vwap(stock_ticker=input1,periods=input2,intervals=input3)
    df['willr']=df.ta.willr(length=10)
    df[['K','D','J']]=df.ta.kdj(length=14,signal=5)
    df['rsi']=df.ta.rsi()

    df['average']=(df['High']+df['Low'])/2
    df['EWO']=ta.sma(df["average"],length=5)-ta.sma(df["average"],length=35)
    df["Color"] = np.where(df["EWO"]<0, 'red', 'green')

    df['upper']=df['Close'].map(lambda x:80)
    df['lower']=df['Close'].map(lambda x:20)
    df['upper-']=df['Close'].map(lambda x:-80)
    df['lower-']=df['Close'].map(lambda x:-20)
    #df['rsi']=df.rsi.apply(lambda x:(1-x/100))
    #df['rsi_weighted_close']=df['Close']*(1+ 0.1*df['rsi'])



    def plot2(df):
        fig = make_subplots(rows=5, cols=1, shared_xaxes=True,row_heights=[8,2,2,2,2],
                            start_cell='top-left',vertical_spacing=0.01)#row_titles=['','W & R','K D J','Volume'], row_width=[1, 1])

        fig.add_trace(go.Candlestick(x=df.Datetime,
                                 open=df.Open,
                                 high=df.High,
                                 low=df.Low,
                                 close=df.Close,showlegend=False,legendgroup='1'), row=1, col=1)


        cs = fig.data[0]
        # Set line and fill colors
        cs.increasing.fillcolor = '#109618'
        cs.increasing.line.color = '#109618'#3D9970
        cs.decreasing.fillcolor = '#FF4136'
        cs.decreasing.line.color = '#FF4136'

        fig.append_trace(go.Scatter(x=df.Datetime, y=df['willr'],line=dict(color='purple', width=1.5),name='W & R',legendgroup='2'), row=2, col=1)
        fig.append_trace(go.Scatter(x=df.Datetime, y=-1*df['upper'],line=dict(color='green', width=2),showlegend=False,legendgroup='2'), row=2, col=1)
        fig.append_trace(go.Scatter(x=df.Datetime, y=-1*df['lower'],line=dict(color='red', width=2),showlegend=False,legendgroup='2'), row=2, col=1)
        fig.append_trace(go.Scatter(x=df.Datetime, y=df['K'],line=dict(color='green', width=1.5),name='K',legendgroup='3'), row=3, col=1)
        fig.append_trace(go.Scatter(x=df.Datetime, y=df['D'],line=dict(color='red', width=1.5),name='D',legendgroup='3'), row=3, col=1)
        fig.append_trace(go.Scatter(x=df.Datetime, y=df['J'],line=dict(color='blue', width=1.5),name='J',legendgroup='3'), row=3, col=1)
        fig.append_trace(go.Scatter(x=df.Datetime, y=df['upper'],line=dict(color='red', width=2),showlegend=False,legendgroup='3'), row=3, col=1)
        fig.append_trace(go.Scatter(x=df.Datetime, y=df['lower'],line=dict(color='green', width=2),showlegend=False,legendgroup='3'), row=3, col=1)
        fig.append_trace(go.Scatter(x=df.Datetime, y=df['rsi'],line=dict(color='orange', width=1.5),name='rsi',legendgroup='5'), row=4, col=1)
        fig.append_trace(go.Scatter(x=df.Datetime, y=df['upper'],line=dict(color='red', width=2),name='rsi',showlegend=False,legendgroup='4'), row=4, col=1)
        fig.append_trace(go.Scatter(x=df.Datetime, y=df['lower'],line=dict(color='green', width=2),name='rsi',showlegend=False,legendgroup='4'), row=4, col=1)
        fig.append_trace(go.Bar(x=df.Datetime, y=df['EWO'],marker_color=df['Color'],name='elliot oscillator',showlegend=False,legendgroup='5'),row=5, col=1)

        fig.update_layout(barmode="stack")

    #fig.add_bar(x=df.Datetime, y=df['Volume'], showlegend=False, marker_color='green',row=4, col=1,name='Volume')


        fig.update_layout(
               autosize=True,

               height=1200,
               legend=dict(
               x=0.03,
               y=0.97,
               #x=1,
               #y=0.2,
               traceorder="normal",
               font=dict(
               family="sans-serif",
               size=15,
               color="black"),
               bgcolor='rgba(0,0,0,0)'),
               plot_bgcolor='GhostWhite',
               paper_bgcolor='white',
               margin=dict(l=10, r=10, t=20, b=20)
            )

        fig.update_xaxes(
            rangeslider_visible=False,
            rangebreaks=[
            # NOTE: Below values are bound (not single values), ie. hide x to y
            dict(bounds=["sat", "mon"]),  # hide weekends, eg. hide sat to before mon
            dict(bounds=[16, 9.5], pattern="hour"),
            # dict(values=["2019-12-25", "2020-12-24"])  # hide holidays (Christmas and New Year's, etc)
            ],)
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightPink',tickfont=dict(size=20))
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightPink')
        fig.update_yaxes(title_text="stock price", title_font=dict(size=20),secondary_y=False,showgrid=True,tickfont=dict(size=20))
        fig.update_yaxes(title_text="W % R", title_font=dict(size=20),secondary_y=False,showgrid=True,tickfont=dict(size=20), row=2, col=1)
        fig.update_yaxes(title_text="KDJ", title_font=dict(size=20),secondary_y=False,showgrid=True,tickfont=dict(size=20), row=3, col=1)
        fig.update_yaxes(title_text="RSI", title_font=dict(size=20),secondary_y=False,showgrid=True,tickfont=dict(size=20), row=4, col=1)
        fig.update_yaxes(title_text="EWO", title_font=dict(size=20),secondary_y=False,showgrid=True,tickfont=dict(size=20), row=5, col=1)
        #fig.update_yaxes(title_text="stock price", title_font=dict(size=20),secondary_y=True,tickfont=dict(size=15))
        return fig
    return plot2(df)