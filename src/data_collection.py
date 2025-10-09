import requests
import pandas as pd
import json
import os
from time import sleep

print("🚀 Starting Paris Commercial Data Collection...")

# Create processed directory if it doesn't exist
os.makedirs('../processed', exist_ok=True)

# CORRECT API Configuration
API_URL = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/commerces-paris/records"
params = {
    'limit': 100,
    'offset': 0,
    'timezone': 'UTC'
}

all_records = []
max_records = 1000  # Safety limit

try:
    # Paginated data collection
    while len(all_records) < max_records:
        print(f"📡 Fetching records {len(all_records)} to {len(all_records) + params['limit']}...")
        
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        data = response.json()
        
        records = data.get('results', [])
        if not records:
            break
            
        all_records.extend(records)
        params['offset'] += params['limit']
        
        # Small delay to be nice to the API
        sleep(0.5)
    
    print(f"✅ Success! Retrieved {len(all_records)} shops")
    
    # Convert to DataFrame
    df = pd.DataFrame(all_records)
    
    # Quick analysis
    print(f"📊 Dataset shape: {df.shape}")
    print("🔍 Columns available:")
    for col in df.columns:
        print(f"   - {col}")
    
    # Check for key columns
    if 'arrondissement' in df.columns:
        print(f"🏙️ Districts: {df['arrondissement'].nunique()}")
    
    if 'categorie' in df.columns:
        print("🏷️ Top Categories:")
        print(df['categorie'].value_counts().head(10))
    
    # Save to processed folder
    output_path = '../processed/paris_commerce_raw.csv'
    df.to_csv(output_path, index=False, encoding='utf-8')
    print(f"💾 Data saved as '{output_path}'")
    
    # Also save a sample for quick inspection
    sample_path = '../processed/paris_commerce_sample.csv'
    df.head(100).to_csv(sample_path, index=False, encoding='utf-8')
    print(f"🔍 Sample saved as '{sample_path}'")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("💡 Trying alternative API endpoint...")
    
    # Alternative approach - try different dataset
    try:
        alt_url = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/commerces-de-detail-paris/records"
        response = requests.get(alt_url, params={'limit': 100})
        if response.status_code == 200:
            print("✅ Alternative endpoint works! Adjusting...")
            # You can modify the script to use this endpoint
    except:
        print("❌ Alternative endpoint also failed")