import dash
from dash import dcc, html, Input, Output, no_update, ctx, callback
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.io as pio
import pandas as pd
import os
import plotly.io as pio

dash.register_page(__name__)

# Resultados

# Diccionario 
df = pd.read_csv(os.path.join(os.getcwd(),'khoka.csv'))
diccionario_ing_esp = dict(list(zip(df['All Metabolites'],df['Traduccion'])))
diccionario_esp_ing = dict(list(zip(df['Traduccion'],df['All Metabolites'])))
### Fin Diccionario

pagina_khoka = False
pagina_trux = True
pagina_coca = False
pagina_novo = False
pagina_ipadu = False

def treemap_layout():
    pie=[dcc.Dropdown(['All Metabolites','Primary Metabolites','Secondary Metabolites'],'All Metabolites',id='dropdown_treemap'),dcc.Graph(id="treemap",clear_on_unhover=True),dcc.Tooltip(id="graph-tooltip", direction='bottom')]
    return pie
    
def area(variety,label):
   
    if variety !=  'khoka':
         dropdown_area=os.listdir(os.path.join(os.getcwd(),'Varieties/'+variety))
         area_graph=[dbc.Row([dbc.Col(id="titulo_cromatografia",className="titulos_graficas titulo_metabolitos")]),dcc.Dropdown(dropdown_area,dropdown_area[0],id='dropdown_area'),dcc.Graph(id='area',clear_on_unhover=True),dcc.Tooltip(id="graph-tooltip", direction='bottom')]
    else:
        area_graph = [html.Div(id='area')]
    return area_graph

def description():
    description_block= [
        dbc.Row(html.Div("Cocaine",id='titulo_descripcion_compound',className="titulo_grafica_compound")),
        dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
        dbc.Row([dbc.Col(html.Img(id='compound_image',className="compound_images",src="../assets/structures/Cocaine.svg"),xs={"size":12},lg={"size":6},
                        ),
        dbc.Col(html.P('Se conoce también como benzoilmetilecgonina. Es un alcaloide tipo tropano y fuerte estimulante. \
                       La cocaína tiene conocidos efectos vasoconstrictores y analgesicos locales',
                       id="compound_description_text", className="text_description compound_descriptions"),xs={"size":12},lg={"size":6})])]
    return description_block

def classification():
    classification_graph=[dcc.Graph(id='classification_graph',clear_on_unhover=True)]
    return classification_graph

def general_tree():
    fig = pio.read_json(os.path.join(os.getcwd(),'assets','treemap_khoka_all_metabolites.json'))
    fig.update_layout(autosize=True,
         margin=dict(l=0, r=0, t=0, b=0, pad=0), # margenes de la gráfica
         paper_bgcolor="white", # color de fondo
    )
    return fig

# Define the navigation bar with the dropdown menu

portada =  dbc.Row(
        [
            html.Img(src="/assets/h_results.webp",style={"width": "100%",'marginTop':'3%','marginBottom':'3%'},className="center-image"),
        ]
                )

resultado = [dbc.Row([
    dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
    html.Div("RESULTS", className="body-title-green"),
    dbc.Row([dbc.Col([
    dbc.Container(
            [
            # CARACTERIZACION QUIMICA POR VARIEDADES
            dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
            dbc.Row("CHEMICAL CHARACTERIZATION BY VARIETY",className="results_title",id="caracterizacion"),
            dbc.Row(className="espaciado_48_esc espaciado_48_mov"),
            dbc.Row("Explore the chemical profile of each coca variety to learn about the metabolites they contain, which ones have biological activity, and visualize the chromatograms of each sample studied.",style={'textAlign':'center'}),
            dbc.Row(className="espaciado_48_esc espaciado_48_mov")],className="subcontainer-results"),
    dbc.Row([
        dbc.Col(html.Img(src="/assets/trux.png", height="150px"), width=2,style={"padding":0}),
        dbc.Col(html.Img(src="/assets/ipadu.png", height="150px"), width=2,style={"padding":0}),
        dbc.Col(html.Img(src="/assets/coca.png", id="h-coca", height="150px"), width=2,style={"padding":0}),
        dbc.Col(html.Img(src="/assets/novo.png", height="150px"), width=2,style={"padding":0})
    ], justify="center"),
    dbc.Row(style={'height':'1rem'}),
    dbc.Row([dbc.Col([
                        html.A(["Erythroxylum novogranatense ",html.Span(" var. ",className="var")," truxillense"],href=f"#all_compounds_treemap",
                        className="var_trux_text ",id="trux", n_clicks=0)],id="trux_box",className="var_trux_box",width=4),
                    
                    dbc.Col([  
                        html.A(["Erythroxylum coca ",html.Span("var. ",className="var")," ipadu"],href=f"#all_compounds_treemap",
                        className="var_ipadu_text", id="ipadu", n_clicks=0)],id="ipadu_box",className="var_ipadu_box",width=4),
               
                    dbc.Col([ 
                        html.A(["Erythroxylum coca ",html.Span("var. ",className="var")," coca"],href=f"#all_compounds_treemap",
                        className="var_coca_text", id="coca")],id="coca_box",className="var_coca_box",width=4),
                    dbc.Col([ 
                        html.A(["Erythroxylum novogranatense ",html.Span("var. ",className="var")," novogranatense"],href=f"#all_compounds_treemap",
                        className="var_novo_text", id="novo")],id="novo_box",className="var_novo_box",width=4),
                    dcc.Store(id='clicked-button', data=None)
                    ],className="gap-1",justify="center"), 
    dbc.Container([
            dbc.Row(className="espaciado_48_esc espaciado_48_mov"),
            dbc.Row("This graph shows all the metabolites found in this coca variety. You can select between primary and secondary metabolites, view their molecular structure, and learn more about them.",style={'textAlign':'center'}),
            dbc.Row(className="espaciado_48_esc espaciado_48_mov"),
            ],className="subcontainer-results"),
    dbc.Row(html.Div(html.Div(id='all_compounds_treemap',className="treemap"))),
    dbc.Row(className="espaciado_48_esc hide"),
    dbc.Row(className="espaciado_96_esc hide"),   
   
    dbc.Container([    
            # COMPUESTOS BIOACTIVOS
            dbc.Row(html.Div("BIOACTIVE COMPOUNDS", id="compuestos_bioactivos", className="results_title")),
            dbc.Row(className="espaciado_48_esc espaciado_48_mov"),
            html.Div("Learn about the compounds in this coca variety that have biological activity, meaning they may have physiological effects on humans."),
            ],className="subcontainer-results hide"),
    dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
    dbc.Row(html.Div(id='classification'),className="hide"),
    dbc.Row(className="espaciado_96_esc hide"),
    dbc.Container([ 
            # CROMATOGRAMA
            dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
            dbc.Row(html.Div("CHROMATOGRAM", id="cromatogramas", className="results_title")),
            dbc.Row(className="espaciado_48_esc espaciado_48_mov"),
            html.Div("This chart shows the results of the chromatographic readings of each analyzed extract. It allows you to visualize the data by coca variety and extract type. The retention time indicates the chemical nature of the substance: a short retention time suggests compounds with a fatty nature, while a longer retention time indicates compounds that dissolve in water, such as sugars or amino acids."),            
            ],className="subcontainer-results hide"),
    dbc.Row(className="espaciado_24_esc hide"),
    dbc.Row([dbc.Col(html.Div(id='area_compounds'),width={"size":12,"order":1})],className="hide")],xs={"size": 12, "order": 1},md={"size": 6, "order": 1}),
    
    dbc.Col([html.Div(id='compound_description',className="compound_description")],className="compound_description_box", 
            xs={"size": 12, "order": 2},md={"size": 6, "order": 2})]),
    ], className="container-results")]
    
