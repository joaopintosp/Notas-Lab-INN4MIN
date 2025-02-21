import pandas as pd

df = pd.read_csv('report (29) - original.csv')

colunas_a_remover = ["Class", "Date", "Time", "Duration",
   "Grade"]

df = df.drop(columns=colunas_a_remover, errors='ignore')

df_limpo = df.loc[:, ~df.columns.str.contains(r"\+/-")].dropna(axis=1, how="all")

df_limpo.to_excel("report (29) - original limpo.xlsx", index=False)