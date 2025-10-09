import requests
import pandas as pd
import json
import os

print("🚀 Starting Paris Commercial Data Collection...")

# Create processed directory if it doesn't exist
os.makedirs('../processed', exist_ok=True)

# API Configuration
API_URL = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/commerces-de-detail/records"
params = {
    'limit': 10000,
    'offset': 0
}

try:
    # API Call
    response = requests.get(API_URL, params=params)
    response.raise_for_status()
    data = response.json()
    
    print(f"✅ Success! Retrieved {len(data.get('results', []))} shops")
    
    # Convert to DataFrame
    df = pd.DataFrame(data['results'])
    
    # Quick analysis
    print(f"📊 Dataset shape: {df.shape}")
    print(f"🏙️ Districts: {df['arrondissement'].nunique()}")
    print("🏷️ Top Categories:")
    print(df['categorie'].value_counts().head(10))
    
    # Save to processed folder
    output_path = '../processed/paris_commerce_raw.csv'
    df.to_csv(output_path, index=False)
    print(f"💾 Data saved as '{output_path}'")
    
except Exception as e:
    print(f"❌ Error: {e}")