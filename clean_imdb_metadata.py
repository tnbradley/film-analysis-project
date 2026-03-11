#!/usr/bin/env python3
"""
Clean and Merge IMDb Datasets for Film Analysis
"""
import pandas as pd
import os

os.chdir('/Users/moltatron/Downloads/imdb_datasets')

print("=" * 60)
print("IMDB DATASET CLEANING & MERGING")
print("=" * 60)

# ============================================
# 1. LOAD TITLE.BASICS (Movie Metadata)
# ============================================
print("\n📽️  Loading title.basics.tsv (this may take a moment)...")
basics = pd.read_csv('title.basics.tsv', sep='\t', na_values='\\N', low_memory=False)

print(f"   Total titles: {len(basics):,}")
print(f"   Columns: {basics.columns.tolist()}")
print(f"   Title types: {basics['titleType'].value_counts().head()}")

# Filter to movies only (not TV episodes, shorts, etc.)
movies = basics[basics['titleType'] == 'movie'].copy()
print(f"\n   Movies only: {len(movies):,}")

# Filter to movies with valid years (1900-2025)
movies = movies[(movies['startYear'] >= 1900) & (movies['startYear'] <= 2025)]
print(f"   Movies (1900-2025): {len(movies):,}")

# Select relevant columns
movies = movies[['tconst', 'primaryTitle', 'originalTitle', 'startYear', 
                 'runtimeMinutes', 'genres']].copy()

# Clean genres (split pipe-separated into list, take first 3)
movies['genres'] = movies['genres'].fillna('Unknown')
movies['primaryGenre'] = movies['genres'].str.split(',').str[0]

print(f"\n   Top genres:")
print(movies['primaryGenre'].value_counts().head(10))

# ============================================
# 2. LOAD TITLE.RATINGS (User Ratings)
# ============================================
print("\n⭐ Loading title.ratings.tsv...")
ratings = pd.read_csv('title.ratings.tsv', sep='\t', na_values='\\N')

print(f"   Total rated titles: {len(ratings):,}")
print(f"   Columns: {ratings.columns.tolist()}")
print(f"   Rating stats:")
print(ratings['averageRating'].describe())

# ============================================
# 3. LOAD TITLE.CREW (Directors/Writers)
# ============================================
print("\n🎬 Loading title.crew.tsv (this may take a moment)...")
crew = pd.read_csv('title.crew.tsv', sep='\t', na_values='\\N')

print(f"   Total crew entries: {len(crew):,}")
print(f"   Columns: {crew.columns.tolist()}")

# Count movies with directors
movies_with_directors = crew[crew['directors'].notna()]
print(f"   Titles with directors: {len(movies_with_directors):,}")

# ============================================
# 4. MERGE DATASETS
# ============================================
print("\n🔗 Merging datasets...")

# Merge movies with ratings
merged = movies.merge(ratings, on='tconst', how='inner')
print(f"   After merging with ratings: {len(merged):,}")

# Merge with crew (directors/writers)
merged = merged.merge(crew, on='tconst', how='left')
print(f"   After merging with crew: {len(merged):,}")

# ============================================
# 5. FILTER & CLEAN
# ============================================
print("\n🧹 Cleaning data...")

# Filter to movies with at least 100 votes (more reliable ratings)
merged = merged[merged['numVotes'] >= 100]
print(f"   Movies with 100+ votes: {len(merged):,}")

# Filter to movies with runtime data
merged = merged[merged['runtimeMinutes'].notna()]
print(f"   Movies with runtime: {len(merged):,}")

# Filter to recent movies (2000-2024) for relevance
merged = merged[(merged['startYear'] >= 2000) & (merged['startYear'] <= 2024)]
print(f"   Movies (2000-2024): {len(merged):,}")

# Create decade column
merged['decade'] = (merged['startYear'] // 10) * 10

# Create rating categories
def categorize_rating(rating):
    if rating >= 8.0:
        return 'Excellent (8.0+)'
    elif rating >= 7.0:
        return 'Good (7.0-7.9)'
    elif rating >= 6.0:
        return 'Average (6.0-6.9)'
    elif rating >= 5.0:
        return 'Below Average (5.0-5.9)'
    else:
        return 'Poor (<5.0)'

merged['ratingCategory'] = merged['averageRating'].apply(categorize_rating)

# Create popularity tier based on vote count
def categorize_popularity(votes):
    if votes >= 100000:
        return 'Blockbuster (100K+ votes)'
    elif votes >= 50000:
        return 'Major (50K-100K)'
    elif votes >= 10000:
        return 'Popular (10K-50K)'
    elif votes >= 1000:
        return 'Known (1K-10K)'
    else:
        return 'Niche (<1K)'

merged['popularityTier'] = merged['numVotes'].apply(categorize_popularity)

# Flag for director presence
merged['hasDirector'] = merged['directors'].notna()

# ============================================
# 6. FINAL STATS
# ============================================
print("\n📊 FINAL DATASET SUMMARY")
print("=" * 60)
print(f"Total movies: {len(merged):,}")
print(f"\nYear range: {merged['startYear'].min():.0f} - {merged['startYear'].max():.0f}")
print(f"\nRating distribution:")
print(merged['ratingCategory'].value_counts())
print(f"\nPopularity distribution:")
print(merged['popularityTier'].value_counts())
print(f"\nTop genres:")
print(merged['primaryGenre'].value_counts().head(10))
print(f"\nRuntime stats (minutes):")
print(merged['runtimeMinutes'].describe())

# ============================================
# 7. SAVE CLEANED DATASET
# ============================================
print("\n💾 Saving cleaned dataset...")

# Select final columns for analysis
final_cols = ['tconst', 'primaryTitle', 'originalTitle', 'startYear', 'decade',
              'runtimeMinutes', 'primaryGenre', 'genres', 'averageRating', 
              'numVotes', 'ratingCategory', 'popularityTier', 'hasDirector',
              'directors', 'writers']

final_df = merged[final_cols].copy()

# Save as CSV
output_path = '/Users/moltatron/Downloads/imdb_movies_cleaned.csv'
final_df.to_csv(output_path, index=False)
print(f"   ✅ Saved to: {output_path}")
print(f"   File size: {os.path.getsize(output_path) / (1024*1024):.1f} MB")

# Also save a sample for quick inspection
sample_path = '/Users/moltatron/Downloads/imdb_movies_sample.csv'
final_df.head(1000).to_csv(sample_path, index=False)
print(f"   ✅ Sample (1,000 rows) saved to: {sample_path}")

print("\n" + "=" * 60)
print("CLEANING COMPLETE!")
print("=" * 60)
print(f"\nYour dataset has {len(final_df):,} movies ready for analysis.")
print("\nKey columns for your Regal Film Analyst project:")
print("  - primaryTitle: Movie title")
print("  - startYear: Release year")
print("  - primaryGenre: Main genre")
print("  - averageRating: IMDb user rating (0-10)")
print("  - numVotes: Number of ratings (popularity proxy)")
print("  - ratingCategory: Grouped ratings")
print("  - popularityTier: Grouped by vote count")
print("  - hasDirector: Whether director data exists")
