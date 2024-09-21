import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import os

dash.register_page(__name__,path='/')

# Define the navigation bar with the dropdown menu

portada =  dbc.Row(
        [
            html.Img(src="/assets/h_intro_1.webp",style={"width": "100%",'marginTop':'3%','marginBottom':'3   %'},className="center-image"),
        ]
                )

introduccion = dbc.Container(
    dbc.Row([
                dbc.Row(className="espaciado_96_esc espaciado_intr_img"),
                html.Div("INTRODUCTION", className="body-title-green"), 
                dbc.Row(className="espaciado_48_esc espaciado_48_mov"),
                html.Div(["Since ancient times, the active components of the coca leaf have sparked profound human interest. Only through advancements in chemical science was it possible to isolate its main ", html.Span("alkaloid", id="alcaloide",className="underlined-text"), ", cocaine, becoming one of the most significant scientific achievements of the 19th century. Since then, numerous researchers have sought to identify the ", html.Span("chemical compounds", id="compuestos_quimicos",className="underlined-text"), " present in its various varieties. Among them, Timothy Plowman is considered the most important coca researcher of the 20th century. Not only did he botanically classify this family of plants, but he also conducted various comparative studies to understand the chemical composition of each variety."]),
                dbc.Row(className="espaciado_48_esc espaciado_48_mov"),
                html.Img(src="/assets/h_intro_2.webp",style={"width": "102%"},className="center-image large-image"),
                html.Img(src="/assets/h_intro_2.webp",style={"width": "100%"},className="center-image small-image"),
                html.Div([html.Span("Courtesy of The Field Museum of Chicago, USA.",className="footer-image footer-image-mobil" )]),
                dbc.Row(className="espaciado_48_esc espaciado_48_mov"),
                html.Div(["A review of the existing academic literature on the chemical composition of this plant family reveals that some of its components could have great potential for applications ranging from pharmacological and nutritional to agricultural, highlighting the importance of continuing research in this field."]),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["At ",html.Span("Khoka Project", className="italic-text"), ", we have dedicated over a decade to maintaining a garden that houses the four varieties of coca that Plowman identified in the late 1970s as those ancestrally cultivated and used by various cultures in South America."]),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["The coca family includes two species:"]),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Img(src="/assets/h_intro_3.webp",style={"width": "100%"},className="center-image large-image"),
                html.Img(src="/assets/v_intro_3.webp",style={"width": "100%"},className="center-image small-image"),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Div(["This study aims to identify the chemical compounds contained in the plants from our garden. Chromatographic readings were performed at the Met Core Laboratory of Universidad de los Andes in 2021, and the data obtained were processed, analyzed, and graphed by the ",html.Span("Khoka Project", className="italic-text"), " team."]),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Div("What is Metabolomics?",className="body-title-2",id="intro_metabol_1"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Metabolomics is a branch of natural sciences that focuses on the detailed study of the metabolic processes in living organisms, specifically through the analysis of small ", html.Span("molecules",id="moleculas_1", className="underlined-text")," know as ",html.Span("metabolites", className="italic-text"),", which are the compounds produced during metabolism."]),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Div("Plant Metabolism",className="body-title-2",id="intro_metabol_2"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Metabolism is the set of chemical and physical processes that occur in the cells of living organisms to convert food into ", html.Span("energy",id="energia_1",className="underlined-text"), ", enabling them to perform biological functions essential for life: respiration, digestion, circulation, body temperature regulation, waste elimination, etc."]),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Img(src="/assets/h_intro_4.webp",style={"width": "100%"},className="center-image large-image"),
                html.Img(src="/assets/v_intro_4.webp",style={"width": "100%"},className="center-image small-image"),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Div(["In plants, these processes include vital functions like photosynthesis (where solar energy is transformed into chemical energy), respiration, and nutrient regulation, among others."]),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Div("Metabolites",className="body-title-3",id="intro_metabol_3"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Metabolites are all the substances produced during metabolism."]),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Div("Primary Metabolism",className="body-title-3",id="intro_metabol_p"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Primary metabolism in plants encompasses all physical and chemical processes that convert or consume ", html.Span("energy",id="energia_2",className="underlined-text"), " and are directly involved in their growth, reproduction, and survival."]),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Div("Secondary Metabolism",className="body-title-3",id="intro_metabol_s"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["In plants, secondary metabolism refers to the set of biochemical reactions that perform vital functions not directly related to growth or reproduction."]),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Plants allocate a significant portion of assimilated carbon and  ", html.Span("energy",id="energia_3",className="underlined-text"), " to the ", html.Span("synthesis",id="sintesis_2",className="underlined-text"), " of a wide variety of organic ", html.Span("molecules",id="moleculas_2",className="underlined-text"), " that do not directly participate in photosynthesis, respiration, nutrient assimilation, ", html.Span("solute",id="solutos",className="underlined-text"), " transport, or the ", html.Span("synthesis",id="sintesis_1",className="underlined-text"), " of ", html.Span("proteins",id="proteinas",className="underlined-text"), ", carbohydrates, or lipids."]),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["The majority of secondary metabolites play protective roles. This protection can be against ultraviolet radiation, significant temperature changes ", html.Span("oxidative",id="oxidativo",className="underlined-text"), ", damage, and the attack of microorganisms such as fungi and bacteria, as well as herbivores like insects, reptiles, birds, or mammals. They can even protect against other plants."]),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["The main production pathways for these secondary metabolites in plants derive from primary carbon metabolism. These compounds are also known as natural products and hold significant value in both medicinal and economic realms. The latter stems from their use in various industries, including cosmetics, food, pharmaceuticals, and agriculture."]),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Secondary metabolites are low molecular weight chemical compounds of diverse nature. Due to their properties (toxic, ", html.Span("narcotic",id="narcoticas",className="underlined-text"), ", ", html.Span("sedative",id="sedantes",className="underlined-text"), ", etc.), they have been used for medicinal, insecticidal, repellent, and cosmetic purposes, among others."]),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Div("Metabolomics in Coca Research",className="body-title-2L",id="intro_metabol_4"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Studying the coca plant from a metabolomic perspective means expanding our understanding of the plant’s chemistry, delving into the various metabolites it produces and their potential industrial, pharmacological, and therapeutic applications."]),
            ],
            className="container-text"
        ))

