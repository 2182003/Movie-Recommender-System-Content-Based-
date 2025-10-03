import streamlit as st
import pickle
# import pandas as pd
import requests



def fetch_poster(movie_id):
    try:
        url = "https://api.themoviedb.org/3/movie/{}?api_key=e48791bcd864204c3a042af655655073&language=en-US".format(
            movie_id)
        data = requests.get(url)
        data = data.json()
        if 'poster_path' in data and data['poster_path']:
            poster_path = data['poster_path']
            full_path =  "https://image.tmdb.org/t/p/w500/" + poster_path
            return full_path
        else:
            return "https://via.placeholder.com/500x750/000000/FFFFFF?text=No+Poster"

    except Exception as e:
        return "https://via.placeholder.com/500x750/FF0000/FFFFFF?text=API+Error"


def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list_sorted = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = []
    recommend_movies_posters = []
    for i in movies_list_sorted:
        movie_id = movies_list.iloc[i[0]]['movie_id']
        recommend_movies.append(movies_list.iloc[i[0]]['title'])
        recommend_movies_posters.append(fetch_poster(movie_id))
    return recommend_movies, recommend_movies_posters


# Load data
movies_list = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie:',
    movies_list['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])