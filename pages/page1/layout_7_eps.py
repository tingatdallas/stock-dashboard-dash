from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash import Input, Output, callback
from dash.dependencies import Input, Output
from datetime import datetime
import pandas as pd
import numpy as np
import plotly.express as px
from yahoo_fin.stock_info import *


style_input={'width':'14rem','height':'2rem','border':'1px solid',
                'border-radius':'10px','border-color':'green','background':'#F5F5F5'}

tabs_styles = {
    'height': '2rem',
    'margin-bottom':'1rem'
}
tab_style = {
    'border':'0.5px solid SeaShell',
    'border-radius':'0.1rem',
    'borderBottom': '1px solid GhostWhite',
    'padding': '2.5px',
    'font-size':'1rem',
    'overflow':'hidden',
    'fontWeight': None,
    'backgroundColor': 'lightblue',

}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'font-size':'1rem',
    'overflow':'visible',
    'color': 'white',
    'padding': '4px'
}

layout_eps=dbc.Col([
    html.H5("The Quarterly EPS",
                        className='text-center md-4'),
    html.Div([
    dcc.Tabs(id='tabs-eps', value='5', children=[
        dcc.Tab(label='2 years', value='2', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='5 years', value='5', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='10 years', value='10', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='max', value='max', style=tab_style, selected_style=tab_selected_style),
    ])], style=tabs_styles),

    dcc.Graph(id='display-graphic6', figure={})
    ],# width={'size':5, 'offset':1, 'order':1},
            xs=12, sm=12, md=12, lg=3, xl=3,style={'border':'6px solid SeaShell','padding-top':'0.5rem',
                                                   'background-color':'lightblue'}
    )


@callback(
    Output('display-graphic6', 'figure'),
    Input('intermediate-value', 'data'),
    Input('tabs-eps','value'),
)

def update_graph1(input1,input2): # Plot candlestick price
    df=get_earnings_history(input1)
    eps=[]
    for i in df:
       eps.append({'date':i['startdatetime'],'eps':i['epsactual']})
    df1=pd.DataFrame.from_records(eps)
    df1.dropna(axis=0,inplace=True)
    if input2=='max':
        fig=px.bar(x=df1['date'],y=df1['eps'])
    else:
        input3=int(input2)
        fig=px.bar(x=df1['date'][:input3*4],y=df1['eps'][:input3*4])

    fig.update_layout(
        autosize=True,
        height=400,
        plot_bgcolor='lightblue', #'GhostWhite',
        paper_bgcolor='lightblue', #'white',
        margin=dict(l=20, r=20, t=20, b=20)
    )

    fig.update_xaxes(title_text='',title_font=dict(size=20),tickfont=dict(size=20))
    fig.update_yaxes(title_text=f'EPS ({input1.upper()})', title_font=dict(size=20),tickfont=dict(size=20))

    return fig


    # def add_ema_vwap(stock_ticker,periods,intervals):# add ema, vwamp. Parameters:stock ticker,interval
    #     df=yf.download(tickers=stock_ticker,period=periods,interval=intervals)

    #     df.reset_index(inplace=True)
    #     df.rename(columns={'Date':'Datetime'},inplace=True)
    #     df['Return']=100*(df['Close']-df['Close'].iloc[0])/df['Close'].iloc[0]
    #     return df

    # df=add_ema_vwap(stock_ticker=input1,periods=input2,intervals=input3)



    # def plot2(df):
    #     fig = make_subplots(specs=[[{"secondary_y": True}]])


    #     fig.add_trace(go.Scatter(x=df.Datetime, y=df['Close'],line=dict(color='green', width=2),name=input1.upper()),secondary_y=True)
    #     fig.add_trace(go.Scatter(x=df.Datetime, y=df['Return'],line=dict(color='green', width=2),showlegend=False),secondary_y=False)


    #     fig.update_layout(
    #            autosize=True,
    #            legend=dict(
    #            x=0.03,
    #            y=0.97,
    #            traceorder="normal",
    #            font=dict(
    #            family="sans-serif",
    #            size=12,
    #            color="black"),
    #            bgcolor='rgba(0,0,0,0)',
    #         )
    #         )

    #     fig.update_xaxes(
    #         rangeslider_visible=False,
    #         rangebreaks=[
    #         # NOTE: Below values are bound (not single values), ie. hide x to y
    #         dict(bounds=["sat", "mon"]),  # hide weekends, eg. hide sat to before mon
    #         # dict(values=["2019-12-25", "2020-12-24"])  # hide holidays (Christmas and New Year's, etc)
    #         ],)
    #     fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightPink',tickfont=dict(size=15))
    #     fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightPink')
    #     fig.update_yaxes(title_text="return (%)", title_font=dict(size=20),secondary_y=False,showgrid=False,tickfont=dict(size=15))
    #     fig.update_yaxes(title_text="stcok price", title_font=dict(size=20),secondary_y=True,tickfont=dict(size=15))
    #     return fig
    # return plot2(df)
'''            
            html.Div([
                
                   dbc.Label('Enter Ticker:',className='text-center mb-3 bold'),
                   dcc.Input(id='ticker3',
                      placeholder='Enter ticker like tsla, aapl',
                      value='tsla',className='text-center text-primary md-4'
                      ,style=style_input)]
                      ,style={'display': 'flex','justify-content':'center','gap':'2.3rem'},
                
            ),
                        html.Div([
            dbc.Label('Choose Period: ',className='text-center success mb-3'),
            dcc.Dropdown(
                id='period3',
                options=[
                {'label':'2y','value':2},
                {'label':'5y','value':5},
                {'label':'10y','value':10},
                {'label':'max','value':'max'},
                ],
                value=5,placeholder='2y',className='text-primary mb-4',
                style=style_dropdown1,
            ),],style={'display': 'flex','justify-content':'center','gap':'1rem'}),
            '''