import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import os

dash.register_page(__name__,path='/khoka_methodology')

# Define the navigation bar with the dropdown menu

portada =  dbc.Row(
        [
            html.Img(src="/assets/h_meto_1.webp",style={"width": "100%",'marginTop':'3%','marginBottom':'3   %'},className="center-image"),
        ]
                )

metodologia = dbc.Container(
    dbc.Row([
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Div("METHODOLOGY", className="body-title-green"), 
                dbc.Row(className="espaciado_48_esc espaciado_48_mov"),
               html.Div(["In the Khoka Project garden, located in Medellín, Colombia, leaves from two species of ", html.Span("Erythroxylum", className="italic-text"), " were collected and dried, covering four distinct varieties: E. ", html.Span("coca", className="italic-text"), " var. coca, E. ", html.Span("coca", className="italic-text"), " var. ", html.Span("ipadu", className="italic-text"), ", E. ", html.Span("novogranatense", className="italic-text"), " var. ", html.Span("novogranatense", className="italic-text"), " y E. ", html.Span("novogranatense", className="italic-text"), " var. ", html.Span("truxillense", className="italic-text"), ". From each variety, 100 grams of dry leaves were weighed."]),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Using the Soxhlet technique*, three types of extracts were prepared with 300 mL of ", html.Span("solvents", id="solvente_1",className="underlined-text"), " of different polarities: ethanol, dichloromethane, and hexane. These extracts were made in triplicate and later concentrated by reduced-pressure distillation using a Biobase RE100-pro rotary evaporator."]),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["The concentrated extracts were stored in amber bottles and sent to the MetCore laboratory at Universidad de los Andes for analysis. There, the extracts were processed and stored at -80°C. The analyses were performed using a gas chromatograph coupled with a mass spectrometer, with a triple quadrupole detector from the Agilent brand, MS-QTOF 6545 model."]),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Img(src="/assets/h_meto_2.webp",style={"width": "100%"},className="center-image large-image"),
                html.Img(src="/assets/v_meto_2.webp",style={"width": "100%"},className="center-image small-image"),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Div("Gas Chromatography",className="body-title-2",id="meto_croma"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Gas chromatography is a reference technique for separating and analyzing volatile compounds and is widely used in determining gases, liquids, and solids. For solid analysis, the samples usually need to be dissolved in a volatile ", html.Span("solvent", id="solvente_2",className="underlined-text"), ". It is suitable for analyzing organic and inorganic compounds whose molecular weights range between 2 and 1000 daltons**."]),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["This methodology is one of the most commonly employed worldwide. For example, up to 400 compounds can be separated from a single coffee sample using a capillary column. Various types of detectors can be used with this method, with the flame ionization detector being the most common. This detector can identify concentrations as low as 50 parts per billion of organic compounds, with a standard deviation of 5%, according to McNair & Miller (1997)."]),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Div("Retention Time",className="body-title-2",id="meto_tiempo"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["In both liquid and gas chromatography, retention time is defined as the interval that elapses from the sample injection into the equipment until the detector registers the maximum response. This parameter is crucial and is commonly used for identifying compounds in an analytical mixture."]),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Div(["_______________"]),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["* ", html.Span("Técnica de extracción Soxhlet", className="italic-text"), ": es un método de separación que utiliza un disolvente líquido para extraer componentes de interés de una muestra sólida. Es ampliamente empleada para determinar el contenido graso en diversas muestras. El extractor Soxhlet, hecho de vidrio, incluye un condensador acoplado a una chaqueta que facilita el ingreso y la salida de agua."], className="body-footer"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["La muestra sólida se coloca dentro de un recipiente que está conectado a un sistema de sifón, similar al de las cisternas de inodoros. El proceso comienza calentando el ", html.Span("solvente", id="solvente_3",className="underlined-text"), " en un balón de fondo redondo, que está adaptado tanto al recipiente con el sifón como al condensador. Al alcanzar el punto de ebullición, el disolvente asciende por un canal hacia el condensador, donde se enfría y posteriormente gotea sobre la muestra. Cuando el nivel del ", html.Span("solvente", id="solvente_4",className="underlined-text"), " supera la entrada del sifón, se genera un vacío que lo impulsa de vuelta hacia el balón. Este ciclo se repite normalmente tres veces, y el tiempo total del proceso puede variar entre 6 y 18 horas, dependiendo del ", html.Span("solvente", id="solvente_5",className="underlined-text"), " utilizado."], className="body-footer"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["**",  html.Span("Dalton", className="italic-text"), " es la unidad de masa atómica unificada. Es una unidad estándar definida como un doceavo (1/12) de la masa de un átomo neutro y no enlazado de carbono-12, en su estado fundamental eléctrico y nuclear. Equivale a 1.6605402×10⁻²⁷ kilogramos. Un mol de unidades de masa atómica es equivalente a un gramo. Un átomo de hidrógeno tiene una masa de 1.00784 dáltones, y una molécula de agua tiene una masa de 18.01528 dáltones."], className="body-footer"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["La relación entre los valores de masa atómica y la masa macroscópica se establece a través del concepto de mol, que es la cantidad de unidades de una sustancia que contiene aproximadamente 6.022 1367(36)x10²³ entidades elementales, cifra que corresponde al valor numérico de la constante de Avogadro o número de Avogadro. Este número representa la cantidad total de átomos presentes en 12 gramos del isótopo de carbono-12. "], className="body-footer"),
                
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
                metodologia,
                xs={"size": 12, "order": 4},  # Change order to 2 on extra small devices
                sm={"size": 12, "order": 4},  # Change order to 2 on small devices
                md={"size": 12, "order": 4},
                lg={"size": 12, "order": 4},
                xl={"size": 12, "order": 4},
                style={'paddingRight':'0rem','paddingLeft':'0rem'}
            ),
            *tooltips
        ]