# Define the layout
layout= [
            dbc.Col(
                portada,
                xs={"size": 12, "order": 2},  # Change order to 2 on extra small devices
                sm={"size": 12, "order": 2},  # Change order to 2 on small devices
                md={"size": 12, "order": 3},
                lg={"size": 12, "order": 3},
                xl={"size": 12, "order": 3},
                
            ),
            dbc.Col(
                resultado,
                xs={"size": 12, "order": 4},  # Change order to 2 on extra small devices
                sm={"size": 12, "order": 4},  # Change order to 2 on small devices
                md={"size": 12, "order": 4},
                lg={"size": 12, "order": 4},
                xl={"size": 12, "order": 4},
                
            )
   ]

@callback(
    Output('all_compounds_treemap', 'children'),
    Output('area_compounds','children'),
    Output('classification','children'),
    Output('compound_description','children'),
    Input('trux','n_clicks'),
    Input('coca','n_clicks'),
    Input('ipadu','n_clicks'),
    Input('novo','n_clicks'))

def display_click_data(n_clicks1,n_clicks2,n_clicks3,n_clicks4):
    global pagina_trux,pagina_coca,pagina_ipadu,pagina_novo,pagina_khoka
    fig_1 = treemap_layout()
    fig_2 = area('Truxillense','_2') # default area
    fig_3 = classification()
    fig_5 = description()

    pagina_trux = True

    if ctx.triggered_id == 'trux' :
        fig_1 = treemap_layout()
        fig_2 = area('Truxillense','_trux')
        fig_3 = classification()
        fig_5 = description()
        pagina_trux = True
        pagina_coca,pagina_ipadu,pagina_novo,pagina_khoka = False, False, False, False

    if ctx.triggered_id == 'coca' :
        fig_1 = treemap_layout()
        fig_2 = area('Coca','_coca')
        fig_3 = classification()
        fig_5 = description()
        pagina_coca = True
        pagina_trux,pagina_ipadu,pagina_novo,pagina_khoka = False, False, False, False
    
    if ctx.triggered_id == 'ipadu' :
        fig_1 = treemap_layout()
        fig_2 = area('Ipadu','_ipadu')
        fig_3 = classification()
        fig_5 = description()
        pagina_ipadu = True
        pagina_trux,pagina_coca,pagina_novo,pagina_khoka = False, False, False, False

    if ctx.triggered_id == 'novo' :
        fig_1 = treemap_layout()
        fig_2 = area('Novogranatense','_novo')
        fig_3 = classification()
        fig_5 = description()
        pagina_novo = True
        pagina_trux,pagina_ipadu,pagina_coca,pagina_khoka = False, False, False, False

    return fig_1, fig_2, fig_3, fig_5

@callback(
    Output('treemap', 'figure'),
    Input('dropdown_treemap', 'value'),
    Input('trux','n_clicks'),
    Input('coca','n_clicks'),
    Input('ipadu','n_clicks'),
    Input('novo','n_clicks'))

