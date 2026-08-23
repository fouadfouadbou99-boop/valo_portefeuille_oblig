import pandas as pd


def calculate_residual_maturity(df):

    df["Maturite_Residuelle"] = (
        pd.to_datetime(df["Date Echéance"])
        - pd.to_datetime(df["Date Règlement"])
    ).dt.days / 365.25

    return df


def calculate_annual_coupon(df):

    df["Annual_Coupon"] = (
        df["Nominal Unitaire"]
        * df["Taux facial"]
    )

    return df


def calculate_accrued_coupon(df):

    df["Accrued_Coupon"] = (
        df["Annual_Coupon"] * 0.5
    )

    return df
