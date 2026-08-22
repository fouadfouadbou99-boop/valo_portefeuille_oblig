import pandas as pd

def load_portfolio_data(path, sheet_name="portfolio_data"):
    return pd.read_excel(path, sheet_name=sheet_name)

def load_curve_rate_data(path, sheet_name="curve_rate"):
    return pd.read_excel(path, sheet_name=sheet_name)
