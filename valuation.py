import pandas as pd

def calculate_annual_coupon(df):
    df["Annual_Coupon"] = df["Unit_Nominal"] * df["Facial_Rate"]
    return df
