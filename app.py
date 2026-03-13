import streamlit as st
from analysis import age_distribution, age_statistics

from mongo_db import (
    connect_mongo,
    insert_user,
    get_users,
    update_user,
    delete_user
)

from neo4j_db import Neo4jDB


# connexion aux bases
collection = connect_mongo()
neo = Neo4jDB()


st.title("Projet NoSQL")

st.sidebar.title("Menu")

menu = st.sidebar.radio(
    "Choisir une section",
    [
        "Ajouter utilisateur",
        "Voir utilisateurs",
        "Modifier utilisateur",
        "Supprimer utilisateur",
        "Neo4j - Ajouter personne",
        "Neo4j - Créer relation",
        "Analyse données"
    ]
)


# ---------------------------
# Ajouter utilisateur
# ---------------------------

if menu == "Ajouter utilisateur":

    st.header("Ajouter utilisateur")

    name = st.text_input("Nom")
    age = st.number_input("Age", min_value=0)

    if st.button("Ajouter"):

        insert_user(collection, name, age)

        st.success("Utilisateur ajouté")


# ---------------------------
# Voir utilisateurs
# ---------------------------

elif menu == "Voir utilisateurs":

    st.header("Liste des utilisateurs")

    users = get_users(collection)

    for user in users:

        st.write(
            f"Nom : {user['name']} | Age : {user['age']}"
        )


# ---------------------------
# Modifier utilisateur
# ---------------------------

elif menu == "Modifier utilisateur":

    st.header("Modifier utilisateur")

    name = st.text_input("Nom utilisateur")
    new_age = st.number_input("Nouvel âge", min_value=0)

    if st.button("Modifier"):

        update_user(collection, name, new_age)

        st.success("Utilisateur modifié")


# ---------------------------
# Supprimer utilisateur
# ---------------------------

elif menu == "Supprimer utilisateur":

    st.header("Supprimer utilisateur")

    name = st.text_input("Nom à supprimer")

    if st.button("Supprimer"):

        delete_user(collection, name)

        st.success("Utilisateur supprimé")


# ---------------------------
# Neo4j ajouter personne
# ---------------------------

elif menu == "Neo4j - Ajouter personne":

    st.header("Ajouter personne dans Neo4j")

    name = st.text_input("Nom de la personne")

    if st.button("Créer personne"):

        neo.create_person(name)

        st.success("Personne créée")


# ---------------------------
# Neo4j créer relation
# ---------------------------

elif menu == "Neo4j - Créer relation":

    st.header("Créer relation")

    person1 = st.text_input("Personne 1")
    person2 = st.text_input("Personne 2")

    if st.button("Créer relation"):

        neo.create_relation(person1, person2)

        st.success("Relation créée")
#code d'analyse 
elif menu == "Analyse données":

    st.header("Analyse des utilisateurs")

    users = get_users(collection)

    stats = age_statistics(users)

    st.subheader("Statistiques")

    for key, value in stats.items():
        st.write(f"{key} : {value}")

    st.subheader("Distribution des âges")

    fig = age_distribution(users)

    st.pyplot(fig)