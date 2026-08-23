import pandas as pd


def calculate_residual_maturity(df):

    df["Maturite_Residuelle"] = (
        pd.to_datetime(df["Date_Echeance"])
        - pd.to_datetime(df["Date_Reglement"])
    ).dt.days / 365.25

    return df


def calculate_annual_coupon(df):

    df["Annual_Coupon"] = (
        df["Nominal_Unitaire"]
        * df["Taux_Facial"]
    )

    return df


def calculate_accrued_coupon(row):

    return row["Annual_Coupon"] * 0.5


def generate_cashflows(row):

    nominal = row["Nominal_Unitaire"]

    coupon = row["Annual_Coupon"]

    maturity = pd.to_datetime(
        row["Date_Echeance"]
    )

    settlement = pd.to_datetime(
        row["Date_Reglement"]
    )

    enjoyment = pd.to_datetime(
        row["Date_Jouissance"]
    )

    flows = []

    current_date = enjoyment

    while current_date <= settlement:
        current_date += pd.DateOffset(years=1)

    while current_date <= maturity:

        flows.append({
            "Date": current_date,
            "Type": "Coupon",
            "Amount": coupon
        })

        current_date += pd.DateOffset(years=1)

    flows.append({
        "Date": maturity,
        "Type": "Principal",
        "Amount": nominal
    })

    return flows


def calculate_dirty_price(row):

    price = 0

    rate = row["Taux_Interpole"]

    settlement = pd.to_datetime(
        row["Date_Reglement"]
    )

    for cf in row["Cash_Flows"]:

        t = (
            cf["Date"] - settlement
        ).days / 365.25

        if t > 0:

            pv = (
                cf["Amount"]
                / ((1 + rate) ** t)
            )

            price += pv

    return price


def calculate_clean_price(row):

    return (
        row["Dirty_Price"]
        - row["Accrued_Coupon"]
    )
