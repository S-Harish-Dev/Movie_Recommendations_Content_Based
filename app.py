# TO run :py -3.11 -m streamlit run app.py

import streamlit as st
import pickle
import requests

movies = pickle.load(open('movies_list.pkl','rb'))
similairty = pickle.load(open('Similairty.pkl','rb'))

st.header(" Movie Recommendation System 🍿 ")

Movie_name = st.selectbox(" Drop-Down Select Movies ↕️ ", movies['title'].values) # Because Movies has many column (we want to show only the title)


def get_api(file_path='API.txt'):

    with open(file_path,'r') as file:
        line = file.read().strip()
        api_key = line.split('=',1)[1].strip() # ('=', 1 ) 1 is max split (number of = replaced with ,)
    return str(api_key)


def fetch_poster(movie_id):
    api = get_api()
    url = "https://api.themoviedb.org/3/movie/{}?api_key={}".format(movie_id, api)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/"+ poster_path
    return full_path



def Recommend(name):
    movies_index = movies[movies['title']==name].index[0]
    distance  = sorted(enumerate(similairty[int(movies_index)]), reverse=True , key=lambda x:x[1])
    Recommend_list = []
    Recommend_poster = []
    for i in distance[1:16]:  # no starting 0 because its the movie itself
        movies_id = movies.iloc[i[0]].id
        Recommend_list.append(movies.iloc[i[0]].title) 
        Recommend_poster.append(fetch_poster(movie_id=movies_id))
    return Recommend_list, Recommend_poster



if st.button("Show Recommendations"):
    Movie_recommend, Movie_Poster = Recommend(Movie_name)
    col1 ,col2 ,col3 ,col4 , col5 = st.columns(5)


    with col1:
        st.image(Movie_Poster[0])
        st.text(Movie_recommend[0])

        st.image(Movie_Poster[5])
        st.text(Movie_recommend[5])

        st.image(Movie_Poster[10])
        st.text(Movie_recommend[10])
    
    with col2:
        st.image(Movie_Poster[1])
        st.text(Movie_recommend[1])

        st.image(Movie_Poster[6])
        st.text(Movie_recommend[6])

        st.image(Movie_Poster[11])
        st.text(Movie_recommend[11])
    
    with col3:
        st.image(Movie_Poster[2])
        st.text(Movie_recommend[2])

        st.image(Movie_Poster[7])
        st.text(Movie_recommend[7])

        st.image(Movie_Poster[12])
        st.text(Movie_recommend[12])

    with col4:
        st.image(Movie_Poster[3])
        st.text(Movie_recommend[3])

        st.image(Movie_Poster[8])
        st.text(Movie_recommend[8])

        st.image(Movie_Poster[13])
        st.text(Movie_recommend[13])

    with col5:
        st.image(Movie_Poster[4])
        st.text(Movie_recommend[4])

        st.image(Movie_Poster[9])
        st.text(Movie_recommend[9])

        st.image(Movie_Poster[14])
        st.text(Movie_recommend[14])






