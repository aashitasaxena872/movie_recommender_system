# import pandas as pd
# import streamlit as st
# import pickle
# import  requests
#
# def fetch_poster(movie_id):
#     data=requests.get("https://api.themoviedb.org/3/movie/{}"
#                  "?api_key=4e1341d0530541a751fcf4612cb4dbe9&langage=en-US".format(movie_id)
#                  )
#     data=data.json()
#     print(data)
#     return "https://image.tmdb.org/t/p/w500/1E5baAaEse26fej7uHcjOgEE2t2.jpg" + data["poster_path"]
#
#
# def recommend(movie):
#     movie_index=movies[movies["title"]==movie].index[0]
#     distances=similarity[movie_index]
#     movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
#
#     recommended_movies=[]
#     recommended_movies_posters=[]
#     for i in movie_list:
#         movie_id=movies.iloc[i[0]].movie_id
#         #fetch poster from api
#         recommended_movies.append(movies.iloc[i[0]].title)
#         recommended_movies_posters=fetch_poster(movie_id)
#     return recommended_movies,recommended_movies_posters
#
# movies_dict = pickle.load(open("movie_dict.pkl","rb"))
# movies=pd.DataFrame(movies_dict)
#
# similarity=pickle.load(open("similarity.pkl","rb"))
#
#
# st.title("Movie Recommender System")
# selected_movie_name=st.selectbox(
#     'How many movies do you like? ',
#    movies["title"].values
# )
#
# if st.button("recommend"):
#     names,posters=recommend(selected_movie_name)
#
#     import streamlit as st
#
#     col1, col2, col3,col4,col5 = st.columns(5)
#
#     with col1:
#         st.header(names[0])
#         st.image(posters[0])
#
#     with col2:
#         st.header(names[1])
#         st.image(posters[1])
#
#     with col3:
#         st.header(names[2])
#         st.image(posters[2])
#
#     with col4:
#         st.header(names[3])
#         st.image(posters[3])
#
#     with col5:
#         st.header(names[4])
#         st.image(posters[4])

import pickle
import streamlit as st
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=14ff410a586f6988d9164ec9b6ee4d4a&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


st.header('Movie Recommender System')
movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])




