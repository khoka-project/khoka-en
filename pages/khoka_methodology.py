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
                html.Div(["* ", html.Span("Soxhlet extraction technique", className="italic-text"), ": it is a separation method that uses a liquid solvent to extract components of interest from a solid sample. It is widely used to determine the fat content in various samples. The Soxhlet extractor, made of glass, includes a condenser attached to a jacket that facilitates the inflow and outflow of water."], className="body-footer"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["The solid sample is placed inside a container connected to a siphon system, similar to that of toilet tanks. The process begins by heating the solvent in a round-bottom flask, which is connected to both the container with the siphon and the condenser. Once the boiling point is reached, the solvent rises through a channel to the condenser, where it cools and then drips onto the sample. When the solvent level exceeds the siphon inlet, a vacuum is generated, pushing the solvent back into the flask. This cycle typically repeats three times, and the total process time can vary between 6 and 18 hours, depending on the solvent used."], className="body-footer"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["**",  html.Span("Dalton", className="italic-text"), " is the unified atomic mass unit. It is a standard unit defined as one-twelfth (1/12) of the mass of a neutral, unbound carbon-12 atom, in its ground electrical and nuclear state. It is equivalent to 1.6605402×10⁻²⁷ kilograms. One mole of atomic mass units is equivalent to one gram. A hydrogen atom has a mass of 1.00784 daltons, and a water molecule has a mass of 18.01528 daltons."], className="body-footer"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["The relationship between atomic mass values and macroscopic mass is established through the concept of a mole, which is the amount of substance that contains approximately 6.022 1367(36)x10²³ elementary entities, a figure corresponding to the numerical value of Avogadro's constant or Avogadro's number. This number represents the total amount of atoms present in 12 grams of the carbon-12 isotope."], className="body-footer"),
                
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