def treemap_graph(value,n_clicks1,n_clicks2,n_clicks3,n_clicks4):
    global pagina_trux,pagina_coca,pagina_ipadu,pagina_novo,pagina_khoka, diccionario_esp_ing  
    variety = pd.read_csv(os.path.join(os.getcwd(),'khoka.csv')) # cargar excel
    fila_cabecera = list(variety) # Generar una lista con las cabeceras
    color_palet = {'(?)':'white'}
    for k in fila_cabecera[4:]:
            opacidad = 1
            contador=1
            for i in [x for x in variety[k] if pd.isnull(x) == False and x != 'nan']:         
                if k == "Saturated":
                    clasificacion = [x for x in variety[k] if pd.isnull(x) == False and x != 'nan']
                    # opacidad =   0.7
                    #color_palet[i]='rgba(117,68,40,'+str(opacidad)+')'
                    color_palet["Saturated"]='rgba(134, 73, 117,'+str(opacidad)+')'
                    contador+=1
                if k == "Insaturated":
                    clasificacion = [x for x in variety[k] if pd.isnull(x) == False and x != 'nan']
                    # opacidad = 1Insaturated
                    #color_palet[i]='rgba(199, 119, 28,'+str(opacidad)+')'
                    color_palet["Insaturated"]='rgba(18, 9, 124, '+str(opacidad)+')'
                    contador+=1
                if k == "Acids":
                    clasificacion = [x for x in variety[k] if pd.isnull(x) == False and x != 'nan']
                    # opacidad = 1
                    #color_palet[i]='rgba(77, 189, 132,'+str(opacidad)+')'
                    color_palet['Acids']='rgba(0, 151, 131, '+str(opacidad)+')' 
                    contador+=1
                if k == "Bases":
                    clasificacion = [x for x in variety[k] if pd.isnull(x) == False and x != 'nan']
                    # opacidad = 1
                    #color_palet[i]='rgba(120, 51, 109,'+str(opacidad)+')'
                    color_palet['Bases']='rgba(36, 192, 187, '+str(opacidad)+')'
                    contador+=1
                if k == "Alcohols":
                    clasificacion = [x for x in variety[k] if pd.isnull(x) == False and x != 'nan']
                    # opacidad = 1
                    #color_palet[i]='rgba(244, 111, 54,'+str(opacidad)+')'
                    color_palet['Alcohols']='rgba(184, 80, 117, '+str(opacidad)+')'
                    contador+=1
                if k == "Alcohols":
                    clasificacion = [x for x in variety[k] if pd.isnull(x) == False and x != 'nan']
                    # opacidad = 1
                    #color_palet[i]= 'rgba(191, 59, 33,'+str(opacidad)+')'
                    color_palet['Alcohols']= 'rgba(87, 180, 110, '+str(opacidad)+')'
                    contador+=1
                if k == "Amides":
                    clasificacion = [x for x in variety[k] if pd.isnull(x) == False and x != 'nan']
                    # opacidad = 1
                    #color_palet[i]='rgba(224, 182, 23,'+str(opacidad)+')' 
                    color_palet['Amides']='rgba(0, 132, 183, '+str(opacidad)+')'
                    contador+=1
                if k == "Aldehydes":
                    clasificacion = [x for x in variety[k] if pd.isnull(x) == False and x != 'nan']
                    # opacidad = 1
                    #color_palet[i]= 'rgba(82, 154, 52,'+str(opacidad)+')'
                    color_palet['Aldehydes']= 'rgba(255, 66, 135, '+str(opacidad)+')'
                    contador+=1
                if k == "Carbohydrates":
                    clasificacion = [x for x in variety[k] if pd.isnull(x) == False and x != 'nan']
                    # opacidad = 1
                    #color_palet[i]='rgba(219, 67, 88,'+str(opacidad)+')'
                    color_palet['Carbohydrates']='rgba(89, 147, 152, '+str(opacidad)+')'
                    contador+=1
                if k == "Amino acids":
                    clasificacion = [x for x in variety[k] if pd.isnull(x) == False and x != 'nan']
                    # opacidad = 1
                    #color_palet[i]='rgba(102, 206, 245,'+str(opacidad)+')' 
                    color_palet["Amino acids"]='rgba(137, 147, 151, '+str(opacidad)+')' 
                    contador+=1
                if k == "Alkaloids":
                    clasificacion = [x for x in variety[k] if pd.isnull(x) == False and x != 'nan']
                    # opacidad = 1
                    #color_palet[i]='rgba(36, 74, 143,'+str(opacidad)+')'
                    color_palet["Alkaloids"]='rgba(89, 53, 140, '+str(opacidad)+')'
                    contador+=1

    if pagina_khoka == True:
        figura = '' # Conjunto de metabolitos
        lista = list(variety[value])
        lista = [x for x in lista if pd.isnull(x) == False and x != 'nan']
        compuestos = lista    # <-------------
        compuestos = [x for x in compuestos if pd.isnull(x) == False and x != 'nan']
        lista_final = []
        for compuesto in lista:
            for compuesto_variedad in compuestos:
                if str(compuesto_variedad) == str(compuesto):
                    lista_final.append(compuesto_variedad)

        # Crear diccionario para correlacionar a un compuesto con una clasificación
        diccionario_clasificacion = []
        clase = []
        variety_dc = pd.read_csv(os.path.join(os.getcwd(),'khoka.csv')) # cargar excel
        fila_cabecera = list(variety_dc) # Generar una lista con las cabeceras
        for k in fila_cabecera[5:]: #ir desde saturados hasta el final
            for i in [x for x in variety_dc[k] if pd.isnull(x) == False and x != 'nan']:
                for l in lista_final:
                    if l == i:
                            diccionario_clasificacion.append(l)
                            clase.append(k)
        
        if value == 'All Metabolites':
             figura = 'all_metabolites'
             area_cromatografia = pd.read_csv(os.path.join(os.getcwd(),'treemap','all_all_treemap.csv'))
        elif value == 'Primary Metabolites':
             figura = 'primary_metabolites'
             area_cromatografia = pd.read_csv(os.path.join(os.getcwd(),'treemap','all_p_treemap.csv'))
        elif value == 'Secondary Metabolites':
             figura = 'secondary_metabolites'
             area_cromatografia = pd.read_csv(os.path.join(os.getcwd(),'treemap','all_s_treemap.csv'))
        
    elif pagina_trux == True:
        figura = '' # Conjunto de metabolitos
        lista = list(variety[value])
        lista = [x for x in lista if pd.isnull(x) == False and x != 'nan']
        variedad = pd.read_csv(os.path.join(os.getcwd(),'variedades.csv'))
        compuestos = list(variedad['variedad_trux'])     # <-------------
        compuestos = [x for x in compuestos if pd.isnull(x) == False and x != 'nan']
        lista_final = []
        for compuesto in lista:
            for compuesto_variedad in compuestos:
                if str(compuesto_variedad) == str(compuesto):
                    lista_final.append(compuesto_variedad)

        # Crear diccionario para correlacionar a un compuesto con una clasificación
        diccionario_clasificacion = []
        clase = []
        variety_dc = pd.read_csv(os.path.join(os.getcwd(),'khoka.csv')) # cargar excel
        fila_cabecera = list(variety_dc) # Generar una lista con las cabeceras
        for k in fila_cabecera[5:]: #ir desde saturados hasta el final
            for i in [x for x in variety_dc[k] if pd.isnull(x) == False and x != 'nan']:
                for l in lista_final:
                    if l == i:
                            diccionario_clasificacion.append(l)
                            clase.append(k)
        
        if value == 'All Metabolites':
            figura = 'all_metabolites'
            area_cromatografia = pd.read_csv(os.path.join(os.getcwd(),'treemap','trux_all_treemap.csv'))
        elif value == 'Primary Metabolites':
            figura = 'primary_metabolites'
            area_cromatografia = pd.read_csv(os.path.join(os.getcwd(),'treemap','trux_p_treemap.csv'))
        elif value == 'Secondary Metabolites':
            figura = 'secondary_metabolites'
            area_cromatografia = pd.read_csv(os.path.join(os.getcwd(),'treemap','trux_s_treemap.csv'))
    
    elif pagina_novo == True:
        figura = '' # Conjunto de metabolitos
        lista = list(variety[value])
        lista = [x for x in lista if pd.isnull(x) == False and x != 'nan']
        variedad = pd.read_csv(os.path.join(os.getcwd(),'variedades.csv'))
        compuestos = list(variedad['variedad_novo'])     # <-------------
        compuestos = [x for x in compuestos if pd.isnull(x) == False and x != 'nan']
        lista_final = []
        for compuesto in lista:
            for compuesto_variedad in compuestos:
                if str(compuesto_variedad) == str(compuesto):
                    lista_final.append(compuesto_variedad)

        # Crear diccionario para correlacionar a un compuesto con una clasificación
        diccionario_clasificacion = []
        clase = []
        variety_dc = pd.read_csv(os.path.join(os.getcwd(),'khoka.csv')) # cargar excel
        fila_cabecera = list(variety_dc) # Generar una lista con las cabeceras
        for k in fila_cabecera[5:]: #ir desde saturados hasta el final
            for i in [x for x in variety_dc[k] if pd.isnull(x) == False and x != 'nan']:
                for l in lista_final:
                    if l == i:
                            diccionario_clasificacion.append(l)
                            clase.append(k)
        
        if value == 'All Metabolites':
             figura = 'all_metabolites'
             area_cromatografia = pd.read_csv(os.path.join(os.getcwd(),'treemap','novo_all_treemap.csv'))
        elif value == 'Primary Metabolites':
             figura = 'primary_metabolites'
             area_cromatografia = pd.read_csv(os.path.join(os.getcwd(),'treemap','novo_p_treemap.csv'))
        elif value == 'Secondary Metabolites':
             figura = 'secondary_metabolites'
             area_cromatografia = pd.read_csv(os.path.join(os.getcwd(),'treemap','novo_s_treemap.csv'))
        
    elif pagina_coca == True:
        figura = '' # Conjunto de metabolitos
        lista = list(variety[value])
        lista = [x for x in lista if pd.isnull(x) == False and x != 'nan']
        variedad = pd.read_csv(os.path.join(os.getcwd(),'variedades.csv'))
        compuestos = list(variedad['variedad_coca'])     # <-------------
        compuestos = [x for x in compuestos if pd.isnull(x) == False and x != 'nan']
        lista_final = []
        for compuesto in lista:
            for compuesto_variedad in compuestos:
                if str(compuesto_variedad) == str(compuesto):
                    lista_final.append(compuesto_variedad)

        # Crear diccionario para correlacionar a un compuesto con una clasificación
        diccionario_clasificacion = []
        clase = []
        variety_dc = pd.read_csv(os.path.join(os.getcwd(),'khoka.csv')) # cargar excel
        fila_cabecera = list(variety_dc) # Generar una lista con las cabeceras
        for k in fila_cabecera[5:]: #ir desde saturados hasta el final
            for i in [x for x in variety_dc[k] if pd.isnull(x) == False and x != 'nan']:
                for l in lista_final:
                    if l == i:
                            diccionario_clasificacion.append(l)
                            clase.append(k)
        
        if value == 'All Metabolites':
            figura = 'all_metabolites'
            area_cromatografia = pd.read_csv(os.path.join(os.getcwd(),'treemap','coca_all_treemap.csv'))
        elif value == 'Primary Metabolites':
            figura = 'primary_metabolites'
            area_cromatografia = pd.read_csv(os.path.join(os.getcwd(),'treemap','coca_p_treemap.csv'))
        elif value == 'Secondary Metabolites':
            figura = 'secondary_metabolites'
            area_cromatografia = pd.read_csv(os.path.join(os.getcwd(),'treemap','coca_s_treemap.csv'))

    elif pagina_ipadu == True:
        figura = '' # Conjunto de metabolitos
        lista = list(variety[value])
        lista = [x for x in lista if pd.isnull(x) == False and x != 'nan']
        variedad = pd.read_csv(os.path.join(os.getcwd(),'variedades.csv'))
        compuestos = list(variedad['variedad_ipadu'])     # <-------------
        compuestos = [x for x in compuestos if pd.isnull(x) == False and x != 'nan']
        lista_final = []
        for compuesto in lista:
            for compuesto_variedad in compuestos:
                if str(compuesto_variedad) == str(compuesto):
                    lista_final.append(compuesto_variedad)

        # Crear diccionario para correlacionar a un compuesto con una clasificación
        diccionario_clasificacion = []
        clase = []
        variety_dc = pd.read_csv(os.path.join(os.getcwd(),'khoka.csv')) # cargar excel
        fila_cabecera = list(variety_dc) # Generar una lista con las cabeceras
        for k in fila_cabecera[5:]: #ir desde saturados hasta el final
            for i in [x for x in variety_dc[k] if pd.isnull(x) == False and x != 'nan']:
                for l in lista_final:
                    if l == i:
                            diccionario_clasificacion.append(l)
                            clase.append(k)
        
        if value == 'All Metabolites':
             figura = 'all_metabolites'
             area_cromatografia = pd.read_csv(os.path.join(os.getcwd(),'treemap','ipadu_all_treemap.csv'))
        elif value == 'Primary Metabolites':
             figura = 'primary_metabolites'
             area_cromatografia = pd.read_csv(os.path.join(os.getcwd(),'treemap','ipadu_p_treemap.csv'))
        elif value == 'Secondary Metabolites':
             figura = 'secondary_metabolites'
             area_cromatografia = pd.read_csv(os.path.join(os.getcwd(),'treemap','ipadu_s_treemap.csv'))

    # lista final #
    # diccionario ingles español
    treemap_lista_final = []
    for d in diccionario_clasificacion:
        if d in diccionario_clasificacion:
            treemap_lista_final.append(diccionario_ing_esp[d])
    # diccionario fin
    fig = px.treemap(path=[clase,treemap_lista_final],values=area_cromatografia["porcentaje"],color=clase,color_discrete_map=color_palet) # Poner Data Aquí para fig 1
    
    fig.update_traces(textposition='middle center', textinfo='label')
    fig.update_layout(showlegend=False,clickmode="select")
    fig.update_traces(textfont_family="storm-italic",textfont_size=15)
    fig.update_traces(texttemplate= "%{label}: %{value:.2f} %")
    fig.update_traces(hovertemplate="%{label}: %{value:.2f} %")
    fig.update_layout(autosize=True,
         margin=dict(l=0, r=0, t=0, b=0, pad=0), # margenes de la gráfica
         paper_bgcolor="white", # color de fondo
    )
    
    ## SAVE JSON 
    """
    try:
        if pagina_khoka == True:
            pio.write_json(fig, os.path.join(os.getcwd(),'treemap''_khoka_'+figura+'.json'))
        elif pagina_trux == True:
            pio.write_json(fig, os.path.join(os.getcwd(),'treemap''_trux_'+figura+'.json'))
        elif pagina_novo == True:
            pio.write_json(fig, os.path.join(os.getcwd(),'treemap''_novo_'+figura+'.json'))
        elif pagina_coca == True:
            pio.write_json(fig, os.path.join(os.getcwd(),'treemap''_coca_'+figura+'.json'))
        elif pagina_ipadu == True:
            pio.write_json(fig, os.path.join(os.getcwd(),'treemap''_ipadu_'+figura+'.json'))
        
    except:
        pass
    """
    return fig

