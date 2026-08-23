def calculate_modified_duration(df):

    df["Modified_Duration"] = (
        df["Maturite_Residuelle"]
        / (1 + df["Taux_Interpole"])
    )

    return df


def calculate_dv01(df):

    df["DV01"] = (
        df["Modified_Duration"]
        * df["Nominal Global"]
        * 0.0001
    )

    return df


def calculate_convexity(df):

    df["Convexity"] = (
        df["Modified_Duration"] ** 2
    )

    return df
