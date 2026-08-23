import pandas as pd


def calculate_macaulay_duration(row):

    settlement = pd.to_datetime(
        row["Date_Reglement"]
    )

    rate = row["Taux_Interpole"]

    dirty_price = row["Dirty_Price"]

    if dirty_price == 0:
        return 0

    weighted_sum = 0

    for cf in row["Cash_Flows"]:

        t = (
            cf["Date"] - settlement
        ).days / 365.25

        if t > 0:

            pv = (
                cf["Amount"]
                / ((1 + rate) ** t)
            )

            weighted_sum += t * pv

    return weighted_sum / dirty_price


def calculate_modified_duration(row):

    return (
        row["Macaulay_Duration"]
        / (1 + row["Taux_Interpole"])
    )


def calculate_dv01(row):

    return (
        row["Modified_Duration"]
        * row["Dirty_Price"]
        * 0.0001
    )


def calculate_convexity(row):

    settlement = pd.to_datetime(
        row["Date_Reglement"]
    )

    rate = row["Taux_Interpole"]

    dirty_price = row["Dirty_Price"]

    if dirty_price == 0:
        return 0

    total = 0

    for cf in row["Cash_Flows"]:

        t = (
            cf["Date"] - settlement
        ).days / 365.25

        if t > 0:

            pv = (
                cf["Amount"]
                / ((1 + rate) ** t)
            )

            total += (
                t * (t + 1) * pv
            )

    return (
        total
        /
        (
            dirty_price
            * ((1 + rate) ** 2)
        )
    )