# RESULTADOS
@callback(
    Output('classification_graph', 'figure'),
    Input('trux', 'n_clicks'))

def classification_(n_clicks):
    global pagina_ipadu,pagina_novo,pagina_trux,pagina_coca
    sunburst = pd.read_csv(os.path.join(os.getcwd(),'bioactivos.csv'))
    fila_cabecera = list(sunburst)
    # Generador de paleta de colores
    variety = pd.read_csv(os.path.join(os.getcwd(),'khoka.csv')) # cargar excel
    fila_cabecera = list(variety) # Generar una lista con las cabeceras
    
    color_palet = {'(?)':"white"}
    for k in fila_cabecera[4:]:
            contador=1
            opacidad = 1        
            for i in [x for x in variety[k] if pd.isnull(x) == False and x != 'nan']:         
                if k == "Saturated":
                    clasificacion = [x for x in variety[k] if pd.isnull(x) == False and x != 'nan']
                    # opacidad =   0.7
                    #color_palet[i]='rgba(117,68,40,'+str(opacidad)+')'
                    color_palet["Saturated"]='rgba(134, 73, 117,'+str(opacidad)+')'
                    contador+=1
                if k == "Insaturated":
                    clasificacion = [x for x in variety[k] if pd.isnull(x) == False and x != 'nan']
                    # opacidad = 1Insaturated
                    #color_palet[i]='rgba(199, 119, 28,'+str(opacidad)+')'
                    color_palet["Insaturated"]='rgba(18, 9, 124, '+str(opacidad)+')'
                    contador+=1
                if k == "Acids":
                    clasificacion = [x for x in variety[k] if pd.isnull(x) == False and x != 'nan']
                    # opacidad = 1
                    #color_palet[i]='rgba(77, 189, 132,'+str(opacidad)+')'
                    color_palet['Acids']='rgba(0, 151, 131, '+str(opacidad)+')' 
                    contador+=1
                if k == "Bases":
                    clasificacion = [x for x in variety[k] if pd.isnull(x) == False and x != 'nan']
                    # opacidad = 1
                    #color_palet[i]='rgba(120, 51, 109,'+str(opacidad)+')'
                    color_palet['Bases']='rgba(36, 192, 187, '+str(opacidad)+')'
                    contador+=1
                if k == "Alcohols":
                    clasificacion = [x for x in variety[k] if pd.isnull(x) == False and x != 'nan']
                    # opacidad = 1
                    #color_palet[i]='rgba(244, 111, 54,'+str(opacidad)+')'
                    color_palet['Alcohols']='rgba(184, 80, 117, '+str(opacidad)+')'
                    contador+=1
                if k == "Alcohols":
                    clasificacion = [x for x in variety[k] if pd.isnull(x) == False and x != 'nan']
                    # opacidad = 1
                    #color_palet[i]= 'rgba(191, 59, 33,'+str(opacidad)+')'
                    color_palet['Alcohols']= 'rgba(87, 180, 110, '+str(opacidad)+')'
                    contador+=1
                if k == "Amides":
                    clasificacion = [x for x in variety[k] if pd.isnull(x) == False and x != 'nan']
                    # opacidad = 1
                    #color_palet[i]='rgba(224, 182, 23,'+str(opacidad)+')' 
                    color_palet['Amides']='rgba(0, 132, 183, '+str(opacidad)+')'
                    contador+=1
                if k == "Aldehydes":
                    clasificacion = [x for x in variety[k] if pd.isnull(x) == False and x != 'nan']
                    # opacidad = 1
                    #color_palet[i]= 'rgba(82, 154, 52,'+str(opacidad)+')'
                    color_palet['Aldehydes']= 'rgba(255, 66, 135, '+str(opacidad)+')'
                    contador+=1
                if k == "Carbohydrates":
                    clasificacion = [x for x in variety[k] if pd.isnull(x) == False and x != 'nan']
                    # opacidad = 1
                    #color_palet[i]='rgba(219, 67, 88,'+str(opacidad)+')'
                    color_palet['Carbohydrates']='rgba(89, 147, 152, '+str(opacidad)+')'
                    contador+=1
                if k == "Amino acids":
                    clasificacion = [x for x in variety[k] if pd.isnull(x) == False and x != 'nan']
                    # opacidad = 1
                    #color_palet[i]='rgba(102, 206, 245,'+str(opacidad)+')' 
                    color_palet["Amino acids"]='rgba(137, 147, 151, '+str(opacidad)+')' 
                    contador+=1
                if k == "Alkaloids":
                    clasificacion = [x for x in variety[k] if pd.isnull(x) == False and x != 'nan']
                    # opacidad = 1
                    #color_palet[i]='rgba(36, 74, 143,'+str(opacidad)+')'
                    color_palet["Alkaloids"]='rgba(89, 53, 140, '+str(opacidad)+')'
                    contador+=1
    if pagina_khoka:
        figura = 'khoka'
        porcentajes = {}
        porcentaje = pd.read_csv(os.path.join(os.getcwd(),'treemap','all_all_treemap.csv'))
        for k in sunburst['compuesto']:
            contador = 0
            for i in porcentaje['compuesto']:
                if k == i:
                    porcentajes[k]=(list(porcentaje['porcentaje'])[contador])
                contador+=1
    elif pagina_trux:
        figura = 'trux'
        porcentajes = {}
        porcentaje = pd.read_csv(os.path.join(os.getcwd(),'treemap','trux_all_treemap.csv'))
        for k in sunburst['compuesto']:
            contador = 0
            presente = False
            for i in porcentaje['compuesto']:
                if k == i:
                    porcentajes[k]=(list(porcentaje['porcentaje'])[contador])
                    presente = True
                contador+=1
            if presente == False:
               porcentajes[k]=(0) 

    elif pagina_ipadu:
        figura = 'ipadu'
        porcentajes = {}
        porcentaje = pd.read_csv(os.path.join(os.getcwd(),'treemap','ipadu_all_treemap.csv'))
        for k in sunburst['compuesto']:
            contador = 0
            presente = False
            for i in porcentaje['compuesto']:
                if k == i:
                    porcentajes[k]=(list(porcentaje['porcentaje'])[contador])
                    presente = True
                contador+=1
            if presente == False:
               porcentajes[k]=(0)      

    elif pagina_coca:
        figura = 'coca'
        porcentajes = {}
        porcentaje = pd.read_csv(os.path.join(os.getcwd(),'treemap','coca_all_treemap.csv'))
        for k in sunburst['compuesto']:
            contador = 0
            presente = False
            for i in porcentaje['compuesto']:
                if k == i:
                    porcentajes[k]=(list(porcentaje['porcentaje'])[contador])
                    presente = True
                contador+=1
            if presente == False:
               porcentajes[k]=(0)
    
    elif pagina_novo:
        figura = 'novo'
        porcentajes = {}
        porcentaje = pd.read_csv(os.path.join(os.getcwd(),'treemap','novo_all_treemap.csv'))
        for k in sunburst['compuesto']:
            contador = 0
            presente = False
            for i in porcentaje['compuesto']:
                if k == i:
                    porcentajes[k]=(list(porcentaje['porcentaje'])[contador])
                    presente = True
                contador+=1
            if presente == False:
               porcentajes[k]=(0)   
    # Diccionario ingles español
    clasificacion_lista_final = []
    for d in sunburst['compuesto']:
        clasificacion_lista_final.append(diccionario_ing_esp[d])
    clasificacion_lista_final = [x for x in clasificacion_lista_final if pd.isnull(x) == False and x != 'nan']
    # Fin diccionario
    fig = px.sunburst(sunburst,path=['clase',clasificacion_lista_final],values=list(dict.values(porcentajes)),color='clase',color_discrete_map=color_palet,branchvalues="remainder",maxdepth=2) # Poner Data Aquí para fig 2
    fig.update_traces(textfont_family="storm-italic",textfont_size=15)
    fig.update_traces(hovertemplate="%{label}")
    fig.update_traces(texttemplate= "%{label}: %{value:.2f} %")
    fig.update_layout(autosize=True,
         margin=dict(l=0, r=0, t=0, b=0, pad=0), # margenes de la gráfica
         paper_bgcolor="white", # color de fondo
    )

        ## SAVE JSON 
    """
    try:
        if pagina_khoka == True:
     
            pio.write_json(fig, os.path.join(os.getcwd(),'class_'+figura+'.json'))
        elif pagina_trux == True:
      
            pio.write_json(fig, os.path.join(os.getcwd(),'class_'+figura+'.json'))
        elif pagina_novo == True:
       
            pio.write_json(fig, os.path.join(os.getcwd(),'class_'+figura+'.json'))
        elif pagina_coca== True:
  
            pio.write_json(fig, os.path.join(os.getcwd(),'class_'+figura+'.json'))
        elif pagina_ipadu== True:

            pio.write_json(fig, os.path.join(os.getcwd(),'class_'+figura+'.json'))
        
    except:
        pass
    """
    return fig

