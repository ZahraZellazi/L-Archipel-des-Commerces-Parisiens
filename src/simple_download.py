import pandas as pd
import os

print("📥 Simple Download Approach...")

# This should definitely work - direct dataset export
url = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/commerces-paris/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B"

try:
    df = pd.read_csv(url, sep=';')
    print(f"✅ SUCCESS! Downloaded {len(df)} records")
    print(f"📊 Shape: {df.shape}")
    print("🔍 Columns:")
    for col in df.columns:
        print(f"   - {col}")
    
    # Save
    os.makedirs('../processed', exist_ok=True)
    df.to_csv('../processed/paris_commerce_final.csv', index=False)
    print("💾 Data saved as '../processed/paris_commerce_final.csv'")
    
    # Quick stats
    if 'Arrondissement' in df.columns:
        print(f"🏙️ Districts: {df['Arrondissement'].nunique()}")
    
except Exception as e:
    print(f"❌ Failed: {e}")