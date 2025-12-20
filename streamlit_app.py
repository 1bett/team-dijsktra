import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import math
from streamlit_option_menu import option_menu 

st.set_page_config(page_title="Apprendre Dijkstra", layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "Accueil"

def set_page(name):
    st.session_state.page = name 




st.sidebar.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"> 
    <h2 style='color:white'><i class="fa-solid fa-bars"></i> Menu</h2>
""", unsafe_allow_html=True)


st.markdown("""
<style>
    /* Sidebar background */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0e1a3b, #162447) !important;
        padding: 20px 10px !important;
        border-top-right-radius: 25px;
        border-bottom-right-radius: 25px;
    }

    /* Fix height */
    section[data-testid="stSidebar"] > div {
        height: 100vh;
        overflow-y: auto;
    }
</style>
""", unsafe_allow_html=True)

# ====== Option Menu ======
with st.sidebar:
    selected = option_menu(
        menu_title="",
        options=["Accueil", "À propos", "Théorie", "Exemples", "Dijkstra"],
        icons=["house", "info-circle", "book", "shapes", "123"],
        default_index=0,
        styles={
            "container": {
                "padding": "0!important",
                "background": "transparent"
            },
            "icon": {
                "color": "white",
                "font-size": "20px"
            },
            "nav-link": {
                "background-color":"#162447",
                "color": "white",
                "font-size": "17px",
                "text-align": "left",
                "margin": "0",
                "border-radius": "0px",
                "padding": "10px 15px",
            },
           
            "nav-link-selected": {
                "background-color": "#00ccff",
                "color": "white",
                "font-weight": "bold"
            }
        }
    )

if selected == "Accueil":
        st.markdown("""
        <div style="padding:20px; background:#0e1a3b; border-radius:12px; color:white;">
            <h1>Apprendre l'Algorithme de Dijkstra</h1>
            <p>Une application interactive pour visualiser et comprendre le plus court chemin.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            ### <i class="fa-solid fa-star" style="color:#f1c40f;"></i> Pourquoi cette application ?
            """, unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        c1.info("**Théorie illustrée**\nComprendre Dijkstra étape par étape.")
        c2.success("**Calcul manuel**\nTester vos propres matrices de poids.")
        c3.warning("**Exemples prêts**\nExplorer différents graphes déjà configurés.")

        st.markdown("""
                ### Comment utiliser cette application ?
                1. Allez dans **Dijkstra**  
                2. Entrez les **sommets** et la **matrice des poids**  
                3. Choisissez **départ** et **arrivée**  
                4. Cliquez sur **Calculer**  
                5. Visualisez les étapes et le graphe  
                """)


elif selected == "À propos":
        st.markdown("""
        <style>
        .apropos-card {
            background: #0f1b3d;
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 16px;
            padding: 28px;
            max-width: 900px;
            margin: 20px auto;
            color: #eaf2ff;
            box-shadow: 0 10px 30px rgba(0,0,0,0.25);
        }
        .apropos-card h2 {
            color: #00ccff;
            margin: 0 0 12px 0;
            font-weight: 700;
        }
        .apropos-card h3 {
            color: #9bdcff;
            margin: 18px 0 8px 0;
            font-weight: 600;
        }
        .apropos-card ul {
            list-style: none;
            padding-left: 0;
            margin: 8px 0 0 0;
        }
        .apropos-card ul li::before {
            content: "•";
            color: #00ccff;
            margin-right: 8px;
        }
        .apropos-card .signature {
            margin-top: 22px;
            color: #b7c6e6;
            font-style: italic;
            border-top: 1px solid rgba(255,255,255,0.08);
            padding-top: 12px;
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown('<div class="apropos-card">', unsafe_allow_html=True)
        
      



        col1, col2,col3,col4 = st.columns(4) 
        with col1:
            st.markdown("<b style='color: #1E3A8A; font-size:30px;'> Chef de projet</b>", unsafe_allow_html=True)
            st.markdown("<b>Salah-Eddine Bechari</b>", unsafe_allow_html=True)
        with col2:
            st.markdown("<b style='color: #10B981; font-size:30px;'> Développement et codage</b>", unsafe_allow_html=True)
            st.markdown("<b>IBTIHAL MERIMI </b>: Algorithmes et Backend<br><b>Souhail Bouazzaoui , Nouhaila Yazidi , Manal Zamraoui </b>: Frontend", unsafe_allow_html=True)
        with col3:
            st.markdown("<b style='color: #8B5CF6;font-size:30px;'>Documentation et organisation</b>", unsafe_allow_html=True)
            st.markdown("<b>Raouaa Hachmi, Ouafae Rhomari , Doae Rahhaoui</b>", unsafe_allow_html=True)
        with col4:
            st.markdown("<b style=' color: #F59E0B;font-size:30px;'>Rédaction et mise en page du rapport</b>", unsafe_allow_html=True)
            st.markdown("<b> Youness Maimouni , Salah-Eddine Bechari , Noumidia Rotbi</b>", unsafe_allow_html=True)
        
           

 
       

        st.markdown('<b style="font-size:30px;">Objectif du projet</b>', unsafe_allow_html=True)
        st.markdown("""
        <span style="color:#333333;">
        Ce projet a été conçu pour permettre à chacun de mieux comprendre et appliquer l'algorithme de Dijkstra.  
        Concrètement, il vous permet de :  <br>
        - Visualiser facilement une matrice de poids d’un graphe.<br>  
        - Trouver le plus court chemin entre deux points grâce à Dijkstra.<br>  
        - Suivre toutes les étapes du calcul de manière claire et pédagogique.
        </span>
        """, unsafe_allow_html=True)

        st.markdown('<b style="font-size:30px;">Démarche pédagogique</b>', unsafe_allow_html=True)
        st.markdown("""
        <span style="color:#333333;">
        L’idée est de rendre l’apprentissage interactif et intuitif : <br> 
        - Une interface simple et facile à utiliser.  <br>
        - Des explications intégrées pour chaque étape.  <br>
        - Des exemples concrets que vous pouvez tester vous-même.  <br>
        - La possibilité de suivre le calcul étape par étape, comme si vous le faisiez à la main.
        </span>
        """, unsafe_allow_html=True)

        st.markdown('<b style="font-size:30px;;">Technologies utilisées</b>', unsafe_allow_html=True)
        st.markdown("""
        <span style="color:#333333;">
        Pour réaliser ce projet, nous avons utilisé : <br> 
        - <b>Python et Streamlit </b>pour créer l’interface interactive.<br>  
        - <b>Pandas, NetworkX et Matplotlib </b>pour gérer et visualiser les graphes. <br> 
        - Un peu de <b>CSS </b>pour personnaliser l’affichage et le rendre agréable.
        </span>
        """, unsafe_allow_html=True)


        st.markdown('</div>', unsafe_allow_html=True)



elif selected == "Théorie":
   
    st.markdown("""
    <div style="padding:20px; background:#0e1a3b; border-radius:12px; color:white;">
        <h1> Théorie : Algorithme de Dijkstra</h1>
        <p>L’algorithme de Dijkstra est une méthode pour trouver le plus court chemin 
        dans un graphe pondéré avec des poids positifs.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("###  Les notions clés")
    c1, c2, c3 = st.columns(3)
    c1.info("🔵 **Sommet (nœud)** : point du graphe")
    c2.success("🟢 **Arête** : lien entre deux sommets")
    c3.warning("⚖️ **Poids** : coût ou distance associée à une arête")

    st.markdown("""
    - **Y** : ensemble des sommets déjà traités  
    - **Ȳ** : ensemble des sommets restants  
    - **Tableau des distances** : valeurs minimales connues pour atteindre chaque sommet
    """)

    st.markdown("###   Étapes de l’algorithme")
    st.markdown("""
    1. Initialiser les distances (0 pour le départ, ∞ pour les autres).  
    2. Ajouter le nœud de départ à **Y**.  
    3. Mettre à jour les distances des voisins.  
    4. Choisir le nœud avec la plus petite distance dans **Ȳ**.  
    5. Répéter jusqu’à ce que tous les sommets soient traités.  
    """)

  

    G = nx.Graph()
    G.add_edge("A", "B", weight=1)
    G.add_edge("A", "C", weight=4)
    G.add_edge("B", "C", weight=2)
    G.add_edge("B", "D", weight=6)
    G.add_edge("C", "D", weight=3)

    pos = nx.spring_layout(G)
    plt.figure(figsize=(6,4))
    nx.draw(G, pos, with_labels=True, node_color="#00ccff", node_size=800, font_size=12)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    st.pyplot(plt)

    st.markdown("###   Remarques importantes")
    st.info("L’algorithme ne fonctionne pas avec des poids négatifs.")
    st.success(" Utilisé en GPS, réseaux, planification et optimisation.")

elif selected == "Exemples":
    st.markdown("""
    <div style="padding:20px; background:#0e1a3b; border-radius:12px; color:white;">
        <h1>  Exemple : Algorithme de Dijkstra</h1>
    </div>
    """, unsafe_allow_html=True)
    st.title("") 
    col1, col2 = st.columns([1,2])

    with col1:
         

     with col2:
            st.image("Dijsktra.png", caption="Graphe de l'exemple (1→6)", width=500)

    st.markdown("""
<h3 style="
    font-weight:700;
    background: ;
    color: black;
">
    Étapes détaillées avec r(j) (Γ(j)) et min
</h3>
""", unsafe_allow_html=True)


    st.markdown("**(a) Initialisation**")
    c1, c2, c3, c4 = st.columns([1,1,2,2])
    c1.markdown("✅ **Y = {1}**")
    c2.markdown("🟠 **Ȳ = {2, 3, 4, 5, 6}**")
    c3.write({
        "D(1)": 0,
        "D(2)": 8,
        "D(3)": 1,
        "D(4)": "∞",
        "D(5)": "∞",
        "D(6)": "∞"
    })
    c4.markdown("🔵 **r(1) = Γ(1)** : {2, 3}")

    st.markdown("**(b) Sélection du minimum**")
    c1, c2, c3, c4 = st.columns([1,1,2,2])
    c1.markdown("✅ **Y = {1, 3}**")
    c2.markdown("🟠 **Ȳ = {2, 4, 5, 6}**")
    c3.write({
        "D(2)": 8,
        "D(3)": 1,
        "D(4)": "∞",
        "D(5)": "∞",
        "D(6)": "∞"
    })
    c4.markdown("🔵 **r(3) = Γ(3)** : {2, 5, 6}")
    st.markdown("🔴 min D(i) = D(3) = 1 → j = 3")


    st.markdown("**(c) Relaxation depuis j=3**")
    c1, c2, c3, c4 = st.columns([1,1,2,2])
    c1.markdown("✅ **Y = {1, 3}**")
    c2.markdown("🟠 **Ȳ = {2, 4, 5, 6}**")
    c3.write({
        "i=2": "D(2) = min{8, 1+5} = 6",
        "i=5": "D(5) = min{∞, 1+2} = 3",
        "i=6": "D(6) = min{∞, 1+7} = 8"
    })
    c4.write({
        "D(2)": 6,
        "D(5)": 3,
        "D(6)": 8,
        "D(4)": "∞"
    })

    # Étape suivante — Sélection de 5
    st.markdown("**(b) min D(i) = D(5) = 3 → j = 5**")
    c1, c2, c3, c4 = st.columns([1,1,2,2])
    c1.markdown("✅ **Y = {1, 3, 5}**")
    c2.markdown("🟠 **Ȳ = {2, 4, 6}**")
    c3.write({
        "D(2)": 6,
        "D(4)": "∞",
        "D(6)": 8
    })
    c4.markdown("🔵 **r(5) = Γ(5)** : {2, 4}")

    # Relaxation depuis j=5
    st.markdown("**(c) Relaxation depuis j=5**")
    c1, c2, c3, c4 = st.columns([1,1,2,2])
    c1.markdown("✅ **Y = {1, 3, 5}**")
    c2.markdown("🟠 **Ȳ = {2, 4, 6}**")
    c3.write({
        "i=2": "D(2) = min{6, 3+2} = 5",
        "i=4": "D(4) = min{∞, 3+5} = 8"
    })
    c4.write({
        "D(2)": 5,
        "D(4)": 8,
        "D(6)": 8
    })

    # Étape suivante — Sélection de 2
    st.markdown("**(b) min D(i) = D(2) = 5 → j = 2**")
    c1, c2, c3, c4 = st.columns([1,1,2,2])
    c1.markdown("✅ **Y = {1, 3, 5, 2}**")
    c2.markdown("🟠 **Ȳ = {4, 6}**")
    c3.write({
        "D(4)": 8,
        "D(6)": 8
    })
    c4.markdown("🔵 **r(2) = Γ(2)** : {4, 6}")

    # Relaxation depuis j=2
    st.markdown("**(c) Relaxation depuis j=2**")
    c1, c2, c3, c4 = st.columns([1,1,2,2])
    c1.markdown("✅ **Y = {1, 3, 5, 2}**")
    c2.markdown("🟠 **Ȳ = {4, 6}**")
    c3.write({
        "i=4": "D(4) = min{8, 5+3} = 8",
        "i=6": "D(6) = min{8, 5+1} = 6"
    })
    c4.write({
        "D(4)": 8,
        "D(6)": 6
    })

    # Étape suivante — Sélection de 6
    st.markdown("**(b) min D(i) = D(6) = 6 → j = 6**")
    c1, c2, c3, c4 = st.columns([1,1,2,2])
    c1.markdown("✅ **Y = {1, 3, 5, 2, 6}**")
    c2.markdown("🟠 **Ȳ = {4}**")
    c3.write({
        "D(4)": 8
    })
    c4.markdown("🔵 **r(6) = Γ(6)** : ∅")

    # Étape finale — Sélection de 4
    st.markdown("**(b) min D(i) = D(4) = 8 → j = 4**")
    c1, c2, c3, c4 = st.columns([1,1,2,2])
    c1.markdown("✅ **Y = {1, 3, 5, 2, 6, 4}**")
    c2.markdown("🟠 **Ȳ = ∅**")
    c3.write({
        "D(4)": 8
    })
    c4.markdown("🔵 **r(4) = Γ(4)** : (non utilisé)")

    
    st.success("Plus court chemin entre 1 et 6 : {1 → 3 → 5 → 2 → 6} (Distance : 6)")


elif selected == "Dijkstra":
   
    st.title("     Algorithme de Dijkstra")

    st.markdown("<h2 style='color:#0d47a1;'> Matrice des poids entre sommets</h2>", unsafe_allow_html=True)
    
    st.sidebar.markdown(
        "<span style='color:white; font-weight:bold;'>🧠 Sommets (ex: A,B,C,D)</span>",
        unsafe_allow_html=True
    )
    nodes_input = st.sidebar.text_input("", value="A,B,C,D")
    nodes = [s.strip() for s in nodes_input.split(",") if s.strip()]

    if len(nodes) >= 2:
        
        matrix = pd.DataFrame(0, index=nodes, columns=nodes)
        st.markdown("""
        <div style="background-color:#e3f2fd; padding:15px; border-radius:10px; margin-bottom:20px;">
        <h4 style="color:#1565c0; font-family:Segoe UI;">Remplissez la matrice des poids entre sommets</h4>
        <p style="color:#555;">Entrez les valeurs directement dans le tableau ci-dessous. Les cases vides ou 0 signifient qu'il n'y a pas d'arête.</p>
        </div>
        """, unsafe_allow_html=True)
       
        edited = st.data_editor(matrix, use_container_width=True, num_rows="dynamic")
        st.markdown("""
        <style>
    /* Bouton personnalisé */
    div.stButton > button:first-child {
        background-color: #1565c0;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 8px 16px;
        border: none;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
    }
    div.stButton > button:first-child:hover {
        background-color: #0d47a1;
        color: #fff;
    }

    /* Selectbox personnalisé */
    div[data-testid="stSelectbox"] > div {
        background-color: #e3f2fd;
        border-radius: 6px;
        padding: 4px;
    }
    div[data-testid="stSelectbox"] label {
        color: #1565c0;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        c1.markdown("<p style='color:blue; font-size:18px; font-weight:600;'>Nœud de départ</p>", unsafe_allow_html=True)
        start = c1.selectbox("", nodes)
        c2.markdown("<p style='color:blue; font-size:18px; font-weight:600;'>Nœud d'arrivée</p>", unsafe_allow_html=True)
        end = c2.selectbox(" ", nodes)

        if st.button("Calculer le plus court chemin"):
            
            graph = {}
            for i in nodes:
                graph[i] = {}
                for j in nodes:
                    w = edited.at[i, j]
                    if i != j and w > 0:
                        graph[i][j] = w

            # ⚙️ Algorithme de Dijkstra
            def dijkstra_etapes(g, start):
                X = list(g.keys())
                Y = set()
                D = {i: math.inf for i in X}
                parent = {i: None for i in X}
                D[start] = 0
                Y.add(start)
                for succ, w in g.get(start, {}).items():
                    if w < D[succ]:
                        D[succ] = w
                        parent[succ] = start
                barY = set(X) - Y
                steps = []
                steps.append({"Y": Y.copy(), "barY": barY.copy(), "D": D.copy()})
                while barY:
                    j = min(barY, key=lambda node: D[node])
                    if D[j] == math.inf:
                        Y.add(j)
                        barY.remove(j)
                        steps.append({"Y": Y.copy(), "barY": barY.copy(), "D": D.copy()})
                        break
                    barY.remove(j)
                    Y.add(j)
                    for i, w in g.get(j, {}).items():
                        if D[j] + w < D[i]:
                            D[i] = D[j] + w
                            parent[i] = j
                    steps.append({"Y": Y.copy(), "barY": barY.copy(), "D": D.copy()})
                return D, parent, steps

            distances, parent, steps = dijkstra_etapes(graph, start)
            dist = distances[end]

            if dist == math.inf or parent[end] is None:
                st.error("Aucun chemin atteignable entre le départ et l’arrivée.")
            else:
                path = []
                cur = end
                while cur is not None:
                    path.append(cur)
                    if cur == start:
                        break
                    cur = parent[cur]
                path.reverse()
                st.success(f" Chemin trouvé : {' → '.join(path)} (Distance : {dist})")

                                    
                
                st.markdown("""
                <style>
                .step-title {
                    font-size: 22px;
                    font-weight: bold;
                    color: #008CFF;
                    margin-top: 25px;
                    margin-bottom: 10px;
                }

                .data-box {
                    background: #f7faff;
                    padding: 10px 14px;
                    border-radius: 8px;
                    border-left: 4px solid #008CFF;
                    font-size: 16px;
                    margin-bottom: 10px;
                }
                </style>
                """, unsafe_allow_html=True)

               
                st.subheader("Étapes de l’algorithme Dijkstra ")

                for k, s in enumerate(steps):

                   
                    st.markdown(f"<div class='step-title'>Étape {k+1}</div>", unsafe_allow_html=True)

                    
                    c1, c2, c3 = st.columns([1, 1, 2])

                    
                    c1.markdown(f"<div class='data-box'><b>Y :</b> {s['Y']}</div>", unsafe_allow_html=True)

                    
                    c2.markdown(f"<div class='data-box'><b>Ȳ :</b> {s['barY']}</div>", unsafe_allow_html=True)

                    
                    df = pd.DataFrame.from_dict(s["D"], orient="index", columns=["Distance"])
                    df = df.astype(object)  

                    
                    def format_val(x):
                        if x == math.inf or x == "∞":
                            return "∞"
                        try:
                            return int(x) 
                        except:
                            return x

                    df["Distance"] = df["Distance"].apply(format_val)

                    
                    styled_df = df.style.applymap(
                        lambda v: "color: #999; font-style: italic;" if v == "∞" else ""
                    )

                   
                    c3.markdown("**Distances actuelles :**")
                    c3.dataframe(styled_df, use_container_width=True)


            
            G = nx.DiGraph()
            for i in nodes:
                for j, w in graph[i].items():
                    G.add_edge(i, j, weight=w)

            pos = nx.kamada_kawai_layout(G)  

            
            color_map = []
            for node in G.nodes():
                if node == start:
                    color_map.append("green")
                elif node == end:
                    color_map.append("orange")
                else:
                    color_map.append("#00B4D8")

            plt.figure(figsize=(10, 8))
            nx.draw(G, pos, with_labels=True, node_color=color_map, node_size=900, edge_color="gray", arrows=True)

            
            edge_labels = nx.get_edge_attributes(G, 'weight')
            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

            
            if dist != math.inf and parent[end] is not None:
                path_edges = list(zip(path, path[1:]))
                nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=3, arrows=True)

            st.pyplot(plt)

    else:
        st.info(" Entrez au moins deux sommets pour commencer.")



