import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import os

dash.register_page(__name__,path='/khoka_conclusions')

# Define the navigation bar with the dropdown menu

portada =  dbc.Row(
        [
            html.Img(src="/assets/h_conclu.webp",style={"width": "100%",'marginTop':'3%','marginBottom':'3   %'},className="center-image"),
        ]
                )

conclusiones = dbc.Container(
    dbc.Row([
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Div("CONCLUSIONES", className="body-title-green"), 
                dbc.Row(className="espaciado_48_esc espaciado_48_mov"),
               html.Div(["1.-"]),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["2.-"]),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                
            ],
            className="container-text"
        ))

# Definir los tooltips
tooltips = []
# solvente
for i in range(1,6):
       tooltips.append(
              dbc.Tooltip("También llamado solvente, un disolvente es una sustancia, generalmente líquida, que puede disolver otras sustancias sin alterarlas químicamente para formar una solución.", 
                    target="solvente_{0}".format(str(i)), className="custom-tooltip"))




# Define the layout
layout =    [ dbc.Col(
                portada,
                xs={"size": 12, "order": 2},  # Change order to 2 on extra small devices
                sm={"size": 12, "order": 2},  # Change order to 2 on small devices
                md={"size": 12, "order": 3},
                lg={"size": 12, "order": 3},
                xl={"size": 12, "order": 3},
                style={'paddingRight':'0rem','paddingLeft':'0rem'}
                
            ),
            dbc.Col(
                conclusiones,
                xs={"size": 12, "order": 4},  # Change order to 2 on extra small devices
                sm={"size": 12, "order": 4},  # Change order to 2 on small devices
                md={"size": 12, "order": 4},
                lg={"size": 12, "order": 4},
                xl={"size": 12, "order": 4},
                style={'paddingRight':'0rem','paddingLeft':'0rem'}
            ),
            *tooltips
        ]