@callback(
    Output('area', 'figure'),
    Input('dropdown_area', 'value'),
    Input('trux', 'n_clicks'),
    Input('coca', 'n_clicks'),
    Input('ipadu', 'n_clicks'),
    Input('novo', 'n_clicks'))

def area_(value,n_clicks1,n_clicks2,n_clicks3,n_clicks4):
    global pagina_ipadu,pagina_novo,pagina_trux,pagina_coca

    if pagina_trux == True :
        ruta = os.path.join(os.getcwd(),'Varieties','Truxillense')
        pagina_coca,pagina_ipadu,pagina_novo = False, False, False
    elif pagina_coca == True :
        ruta = os.path.join(os.getcwd(),'Varieties','Coca')
        pagina_trux,pagina_ipadu,pagina_novo = False, False, False
    elif pagina_novo == True :
        ruta = os.path.join(os.getcwd(),'Varieties','Novogranatense')
        pagina_trux,pagina_ipadu,pagina_coca = False, False, False
    elif pagina_ipadu == True :
        ruta = os.path.join(os.getcwd(),'Varieties','Ipadu')
        pagina_trux,pagina_coca,pagina_novo = False, False, False
   
    variety_area = pd.read_csv(os.path.join(ruta,value)) #'Varieties/Truxillense/'+value)) # Modificar archivos agregar area relativa
    rows= []
    for i in range(0,len(variety_area)):
        rows.append(i)
    # Diccionario
    cromato_lista_final = []
    for d in variety_area["Compound Name"]:
        cromato_lista_final.append(diccionario_ing_esp[d])
    cromato_lista_final = [x for x in cromato_lista_final if pd.isnull(x) == False and x != 'nan']
    # fin
    fig = px.scatter(variety_area, x=rows,y="RT",
                    size="Sample.1", hover_name=cromato_lista_final, color="RT",
                    labels={"x": "Numero de Compuesto", "RT": "Tiempo de Retención"})
    #fig.update_layout(title_text='Relative Area Compound (%)',title_y=0.95,title_x=0.5,plot_bgcolor='rgba(0,0,0,0)')
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)')
    #legend
    fig.update_layout(showlegend=False)

    #x axis
    fig.update_xaxes(visible=False)

    #y axis    
    fig.update_yaxes(visible=False)
    return  fig

