from dash import Dash, html, dcc
import dash_bootstrap_components as dbc


text1="""This dashboard illustrates the performance of individual stock Vs benchmark SPY ETF and its relationship with earning per share (EPS).
Over the long run, the stock market is one of the best places to put your money to work.
History shows that holding stocks for long time could be a huge win if the businesses of the corresponding companies keep growing and expanding
for a long period of time, such as Nike, Apple, Microsoft, Amazon, Google and Tesla. One of key metrics of the businesses is EPS.
EPS is a company's net profit divided by the number of outstanding shares.
It indicates how much money a company makes for each share of its stock and is a widely used metric for measuring corporate value.
Generally, it is advisable to invest in a company that has disruptive businesses, with potential of generating positive EPS
in a sustainable way. For details regarding fundamentals, check out the bar graphs."""


layout_notes = dbc.Col([
            html.H5("Notes", className='text-center md-3'),
            html.P(text1, style={'font-size':'0.95rem','text-align':'justify'}),
            html.P('Copyright © 2022 Ting Su. All Rights Reserved.')
        ],# width={'size':5, 'offset':1, 'order':1},
        xs=12, sm=12, md=12, lg=3, xl=3,style={'border':'6px solid SeaShell','padding-top':'0.2rem'}
        )

