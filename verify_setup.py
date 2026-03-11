#!/usr/bin/env python3
"""
Quick verification script for Film Analysis Project
Run this to confirm everything is set up correctly.
"""
import pandas as pd
import os

print("=" * 60)
print("🎬 FILM ANALYSIS PROJECT - SETUP VERIFICATION")
print("=" * 60)

# Check folder structure
base_path = os.path.expanduser("~/Documents/Film Analysis Project")
subfolders = ['data_raw', 'notebooks', 'outputs']

print("\n📁 Folder Structure:")
for folder in subfolders:
    path = os.path.join(base_path, folder)
    exists = "✅" if os.path.exists(path) else "❌"
    print(f"   {exists} {folder}/")

# Check data files
print("\n📊 Data Files:")
data_files = [
    'data_raw/imdb_movies_cleaned.csv',
    'data_raw/imdb_movies_sample.csv', 
    'data_raw/imdb_reviews_cleaned.csv'
]

for file in data_files:
    path = os.path.join(base_path, file)
    if os.path.exists(path):
        size_mb = os.path.getsize(path) / (1024 * 1024)
        print(f"   ✅ {file} ({size_mb:.1f} MB)")
    else:
        print(f"   ❌ {file} (missing)")

# Quick data load test
print("\n🧪 Data Load Test:")
try:
    df = pd.read_csv(os.path.join(base_path, 'data_raw/imdb_movies_cleaned.csv'))
    print(f"   ✅ Successfully loaded {len(df):,} movies")
    print(f"   ✅ Columns: {len(df.columns)} fields")
    print(f"   ✅ Year range: {df['startYear'].min():.0f} - {df['startYear'].max():.0f}")
except Exception as e:
    print(f"   ❌ Error loading data: {e}")

print("\n" + "=" * 60)
print("✨ Setup complete! You're ready to start analyzing.")
print("=" * 60)
print("\nNext steps:")
print("   1. Open notebooks/01_exploratory_analysis.ipynb")
print("   2. Run cells to explore the data")
print("   3. Create your Tableau dashboard")
print("   4. Document insights for your Regal application")
