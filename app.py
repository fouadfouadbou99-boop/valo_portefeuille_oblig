import streamlit as st
import pandas as pd

from data_loader import (
    load_portfolio_data,
    load_curve_data
)

from data_preprocessing import (
    rename_columns
)

from valuation import (
    calculate_residual_maturity,
    calculate_annual_coupon,
    calculate_accrued_coupon,
    generate_cashflows,
    calculate_dirty_price,
    calculate_clean_price
)

from yield_curve import (
    interpolate_rates
)

from risk import (
    calculate_macaulay_duration,
    calculate_modified_duration,
    calculate_dv01,
    calculate_convexity
)

st.set_page_config(
    page_title="Valorisation Portefeuille Obligataire",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Valorisation de Portefeuille Obligataire")

uploaded_file = st.file_uploader(
    "Importer le fichier Excel",
    type=["xlsx"]
)

if uploaded_file:

    try:

        # Chargement des données

        portfolio_df = load_portfolio_data(
            uploaded_file
        )

        curve_df = load_curve_data(
            uploaded_file
        )

        # Préparation

        portfolio_df = rename_columns(
            portfolio_df
        )

        # Calcul maturité résiduelle

        portfolio_df = calculate_residual_maturity(
            portfolio_df
        )

        # Interpolation

        portfolio_df = interpolate_rates(
            portfolio_df,
            curve_df
        )

        # Coupon annuel

        portfolio_df = calculate_annual_coupon(
            portfolio_df
        )

        # Coupon couru

        portfolio_df["Accrued_Coupon"] = (
            portfolio_df.apply(
                calculate_accrued_coupon,
                axis=1
            )
        )

        # Cash flows

        portfolio_df["Cash_Flows"] = (
            portfolio_df.apply(
                generate_cashflows,
                axis=1
            )
        )

        # Dirty Price

        portfolio_df["Dirty_Price"] = (
            portfolio_df.apply(
                calculate_dirty_price,
                axis=1
            )
        )

        # Clean Price

        portfolio_df["Clean_Price"] = (
            portfolio_df.apply(
                calculate_clean_price,
                axis=1
            )
        )

        # Risk metrics

        portfolio_df["Macaulay_Duration"] = (
            portfolio_df.apply(
                calculate_macaulay_duration,
                axis=1
            )
        )

        portfolio_df["Modified_Duration"] = (
            portfolio_df.apply(
                calculate_modified_duration,
                axis=1
            )
        )

        portfolio_df["DV01"] = (
            portfolio_df.apply(
                calculate_dv01,
                axis=1
            )
        )

        portfolio_df["Convexity"] = (
            portfolio_df.apply(
                calculate_convexity,
                axis=1
            )