@callback(
    Output("titulo_descripcion_compound",'children'),
    Output('compound_image','src'),
    Output("graph-tooltip", "show"),
    Output("graph-tooltip", "bbox"),
    Output("graph-tooltip", "children"),
    Output("graph-tooltip", "direction"),
    Input("treemap", "hoverData"),
    Input("classification_graph", "hoverData"),
    Input("area","hoverData")
   )

def display_hover(hoverData1,hoverData2,hoverData3):
    global diccionario_esp_ing
    
    if hoverData1 is not None:
        print(hoverData1["points"][0]['label'])
        hover_data1 = diccionario_esp_ing[hoverData1["points"][0]['label']]
        bbox = hoverData1["points"][0]["bbox"]
        if str(hover_data1[-1]) == " ":
            compound = str(hover_data1[:-1]).replace(' ','_')
        else:
            compound = str(hover_data1).replace(' ','_')
        y = hoverData1['points'][0]['bbox']['y0']
        direction = "bottom" if y > 1.5 else "top"
        im_url = "/assets/structures/"+ compound +'.svg'
    
        children = [
            html.Img(
                src=im_url,
                style={"width": "100px"},
            ),
        ]
        
        molecule_image="/assets/structures/"+ compound +'.svg'
        return hoverData1["points"][0]['label'], molecule_image, None, None, None, None

        
    elif hoverData2 is not None:
       
        hover_data2 = diccionario_esp_ing[hoverData2["points"][0]['label']]
        bbox = hoverData2["points"][0]["bbox"]
        if str(hover_data2[-1]) == " ":
            compound = str(hover_data2[:-1]).replace(' ','_')
        else:
            compound = str(hover_data2).replace(' ','_')
        y = hoverData2['points'][0]['bbox']['y0']
        direction = "bottom" if y > 1.5 else "top"
        im_url = "/assets/structures/"+ compound +'.svg'
    
        children = [
            html.Img(
                src=im_url,
                style={"width": "10rem"},
            ),
        ]
        
        molecule_image="/assets/structures/"+ compound +'.svg'

        return hoverData2["points"][0]['label'], molecule_image, None, None, None, None
        
    elif hoverData3 is not None:
        #hover_data3 = hoverData3["points"]
        bbox = hoverData3["points"][0]["bbox"]
        hover_data3=diccionario_esp_ing[hoverData3['points'][0]['hovertext']]
        if str(hover_data3[-1]) == " ":
            compound = str(hover_data3[:-1].replace(' ','_'))
        else:
            compound = str(hover_data3.replace(' ','_'))
        y = hoverData3['points'][0]['bbox']['y0']
        direction = "bottom" if y > 1.5 else "top"
        im_url = "/assets/structures/"+ compound +'.svg'
    
        children = [

            html.Img(
                src=im_url,
                style={"width": "200px"},
            ),
            
        ]
        
        molecule_image="/assets/structures/"+ compound +'.svg'
        
        return hoverData3["points"][0]['hovertext'], molecule_image,True, bbox, children, direction

