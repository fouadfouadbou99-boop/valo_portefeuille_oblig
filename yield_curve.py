import numpy as np

def interpolate_rate(maturity, curve_df):
    return float(np.interp(maturity, curve_df["tenor"], curve_df["rate"]))
