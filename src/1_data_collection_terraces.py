import requests
import pandas as pd
import os
import time

print("🏪 Téléchargement des données des terrasses commerciales...")

# LE VRAI NOM DU DATASET
dataset = "terrasses-autorisations"
base_url = f"https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/{dataset}/records"

all_records = []
limit = 100  # Plus petit pour éviter les erreurs
offset = 0
max_records = 5000  # Pour tester rapidement

try:
    while offset < max_records:
        print(f"📡 Récupération {offset} à {offset + limit}...")
        
        url = f"{base_url}?limit={limit}&offset={offset}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            records = data.get('results', [])
            
            if not records:
                print("✅ Plus d'enregistrements à récupérer")
                break
                
            all_records.extend(records)
            offset += limit
            
            # Petite pause
            time.sleep(0.1)
        else:
            print(f"❌ Erreur {response.status_code}")
            break
    
    print(f"✅ Succès ! {len(all_records)} terrasses récupérées")
    
    # Conversion en DataFrame
    df = pd.DataFrame(all_records)
    
    # Sauvegarde
    os.makedirs('data/raw', exist_ok=True)
    os.makedirs('data/processed', exist_ok=True)
    
    raw_path = 'data/raw/terrasses_paris.csv'
    processed_path = 'data/processed/terrasses_paris_clean.csv'
    
    df.to_csv(raw_path, index=False, encoding='utf-8')
    df.to_csv(processed_path, index=False, encoding='utf-8')
    
    print(f"💾 Données sauvegardées dans {raw_path}")
    print(f"📊 Shape: {df.shape}")
    
    # Analyse des données
    print("\n🔍 ANALYSE DES DONNÉES RÉCUPÉRÉES:")
    print(f"   - Total: {len(df)} enregistrements")
    print(f"   - Colonnes: {df.columns.tolist()}")
    
    if 'arrondissement' in df.columns:
        print(f"   - Arrondissements: {df['arrondissement'].nunique()}")
        print(f"   - Top arrondissements: {df['arrondissement'].value_counts().head()}")
    
    if 'typologie' in df.columns:
        print(f"   - Types de terrasses: {df['typologie'].value_counts().head()}")
    
    if 'geo_point_2d' in df.columns:
        print(f"   - Données géolocalisées: OUI")
    
    print(f"\n🎯 DONNÉES PARFAITES POUR VOTRE PROJET!")
    print("   Vous pouvez maintenant analyser les clusters de terrasses parisiens")
    
except Exception as e:
    print(f"❌ Erreur: {e}")