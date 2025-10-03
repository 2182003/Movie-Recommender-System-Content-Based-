# Movie Recommender System (Content-Based)

A Content-Based Movie Recommender System that suggests movies based on their metadata: genres, keywords, cast, crew, and overview.

It uses Natural Language Processing (NLP) and cosine similarity to find movies similar to a given movie.


# Table of Contents

Project Overview

Dataset

Data Preprocessing

Feature Engineering

Text Vectorization

Similarity Calculation

Movie Recommendation

Saving Model

Libraries Used

# Project Overview

Movie recommendation helps users discover relevant films from large collections.

Input: Movie title

Output: Top 5 recommended movies similar to the input

This project is content-based, meaning it recommends movies by analyzing their features, not user ratings.


# 📂 Dataset

Dataset source: TMDB (The Movie Database)

Files used:
tmdb_5000_movies.csv,
tmdb_5000_credits.csv

Relevant columns:movie_id,title,overview,genres,keywords,cast,crew



# Data Preprocessing

Steps performed:

Merged movies and credits datasets on title.

Selected relevant columns.

Dropped missing values and duplicates.

Converted JSON-like strings in genres, keywords, cast, and crew to Python lists.

Kept only top 3 cast members and director in crew.

Removed spaces from names to maintain consistency.

Combined all features into a single column: tags.



# Feature Engineering

Converted tags to lowercase.

Applied stemming using NLTK’s PorterStemmer to reduce words to their root.

Final tags column = overview + genres + keywords + cast + crew.



# Text Vectorization

Used CountVectorizer (max features = 5000, stop words = English).

Converted tags into numerical vectors representing movie features.




# Similarity Calculation

Used cosine similarity to calculate similarity between movies based on their vectorized tags.

Created a similarity matrix storing pairwise movie similarities.

# Movie Recommendation

Function recommend(movie) takes a movie title and returns top 5 similar movies.



# Libraries Used

numpy

pandas

matplotlib

seaborn

scikit-learn (CountVectorizer, cosine_similarity)

nltk (PorterStemmer)

pickle

# Dataset link
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata