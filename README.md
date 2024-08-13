# CODSOFT_Recommendation_Sys_04
RECOMMENDATION SYSTEM
<br>OVERVIEW
<br>This is a simple movie recommendation system implemented in Python. The system leverages user ratings to recommend movies to users based on the preferences of similar users. It uses a basic collaborative filtering approach with cosine similarity to determine user similarity and generate recommendations.

<br>FEATURES
<br>User-Movie Matrix: Constructs a matrix of user ratings for different movies.
<br>Similarity Calculation: Computes user similarity using cosine similarity.
<br>Recommendation Generation: Provides movie recommendations for a specified user based on the ratings of similar users.

<br>CODE DESCRIPTION
<br>1. Data Preparation
<br>The script begins with sample data representing user ratings for various movies. This data is used to build the recommendation model.

<br>2. User-Movie Matrix
<br>The code transforms the raw rating data into a user-movie matrix, where rows represent users, columns represent movies, and values indicate ratings. Missing ratings are filled with zeroes.

<br>3. User Similarity Calculation
<br>Cosine similarity is computed between users to evaluate how similar they are based on their movie ratings.

<br>4. Recommendation Function
<br>The recommend_movies function:

<br>Takes a username and returns a list of movie recommendations.
<br>Considers ratings from users similar to the specified user.
<br>Aggregates scores to suggest movies that the user has not rated yet.
<br>5. Main Function
<br>The main function:

<br>Provides a command-line interface for user interaction.
<br>Prompts for a username and the number of recommendations.
<br>Displays the recommended movies or an error message if the user is not found.

<br>EXAMPLE
<br>For the sample data provided in the script, if you input the username "Alice" and request 3 recommendations, the system will output the top 3 movies recommended for Alice based on similar users' ratings.
