from dash import html, dcc
import dash_bootstrap_components as dbc
from dash import Input, Output, callback
from dash.dependencies import Input, Output


from datetime import datetime
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots



style_input={'width':'14rem','height':'2rem','border':'1px solid',
                'border-radius':'10px','border-color':'green','background':'#F5F5F5'}

style_dropdown1={'width':'12rem','height':'2rem','border':'5px dash',
                'border-radius':'10px','border-color':'green','background':'#7FFFD4'}

style_dropdown2={'width':'12rem','height':'2rem','border':'5px dash',
                'border-radius':'10px','border-color':'green','background':'#AFEEEE'}


layout_single=dbc.Col([

           html.H5("Stock Price & Return",
                       className='text-center md-4'),

            html.Div([
            dbc.Label('Choose Period: ',className='text-center success mb-3'),
            dcc.Dropdown(
                id='period',
                options=[
                {'label':'1y','value':'1y'},
                {'label':'5y','value':'5y'},
                {'label':'10y','value':'10y'},
                {'label':'max','value':'max'},
                {'label':'ytd','value':'ytd'},
                ],
                value='1y',placeholder='period',className='text-primary mb-4',
                style=style_dropdown1,
            ),],style={'display': 'flex','justify-content':'center','gap':'1rem'}),

            html.Div([
            dbc.Label('Choose Interval: ',className='text-center success mb-3'),
            dcc.Dropdown(
                id='interval',
                options=[
                {'label':'1d','value':'1d'},
                {'label':'1wk','value':'1wk'},
                ],
                value='1d',placeholder='interval',className='text-primary mb-4',
                style=style_dropdown2,
            ),],style={'display': 'flex','justify-content':'center','gap':'0.75rem'}),

            dcc.Graph(id='display-graphic1', figure={})
        ],# width={'size':5, 'offset':1, 'order':1},
            xs=12, sm=12, md=12, lg=3, xl=3,style={'border':'6px solid SeaShell','padding-top':'0.5rem','background-color':'lightblue',}
        )


@callback(
    Output('display-graphic1', 'figure'),
    Input('intermediate-value', 'data'),
    Input('period','value'),
    Input('interval','value'),
)

def update_graph(input1,input2,input3): # Plot candlestick price

    def add_ema_vwap(stock_ticker,periods,intervals):# add ema, vwamp. Parameters:stock ticker,interval
        df=yf.download(tickers=stock_ticker,period=periods,interval=intervals)

        df.reset_index(inplace=True)
        df.rename(columns={'Date':'Datetime'},inplace=True)
        df['Return']=100*(df['Close']-df['Close'].iloc[0])/df['Close'].iloc[0]
        return df

    df=add_ema_vwap(stock_ticker=input1,periods=input2,intervals=input3)



    def plot2(df):
        fig = make_subplots(specs=[[{"secondary_y": True}]])


        fig.add_trace(go.Scatter(x=df.Datetime, y=df['Close'],line=dict(color='green', width=2),name=input1.upper()),secondary_y=True)
        fig.add_trace(go.Scatter(x=df.Datetime, y=df['Return'],line=dict(color='green', width=2),showlegend=False),secondary_y=False)


        fig.update_layout(
               autosize=True,
               height=450,
               legend=dict(
               x=0.03,
               y=0.97,
               traceorder="normal",
               font=dict(
               family="sans-serif",
               size=15,
               color="black"),
               bgcolor='rgba(0,0,0,0)'),
               plot_bgcolor='lightblue', #'GhostWhite',
               paper_bgcolor='lightblue', #'white',
               margin=dict(l=20, r=10, t=20, b=20)
            )


        fig.update_xaxes(
            rangeslider_visible=False,
            rangebreaks=[
            # NOTE: Below values are bound (not single values), ie. hide x to y
            dict(bounds=["sat", "mon"]),  # hide weekends, eg. hide sat to before mon
            # dict(values=["2019-12-25", "2020-12-24"])  # hide holidays (Christmas and New Year's, etc)
            ],)
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightPink',tickfont=dict(size=20))
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightPink')
        fig.update_yaxes(title_text="return (%)", title_font=dict(size=20),secondary_y=False,showgrid=False,tickfont=dict(size=20))
        fig.update_yaxes(title_text="stock price", title_font=dict(size=20),secondary_y=True,tickfont=dict(size=20))
        return fig
    return plot2(df)



'''         html.Div([
        
           dbc.Label('Enter Ticker:',className='text-center mb-3'),
           dcc.Input(id='ticker',
              placeholder='Enter ticker like tsla, aapl',
              value='tsla',className='text-center text-primary md-4'
              ,style=style_input)]
              ,style={'display': 'flex','justify-content':'center','gap':'2.3rem'})
'''