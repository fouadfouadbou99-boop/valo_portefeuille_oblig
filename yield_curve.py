import numpy as np


def interpolate_rates(portfolio_df, curve_df):

    portfolio_df["Taux_Interpole"] = np.interp(
        portfolio_df["Maturite_Residuelle"],
        curve_df["tenor"],
        curve_df["rate"]
    )

    return portfolio_df
