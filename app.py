import streamlit as st
import pickle
import pandas as pd


st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="centered"
)


movies_dict = pickle.load(open('artifacts/tmdb_5000_credits.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))

# Convert dictionary to DataFrame
movies = pd.DataFrame(movies_dict)


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []
    for i in movie_list:
        recommendations.append(movies.iloc[i[0]].title)

    return recommendations


st.title("🎬 Movie Recommendation System")
st.write("Select a movie and get similar movie recommendations")

selected_movie = st.selectbox(
    "Choose a movie",
    movies['title'].values
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)

    st.subheader("🎯 Recommended Movies:")
    for movie in recommendations:
        st.write("👉", movie)

