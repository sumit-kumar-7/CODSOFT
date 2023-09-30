import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MultiLabelBinarizer

movies_data = [
    (1, "Movie A", ["Action", "Adventure"]),
    (2, "Movie B", ["Adventure", "Comedy"]),
    (3, "Movie C", ["Action", "Drama"]),
    (4, "Movie D", ["Comedy", "Romance"]),
    (5, "Movie E", ["Action", "Comedy"])
]

user_genres = ["Action", "Adventure", "Comedy"]

mlb = MultiLabelBinarizer()
movies_genres = [movie[2] for movie in movies_data]
movies_genres_binary = mlb.fit_transform(movies_genres)

user_genres_binary = mlb.transform([user_genres])

similarities = cosine_similarity(user_genres_binary, movies_genres_binary)

recommendations = [(movies_data[i][1], similarities[0][i]) for i in range(len(movies_data))]
recommendations.sort(key=lambda x: x[1], reverse=True)

print("Recommendations:")
for movie, similarity in recommendations:
    print(f"{movie} - Similarity: {similarity:.2f}")
