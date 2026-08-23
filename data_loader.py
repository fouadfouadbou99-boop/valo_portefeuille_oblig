import pandas as pd


def load_portfolio_data(uploaded_file):
    return pd.read_excel(
        uploaded_file,
        sheet_name="portfolio_data"
    )


def load_curve_data(uploaded_file):
    return pd.read_excel(
        uploaded_file,
        sheet_name="curve_rate"
    )
