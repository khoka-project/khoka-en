import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import os

dash.register_page(__name__)

# Define the navigation bar with the dropdown menu

portada =  dbc.Row(
        [
            html.Img(src="/assets/h_exp_1.webp",style={"width": "100%",'marginTop':'3%','marginBottom':'3   %'},className="center-image"),
        ]
                )

experimento = dbc.Container(
    dbc.Row([
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Div("EXPERIMENT", className="body-title-green"), 
                dbc.Row(className="espaciado_48_esc espaciado_48_mov"),
                html.Div(["This study aims to identify the ", html.Span("chemical compounds", id="compuestos_quimicos",className="underlined-text"),  " present in the four varieties of coca cultivated in the Khoka Project garden. To achieve this, extracts were prepared from the leaves of each variety using different ", html.Span("solvents", id="solvente_1",className="underlined-text") ,", and the metabolites present in their leaves were characterized through chromatographic techniques. This allowed us to conduct a comparative analysis and identify the similarities and differences in the production of these compounds among the different varieties."]),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Div("Step 1:",className="body-title-1",id="experimento_paso_1"),
                html.Div("Extraction of Compounds from the Leaves",className="body-title-2"),
                dbc.Row(className="espaciado_48_esc espaciado_48_mov"),
                html.Div(["The extraction process involves mixing dried leaves from each coca variety with different ", html.Span("solvents", id="solvente_2", className="underlined-text"),", using heat to extract and concentrate the components present in the leaves, which are then analyzed using gas chromatography."]),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Img(src="/assets/h_exp_2_esc.webp",style={"width": "100%",'marginTop':'4rem','marginBottom':'1rem'},className="center-image large-image"),
                html.Img(src="/assets/exp_2_m.webp",style={"width": "100%",'marginTop':'4rem','marginBottom':'1rem'},className="center-image small-image"),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Div("Basic Principles of Chemical Extraction",className="body-title-3", id = "pbe"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Solvent extraction is a separation technique that takes advantage of the differences in solubility of the components in a ", html.Span("mixture", id="mezcla_1", className="underlined-text"), ", whether solid or liquid, to isolate a specific compound by selectively transferring it from the original ", html.Span("mixture", id="mezcla_2", className="underlined-text")," into a liquid phase using an organic ", html.Span("solvent", id="solvente_3", className="underlined-text"), " such as ethanol or acetone."]),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Div("Simple Liquid-Liquid Extraction",className="body-title-3", id = "extraccion_liquido"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Liquid-liquid extraction is an effective method for separating components of a liquid ", html.Span("mixture",id="mezcla_3", className="underlined-text"),". The efficiency of this technique is based on the difference in ",html.Span("solubility", id="solubilidad_1",className="underlined-text")," of the compound to be extracted in two different, ",html.Span("inmiscible", id="inmiscible_1",className="underlined-text"),html.Span("solvents", id="solvente_4", className="underlined-text"),". When the ", html.Span("mixture", id="mezcla_4", className="underlined-text")," is shaken, the compound is selectively distributed between the two solvents, creating two distinct ",html.Span("phases",id="fases", className="underlined-text"),". For example, water and petroleum ether."]),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Img(src="/assets/h_exp_3_esc.webp",style={"width": "100%"},className="center-image large-image"),
                html.Img(src="/assets/exp_3_m.webp",style={"width": "100%"},className="center-image small-image"),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Div("Solvent Extraction Characteristics",className="body-title-3", id = "car_sol"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Selective extraction of a component from a ",html.Span("mixture", id="mezcla_5", className="underlined-text")," is achieved by adding another solvent that meets the following conditions:"]),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div([html.Span("Immiscibility: ", className="italic-text"), "The added solvent should not form a homogeneous ", html.Span("mixture", id="mezcla_6", className="underlined-text")," with the original solvent, similar to mixing water and oil."]),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div([html.Span("Higher ", className="italic-text"), html.Span("solubility", id="solubilidad_2",className="underlined-text italic-text"),
                          html.Span(":", className="italic-text"), "The compound to be isolated must be more ", html.Span("soluble", id="solubilidad_4", className="underlined-text"), 
                          " in the extraction solvent than in the original ", html.Span("solvent", id="solvente_5", className="underlined-text")]),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div([
                    html.Span(["Lower ", html.Span("solubility", id="solubilidad_3", className="underlined-text"), " of Other Components: "], className="italic-text "),
                    "The other components of the mixture should not be ",
                    html.Span("soluble", id="solvente_6", className="underlined-text"),
                    " in the extraction ",html.Span("solvent", id="solvente_13", className="underlined-text")]),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div([
                    html.Span("Volatility", className="italic-text")," the ", html.Span("solvent", id="solvente_7", className="underlined-text"),
                    "solvent should be volatile enough to be easily removed through distillation or evaporation."]),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div([
                html.Span("Safety", className="italic-text")," the ",html.Span("solvent", id="solvente_8", className="underlined-text"), 
                " should not be toxic or flammable, although it is difficult to find solvents that meet both criteria. Some solvents are relatively non-toxic but flammable, such as hexane; others are non-flammable but toxic, like dichloromethane or chloroform; and some are both toxic and flammable, like benzene."]),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div([
                html.Span("Common Immiscible Solvents", className="italic-text"), 
                html.Span(" Most frequently used solvents", className="italic-text"), html.Br(),
                "The ", html.Span("miscibility",id="miscible", className="underlined-text")," of an organic ",html.Span("solvent", id="solvente_9", className="underlined-text")," with water depends on its polarity:"]),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div([
                html.Span("High polarity:", className="italic-text"),
                " Polar ", html.Span("solvents", id="solvente_10", className="underlined-text"),
                " such as methanol, ethanol, or acetone are miscible with water, making them unsuitable for liquid-liquid extractions."]),
                html.Div([
                html.Span("Low polarity:", className="italic-text"),
                " Organics ", html.Span("solvents", id="solvente_10", className="underlined-text"),
                " with low polarity are preferred for extraction because of their immiscibility with water. Among the most commonly used are:",
                 html.Ul([
                    html.Li("Dichloromethane"),
                    html.Li("Diethyl ether"),
                    html.Li("Ethyl acetate"),
                    html.Li("Hexane")
                ],style={"marginBottom": "1rem","marginTop": "1rem"}),
                "These organic ",html.Span("solvents", id="solvente_11", className="underlined-text"), 
                " are selected specifically for their ability to efficiently separate components in liquid-liquid extraction techniques."],style={'paddingRight':'0rem',}),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Div("Step 2: ",className="body-title-1",id="experimento_paso_2"),
                html.Div("Compound Analysis: Gas Chromatography",className="body-title-2"),
                dbc.Row(className="espaciado_48_esc espaciado_48_mov"),
                html.Div(["At this stage, chromatographic analyses were performed on the extracts from the leaves of each coca variety, prepared in various ", 
                         html.Span("solvents", id="solvente_12", className="underlined-text")," such as ethanol, dichloromethane, and hexane."]),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Div("What is Chromatography?",className="body-title-3", id = "que_es_cro"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Chromatography encompasses a set of laboratory techniques used to separate the components of a ",html.Span("mixture", id="mezcla_7", className="underlined-text"), 
                          ". Since plant extracts contain hundreds of metabolites, gas chromatography stands out as a rapid and precise technique for identifying each metabolite present. This procedure involves taking a sample from each extract, heating it to high temperatures to volatilize the compounds, and injecting it into a 20-meter hollow metal column internally coated with silica or another finely powdered material. The components move through the column at different speeds depending on their chemical nature, pushed by an inert gas such as nitrogen or helium. At the end of the column, a detector identifies the emerging compounds. This result is recorded in a ",html.Span("chromatogram.",style={'fontStyle':'italic'})]),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Img(src="/assets/h_exp_4_esc.webp",style={"width": "100%"},className="center-image large-image"),
                html.Img(src="/assets/exp_4_m.webp",style={"width": "100%"},className="center-image small-image"),
                html.A(className='boton-scroll',href='#top', children=html.Img(src='/assets/icon-top.jpeg',style={'width': '48px', 'height': '48px'})),
            ],
            className="container-text"
        ))