@callback(
    Output('compound_description_text','children'),
    Input("titulo_descripcion_compound",'children'),
    Input("treemap", "hoverData")
   )
   

def texto_descriptivo(children,hoverData1):
    
    variety = pd.read_csv(os.path.join(os.getcwd(),'khoka.csv'))
    variety_metabolitos_secundarios = list(variety['Secondary Metabolites'])
    variety_metabolitos_secundarios = [x for x in  variety_metabolitos_secundarios if pd.isnull(x) == False and x != 'nan']
    relacion_metabolito_texto_s =  dict(list(zip(variety['Secondary Metabolites'], variety['Description Secondary Metabolites'])))
    
    variety_metabolitos_primarios = list(variety['Primary Metabolites'])
    variety_metabolitos_primarios = [x for x in  variety_metabolitos_primarios if pd.isnull(x) == False and x != 'nan']
    relacion_metabolito_texto_p =  dict(list(zip(variety['Primary Metabolites'], variety['Description Primary Metabolites'])))
    
    # cambio español ingles
    children = diccionario_esp_ing[children]

    if children in variety_metabolitos_secundarios:
        texto_metabolito = relacion_metabolito_texto_s[children]
    else:
        texto_metabolito = relacion_metabolito_texto_p[children]

    #if hoverData1['points'][0]['label'] == "Acids" :
    #    texto_metabolito = "ESTE TEXTO SE DEBE MOSTRAR"
    return texto_metabolito

