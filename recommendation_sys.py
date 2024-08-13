import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Sample data: User ratings for movies
data = {
    'user': ['Aayush', 'Aayush', 'Aayush', 'Rashika', 'Rashika', 'Manan', 'Manan', 'Alice'],
    'movie': ['Batman', 'Deadpool', 'Spiderman', 'Batman', 'Spiderman', 'Deadpool', 'Spiderman', 'Batman'],
    'rating': [5, 4, 4, 5, 3, 4, 5, 2]
}
df = pd.DataFrame(data)

# Creating a user-movie matrix
user_movie_matrix = df.pivot(index='user', columns='movie', values='rating').fillna(0)

# Computing similarity between users
user_similarity = cosine_similarity(user_movie_matrix)
user_similarity_df = pd.DataFrame(user_similarity, index=user_movie_matrix.index, columns=user_movie_matrix.index)

def recommend_movies(user, user_movie_matrix, user_similarity_df, top_n=3):
    """
    Recommend movies to a user based on the ratings of similar users.
    
    Args:
        user (str): The username for whom recommendations are to be made.
        user_movie_matrix (pd.DataFrame): User-movie matrix with ratings.
        user_similarity_df (pd.DataFrame): DataFrame with user similarity scores.
        top_n (int): Number of top recommendations to return.

    Returns:
        list: A list of recommended movies.
    """
    if user not in user_movie_matrix.index:
        return f"User '{user}' not found in the dataset."
    
    # Getting similar users sorted by similarity
    similar_users = user_similarity_df[user].sort_values(ascending=False).index
    similar_users = similar_users[similar_users != user]  # Exclude the user itself

    print(f"Similar users to {user}: {similar_users.tolist()}")
    
    recommended_movies = {}
    
    for similar_user in similar_users:
        similar_user_ratings = user_movie_matrix.loc[similar_user]
        print(f"Ratings by {similar_user}:")
        print(similar_user_ratings)
        
        for movie, rating in similar_user_ratings.items():
            # Only consider movies that the user has not rated
            if rating > 0 and user_movie_matrix.loc[user, movie] == 0:
                if movie not in recommended_movies:
                    recommended_movies[movie] = 0
                # Aggregate the score based on similarity and rating
                recommended_movies[movie] += rating * user_similarity_df.loc[user, similar_user]

    # Printing aggregated scores for debugging
    print(f"Aggregated movie scores: {recommended_movies}")
    
    # Sorting movies based on the aggregated score and return top_n recommendations
    if not recommended_movies:
        return "No recommendations available."

    recommended_movies = sorted(recommended_movies.items(), key=lambda x: x[1], reverse=True)
    
    return [movie for movie, _ in recommended_movies[:top_n]]

def main():
    """
    Main function to run the recommendation system.
    """
    print("Welcome to the Movie Recommendation System!")
    
    # Input from the terminal
    user = input("Enter the user name for recommendations (e.g., Alice): ").strip()
    try:
        top_n = int(input("Enter the number of recommendations to provide (e.g., 3): ").strip())
        if top_n <= 0:
            raise ValueError("Number of recommendations must be a positive integer.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return
    
    # Get recommendations
    recommendations = recommend_movies(user, user_movie_matrix, user_similarity_df, top_n)
    
    if isinstance(recommendations, str):
        print(recommendations)
    else:
        print("Recommended Movies:", recommendations)

if __name__ == "__main__":
    main()
