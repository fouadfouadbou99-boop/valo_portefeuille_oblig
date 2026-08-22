import streamlit as st

st.title("Analyse de Portefeuille Obligataire")
st.info("Version de démarrage du projet. Importez un fichier Excel pour lancer l'analyse.")
file = st.file_uploader("Fichier Excel", type=["xlsx"])
if file:
    st.success("Fichier chargé avec succès")
