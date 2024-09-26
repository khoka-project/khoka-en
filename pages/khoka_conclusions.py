import dash
from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import os
import base64

dash.register_page(__name__,path='/khoka_conclusions')

pdf_filename = './assets/metabolitos.pdf'
encoded_pdf = base64.b64encode(open(pdf_filename, 'rb').read()).decode('utf-8')

# Define the navigation bar with the dropdown menu

portada =  dbc.Row(
        [
            html.Img(src="/assets/h_conclu.webp",style={"width": "100%",'marginTop':'3%','marginBottom':'3   %'},className="center-image"),
        ]
                )

conclusiones = dbc.Container(
    dbc.Row([
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Div("CONCLUSIONS", className="body-title-green"), 
                dbc.Row(className="espaciado_48_esc espaciado_48_mov"),
                html.Button('DOWNLOAD METABOLITE MAP', id='bt-descarga', n_clicks=0, className="boton-descarga"),
                dcc.Download(id="download-pdf"),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Div("The Study of Metabolites in Coca Leaves",className="body-title-2",id="conclu_estudio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Throughout history, humanity has recognized and venerated various animal and plant species as sacred. In the plant kingdom, a group of plants stands out for producing specialized substances to protect themselves from their environment: alkaloids. These natural organic compounds, which contain at least one nitrogen atom in a unique molecular configuration, can exert profound effects on the human body, influencing perception and states of consciousness."]),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.A(className='boton-scroll boton-scroll_m',href='#top', children=html.Img(src='/assets/icon-top.jpeg',style={'width': '48px', 'height': '48px'})),


                html.Div(children=[
                    html.P("Plants have developed ingenious mechanisms to make use of the elements available in their environment, synthesizing substances unique to each species. This fascinating field of study continues to reveal surprising discoveries. It is particularly admirable how ancestral cultures identified these plants and determined the optimal conditions to maximize their benefits. A notable example is the traditional use of coca leaves: by adding ashes from calcined seashells and chewing the leaf for an extended period, the release and absorption of its alkaloids are enhanced."),
                    dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                    html.P("Fundamental elements such as nitrogen, carbon, and oxygen form the basis of organic matter and are essential in proteins, which provide structure to muscles and are indispensable in our diet. However, in alkaloids, nitrogen plays a different role. It possesses a pair of free electrons that do not participate in chemical bonds, giving it basic properties. This characteristic, shared with other elements in the nitrogen group of the periodic table, such as phosphorus and arsenic, makes alkaloids similar to acidic substances, forming water-soluble salts. Conversely, in alkaline solutions, alkaloids are less soluble."),
                    dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                    html.P("Another notable property of alkaloids is their affinity for tissues with high lipid content, such as the brain and the nervous system. This affinity allows them to cross biological barriers and exert significant effects on various body systems, influencing vital functions and states of consciousness."),
                    dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                    html.Div(["Among the most well-known alkaloids are caffeine, found in coffee and tea and consumed massively worldwide; morphine, used as a potent painkiller in medicine; and nicotine, produced by tobacco, which, besides being an effective insecticide, is responsible for the addiction associated with tobacco use. Many alkaloids have the potential to cause dependency when consumed repeatedly. Heroin, derived from morphine, was initially employed for therapeutic purposes, but its medical use was quickly discontinued due to its high addictive potential."]),
                    dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                    html.Div(["Within alkaloids, there is a subgroup called tropane alkaloids, whose name derives from the plant "
                          , html.Span("Atropa belladonna", className="italic-text"), 
                          ", from which scopolamine and atropine are extracted. These substances are known for inducing states of confusion, loss of will, paralysis, and in high doses, they can lead to death by heart failure."]),
                    dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                    html.Div(["The coca leaf contains several tropane alkaloids, with cocaine and ecgonine being the most prominent. Cocaine has an extensive history: it was the first local anesthetic discovered, capable of numbing the nerves in the oropharyngeal area, proving very useful in surgery. Although cocaine often garners attention, the coca leaf contains other tropane alkaloids whose effects are not yet fully understood. Additionally, it contains flavonoids and phenolic compounds that, in synergy with the alkaloids, contribute to effects such as reducing hunger, increasing vitality, decreasing fatigue, and enhancing mental focus."]),
                    dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                    html.Div(["To delve into the chemical richness of coca leaves, ", 
                          html.Span("Khoka Project", className="italic-text"), " conducted a comparative study of four varieties: ", 
                          html.Span("Erythroxylum coca", className="italic-text"), " var. ", 
                          html.Span("coca", className="italic-text"), ", ",
                          html.Span("Erythroxylum coca", className="italic-text"), " var. ", 
                          html.Span("ipadu", className="italic-text"), ", ",
                          html.Span("Erythroxylum novogranatense", className="italic-text"), " var. ", 
                          html.Span("novogranatense", className="italic-text"), " and ", 
                          html.Span("Erythroxylum novogranatense", className="italic-text"), " var. ", 
                          html.Span("truxillense", className="italic-text"), "Each of these varieties exhibits a unique profile of secondary metabolites, reflecting the diversity and complexity of their biochemical processes."]),
                    dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                    html.Div(["Cocaine is present in all varieties, reaching its highest concentration in E. coca var. coca. Ecgonine predominates in E. coca var. ipadu, native to the Amazon, suggesting that high humidity conditions favor its accumulation, possibly due to the ease with which cocaine hydrolyzes in the presence of water."]),
                    dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                    html.Div(["In addition to these alkaloids, other compounds such as methyl ecgonine ester and various flavonoids and phenolic acids were identified, including abietic acid and chlorogenic acid. These components underscore the specificity and ecological adaptation of each type of coca, demonstrating the versatility of these plants in producing defense and adaptation substances."]),
                    dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                    html.Div(["Exploring the critical functions of these substances, we find that ecgonine acts as a precursor in the biosynthesis of cocaine. It serves as a reserve of carbon and nitrogen, essential elements for the plant's growth and development. Its accumulation may be a response to environmental stress factors, allowing the plant to adapt to diverse conditions."]),
                    dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                    html.Div(["Cocaine, the most studied alkaloid in coca leaves, plays multiple vital roles. It functions as a potent herbivore repellent due to its toxicity, deterring attacks and protecting the plant. It also possesses antimicrobial properties, helping to resist infections by bacteria, fungi, and other pathogens. In stressful situations, such as drought or high solar radiation, cocaine production may increase, suggesting a role in mitigating cellular damage and adapting to adverse conditions."]),
                    dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                    html.Div(["Abietic acid is a diterpene present in coca leaves that serves protective and adaptive functions. Known for its anti-inflammatory and wound-healing properties, it contributes to the repair of damaged tissues and defense against pathogens and herbivores. Additionally, it acts as an antioxidant, protecting plant cells from oxidative damage caused by environmental factors such as UV radiation and free radicals. This compound may also influence the plant’s interaction with beneficial soil microorganisms, fostering symbiosis and improving nutrient absorption."]),
                    dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                    html.Div(["It is important to note that when chewing coca leaves, alkaloids such as cocaine are released and can undergo chemical transformations in the human body. The process of hydrolysis converts cocaine into benzoylecgonine and methyl ecgonine ester, metabolites with different effects and activity profiles. However, cocaine ingested in this manner is primarily metabolized in the liver and, to a lesser extent, in the mouth."]),
                    dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                    html.Div(["The coca leaf is a compendium of complex chemical compounds that reflect the sophistication of plant defense and adaptation mechanisms. The study of its secondary metabolites offers us a window into the evolutionary survival strategies of plants and reveals potential pharmacological and therapeutic applications that have been harnessed by various cultures throughout history."]),
                ],id="conclu1", className="text-none"),

                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Button(id='toggle-button1', children=html.Img(src='/assets/icon-mas.webp',style={'width': '48px', 'height': '48px'}), n_clicks=0, className="boton-imagen"),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),

                html.Div("Results of the Chemical Analysis of the Four Varieties",className="body-title-2",id="conclu_resultados"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["In an exhaustive analysis of the four coca varieties, notable differences emerged in the expression of their secondary metabolites. We conducted a detailed comparison of the presence or absence of various alkaloids in each variety. It is noteworthy that the Truxillense variety lacks trigonelline, while the Novogranatense variety shows neither trigonelline nor methyl ecgonine ester. On the other hand, mimosine was detected exclusively in the Ipadu variety, though in very low proportions."]),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),


                html.Div(children=[
                        html.Div(["The proportions of metabolites revealed a marked predominance of cocaine and ecgonine, with other alkaloids present in smaller amounts. Of particular relevance were the methyl ecgonine ester and ethyl ecgonine ester, identified only in the Ipadu variety. The Coca variety presented the highest proportion of cocaine relative to ecgonine, while Novogranatense exhibited a balanced ratio between the two. In contrast, the Ipadu and Truxillense varieties displayed a higher proportion of ecgonine compared to cocaine, with Ipadu showing the most pronounced difference, almost the opposite of the Coca variety. It is important to clarify that this study provides qualitative data, and the reported percentages were calculated based on the intensity of the signal of the most abundant compound in each chromatogram. Quantitative analyses of each metabolite will be carried out in future studies."]),
                        dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                        html.Div(["When comparing the secondary metabolites of an acidic or phenolic nature, the Truxillense variety stood out for its greater diversity, presenting ten phenols. This was followed by the Coca variety with seven phenols, and the Ipadu and Novogranatense varieties with six phenols each. Among the phenolic acids, abietic acid was the most prevalent in all varieties, followed by cinnamic acid and shikimic acid."]),
                        dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                        html.Div(["Overall, the apparent proportions of phenolic acids were lower than those of the alkaloids. The Ipadu variety showed the highest presence of phenolic acids, while the Novogranatense variety presented the least diversity in its expression."]),
                ],id="conclu2", className="text-none"),

                dbc.Row(className="espaciado_48_esc espaciado_48_mov"),
                html.Button(id='toggle-button2', children=html.Img(src='/assets/icon-mas.webp',style={'width': '48px', 'height': '48px'}), n_clicks=0, className="boton-imagen"),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),


                html.Div("Conclusions from the Study of Metabolites in Coca Varieties",className="body-title-2",id="conclu_variedades"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["The comparative analysis of the four varieties revealed substantial differences in the presence and proportion of various secondary metabolites, with alkaloids and phenolic acids being the most notable."]),
                dbc.Row(className="espaciado_48_esc espaciado_48_mov"),
                html.Div("Alkaloids:",className="body-title-3",id="conclu_var-1"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Regarding the proportions of cocaine and ecgonine, distinctive trends were observed: the Coca variety exhibited a predominance of cocaine over ecgonine, while the Ipadu and Truxillense varieties showed a higher proportion of ecgonine relative to cocaine. On the other hand, the Novogranatense variety maintained a balanced ratio between these two metabolites."]),
                dbc.Row(className="espaciado_48_esc espaciado_48_mov"),
                html.Div("Phenolic Acids:",className="body-title-3",id="conclu_var-2"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Among the four analyzed varieties, Truxillense stood out for its greater phenolic diversity, presenting ten different phenols. This was followed by the Coca variety with seven phenols, and both Ipadu and Novogranatense with six each."]),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),


                html.Div(children=[
                        html.Div(["Regarding specific acids, abietic acid predominated in all varieties, showing the highest proportion among the identified phenols. Similarly, both cinnamic acid and shikimic acid were uniformly present in all the studied varieties. However, certain varieties exhibited notable absences: chlorogenic acid and 3-O-coumaroylquinic acid were not detected in Novogranatense, while 5-O-coumaroylquinic acid and caffeic acid were absent in Truxillense and Novogranatense, respectively."]),
                        dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                        html.Div(["The proportions of phenolic acids were lower compared to alkaloids, with the Ipadu variety standing out for its higher concentration of these compounds, in contrast to Novogranatense, which presented the lowest diversity of phenolic expression. This notable presence of organic acids in Ipadu could be attributed to the greater environmental stress it faces, given its Amazonian origin. In this region, soils rich in organic matter and the high biodiversity of plants and microorganisms favor the production of a wide range of diverse metabolites."]),
                        dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                        html.Div(["This study not only highlights the biochemical variability among the different coca varieties but also suggests that specific environmental conditions play a crucial role in the synthesis and accumulation of secondary metabolites. Such findings could have significant implications for both the traditional use of these varieties and future scientific research aimed at harnessing their bioactive compounds."]),
                ],id="conclu3", className="text-none"),

                dbc.Row(className="espaciado_48_esc espaciado_48_mov"),
                html.Button(id='toggle-button3', children=html.Img(src='/assets/icon-mas.webp',style={'width': '48px', 'height': '48px'}), n_clicks=0, className="boton-imagen"),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),


                html.Div(["Comparison of Compounds Reported in Literature vs. Those Present in the ", html.Span("Khoka Project", className="italic-text"), "Garden."],className="body-title-2",id="conclu_compara"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["The analysis of the four coca varieties present in the bioarchive of ", html.Span("Khoka Project", className="italic-text"), " revealed the identification of eighteen secondary metabolites, with alkaloids standing out as the predominant group, followed by hydroxycinnamic acids. A notable finding was the exclusive presence of trans-cinnamoylcocaine, corroborating Plowman's reports, which indicate a higher incidence of this isomer compared to cis-cinnamoylcocaine, whose absence was also confirmed in all the studied varieties."]),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),

                html.Div(children=[
                        html.Div(["Regarding other classes of compounds, a low presence of terpenes and sesquiterpenes was observed across all four varieties. Additionally, flavonoids were completely absent, even in the Truxillense variety, highlighting a particular lack in this group of metabolites. However, the detection of compounds such as mimosine and trigonelline provided a distinctive alkaloid profile, significantly differentiating each variety."]),
                        dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                        html.Div(["It is important to note that only the alkaloids match both the existing reports in the literature and the findings obtained from the herbarium. The identified alkaloids include cocaine, trans-cinnamoylcocaine, ecgonine, ethyl ecgonine ester, benzoylecgonine, methyl ecgonine ester, and tropine. This consistency reinforces the reliability of the data obtained and underscores the relevance of alkaloids in the biochemical profile of the studied coca varieties."]),
                        dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                        html.Div(["In summary, this study not only confirms the predominance of alkaloids in coca varieties but also highlights the variability in the presence of other secondary metabolites, possibly influenced by genetic and environmental factors. These findings provide a solid foundation for future research focused on the biotechnological and pharmacological exploitation of these compounds."]),
                ],id="conclu4", className="text-none"),
                
                dbc.Row(className="espaciado_48_esc espaciado_48_mov"),
                html.Button(id='toggle-button4', children=html.Img(src='/assets/icon-mas.webp',style={'width': '48px', 'height': '48px'}), n_clicks=0, className="boton-imagen"),
                dbc.Row(className="espaciado_48_esc espaciado_48_mov"),


                html.Div("Bibliographic References",className="body-title-2",id="conclu_referen"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Adams, R., Cristol, S. J., Anderson, A. A., & Albert, A. A. (1945). The structure of leucenol.", 
                          html.Span("I. Journal of the American Chemical Society",className="italic-text"),", 67, 89–92. https://doi.org/10.1021/ja01217a032"],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Albert Niemann. (1860). Ueber eine neue organische Base in den Cocablättern.", 
                          html.Span("Archiv der Pharmazie",className="italic-text"),"153(2-3), 129–155, 291–308."],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Budavari, S. (Ed.). (1996). The Merck Index: An encyclopedia of chemicals, drugs, and biologicals (12a ed.). Merck. ISBN 0911910123.", 
                          ],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Casale, J. F., Pinero, E. L., & Corbeil, E. M. (2006). Isolation of cis-cinnamoylcocaine from crude illicit cocaine via alumina column chromatography.", 
                          html.Span("Journal of Microbiology",className="italic-text"),"4(1-4), 37-41."],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Chow, W. L., Gonzalez, M. A., Avanes, A. A., & Olson, D. E. (2023). Rapid synthesis of psychoplastogenic tropane alkaloids. JACS Au, 3(10), 2703-2708.", 
                          ],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Cognard, E., et al. (2006). [Título del artículo].", 
                          html.Span("Journal of Pharmaceutical and Biomedical Analysis",className="italic-text"),", 41, 925."],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Collins, A., & Matthews, J. C. (1983, febrero). Interactions of cocaine and cocaine congeners with sodium channels.", 
                          html.Span("Biochemical Pharmacology",className="italic-text"),", 32(3), 455–460. https://doi.org/10.1016/0006-2952(83)90523-3"],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Curry, S. H., & Marler, M. (2020, mayo). Effects of ecgonine methyl ester on cognition in scopolamine-impaired and aged rats.", 
                          html.Span("[Nombre de la revista]",className="italic-text"),", Volumen, [Páginas]."],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Dewick, P. M. (2002). Medicinal natural products: A biosynthetic approach (3ª ed.). John Wiley & Sons.", 
                          ],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Evans, W. C. (1981). The comparative phytochemistry of the genus Erythroxylon.", 
                          html.Span("Journal of Ethnopharmacology",className="italic-text"),", 3."],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Facchini, P. J., & St-Pierre, B. (2005). Synthesis and accumulation of alkaloids in pharmaceutical plants.", 
                          html.Span("Current Opinion in Plant Biology",className="italic-text"),", 8(3), 317-324."],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Findlay, S. P. (1954). The three-dimensional structure of the cocaines. Part I. Cocaine and pseudococaine.", 
                          html.Span("Journal of the American Chemical Society",className="italic-text"),", 76(11), 2855-2862."],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Gaedcke, F. (1855). Ueber das Erythroxylin, dargestellt aus den Blättern des in Südamerika.", 
                          ],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Gootenberg, P. (2009). Andean cocaine: The making of a global drug.", 
                          html.Span("University of North Carolina Press.",className="italic-text"),""],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Harris, G. C., & Sanderson, T. F. (1963). Abietic acid.", 
                          html.Span("Organic Syntheses",className="italic-text"),", 32, 1; Coll. Vol. 4:1."],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Hemel, P. B., & Chiltoskey, M. U. (1975). Cherokee plants and their uses – A 400 year history. Sylva, NC: Herald Publishing Co.; citado en Moerman,", 
                          html.Span("D. A. A database of foods, drugs, dyes and fibers of Native American peoples, derived from plants.",className="italic-text"),""],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Hoffman, R. S., Kaplan, J. L., Hung, O. L., & Goldfrank, L. R. (2004). Ecgonine methyl ester protects against cocaine lethality in mice.", 
                          html.Span("Journal of Toxicology: Clinical Toxicology",className="italic-text"),", 42(4), 349–354. https://doi.org/10.1081/clt-120039540"],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Henry, T. A. (1949). Leucenol. En The Plant Alkaloids (4ª ed., pp. 2–3).", 
                          html.Span("The Blakiston Company.",className="italic-text"),""],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Jowett, H. A. D., & Pyman, F. L. (1909). CXVI.—Relation between chemical constitution and physiological action in the tropane alkaloids. Part II.", 
                          html.Span("Journal of the Chemical Society",className="italic-text"),", Transactions, 95, 1020-1032."],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Johnson, E. L., & Emche, S. D. (1994). Variation of alkaloid content in Erythroxylum coca leaves from leaf bud to leaf drop.", 
                          html.Span("Annals of Botany",className="italic-text"),", 73(6), 645-650."],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Kutchan, T. M. (1995). Alkaloid biosynthesis—The basis for metabolic engineering of medicinal plants.", 
                          html.Span("The Plant Cell",className="italic-text"),", 7(7), 1059-1070."],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Kuroda, R., Kazumura, K., Ushikata, M., Minami, Y., & Kajiya, K. (2018). Elucidating the improvement in vascular endothelial function from Sakurajima Daikon and its mechanism of action: A comparative study with Raphanus sativus.", 
                          html.Span("Journal of Agricultural and Food Chemistry",className="italic-text"),", 66(33), 8714–8721. https://doi.org/10.1021/acs.jafc.8b04899"],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Mascré, M. (1937). Le leucaenol, principe défini retiré des graines de Leucaena glauca Benth. (Légumineuses Papilionacées).", 
                          html.Span("Comptes Rendus",className="italic-text"),", 204, 890–891."],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Matthews, J. C., & Collins, A. (1983, febrero). Interactions of cocaine and cocaine congeners with sodium channels.", 
                          html.Span("Biochemical Pharmacology",className="italic-text"),", 32(3), 455–460. https://doi.org/10.1016/0006-2952(83)90523-3"],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Meyer, E. M., Potter, L. T., De Vane, C. L., Irwin, I., MacKay, S. L., Miller, R., & Ruttenber, A. J. (1990). Effects of benzoyltropine and tropacocaine on several cholinergic processes in the rat brain.", 
                          html.Span("Journal of Pharmacology and Experimental Therapeutics",className="italic-text"),", 254(2), 584-590."],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Niemann, A. (1860). Ueber eine neue organische Base in den Cocablättern.", 
                          html.Span("Archiv der Pharmazie",className="italic-text"),"153(2-3), 129–155, 291–308."],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Nov, M., Ka, Saleminka, C. A., & Khanb, I. (n.d.). Review paper: Biological activity of the alkaloids of Erythroxylum coca and Erythroxylum novogranatense.", 
                          html.Span("",className="italic-text"),""],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Oliveira, S. L. D. (2012). Fitoquímica de espécies de Erythroxylum do semiárido: isolamento e determinação estrutural de alcaloides tropânicos, flavonoides e diterpenos.", 
                          html.Span("",className="italic-text"),""],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["O’Hagan, D. (2000). Pyrrole, pyrrolidine, pyridine, piperidine and tropane alkaloids.", 
                          html.Span("Natural Product Reports",className="italic-text"),", 17(5), 435-446. https://doi.org/10.1039/A998546A"],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Plowman, T., & Rivier, L. (1983). Cocaine and cinnamoylcocaine content of Erythroxylum species.", 
                          html.Span("Annals of Botany",className="italic-text"),", 51(5), 641-659."],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Schaffer, M., Hill, V., & Cairns, T. (2005). Hair analysis for cocaine: The requirement for effective wash procedures and effects of drug concentration and hair porosity in contamination and decontamination.", 
                          html.Span("Journal of Analytical Toxicology",className="italic-text"),", 29(5), 319–326. https://doi.org/10.1093/jat/29.5.319"],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Wink, M. (2008). Plant secondary metabolites: Occurrence, structure, and role in the human diet.", 
                          html.Span("Blackwell Publishing.",className="italic-text"),""],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Wolff, K., et al. (1999). [Título del artículo].", 
                          html.Span("Addiction",className="italic-text"),", 94, 1279."],className="body-biblio"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Xujiang, Y. U. A. N., Lijiao, M. E. N., Yadi, L. I. U., Yu, Q. I. U., Cuimin, H. E., & Huang, W. (2020). Truxillic and truxinic acid derivatives: Configuration, source, and bioactivities of natural cyclobutane dimers.", 
                          html.Span("Journal of Holistic Integrative Pharmacy",className="italic-text"),", 1(1), 48-69. https://doi.org/10.1016/j.jhip.2020.05.002"],className="body-biblio"),


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

