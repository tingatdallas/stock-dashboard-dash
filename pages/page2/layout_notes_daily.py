from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash import Input, Output, callback
from dash.dependencies import Input, Output

from yahoo_fin.stock_info import *

from datetime import datetime
import pandas as pd
import yfinance as yf
import pandas_ta as ta
#import stock_pandas as spd
#import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots


text1="""There is a basic assumption for long-term investment. That is the U.S economy is keeping innovating and expanding over the long run.
      The history seems to show that this is the case. The soundness of economy is determined by a lot of other factors such as stability of U.S political system,
      science, technology, geopolitics and so on. In addition to factors aforementioned, the monetary policies set by
      Federal Reserve also have a huge effect on stock markets, especially in short and middle-term by controlling the supply of money, thus the liquidity.
      Beside overall market, the price of individual stock is also affected by the earning report, management change, etc. All these factors together control
      the supply and demand of stocks, which ultimately determines the stock prices. People use the technical indicators to
      gain insight into the supply and demand of the stocks, trying to forecast price movement in short and middle-term. 
      An informed investor takes advantage of the fluctuation and volatility (like just what is happening right now) to buy a potential good company's stock
      at a discount or simply make short-term gains. The indicators on the left charts clearly demonstrate their correlation with stock price.
      """


layout_notes_daily = dbc.Col([
            html.H3("Notes", className='text-center md-3'),
            html.P(text1, style={'font-size':'1.4rem','text-align':'justify'}),
            html.P('Copyright © 2022 Ting Su. All Rights Reserved.')
        ],# width={'size':5, 'offset':1, 'order':1},
        xs=12, sm=12, md=12, lg=6, xl=6,style={'border':'6px solid SeaShell','padding-top':'0.5rem'}
        )

