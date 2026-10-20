# Supprimer les colonnes inutiles et nettoyer les textes.
import pandas as pd
import pathlib

data_path = pathlib.Path("datas")
unformated_datas = pathlib.Path("1900_2021_DISASTERS.xlsx - emdat data copy.csv")
cleaned_datas = pathlib.Path("1900_2021_DISASTERS.csv")

datas = pd.read_csv(data_path / unformated_datas, encoding="utf-8")

# Colonnes utiles
usable_cols = [
    'Year', 'Seq', 'Disaster Group', 'Disaster Subgroup', 'Disaster Type', 
    'Disaster Subtype', 'Event Name', 'Country', 'ISO', 'Region', 'Continent', 
    'Start Year', 'Start Month', 'Total Deaths', 'Total Affected', "Total Damages ('000 US$)",
    'Latitude', 'Longitude'
]

clean_df = datas[usable_cols]

# save ce qui nous intéresse
clean_df.to_csv(data_path / cleaned_datas, index=False, encoding="utf-8")