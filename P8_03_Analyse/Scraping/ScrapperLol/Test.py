
import pandas as pd
import numpy as np
import seaborn as sns


import matplotlib.pyplot as plt
import datetime as dt

plt.style.use('seaborn-deep')

df_bans = pd.read_csv("Data/bans.csv")
df_date = pd.read_csv("Data/dateAddress.csv")
df_bans = pd.merge(df_bans, df_date[["Address","Date"]], on='Address', how='left')
df_bans['Date'] = pd.to_datetime(df_bans['Date'])
df_bans.head()


liste_champions = df_bans.ban_1.value_counts().index.to_list() + df_bans.ban_2.value_counts().index.to_list() + df_bans.ban_3.value_counts().index.to_list() + df_bans.ban_5.value_counts().index.to_list() + df_bans.ban_5.value_counts().index.to_list()
liste_champions = pd.DataFrame(liste_champions)
liste_champions = liste_champions.drop_duplicates()
liste_champions = liste_champions.reset_index()
liste_champions = liste_champions.drop(columns='index')
liste_champions.columns = ['Champions']

liste_champions["Ban_pos"] = 0
liste_champions["teamBan"] = 0
liste_champions["Date"] = 0

df_tempo = pd.DataFrame()

for i, row in df_bans.iterrows():
    df_tempo.loc[i,"Champions"] = row.ban_1
    df_tempo.loc[i,"ban_pos"] = "ban_1"
    df_tempo.loc[i,"TeamBan"] = row.Team
    df_tempo.loc[i,"Date"] = row.Date



df_tempo
