import pandas as pd
from io import BytesIO


def generate_aggregated_metrics(df):

    nominal_value = df["Nominal_Global"].sum()

    market_value = (
        df["Clean_Price"] * df["Quantite"]
    ).sum()

    duration = (
        df["Modified_Duration"]
        * df["Nominal_Global"]
    ).sum() / nominal_value

    convexity = (
        df["Convexity"]
        * df["Nominal_Global"]
    ).sum() / nominal_value

    dv01 = (
        df["DV01"]
        * df["Quantite"]
    ).sum()

    return pd.DataFrame({

        "Metric": [

            "Nominal Value (Global)",

            "Market Value (Global Valuation)",

            "Weighted Average Modified Duration",

            "Weighted Average Convexity",

            "Aggregated DV01"

        ],

        "Value": [

            nominal_value,

            market_value,

            duration,

            convexity,

            dv01

        ]
    })


def export_to_excel(
    portfolio_df,
    aggregated_df
):

    output = BytesIO()

    with pd.ExcelWriter(
        output,
        engine="xlsxwriter"
    ) as writer:

        portfolio_df.to_excel(
            writer,
            sheet_name="Portfolio_Analysis",
            index=False
        )

        aggregated_df.to_excel(
            writer,
            sheet_name="Aggregated_Metrics",
            index=False
        )

    return output.getvalue()
