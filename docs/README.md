<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>📊 Analyse des Terrasses à Paris - README</title>
<style>
    body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; color: #333; line-height: 1.6; }
    h1 { text-align: center; color: #FECA55; font-size: 36px; font-weight: bold; margin-bottom: 20px; }
    h2 { color: #EF806C; font-size: 28px; font-weight: bold; margin-top: 30px; }
    h3 { color: #00FFFF; font-size: 22px; margin-top: 20px; }
    ul { margin-left: 20px; }
    li { margin: 8px 0; }
    p { margin: 10px 0; }
    code { background-color: #eee; padding: 2px 5px; border-radius: 3px; }
    pre { background-color: #eee; padding: 10px; border-radius: 5px; overflow-x: auto; }
    table { border-collapse: collapse; margin-top: 20px; width: 100%; }
    th, td { border: 1px solid #ccc; padding: 10px; text-align: center; }
    th { background-color: #EF806C; color: white; }
    hr { height: 2px; border: none; background-color: #FECA55; margin: 20px 0; }
</style>
</head>
<body>

<h1>📊 Analyse des Terrasses à Paris</h1>

<h2>📌 Contexte du projet</h2>
<p>Ce projet a pour objectif d’analyser les terrasses commerciales à Paris afin d’identifier les zones les plus denses et de détecter des <b>hotspots</b> stratégiques. L’étude est conçue pour :</p>
<ul>
    <li>• Les acteurs commerciaux souhaitant cibler des quartiers à fort potentiel de fréquentation.</li>
    <li>• Les urbanistes et décideurs publics cherchant à réguler l’occupation de l’espace et l’aménagement urbain.</li>
    <li>• Les investisseurs ou restaurateurs souhaitant localiser de nouvelles terrasses avec un impact maximal.</li>
</ul>
<p>L’angle d’étude choisi se concentre sur la <b>densité, la typologie et la surface des terrasses</b>, combiné à des analyses spatiales et à des algorithmes de clustering pour révéler les zones significatives.</p>

<h2>📂 Données utilisées</h2>
<ul>
    <li>Source : <a href="https://opendata.paris.fr/pages/home/" target="_blank">Open Data Paris</a></li>
    <li>Contenu : longitude, latitude, densité locale (terrasses/200m), typologie commerciale, surface des terrasses</li>
    <li>Préparation : nettoyage, standardisation (Z-score), regroupement des typologies rares en "AUTRES"</li>
</ul>

<h2>🛠 Technologies et librairies</h2>
<ul>
    <li><b>Python 3.10+</b></li>
    <li><b>Data Science & ML :</b> pandas, numpy, scikit-learn, scipy, hdbscan</li>
    <li><b>Visualisation :</b> matplotlib, seaborn, plotly</li>
    <li><b>Analyse spatiale :</b> geopandas, folium, shapely</li>
    <li><b>Notebook & développement :</b> Jupyter, ipykernel, ipywidgets</li>
    <li><b>Export :</b> openpyxl</li>
</ul>

<h2>⚙️ Installation</h2>
<p>1. Créer un environnement Python (recommandé avec conda ou venv) :</p>
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
<p>1. Lancer le Jupyter Notebook :</p>
<pre>
jupyter notebook
</pre>
<p>2. Ouvrir le fichier principal <code>Terrasses_Paris_Analysis.ipynb</code></p>
<p>3. Les cellules sont commentées étape par étape : <b>nettoyage des données → analyse exploratoire → feature engineering → clustering → évaluation → visualisations</b></p>
<p>4. Les visualisations incluent :</p>
<ul>
    <li>Carte de densité des terrasses</li>
    <li>Top 10 hotspots avec score combiné</li>
    <li>Boxplots des surfaces par typologie</li>
    <li>Matrice de corrélation et scatter plots</li>
</ul>

<h2>📊 Méthodologie</h2>
<ul>
    <li>Nettoyage et préparation des données</li>
    <li>Standardisation des features continues</li>
    <li>Application de 3 algorithmes de clustering non supervisé : DBSCAN, OPTICS, HDBSCAN</li>
    <li>Évaluation des clusters via nombre de clusters, couverture, bruit, silhouette et persistence</li>
    <li>Visualisation interactive pour interprétation et communication des résultats</li>
</ul>

<h2>📈 Résultats principaux</h2>
<ul>
    <li>HDBSCAN fournit le meilleur compromis : couverture élevée (~75%), faible bruit (~25%) et persistance pour clusters stables.</li>
    <li>DBSCAN détecte moins de clusters exploitables et génère beaucoup de bruit (~80%).</li>
    <li>OPTICS améliore la couverture mais conserve un bruit relativement élevé (~41%).</li>
    <li>Top 10 hotspots identifiés, utiles pour prioriser les investissements et aménagements commerciaux.</li>
</ul>

<h2>💡 Implications commerciales et urbaines</h2>
<ul>
    <li>Priorisation des zones à forte densité pour implanter de nouvelles terrasses ou optimiser l’aménagement urbain</li>
    <li>Segmentation par typologie et surface pour adapter les stratégies commerciales</li>
    <li>Support clair et visuel pour décisionnaires même sans expertise en data science</li>
</ul>

<h2>✅ Conclusion</h2>
<p>Ce projet démontre que l’analyse spatiale combinée à des algorithmes de clustering (notamment HDBSCAN) est efficace pour détecter des hotspots de terrasses à Paris. Les résultats fournissent des informations stratégiques pour acteurs commerciaux et urbanistes, avec une méthodologie transparente et reproductible.</p>

<hr>
<p style="text-align:center;">📚 Projet réalisé par [Ton Nom] - Data Science & Analyse Spatiale - 2025</p>

</body>
</html>