# Definir los tooltips
tooltips = []
# compuesto químico
tooltips.append(
    dbc.Tooltip("A chemical compound is a substance formed by the combination of two or more different elements from the periodic table. Each compound is characterized by a specific chemical formula that indicates the exact composition of its elements. For example, water (H2O) consists of two hydrogen atoms and one oxygen atom.", 
                    target="compuestos_quimicos", className="custom-tooltip"))

# Alcaloide
tooltips.append(dbc.Tooltip("Alkaloids are natural compounds produced by plants through secondary metabolism. These compounds contain nitrogen in their molecular structure and are known for their potent effects on the body, even in small doses. They are used in medicine to relieve pain and treat mental health disorders. Notable examples of alkaloids include caffeine in coffee and nicotine in tobacco, both stimulants; cocaine from the coca plant, which also functions as a local anesthetic; and morphine from the poppy, used as a pain reliever.", 
                    target="alcaloide", className="custom-tooltip"))

# Moléculas
for i in range(1,3):
       tooltips.append(dbc.Tooltip("A molecule is a defined grouping of two or more atoms chemically bonded together, forming the smallest unit of a pure chemical substance that retains all its characteristic properties. Molecules can range in size from simple diatomic examples, such as molecular oxygen (O2), to complex macromolecules like DNA and proteins, which can contain dozens to thousands of atoms arranged in specific structures. The bonds holding the atoms in a molecule can be covalent, where atoms share electrons, or ionic, where atoms are attracted due to opposite charges. This structure and composition determine the physical and chemical properties of the substance.", 
                    target="moleculas_{0}".format(str(i)), className="custom-tooltip"))

