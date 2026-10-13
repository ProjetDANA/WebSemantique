# Supprimer les colonnes inutiles et nettoyer les textes.
import pandas as pd
import pathlib

data_path = pathlib.Path("datas")
unformated_datas = pathlib.Path("dataset_name.csv")
cleaned_datas = pathlib.Path("cleaned_dataset_name.csv")

datas = pd.read_csv(data_path / unformated_datas, encoding="utf-8")

# Colonnes inutiles
useless_cols = [
    "cols à enlever"
]

for cols in useless_cols:
    datas.drop(cols, inplace=True, axis=1)

# save ce qui nous intéresse
datas.to_csv(data_path / cleaned_datas, index=False, encoding="utf-8")