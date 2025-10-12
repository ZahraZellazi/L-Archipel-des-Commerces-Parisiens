

<h1>📊 Analyse des Terrasses Commerciales à Paris</h1>

<h2>📌 Contexte et justification</h2>
<p>Ce projet vise à analyser les terrasses commerciales à Paris pour identifier les zones les plus denses et détecter des <b>hotspots</b> stratégiques. Il s’adresse à :</p>
<ul>
    <li>Les acteurs commerciaux ciblant des quartiers à fort potentiel de fréquentation.</li>
    <li>Les urbanistes et décideurs souhaitant réguler l’occupation de l’espace et l’aménagement urbain.</li>
    <li>Les investisseurs ou restaurateurs désirant localiser de nouvelles terrasses avec un impact maximal.</li>
</ul>
<p>L’étude se concentre sur la <b>densité, la typologie et la surface des terrasses</b>, combinée à des analyses spatiales et à des algorithmes de clustering pour révéler des zones significatives.</p>

<h2>🌐 Récupération des données via API</h2>
<p>Les données ont été récupérées directement via l’API Open Data Paris (<code>terrasses-autorisations</code>) :</p>
<pre>
dataset = "terrasses-autorisations"
base_url = f"https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/{dataset}/records"

</pre>
<p>✅ Les données sont ainsi à jour et directement exploitables pour l’analyse spatiale et le clustering.</p>

<h2>📂 Données utilisées</h2>
<ul>
    <li>Source : <a href="https://opendata.paris.fr/pages/home/" target="_blank">Open Data Paris</a></li>
    <li>Contenu : longitude, latitude, densité locale (terrasses/200m), typologie commerciale, surface des terrasses</li>
    <li>Préparation : nettoyage, standardisation (Z-score), regroupement des typologies rares en "AUTRES"</li>
</ul>

<h2>🧰 Méthodologie (CRISP-DM)</h2>
<ul>
    <li><b>Compréhension du business :</b> Identifier les zones commerciales et terrasses stratégiques à Paris.</li>
    <li><b>Compréhension des données :</b> Récupération via API, exploration statistique et géospatiale.</li>
    <li><b>Préparation des données :</b> Nettoyage, standardisation, encodage des typologies, gestion des valeurs manquantes.</li>
    <li><b>Modélisation :</b> Clustering non supervisé avec DBSCAN, OPTICS et HDBSCAN.</li>
    <li><b>Évaluation :</b> Nombre de clusters, couverture, bruit, silhouette, persistence.</li>
</ul>

<h2>🛠 Technologies et librairies</h2>
<ul>
    <li><b>Python 3.10+</b></li>
    <li><b>Data Science & ML :</b> pandas, numpy, scikit-learn, scipy, hdbscan</li>
    <li><b>Visualisation :</b> matplotlib, seaborn, plotly</li>
    <li><b>Analyse spatiale :</b> geopandas, folium, shapely</li>
    <li><b>Notebook & développement :</b> Jupyter, ipykernel, ipywidgets</li>
    <li><b>Export :</b> openpyxl</li>
    <li><b>Utilitaires :</b> python-dotenv, tqdm</li>
</ul>

<h2>⚙️ Installation</h2>
<p>1. Créer un environnement Python :</p>
<pre>
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
</pre>
<p>2. Installer les dépendances :</p>
<pre>
pip install pandas numpy matplotlib seaborn plotly geopandas folium shapely scikit-learn scipy hdbscan jupyter ipykernel ipywidgets openpyxl python-dotenv tqdm
</pre>

<h2>💻 Exécution du projet</h2>
<ul>
    <li>Lancer Jupyter Notebook : <code>jupyter notebook</code></li>
    <li>Ouvrir <code>Terrasses_Paris_Analysis.ipynb</code></li>
    <li>Les cellules sont commentées : <b>nettoyage → exploration → feature engineering → clustering → évaluation → visualisation</b></li>
    <li>Visualisations incluses :
        <ul>
            <li>Carte de densité des terrasses</li>
            <li>Top 10 hotspots avec score combiné</li>
            <li>Boxplots des surfaces par typologie</li>
            <li>Matrice de corrélation et scatter plots</li>
        </ul>
    </li>
</ul>

<h2>📈 Résultats principaux</h2>
<ul>
    <li>HDBSCAN : meilleur compromis → couverture élevée (~75%), faible bruit (~25%), clusters stables.</li>
    <li>DBSCAN : moins de clusters exploitables, beaucoup de bruit (~80%).</li>
    <li>OPTICS : bonne couverture, bruit modéré (~41%).</li>
    <li>Top 10 hotspots identifiés pour prioriser investissements et aménagements.</li>
</ul>

<h2>💡 Implications commerciales et urbaines</h2>
<ul>
    <li>Priorisation des zones à forte densité pour nouvelles terrasses ou aménagement urbain</li>
    <li>Segmentation par typologie et surface pour stratégies commerciales ciblées</li>
    <li>Support clair pour décisionnaires, même sans expertise en data science</li>
</ul>

<h2>✅ Conclusion</h2>
<p>Ce projet montre que l’analyse spatiale combinée au clustering (notamment HDBSCAN) est efficace pour détecter des hotspots de terrasses à Paris. Les résultats fournissent un support stratégique et visuel pour acteurs commerciaux et urbanistes, avec une méthodologie transparente, reproductible et basée sur CRISP-DM.</p>

<hr>
<p style="text-align:center;">📚 Projet réalisé par Zahra Zellazi - Data Science & IA Engineering student - 2025</p>

</body>
</html>
