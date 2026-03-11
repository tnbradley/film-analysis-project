#!/usr/bin/env python3
"""
Clean IMDb 50k Movie Reviews Dataset
"""
import pandas as pd
import re
import os

# Load the dataset
print("Loading IMDB Dataset...")
df = pd.read_csv('~/Downloads/IMDB Dataset.csv')

print(f"Original shape: {df.shape}")
print(f"\nColumns: {df.columns.tolist()}")
print(f"\nFirst few rows:")
print(df.head())

# Check for missing values
print(f"\n--- Missing Values ---")
print(df.isnull().sum())

# Check sentiment distribution
print(f"\n--- Sentiment Distribution ---")
print(df['sentiment'].value_counts())

# Clean the review text
print("\n--- Cleaning Review Text ---")

def clean_text(text):
    """Clean HTML tags and normalize text"""
    # Remove HTML tags
    text = re.sub(r'<br\s*/?>', ' ', text)
    text = re.sub(r'<[^>]+>', '', text)
    
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Strip and lowercase
    text = text.strip().lower()
    
    return text

df['review_clean'] = df['review'].apply(clean_text)

# Add review length metrics
df['review_length'] = df['review_clean'].str.len()
df['word_count'] = df['review_clean'].str.split().str.len()

# Convert sentiment to binary (1=positive, 0=negative)
df['sentiment_binary'] = (df['sentiment'] == 'positive').astype(int)

print(f"\n--- Review Length Stats ---")
print(df[['review_length', 'word_count']].describe())

# Sample cleaned reviews
print(f"\n--- Sample Cleaned Reviews ---")
print("\nPOSITIVE example:")
print(df[df['sentiment']=='positive']['review_clean'].iloc[0][:300] + "...")
print("\nNEGATIVE example:")
print(df[df['sentiment']=='negative']['review_clean'].iloc[0][:300] + "...")

# Save cleaned dataset
output_path = '~/Downloads/imdb_reviews_cleaned.csv'
df.to_csv(output_path, index=False)
print(f"\n✅ Cleaned dataset saved to: {output_path}")
print(f"Final shape: {df.shape}")
print(f"\nNew columns added: review_clean, review_length, word_count, sentiment_binary")
