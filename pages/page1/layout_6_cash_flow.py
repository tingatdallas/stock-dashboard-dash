from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash import Input, Output, callback
from dash.dependencies import Input, Output
from datetime import datetime
import pandas as pd
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

dict_item= \
    {
'investments':'Investments',
'changeToLiabilities':'Change To Liabilities',
'totalCashflowsFromInvestingActivities':"Total Cashflows From Investing Activities",
'netBorrowings': 'Net Borrowings',
'totalCashFromFinancingActivities':'Total Cash From Financing Activities',
'changeToOperatingActivities': 'Change To Operating Activities',
'issuanceOfStock':'Issuance Of Stock',
'netIncome':'Net Income',
'changeInCash':'Change In Cash',
#'effectOfExchangeRate':'Effect Of Exchange Rate',
'totalCashFromOperatingActivities':'Total Cash From Operating Activities',
#'depreciation':'Depreciation',
'otherCashflowsFromInvestingActivities':'Other Cashflows From Investing Activities',
'changeToInventory':'Change To Inventory',
'changeToAccountReceivables':'Change To Account Receivables',
'otherCashflowsFromFinancingActivities':'Other Cash flows From Financing Activities',
'changeToNetincome':'Change To Netincome',
'capitalExpenditures': 'Capital Expenditures'
    }


layout_cashflow=dbc.Col([
    html.H5("The Yearly Cash Flow",
            className='text-center md-4'),
    html.Div([
    dcc.Tabs(id='tabs-cash', value='changeInCash', children=[
        dcc.Tab(label="Total Cash flows From Investing Activities", value="totalCashflowsFromInvestingActivities",style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label="Total Cash From Financing Activities", value="totalCashFromFinancingActivities",style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label="Change To Operating Activities", value="changeToOperatingActivities",style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label="Net Income", value="netIncome",style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label="Issuance Of Stock", value="issuanceOfStock",style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label="Change In Cash", value="changeInCash",style=tab_style, selected_style=tab_selected_style),
        #dcc.Tab(label="Effect Of Exchange Rate", value="effectOfExchangeRate",style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label="Total Cash From Operating Activities", value="totalCashFromOperatingActivities",style=tab_style, selected_style=tab_selected_style),
        #dcc.Tab(label="Depreciation", value="depreciation",style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label="Other Cashflows From Investing Activities", value="otherCashflowsFromInvestingActivities",style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label="Change To Inventory", value="changeToInventory",style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label="Change To Account Receivables", value="changeToAccountReceivables",style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label="Other Cash flows From Financing Activities", value="otherCashflowsFromFinancingActivities",style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label="Change To Netincome", value="changeToNetincome",style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label="Capital Expenditures", value="capitalExpenditures",style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label="Investments", value="investments",style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label="Net Borrowings", value="netBorrowings",style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label="Change To Liabilities", value="changeToLiabilities",style=tab_style, selected_style=tab_selected_style),
    ], style=tabs_styles)], style=tabs_styles),
    dcc.Graph(id='display-graphic5', figure={})#,style={'margin-top':'2rem'}
],xs=12, sm=12, md=12, lg=3, xl=3,style={'border':'6px solid SeaShell','border-right':'0px solid SeaShell','padding-top':'0.5rem','background-color':'lightblue'}
)


@callback(
    Output('display-graphic5', 'figure'),
    Input('intermediate-value', 'data'),
    Input('tabs-cash','value')
)
def update_graph(input1,input2):
    df=get_financials(input1, yearly = True, quarterly = True)['yearly_cash_flow'].T
    fig=px.bar(x=df.index,y=df[input2], text_auto=True)
    #fig.update_traces(width=200)

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

'''
dcc.Tab(label='Intangible Assets', value='intangibleAssets',style=tab_style, selected_style=tab_selected_style),
dcc.Tab(label='Capital Surplus', value='capitalSurplus', style=tab_style, selected_style=tab_selected_style),
dcc.Tab(label='Total Liab', value='totalLiab',style=tab_style, selected_style=tab_selected_style),
dcc.Tab(label='Total Stock holder Equity', value='totalStockholderEquity',style=tab_style, selected_style=tab_selected_style),
dcc.Tab(label='Minority Interest', value='minorityInterest', style=tab_style, selected_style=tab_selected_style),
dcc.Tab(label='Other Current Liab', value='otherCurrentLiab',style=tab_style, selected_style=tab_selected_style),
dcc.Tab(label='Total Assets', value='totalAssets', style=tab_style, selected_style=tab_selected_style),
dcc.Tab(label='Common Stock', value='commonStock',
dcc.Tab(label='Other Current Assets', value='otherCurrentAssets', style=tab_style, selected_style=tab_selected_style),
dcc.Tab(label='Retained Earnings', value='retainedEarnings',style=tab_style, selected_style=tab_selected_style),
dcc.Tab(label='Other Liab', value='otherLiab',style=tab_style, selected_style=tab_selected_style),
dcc.Tab(label=Good Will', value='goodWill',
dcc.Tab(label='Treasury Stock', value='treasuryStock',style=tab_style, selected_style=tab_selected_style),
dcc.Tab(label='Other Assets', value='otherAssets',style=tab_style, selected_style=tab_selected_style),
dcc.Tab(label='Cash', value='cash',style=tab_style, selected_style=tab_selected_style),
dcc.Tab(label='Total Current Liabilities', value='totalCurrentLiabilities', style=tab_style, selected_style=tab_selected_style),
dcc.Tab(label='Short Long-Term Debt', value='shortLongTermDebt',style=tab_style, selected_style=tab_selected_style),
dcc.Tab(label='Other Stock holder Equity', value='otherStockholderEquity',style=tab_style, selected_style=tab_selected_style),
dcc.Tab(label='Property Plant Equipment', value='propertyPlantEquipment',style=tab_style, selected_style=tab_selected_style),
dcc.Tab(label='Total Current Assets', value='totalCurrentAssets', style=tab_style, selected_style=tab_selected_style),
dcc.Tab(label='Net Tangible Assets', value='netTangibleAssets', style=tab_style, selected_style=tab_selected_style),
dcc.Tab(label='Short Term Investments', value='shortTermInvestments',style=tab_style, selected_style=tab_selected_style),
dcc.Tab(label='Net Receivables', value='netReceivables', style=tab_style, selected_style=tab_selected_style),
dcc.Tab(label='Long Term Debt', value='longTermDebt', style=tab_style, selected_style=tab_selected_style),
dcc.Tab(label='Inventory', value='inventory',style=tab_style, selected_style=tab_selected_style),
dcc.Tab(label='Accounts Payable', value='accountsPayable',style=tab_style, selected_style=tab_selected_style),
dcc.Tab(label='Long Term Investments', value='longTermInvestments'style=tab_style, selected_style=tab_selected_style),
'''