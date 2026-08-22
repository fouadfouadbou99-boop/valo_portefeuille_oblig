import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Valorisation Portefeuille Obligataire",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Valorisation de Portefeuille Obligataire")

uploaded_file = st.file_uploader(
    "Importer le fichier Excel du portefeuille",
    type=["xlsx"]
)

if uploaded_file is not None:

    try:
        portfolio_df = pd.read_excel(
            uploaded_file,
            sheet_name="portfolio_data"
        )

        curve_df = pd.read_excel(
            uploaded_file,
            sheet_name="curve_rate"
        )

        st.success("Fichier chargé avec succès")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Nombre de lignes portefeuille",
                len(portfolio_df)
            )

        with col2:
            st.metric(
                "Points de courbe",
                len(curve_df)
            )

        st.subheader("Portefeuille")

        st.dataframe(
            portfolio_df,
            use_container_width=True
        )

        st.subheader("Courbe des taux")

        st.dataframe(
            curve_df,
            use_container_width=True
        )

    except Exception as e:
        st.error(f"Erreur : {e}")
