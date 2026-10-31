# Supprimer les colonnes inutiles et nettoyer les textes.
import pandas as pd
import re
import pathlib

data_path = pathlib.Path("datas")
unformated_datas = pathlib.Path("1900_2021_DISASTERS.xlsx - emdat data copy.csv")
cleaned_datas = pathlib.Path("1900_2021_DISASTERS.csv")

datas = pd.read_csv(data_path / unformated_datas, encoding="utf-8")

# Colonnes utiles
usable_cols = [
    "Year",
    "Seq",
    "Disaster Group",
    "Disaster Subgroup",
    "Disaster Type",
    "Disaster Subtype",
    "Event Name",
    "Country",
    "ISO",
    "Region",
    "Continent",
    "Start Month",
    "Start Day",
    "Total Deaths",
    "Total Affected",
    "Total Damages ('000 US$)",
    "Latitude",
    "Longitude",
]

clean_df = datas[usable_cols]

# meilleur nom
clean_df.rename(columns={"Total Damages ('000 US$)": "Total Damages USD"}, inplace=True)


# nettoyer latitudes et longitudes (des fois E N W S à la fin)
def clean_coord(val):
    if pd.isna(val): 
        return None
    s = str(val).strip().upper()

    # coordonnee valide
    match = re.search(r'-?\d+(?:\.\d*)?', s)
    if not match:
        return None
        
    num = float(match.group())
    
    return -num if s.endswith(('S', 'W', 'O')) else num


clean_df["Latitude"] = clean_df["Latitude"].map(clean_coord)
clean_df["Longitude"] = clean_df["Longitude"].map(clean_coord)

clean_df.to_csv(data_path / cleaned_datas, index=False, encoding="utf-8")
