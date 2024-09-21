import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import os
import csv


dash.register_page(__name__,path='/khoka_bibliography')

# Define the navigation bar with the dropdown menu


portada =  dbc.Row(
        [
            html.Img(src="/assets/h_biblio_1.jpg",style={"width": "100%",'marginTop':'3%','marginBottom':'3   %'},className="center-image"),
        ]
                )

bibliografia = dbc.Container(
    dbc.Row([
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Div("BIBLIGRAPHIC REFERENCES", className="body-title-green"), 
                dbc.Row(className="espaciado_48_esc espaciado_48_mov"),
                html.Div(["Ambre, J. J.; Ruo, T.-L.; Smith, G. L.; Backes, D. & Smith, C. M. (1982). Ecgonine Methyl Ester, a major metabolite of cocaine. ", html.Span("Journal of Analytical Toxicology",className="italic-text"),", 6."],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Barco, A.; Benetti, S.; de Risi, C.; Marchetti, P.; Pollini, G. P. & Zanirato, V. (1997). TETRAHEDRON: ASYMMETRY REPORT NUMBER 31 D-(-)-Quinic acid: a chiron store for natural product synthesis. ", html.Span("Tetrahedron: Asymmetry",className="italic-text"),", 8(21)."],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Boerjan, W.; Ralph, J. & Baucher, M. (2003). Lignin biosynthesis. ", html.Span("Annual Review of Plant Biology",className="italic-text"),", 54, 519-546. https://doi.org/10.1146/ annurev.arplant.54.031902. 134938."],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Boo, Y. C. (2019). p-Coumaric acid as an active ingredient in cosmetics: A review focusing on its antimelanogenic effects. ", html.Span("Antioxidants",className="italic-text"),", 8(8). https://doi.org/10.3390/ antiox8080275."],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Cantrell, A.; McGarvey, D. J. & Truscott, T. G. (s. f.). Photochemical and photophysical properties of sunscreens."],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["De Oliveira, D. M.; Finger-Teixeira, A.; Mota, T. R.; Salvador, V. H.; Moreira-Vilar, F. C.; Molinari, H. B. C.; Mitchell, R. A. C.; Marchiosi, R.; Ferrarese-Filho, O. & Dos Santos, W. D. (2015). Ferulic acid: A key component in grass lignocellulose recalcitrance to hydrolysis. ", html.Span("Plant Biotechnology Journal",className="italic-text"),", 13(9), 1224-1232. https://doi.org/10.1111/ pbi.12292."],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["González, M. A.; Correa-Royero, J.; Agudelo, L.; Mesa, A. & Betancur-Galvis, L. (2009). Synthesis and biological evaluation of abietic acid derivatives. ", html.Span("European Journal of Medicinal Chemistry",className="italic-text"),", 44(6), 2468-2472. https://doi.org/10.1016/ j.ejmech.2009.01.014."],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Guaadaoui, A.; Benaicha, S.; Elmajdoub, N.; Bellaoui, M. & Hamal, A. (2014). What is a bioactive compound? A combined definition for a preliminary consensus. ", html.Span("International Journal of Food Sciences and Nutrition",className="italic-text"),", 3(3), 17-179. https://doi.org/10.11648/ j.ijnfs.20140303.16."],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Heller, W. & Kijhnl, T. (1985). Elicitor induction of a microsomal 5-O-(4-Coumaroyl) shikimate 3'-hydroxylase in parsley cell suspension cultures. ", html.Span("Archives of Biochemistry and Biophysics",className="italic-text"),", 241(2)."],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Islam, M. T.; Ali, E. S.; Uddin, S. J.; Shaw, S.; Islam, M. A.; Ahmed, M. I.; Chandra Shill, M.; Karmakar, U. K.; Yarla, N. S.; Khan, I. N.; Billah, M. M.; Pieczynska, M. D.; Zengin, G.; Malainer, C.; Nicoletti, F.; Gulei, D.; Berindan-Neagoe, I.; Apostolov, A.; Banach, M. & Atanasov, A. G. (2018). Phytol: A review of biomedical activities. ", html.Span("Food and Chemical Toxicology",className="italic-text"),", 121, 82-94. https://doi.org/10.1016/  j.fct.2018.08.032."],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Kalsoom, A. K. (2015). Pharmacological activities of protocatechuic acid. ", html.Span("Acta Poloniae Pharmaceutica - Drug Research",className="italic-text"),", 72, 643-650."],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Levine, B. S. & Kerrigan, S. (2020). Principles of forensic toxicology."],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["McGraw-Hill Dictionary of Chemistry. (2003). New York, NY: McGraw-Hill."],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Miao, Z.; Kayahara, H. & Tadasa, K. (1997). Synthesis and biological activities of ferulic acid–amino acid derivatives. ", html.Span("Bioscience, Biotechnology, and Biochemistry",className="italic-text"),", 61(3), 527-529. https://doi.org/10.1271/ bbb.61.527."],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["McNair, H. M. & Miller, J. M. (1997). ", html.Span("Basic gas chromatography.",className="italic-text")," New York, NY: Wiley."],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Nickon, A. & Fieser, L. F. (1952). Configuration of tropine and pseudotropine. ", html.Span("Journal of the American Chemical Society",className="italic-text"),", 74(22), 5566-5570."],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Nguyen, B. C. Q. & Tawata, S. (2016). The chemistry and biological activities of mimosine: A review. ", html.Span("Phytotherapy Research",className="italic-text"),", pp. 1230-1242. https://doi.org/10.1002/ ptr.5636."],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Turner, C. E.; Ma, C. Y. & Elsohly, M. A. (1981). Constituents of Erythroxylon coca II. Gas-chromatographic analysis of cocaine and other alkaloids in coca leaves. ", html.Span("Journal of Ethnopharmacology",className="italic-text"),", 3(2-3), 293-298."],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Touaibia, M.; Jean-François, J. & Doiron, J. (2011). Caffeic acid, a versatile pharmacophore: An overview. ", html.Span("Reviews in Medicinal Chemistry",className="italic-text"),", 11."],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Williams, T. I. & Vyeil, H. (1952). Definition of chromatography. ", html.Span("Nature",className="italic-text"),", 4325(September 20), 503-503."],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Yi, W.; Cao, R.; Peng, W.; Wen, H.; Yan, Q.; Zhou, B.; Ma, L. & Song, H. (2010). Synthesis and biological evaluation of novel 4-hydroxybenzaldehyde derivatives as tyrosinase inhibitors. ", html.Span("European Journal of Medicinal Chemistry",className="italic-text"),", 45(2), 639-646. https://doi.org/10.1016/ j.ejmech.2009.11.007."],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Yokoyama, R.; De Oliveira, M. V. V.; Kleven, B. & Maeda, H. A. (2021). The entry reaction of the plant shikimate pathway is subjected to highly complex metabolite-mediated regulation. ", html.Span("Plant Cell",className="italic-text"),", 33(3), 671-696. https://doi.org/10.1093/ plcell/koaa042."],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Zhou, J.; Chan, L. & Zhou, S. (2012). Trigonelline: a plant alkaloid with therapeutic potential for diabetes and central nervous system disease. ", html.Span("Current Medicinal Chemistry",className="italic-text"),", 19(21), 3523-3531."],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Zhou, S.; Huang, G. & Chen, G. (2019). Synthesis and biological activities of local anesthetics. ", html.Span("RSC Advances",className="italic-text"),", 9(70), 41173-41191. https://doi.org/10.1039/ c9ra09287k."],className="body-biblio"),


                
            ],
            className="container-text"
        ))

# Definir los tooltips
tooltips = []


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
                bibliografia,
                xs={"size": 12, "order": 4},  # Change order to 2 on extra small devices
                sm={"size": 12, "order": 4},  # Change order to 2 on small devices
                md={"size": 12, "order": 4},
                lg={"size": 12, "order": 4},
                xl={"size": 12, "order": 4},
                style={'paddingRight':'0rem','paddingLeft':'0rem'}
            ),
            *tooltips
        ]