# Definir los tooltips
tooltips = []
# compuesto químico
tooltips.append(
    dbc.Tooltip("A chemical compound is a substance formed by the combination of two or more different elements from the periodic table. Each compound is characterized by a specific chemical formula that indicates the exact composition of its elements. For example, water (H2O) consists of two hydrogen atoms and one oxygen atom.", 
                target="compuestos_quimicos", className="custom-tooltip"))

# Solvente
for i in range(1,14):
    tooltips.append(dbc.Tooltip("Also known as a solvent, a dissolvent is a substance, typically liquid, that can dissolve other substances without chemically altering them to form a solution.", 
                                target="solvente_{0}".format(str(i)), className="custom-tooltip"))
    
# Mezcla
for i in range(1,8):
    tooltips.append(dbc.Tooltip("A mixture is a physical combination of two or more substances where each component retains its individual chemical properties. The substances in a mixture do not chemically combine and can therefore be separated by physical methods such as filtration, centrifugation, decantation, or distillation.", 
                    target="mezcla_{0}".format(str(i)), className="custom-tooltip"))

# Inmiscible
tooltips.append(dbc.Tooltip("An immiscible substance does not mix and remains separated into phases or forms a suspension.", 
                    target="inmiscible_1".format(str(i)), className="custom-tooltip"))

# Solubilidad

for i in range(1,5):
    tooltips.append(dbc.Tooltip("Solubility is the ability of a substance, known as a solute, to dissolve in another substance called a solvent, forming a homogeneous solution. The solubility of a solute in a specific solvent depends on factors such as temperature, pH, and environmental pressure. This property is essential for numerous processes in chemistry, biology, pharmacology, and everyday life.", 
                        target="solubilidad_{0}".format(str(i)), className="custom-tooltip"))

# fases
tooltips.append(dbc.Tooltip("A phase defines a distinct physical state within a system, characterized by uniform physical and chemical properties. It commonly refers to the different forms in which matter appears, such as solid, liquid, gas, or plasma. In a heterogeneous system, different phases are separated by clearly defined boundaries, as seen in a mixture of water and oil.",
                       target="fases", className="custom-tooltip"))

# miscible
tooltips.append(dbc.Tooltip("Miscible refers to the ability of two or more substances to completely mix with each other to form a homogeneous solution. This means that when combined, they integrate uniformly into a single phase without separating, within certain ranges of temperature, pressure, and composition. A common example is alcohol and water, which mix to form a uniform solution.",
                       target="miscible", className="custom-tooltip"))

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
                experimento,
                xs={"size": 12, "order": 4},  # Change order to 2 on extra small devices
                sm={"size": 12, "order": 4},  # Change order to 2 on small devices
                md={"size": 12, "order": 4},
                lg={"size": 12, "order": 4},
                xl={"size": 12, "order": 4},
                style={'paddingRight':'0rem','paddingLeft':'0rem'}
            ),
            *tooltips
        ]


