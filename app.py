import streamlit as st
from mongo_db import connect_mongo, get_movies, find_movie_by_title
from neo4j_db import Neo4jDB


# connexion aux bases
collection = connect_mongo()
neo = Neo4jDB()

st.title("Projet NoSQL - Movies Database")

st.sidebar.title("Menu")

menu = st.sidebar.radio(
    "Choisir une section",
    [
        "Voir tous les films",
        "Rechercher un film",
        "Neo4j - Ajouter acteur",
        "Neo4j - Ajouter film",
        "Neo4j - Créer relation acteur-film"
    ]
)


# ---------------------------
# Voir tous les films
# ---------------------------

if menu == "Voir tous les films":

    st.header("Liste des films")

    movies = get_movies(collection)

    for movie in movies:

        st.write(movie)


# ---------------------------
# Rechercher un film
# ---------------------------

elif menu == "Rechercher un film":

    st.header("Rechercher un film")

    title = st.text_input("Titre du film")

    if st.button("Rechercher"):

        movie = find_movie_by_title(collection, title)

        if movie:
            st.write(movie)
        else:
            st.warning("Film non trouvé")


# ---------------------------
# Neo4j ajouter acteur
# ---------------------------

elif menu == "Neo4j - Ajouter acteur":

    st.header("Ajouter acteur")

    actor = st.text_input("Nom de l'acteur")

    if st.button("Ajouter acteur"):

        neo.create_actor(actor)

        st.success("Acteur ajouté")


# ---------------------------
# Neo4j ajouter film
# ---------------------------

elif menu == "Neo4j - Ajouter film":

    st.header("Ajouter film")

    title = st.text_input("Titre")
    year = st.number_input("Année", min_value=1900)

    if st.button("Ajouter film"):

        neo.create_movie(title, year)

        st.success("Film ajouté dans Neo4j")


# ---------------------------
# Neo4j relation acteur-film
# ---------------------------

elif menu == "Neo4j - Créer relation acteur-film":

    st.header("Créer relation ACTED_IN")

    actor = st.text_input("Acteur")
    movie = st.text_input("Film")

    if st.button("Créer relation"):

        neo.create_acted_in(actor, movie)

        st.success("Relation créée")