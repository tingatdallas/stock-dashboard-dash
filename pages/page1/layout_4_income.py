from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash import Input, Output, callback
from dash.dependencies import Input, Output

from yahoo_fin.stock_info import *

from datetime import datetime
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from yahoo_fin.stock_info import *


style_input={'width':'14rem','height':'2rem','border':'1px solid',
             'border-radius':'10px','border-color':'green','background':'#F5F5F5'}

tabs_styles = {
    'height': '4rem',
    'display':'flex',
    'flex-direction': 'column',
    'justify-content': 'stretch',
    'flex-wrap': 'wrap',
    'border':'1px solid SeaShell',
    'margin-bottom':'0.5rem'
}
tab_style = {
    'border':'0.5px solid SeaShell',
    'borderBottom': '1px solid GhostWhite',
    'border-radius':'0.1rem',
    'padding': '2.5px',
    'font-size':'6.5px',
    'overflow':'hidden',
    'backgroundColor': 'yellow',
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'background': '#119DFF',
    'position': 'relative',
    'font-size':'6px',
    'font-weight':'bold',
    'margin':'0px',
    'overflow':'visible',
    'color': 'purple',
    #'width':'20px',
    'padding': '4px'
}

dict_item={'researchDevelopment':'R & D',
            'effectOfAccountingCharges':'Effect Of AccountingCharges',
            'incomeBeforeTax':'Income Before Tax',
            'minorityInterest':'Minority Interest',
            'netIncome':'Net Income',
             'sellingGeneralAdministrative':'Selling General Administrative',
             'grossProfit':'Gross Profit',
             'ebit':'Ebit',
             'operatingIncome':'Operating Income',
            'otherOperatingExpenses':'Other Operating Expenses',
             'interestExpense':'Interest Expense',
              'extraordinaryItems':'Extraordinary Items',
           'nonRecurring':'non Recurring','otherItems':'other Items',
           'incomeTaxExpense':'Income Tax Expense', 'totalRevenue':'Total Revenue', 'totalOperatingExpenses':'Total Operating Expenses',
           'costOfRevenue':'Cost Of Revenue', 'totalOtherIncomeExpenseNet':'Total Other Income Expense Net', 'discontinuedOperations':'Discontinued Operations',
           'netIncomeFromContinuingOps': 'net Income From Continuing Ops', 'netIncomeApplicableToCommonShares':'net Income Applicable To Common Shares'
           }

layout_income=dbc.Col([
    html.H5("The Yearly Income Statement",
            className='text-center md-4'),

    html.Div([
    dcc.Tabs(id='tabs-income', value='netIncome', children=[
        dcc.Tab(label='Net Income', value='netIncome', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Total Revenue', value='totalRevenue', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Operating Income', value='operatingIncome', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Effect Of AccountingCharges', value='effectOfAccountingCharges', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Income Before Tax', value='incomeBeforeTax', style=tab_style, selected_style=tab_selected_style),
        #dcc.Tab(label='Minority Interest', value='minorityInterest', style=tab_style, selected_style=tab_selected_style),

        #dcc.Tab(label='Selling General Administrative', value='sellingGeneralAdministrative', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Gross Profit', value='grossProfit', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Ebit', value='ebit', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='R & D', value='researchDevelopment', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Other Operating Expenses', value='otherOperatingExpenses', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Interest Expense', value='interestExpense', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Extraordinary Items', value='extraordinaryItems', style=tab_style, selected_style=tab_selected_style),
        #dcc.Tab(label= 'non Recurring',value='nonRecurring', style=tab_style, selected_style=tab_selected_style),
        #dcc.Tab(label='other Items',value='otherItems', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Income Tax Expense',value='incomeTaxExpense', style=tab_style, selected_style=tab_selected_style),

        dcc.Tab(label='Total Operating Expenses', value='totalOperatingExpenses', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='cost Of Revenue', value='costOfRevenue', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='total Other Income Expense Net', value='totalOtherIncomeExpenseNet', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Discontinued Operations', value='discontinuedOperations', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Net Income From Continuing Ops', value='netIncomeFromContinuingOps', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Net Income Applicable To Common Shares', value='netIncomeApplicableToCommonShares', style=tab_style, selected_style=tab_selected_style),
           ], style=tabs_styles)], style=tabs_styles),
        dcc.Graph(id='display-graphic3', figure={})#,style={'margin-top':'2rem'}
], xs=12, sm=12, md=12, lg=3, xl=3,style={'display':'flex','flex-direction':'column','border':'6px solid SeaShell','padding-top':'0.5rem','background-color':'lightblue'}
)


@callback(
    Output('display-graphic3', 'figure'),
    Input('intermediate-value', 'data'),
    Input('tabs-income','value')
)
def update_graph(input1,input2):
    df=get_financials(input1, yearly = True, quarterly = True)['yearly_income_statement'].T
    #df=df.reset_index()
    #print(df.columns)
    fig=px.bar(x=df.index,y=df[input2], text_auto=True)

    fig.update_layout(
        autosize=True,
        height=400,
        plot_bgcolor='lightblue', #'GhostWhite',
        paper_bgcolor='lightblue', #'white',
        margin=dict(l=20, r=20, t=20, b=20)
    )
    fig.update_xaxes(title_text='',title_font=dict(size=20),tickfont=dict(size=20))
    fig.update_yaxes(title_text=f'{dict_item[input2]} ({input1.upper()})', title_font=dict(size=20),tickfont=dict(size=20))

    return fig



    #for key, value in dict_item.items():
    #   print(f'dcc.Tab(label="{value}", value="{key}",style=tab_style, selected_style=tab_selected_style),')
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


            
            '''