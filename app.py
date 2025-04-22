import streamlit as st
import pickle
import pandas as pd

def recommend(selected_movie_name):
    movie_index = movie[movie['title'] == selected_movie_name].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movie.iloc[i[0]].title)
    return recommended_movies

# Load data
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movie = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit UI
st.title("Movie Recommendation System")

selected_movie_name = st.selectbox(
    "Select a movie to get recommendations",
    movie['title'].values
)

if st.button('Show Recommendation'):
    recommendations = recommend(selected_movie_name)
    for movie_title in recommendations:
        st.write(movie_title)
