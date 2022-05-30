import dash
import pandas as pd
from dash import Dash, html, dcc,callback
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc


from pages.page1 import layout_1_single,layout_2_Vs_spy,layout_7_eps,layout_8_notes,layout_3_table,layout_5_balance,layout_4_income,layout_6_cash_flow


style_input={'width':'14rem','height':'2rem','border':'2px solid',
             'border-radius':'10px','border-color':'green','background':'#F5F5F5'}
page1=html.Div([
    dbc.Label('Enter Ticker',className='text-center',style={'display': 'flex','justify-content':'center','font-size':'1.3rem'}),
    html.Div([
    dcc.Input(id='ticker7',
              placeholder='Enter ticker like tsla, aapl',
              value='tsla',className='text-center text-primary md-4'
              ,style=style_input)]
    ,style={'display': 'flex','justify-content':'center','gap':'2.3rem','margin-bottom':'10px'},
    ),
    dcc.Store(id='intermediate-value',data=None,storage_type='local'),

dbc.Row([layout_1_single.layout_single, layout_2_Vs_spy.layout_compared_spy, layout_3_table.table1, layout_8_notes.layout_notes],
        ),
dbc.Row([layout_4_income.layout_income, layout_5_balance.layout_balance, layout_6_cash_flow.layout_cashflow,layout_7_eps.layout_eps],
        ),
dbc.Row([],
     )] #,
    #style={'background-color': 'SeaShell','margin-right':'5rem','margin-left':'5rem'}
)

@callback(Output('intermediate-value', 'data'), Input('ticker7', 'value'))
def clean_data(value):
    # some expensive data processing step
    #cleaned_df = slow_processing_step(value)

    # more generally, this line would be
    # json.dumps(cleaned_df)
    return value