@callback(
    [Output('trux_box', 'style'),
     Output('ipadu_box', 'style'),
     Output('coca_box', 'style'),
     Output('novo_box', 'style')],
    [Input('trux', 'n_clicks'),
     Input('ipadu', 'n_clicks'),
     Input('coca', 'n_clicks'),
     Input('novo', 'n_clicks')]
)

def update_button_styles(n_clicks1,n_clicks2,n_clicks3,n_clicks4):

    # Default styles for all buttons (gray background)
    style_inactive = {"background-color": "gray", "height": "3rem",
                         "display": "flex", "alignItems": "center", "justifyContent": "center"}
    style_active = {"background-color": "#455e3c", "height": "3rem",
                         "display": "flex", "alignItems": "center", "justifyContent": "center"}
    # Determine which button was clicked most recently
    ctx = dash.callback_context

    if not ctx.triggered:
        return style_active, style_inactive, style_inactive, style_inactive
    else:
        clicked_button = ctx.triggered[0]['prop_id'].split('.')[0]
        
    # Update styles based on which button was clicked
    if clicked_button == 'trux':

        style_active = {"background-color": "#455e3c", "height": "3rem",
                         "display": "flex", "alignItems": "center", "justifyContent": "center"}
        return style_active, style_inactive, style_inactive, style_inactive
    
    elif clicked_button == 'ipadu':
        style_active = {"background-color": "#737634", "height": "3rem",
                         "display": "flex", "alignItems": "center", "justifyContent": "center"}

        return style_inactive, style_active, style_inactive, style_inactive
    
    elif clicked_button == 'coca':
        style_active = {"background-color": "#678849", "height": "3rem",
                    "display": "flex", "alignItems": "center", "justifyContent": "center"}
        return style_inactive, style_inactive, style_active, style_inactive
    elif clicked_button == 'novo':
        style_active = {"background-color": "#95a823", "height": "3rem",
                    "display": "flex", "alignItems": "center", "justifyContent": "center"}

        return style_inactive, style_inactive, style_inactive, style_active


