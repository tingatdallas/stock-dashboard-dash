import dash
from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from datetime import datetime
import pandas as pd # pandas==1.4.2
import yfinance as yf #yfinance==0.1.70
from yahoo_fin.stock_info import * #yahoo_fin==0.8.9.1
import pandas_ta as ta #pandas_ta==0.3.14b
import plotly.graph_objects as go #plotly==5.7.0
import plotly.express as px
from plotly.subplots import make_subplots
from dash.dependencies import Input, Output
# gunicorn==20.1.0

from pages.page1 import layout_1_single,layout_2_Vs_spy,layout_7_eps,layout_8_notes
from pages.page2 import layout_daily,layout_notes_daily
from pages.page1 import page1



app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}],suppress_callback_exceptions=True)
server = app.server

navbar = dbc.Navbar(

    children=[
        dbc.Button("Sidebar", outline=False, color="warning", id="btn_sidebar"),
        dbc.NavItem(dbc.NavLink("Long-term", href="/page-1")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Short-term investment", href="/page-2"),
                dbc.DropdownMenuItem("Contact", href="/page-3"),
           ],
            nav=False,
            in_navbar=True,
            label="More",
        ),
    ],
    #brand="Stock Dashboard",
    #brand_style={'font-size':'2rem','color':'lightblue'},
    #brand_href="/page-1",
    color="dark",
    dark=True,
    style={'height':'4rem','justify-content':'flex-end','padding-right':'1rem'},
    #sticky='top'


    #toggle1
)


# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    #'font-size':'1rem',
    "position": "fixed",
    "top": 80.5,
    "left": 0,
    "bottom": 0,
    "width": "18rem",
    "height": "100%",
    "z-index": 1,
    "overflow-x": "hidden",
    "transition": "all 0.5s",
    "padding": "1.5rem 1rem",
    "background-color": "#f8f9fa",
}

SIDEBAR_HIDEN = {
    "position": "fixed",
    "top": 62.5,
    "left": "-16rem",
    "bottom": 0,
    "width": "15rem",
    "height": "100%",
    "z-index": 1,
    "overflow-x": "hidden",
    "transition": "all 0.5s",
    "padding": "0rem 0rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "transition": "margin-left .5s",
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

CONTENT_STYLE1 = {
    "transition": "margin-left .5s",
    "margin-left": "0rem",
    "margin-right": "0rem",
    "padding": "2rem 1rem",
    "background-color": '#f8f9fa',
}

sidebar = html.Div(
    [
        html.H4("In investing, what is comfortable is rarely profitable"),
        html.Hr(),
        #html.P(
        #    "A simple sidebar layout with navigation links", className="lead"
        #),
        dbc.Nav(
            [
                dbc.NavLink("Long-term investment", href="/page-1", id="page-1-link",style={'font-size':'1.2rem'}),
                dbc.NavLink("Short-term investment", href="/page-2", id="page-2-link",style={'font-size':'1.2rem'}),
                dbc.NavLink("Contact", href="/page-3", id="page-3-link",style={'font-size':'1.2rem'}),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    id="sidebar",
    style=SIDEBAR_STYLE,
)

content = html.Div(

    id="page-content",
    style=CONTENT_STYLE)

app.layout = html.Div(
    [
        dcc.Store(id='side_click'),
        dcc.Location(id="url"),
        navbar,
        sidebar,
        content,
    ],
)


@app.callback(
    [
        Output("sidebar", "style"),
        Output("page-content", "style"),
        Output("side_click", "data"),
    ],

    [Input("btn_sidebar", "n_clicks")],
    [
        State("side_click", "data"),
    ]
)
def toggle_sidebar(n, nclick):
    if n:
        if nclick == "SHOW":
            sidebar_style = SIDEBAR_STYLE
            content_style = CONTENT_STYLE
            cur_nclick = "HIDDEN"
        else:
            sidebar_style = SIDEBAR_HIDEN
            content_style = CONTENT_STYLE1
            cur_nclick = "SHOW"
    else:
        sidebar_style = SIDEBAR_HIDEN
        content_style = CONTENT_STYLE1
        cur_nclick = 'SHOW'

    return sidebar_style, content_style, cur_nclick

# this callback uses the current pathname to set the active state of the
# corresponding nav link to true, allowing users to tell see page they are on
@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 4)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        # Treat page 1 as the homepage / index
        return True, False, False
    return [pathname == f"/page-{i}" for i in range(1, 4)]


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/page-1"]:
        return page1.page1 #dbc.Row([layout_single.layout_single,layout_compared_SPY.layout_compared_spy]),dbc.Row([layout_eps.layout_eps,layout_notes.layout_notes,]), #html.P("This is the content of page 1!")
    elif pathname == "/page-2":
        return dbc.Row([layout_daily.layout_daily,layout_notes_daily.layout_notes_daily])
    elif pathname == "/page-3":
        return html.P("The dashboard keeps updating! Contact at: sutingatchicago@gmail.com")
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == "__main__":
    app.run_server(debug=True, port=8086)

