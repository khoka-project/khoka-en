import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import os

app = dash.Dash(__name__, use_pages=True , external_stylesheets=[dbc.themes.BOOTSTRAP],
         meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
    ])

server = app.server

header = dbc.Row([
            dbc.Col([],width=1),
            dbc.Col([
            html.Img(src=os.path.join(os.getcwd(),"/assets/header.webp"),className="header-image large-image", style={'width':'100%'}),
            html.Img(src=os.path.join("/assets/header_m.webp"),className="header-image small-image_header", style={'width':'100%'}),

            ],width=9),
            dbc.Col([
            html.A(html.Button(children=html.Img(src='/assets/ES-PC.jpg',style={'width': '48px', 'height': '48px'}), id='bt-language', className='boton-language large-image'), href='https://khoka-sp-gzy5.onrender.com', target='_blank'),
            html.A(html.Button(children=html.Img(src='/assets/ES-MOVIL.jpg',style={'width': '36px', 'height': '36px'}), id='bt-language1', className='boton-language_m header-image small-image_header'), href='https://khoka-sp-gzy5.onrender.com', target='_blank'),

            ],width=1),
            dbc.Col([],width=1),
        ],style={'align-items':'center'})

nav= dbc.Nav(
                    [
                        
                        dbc.DropdownMenu(
                            [
                                dbc.DropdownMenuItem("What is Metabolomics?", header=False,
                                                     href=f"#intro_metabol_1",external_link=True,style={"fontFamily":"basker_120","fontSize":"1rem","line-height":"1"}),
                                dbc.DropdownMenuItem("Plant Metabolism", 
                                                     href=f"#intro_metabol_2",external_link=True,style={"fontFamily":"basker_120","fontSize":"1rem","line-height":"1"}),
                                dbc.DropdownMenuItem("Metabolites", 
                                                     href=f"#intro_metabol_3",external_link=True,style={"fontFamily":"basker_120","fontSize":"0.8rem"}),
                                dbc.DropdownMenuItem("Primary Metabolism", 
                                                     href=f"#intro_metabol_p",external_link=True,style={"fontFamily":"basker_120","fontSize":"0.8rem"}),
                                dbc.DropdownMenuItem("Secondary Metabolism",
                                                     href=f"#intro_metabol_s",external_link=True,style={"fontFamily":"basker_120","fontSize":"0.8rem","line-height":"1"}),
                                dbc.DropdownMenuItem("Metabolomics in Coca Research", 
                                                     href=f"#intro_metabol_4",external_link=True,style={"fontFamily":"basker_120","fontSize":"1rem","line-height":"1"}),
                            ],
                            nav=True,
                            in_navbar=True,
                            label=dbc.NavLink("INTRODUCTION", href="/",style={'padding':0,'marginLeft':'1rem'}),
                        ),
                        dbc.DropdownMenu(
                            [
                                dbc.DropdownMenuItem("Step 1: Extraction of Compounds from the Leaves", header=False,
                                                     style={"fontFamily":"basker_120","fontSize":"1rem","line-height":"1"}, href=f"#experimento_paso_1",external_link=True),
                                dbc.DropdownMenuItem("Basic Principles of Chemical Extraction", href=f"#pbe",external_link=True,style={"fontFamily":"basker_120","fontSize":"0.8rem","line-height":"1"}),
                                dbc.DropdownMenuItem("Simple Liquid-Liquid Extraction", href=f"#extraccion_liquido",external_link=True,style={"fontFamily":"basker_120","fontSize":"0.8rem","line-height":"1"}),
                                dbc.DropdownMenuItem("Solvent Extraction Characteristics", href=f"#car_sol",external_link=True,style={"fontFamily":"basker_120","fontSize":"0.8rem","line-height":"1"}),
                                dbc.DropdownMenuItem("Step 2: Compound Analysis: Gas Chromatography", href=f"#experimento_paso_2",external_link=True,style={"fontFamily":"basker_120","fontSize":"1rem","line-height":"1"}),
                                dbc.DropdownMenuItem("What is Chromatography?", href="#que_es_cro",external_link=True,style={"fontFamily":"basker_120","fontSize":"0.8rem","line-height":"1"}),
                            ],
                            nav=True,
                            in_navbar=True,
                            label=dbc.NavLink("EXPERIMENT", href="/khoka-experiment", style={'padding':0}),
                            
                            
                        ),
                        dbc.DropdownMenu(
                            [

                                dbc.DropdownMenuItem("Chemical characterization by variety",style={"fontFamily":"basker_120","fontSize":"0.75rem","line-height":"1"}, href=f"#caracterizacion",external_link=True),
                                dbc.DropdownMenuItem("Bioactive compounds",style={"fontFamily":"basker_120","fontSize":"0.75rem","line-height":"1"},className="hide", href=f"#compuestos_bioactivos",external_link=True),
                                dbc.DropdownMenuItem("Chromatograms",style={"fontFamily":"basker_120","fontSize":"0.75rem","line-height":"1"},className="hide", href=f"#cromatogramas",external_link=True)

                            ],
                            nav=True,
                            in_navbar=True,
                            label=dbc.NavLink("RESULTS", href="/khoka-results",style={'padding':0}),    
                        ),
                        dbc.DropdownMenu(
                            [
                                dbc.DropdownMenuItem("Gas Chromatography", header=False, href=f"#meto_croma",external_link=True,style={"fontFamily":"basker_120","fontSize":"0.8rem"}),
                                dbc.DropdownMenuItem("Retention Time", href=f"#meto_tiempo",external_link=True,style={"fontFamily":"basker_120","fontSize":"0.8rem"})

                            ],
                            nav=True,
                            in_navbar=True,
                            label=dbc.NavLink("METHODOLOGY", href="/khoka_methodology",style={'padding':0}),    
                        ),
                        dbc.DropdownMenu(
                            [
                                dbc.DropdownMenuItem("METABOLITS MAP", header=False,
                                    href=f"#bt-descarga",external_link=True,style={"fontFamily":"basker_120","fontSize":"1rem","line-height":"1"}),
                                dbc.DropdownMenuItem("The Study of Metabolites in Coca Leaves", header=False,
                                    href=f"#conclu_estudio",external_link=True,style={"fontFamily":"basker_120","fontSize":"1rem","line-height":"1"}),
                                dbc.DropdownMenuItem("Results of the Chemical Analysis of the Four Varieties", header=False,
                                    href=f"#conclu_resultados",external_link=True,style={"fontFamily":"basker_120","fontSize":"1rem","line-height":"1"}),
                                dbc.DropdownMenuItem("Conclusions from the Study of Metabolites in Coca Varieties", header=False,
                                    href=f"#conclu_variedades",external_link=True,style={"fontFamily":"basker_120","fontSize":"1rem","line-height":"1"}),
                                dbc.DropdownMenuItem("Alkaloids", 
                                    href=f"#conclu_var-1",external_link=True,style={"fontFamily":"basker_120","fontSize":"0.8rem","line-height":"1"}),
                                dbc.DropdownMenuItem("Phenolic Acids", 
                                    href=f"#conclu_var-2",external_link=True,style={"fontFamily":"basker_120","fontSize":"0.8rem","line-height":"1"}),
                                dbc.DropdownMenuItem(["Comparison of Compounds Reported in Literature vs. Those Present in the ", html.Span("Khoka Project", className="italic-text"), " Garden."], header=False,
                                    href=f"#conclu_compara",external_link=True,style={"fontFamily":"basker_120","fontSize":"1rem","line-height":"1"}),
                                dbc.DropdownMenuItem("BIBLIOGRAPHIC REFERENCES", header=False,
                                    href=f"#conclu_referen",external_link=True,style={"fontFamily":"basker_120","fontSize":"1rem","line-height":"1"}),
                            ],
                            class_name='conclusions',
                            nav=True,
                            in_navbar=True,
                            label=dbc.NavLink("CONCLUSIONS", href="/khoka_conclusions",style={'padding':0}),    
                        ),  
                        dbc.DropdownMenu(
                            class_name='glosary',
                            nav=True,
                            in_navbar=True,
                            label=dbc.NavLink("GLOSSARY", href="/khoka_glossary",style={'padding':0}),    
                        ),
                        dbc.DropdownMenu(
                            class_name='bibliography',
                            nav=True,
                            in_navbar=True,
                            label=dbc.NavLink("BIBLIOGRAPHY", href="/khoka_bibliography",style={'padding':0,'marginRight':'1.2rem'}),    
                        ),
                    ],
                    style={'fontFamily': 'clutadella_light','backgroundColor': '#9abf99'},
                    justified=True,
                    pills=True,
                    class_name='custom-nav',
                    id='top'
            )

app.layout = html.Div([
            dbc.Row([
            dbc.Col(
                header,
                xs={"size": 12, "order": 1},
                sm={"size": 12, "order": 1},
                md={"size": 12, "order": 1},
                lg={"size": 12, "order": 1},
                xl={"size": 12, "order": 1},
                style={'justify':'center'},
                
            ),
            dbc.Col(
                nav,
                xs={"size": 12, "order": 3},
                sm={"size": 12, "order": 3},
                md={"size": 12, "order": 2},
                lg={"size": 12, "order": 2},
                xl={"size": 12, "order": 2},
                style={'paddingRight':'0rem','paddingLeft':'0rem'}
            ),
             ]),
            dash.page_container
            ])

# Define the layout of the page
# for page in dash.page_registry.values():
#     print('name:', page['name'])
#     print('url:', page['path'])

PORT = 8050
HOST = '0.0.0.0'

if __name__ == "__main__":
    app.run_server(
        debug=True,
        host= HOST,
        port = PORT)
