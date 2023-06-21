import pandas as pd
import matplotlib.pyplot as plt
import os

#paths(relative)
script_dir = os.path.dirname(os.path.realpath(__file__))
data_folder = os.path.join('..', 'data')
output_dir = os.path.join(script_dir, '..', 'output')
genome_scores_file = 'genome-scores.csv'
genome_tags_file = 'genome-tags.csv'
links_file = 'links.csv'
movies_file = 'movies.csv'
ratings_file = 'ratings.csv'
tags_file = 'tags.csv'

genome_scores_path = os.path.join(data_folder, genome_scores_file)
genome_tags_path = os.path.join(data_folder, genome_tags_file)
links_path = os.path.join(data_folder, links_file)
movies_path = os.path.join(data_folder, movies_file)
ratings_path = os.path.join(data_folder, ratings_file)
tags_path = os.path.join(data_folder, tags_file)

#load data
genome_scores = pd.read_csv(genome_scores_path)
genome_tags = pd.read_csv(genome_tags_path)
links = pd.read_csv(links_path)
movies = pd.read_csv(movies_path)
ratings = pd.read_csv(ratings_path)
tags = pd.read_csv(tags_path)

#inspecting
print("Genome Scores:")
print(genome_scores.head())
print("\nGenome Tags:")
print(genome_tags.head())
print("\nLinks:")
print(links.head())
print("\nMovies:")
print(movies.head())
print("\nRatings:")
print(ratings.head())
print("\nTags:")
print(tags.head())

# Check for missing values in the movies DataFrame
print("\nMissing values in Movies:")
print(movies.isnull().sum())

# TOP 10 movies by average rating
merged_data = pd.merge(movies, ratings, on='movieId')

average_ratings = merged_data.groupby('title')['rating'].mean()

top_10_movies = average_ratings.sort_values(ascending=False).head(10)


plt.figure(figsize=(12, 6))
top_10_movies.plot(kind='bar')
plt.title('Top 10 Movies by Average Rating')
plt.xlabel('Movie Title')
plt.ylabel('Average Rating')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'top_10_rating.png'))
plt.show()

# Calculating the average rating for each movie
average_ratings_per_movie = merged_data.groupby('title')['rating'].mean()

plt.figure(figsize=(10, 5))
plt.hist(average_ratings_per_movie, bins=20, edgecolor='black')
plt.title('Distribution of Average Movie Ratings')
plt.xlabel('Average Rating')
plt.ylabel('Number of Movies')
plt.grid(axis='y')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'average_movie_ratings_distribution.png'))
plt.show()

# Count the number of ratings for each movie
number_of_ratings = merged_data.groupby('title')['rating'].count()

top_10_most_rated_movies = number_of_ratings.sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
top_10_most_rated_movies.plot(kind='bar')
plt.title('Top 10 Most Rated Movies')
plt.xlabel('Movie Title')
plt.ylabel('Number of Ratings')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'top_10_most_rated_movies.png'))
plt.show()

#Most popular tags

merged_tags = pd.merge(genome_scores, genome_tags, on='tagId')

tag_popularity = merged_tags.groupby('tag')['relevance'].sum()

top_10_popular_tags = tag_popularity.sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
top_10_popular_tags.plot(kind='bar')
plt.title('Top 10 Most Popular Movie Tags')
plt.xlabel('Tag')
plt.ylabel('Sum of Relevance Scores')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'top_10_popular_tags.png'))
plt.show()