# Energía
for i in range(1,4):
       tooltips.append(dbc.Tooltip("Energy is the capacity to perform work or induce physical changes, and it is a fundamental property of nature that manifests in various forms, such as mechanical, thermal, electrical, chemical, nuclear, and others. This capacity can be transferred between systems and converted from one form to another, but it cannot be created or destroyed (first law of thermodynamics).", 
                    target="energia_{0}".format(str(i)), className="custom-tooltip"))

# Síntesis
for i in range(1,3):
       tooltips.append(dbc.Tooltip("Chemical synthesis is the process by which complex chemical compounds are created from simpler reactants through controlled chemical reactions. This process is fundamental in chemistry for the production of a wide range of products, from medications to advanced materials. Chemical synthesis involves the formation of chemical bonds and is carried out using specific methods and techniques that ensure the desired product is obtained with high purity and efficiency. It is used in both research and industry to develop new substances and enhance the properties of existing ones.", 
                    target="sintesis_{0}".format(str(i)), className="custom-tooltip"))

# Solutos
tooltips.append(dbc.Tooltip("Solute is the substance that dissolves in another substance, known as the solvent, to form a solution. The solute is typically present in a smaller amount in the mixture, although this can vary depending on the specific solution.", 
                    target="solutos", className="custom-tooltip"))

# Proteínas
tooltips.append(dbc.Tooltip("Proteins are complex and essential macromolecules that play a variety of critical roles within living organisms. They are composed of linear chains of amino acids, with their sequence determined by the nucleotides in the corresponding genes of DNA. These amino acid sequences fold into specific three-dimensional structures that define the protein's function. Proteins are indispensable for virtually all biological processes, including catalyzing metabolic reactions (as enzymes), regulating gene expression, transmitting signals between and within cells, providing structural support in cells and tissues, and transporting molecules across cell membranes. Additionally, proteins play a crucial role in the immune system and muscle movement. Due to their functional diversity and involvement in many pathologies, they are a central focus of research in biomedicine and biotechnology.", 
                    target="proteinas", className="custom-tooltip"))

# Oxidativo
tooltips.append(dbc.Tooltip("Oxidation is the chemical process in which an atom, ion, or molecule loses electrons during a chemical reaction. Traditionally, the term was associated with reactions where oxygen combined with other substances, increasing the oxygen content of the compound. However, in a broader sense, oxidation does not necessarily involve oxygen. It is now defined in chemistry as the loss of electrons, which can alter the chemical properties of the substance involved. Oxidation often occurs simultaneously with reduction, a process in which another substance gains the electrons lost in oxidation. Together, these complementary processes are known as redox (reduction-oxidation) reactions.", 
                    target="oxidativo", className="custom-tooltip"))

# Narcóticos
tooltips.append(dbc.Tooltip("The term narcotic is commonly used to describe substances that induce sleep, muscle relaxation, and a loss of sensation and consciousness. In the medical context, narcotics refer to a class of drugs, mostly opioid analgesics, primarily used to manage severe pain. These compounds act on the central nervous system to relieve pain but can also suppress breathing, cause drowsiness, and often lead to physical and psychological dependence if misused or used over prolonged periods. Common examples include morphine, fentanyl, and codeine.", 
                    target="narcoticas", className="custom-tooltip"))

# Sedantes
tooltips.append(dbc.Tooltip("A sedative is a substance or combination of substances that produce a calming effect on the central nervous system. Sedatives are commonly used to treat conditions such as anxiety and insomnia, helping to reduce tension, agitation, and facilitating sleep. These medications can vary in strength, ranging from mild sedatives that help relax the patient to more potent hypnotics that induce sleep.", 
                    target="sedantes", className="custom-tooltip"))




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
                introduccion,
                xs={"size": 12, "order": 4},  # Change order to 2 on extra small devices
                sm={"size": 12, "order": 4},  # Change order to 2 on small devices
                md={"size": 12, "order": 4},
                lg={"size": 12, "order": 4},
                xl={"size": 12, "order": 4},
                style={'paddingRight':'0rem','paddingLeft':'0rem'}
            ),
            *tooltips
        ]


