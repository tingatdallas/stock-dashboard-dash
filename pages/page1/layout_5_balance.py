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

dict_item=\
{
'intangibleAssets':'intangibleAssets',
'capitalSurplus':'Capital Surplus',
'totalLiab':'Total Liab',
#'totalStockholderEquity':'Total Stock holder Equity',
#'minorityInterest':'Minority Interest',
#'otherCurrentLiab':'Other Current Liab',
'totalAssets':'Total Assets',
#'commonStock':'Common Stock',
#'otherCurrentAssets':'Other Current Assets',
'retainedEarnings':'Retained Earnings',
#'otherLiab':'Other Liab',
#'Good Will':'goodWill',
#'treasuryStock':'Treasury Stock',
'otherAssets':'otherAssets',
'cash':'Cash',
'totalCurrentLiabilities':'Total Current Liabilities',
'shortLongTermDebt':'Short Long-Term Debt',
#'otherStockholderEquity':'Other Stock holder Equity',
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

layout_balance=dbc.Col([
    html.H5("The Yearly Balance Sheet",
            className='text-center md-4'),
    html.Div([
    dcc.Tabs(id='tabs-balance', value='cash', children=[
        dcc.Tab(label="Cash", value="cash",style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label="Total Current Assets", value="totalCurrentAssets",style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label="Net Tangible Assets", value="netTangibleAssets",style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label="intangible Assets", value="intangibleAssets",style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label="Capital Surplus", value="capitalSurplus",style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label="Total Liab", value="totalLiab",style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label="Total Stock holder Equity", value="totalStockholderEquity",style=tab_style, selected_style=tab_selected_style),
        #dcc.Tab(label="Minority Interest", value="minorityInterest",style=tab_style, selected_style=tab_selected_style),
        #dcc.Tab(label="Other Current Liab", value="otherCurrentLiab",style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label="Total Assets", value="totalAssets",style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label="Common Stock", value="commonStock",style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label="Other Current Assets", value="otherCurrentAssets",style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label="Retained Earnings", value="retainedEarnings",style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label="Other Liab", value="otherLiab",style=tab_style, selected_style=tab_selected_style),
        #dcc.Tab(label="goodWill", value="Good Will",style=tab_style, selected_style=tab_selected_style),
        #dcc.Tab(label="Treasury Stock", value="treasuryStock",style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label="other Assets", value="otherAssets",style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label="Total Current Liabilities", value="totalCurrentLiabilities",style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label="Short Long-Term Debt", value="shortLongTermDebt",style=tab_style, selected_style=tab_selected_style),
        #dcc.Tab(label="Other Stock holder Equity", value="otherStockholderEquity",style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label="Property Plant Equipment", value="propertyPlantEquipment",style=tab_style, selected_style=tab_selected_style),


        dcc.Tab(label="Short Term Investments", value="shortTermInvestments",style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label="Net Receivables", value="netReceivables",style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label="Long Term Debt", value="longTermDebt",style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label="Inventory", value="inventory",style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label="Accounts Payable", value="accountsPayable",style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label="Long Term Investments", value="longTermInvestments",style=tab_style, selected_style=tab_selected_style),
    ], style=tabs_styles)], style=tabs_styles),
    dcc.Graph(id='display-graphic44', figure={})#,style={'margin-top':'2rem'}
],xs=12, sm=12, md=12, lg=3, xl=3
    ,style={'border':'6px solid SeaShell','border-right':'0px solid SeaShell','padding-top':'0.5rem','background-color':'lightblue'}
)

@callback(
    Output('display-graphic44', 'figure'),
    Input('intermediate-value', 'data'),
    Input('tabs-balance','value')
)
def update_graph(input1,input2):
    df=get_financials(input1, yearly = True, quarterly = True)['yearly_balance_sheet'].T
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