@callback(
    Output("download-pdf", "data"),
    Input("bt-descarga", "n_clicks"),
    prevent_initial_call=True
)
def download_pdf(n_clicks):
    return dcc.send_bytes(base64.b64decode(encoded_pdf), filename=pdf_filename)

@callback(
    Output('conclu1', 'style'),
    Output('toggle-button1', 'children'),    
    [Input('toggle-button1', 'n_clicks')]
)
def toggle_paragraph(n_clicks):
    if n_clicks % 2 == 0:
        return {'display': 'none'}, html.Img(src='/assets/icon-mas.webp',style={'width': '48px', 'height': '48px'})
    else:
        return {'display': 'block'}, html.Img(src='/assets/icon-menos.webp',style={'width': '48px', 'height': '48px'})

@callback(
    Output('conclu2', 'style'),
    Output('toggle-button2', 'children'),    
    [Input('toggle-button2', 'n_clicks')]
)
def toggle_paragraph(n_clicks):
    if n_clicks % 2 == 0:
        return {'display': 'none'}, html.Img(src='/assets/icon-mas.webp',style={'width': '48px', 'height': '48px'})
    else:
        return {'display': 'block'}, html.Img(src='/assets/icon-menos.webp',style={'width': '48px', 'height': '48px'})

@callback(
    Output('conclu3', 'style'),
    Output('toggle-button3', 'children'),    
    [Input('toggle-button3', 'n_clicks')]
)
def toggle_paragraph(n_clicks):
    if n_clicks % 2 == 0:
        return {'display': 'none'}, html.Img(src='/assets/icon-mas.webp',style={'width': '48px', 'height': '48px'})
    else:
        return {'display': 'block'}, html.Img(src='/assets/icon-menos.webp',style={'width': '48px', 'height': '48px'})

@callback(
    Output('conclu4', 'style'),
    Output('toggle-button4', 'children'),    
    [Input('toggle-button4', 'n_clicks')]
)
def toggle_paragraph(n_clicks):
    if n_clicks % 2 == 0:
        return {'display': 'none'}, html.Img(src='/assets/icon-mas.webp',style={'width': '48px', 'height': '48px'})
    else:
        return {'display': 'block'}, html.Img(src='/assets/icon-menos.webp',style={'width': '48px', 'height': '48px'})

