import pandas as pd

def generate_aggregated_metrics(df):
    total = df["Global_Valuation"].sum()
    return pd.DataFrame({"Metric":["Market Value"],"Value":[total]})
