import pandas as pd

daily_df = pd.read_csv("data/daily_reports.csv")

totals_df = (
    daily_df[["Confirmed", "Deaths", "Recovered"]].sum().reset_index(name="count")
)

totals_df = totals_df.rename(columns={"index": "Condition"})
