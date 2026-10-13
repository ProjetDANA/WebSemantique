# Supprimer les colonnes inutiles et nettoyer les textes.
import pandas as pd
import pathlib

data_path = pathlib.Path("datas")
unformated_datas = pathlib.Path("unesco_dataset.csv")
cleaned_datas = pathlib.Path("cleaned_unesco_dataset.csv")

datas = pd.read_csv(data_path / unformated_datas, encoding="utf-8")

# Colonnes inutiles
useless_cols = [
    "Date end",
    "Main Image Caption ES",
    "Main Image Caption RU",
    "Main Image Caption AR",
    "Main Image Caption ZH",
    "Main Video",
    "Main Video Author",
    "Main Video Caption EN",
    "Main Video Caption FR",
    "Main Video Caption ES",
    "Main Video Caption RU",
    "Main Video Caption AR",
    "Main Video Caption ZH",
    "videos_urls",
    "Main Image Copyright",
    "Main Image Author",
    "Images",

    "Description EN",
    "Justification EN",

    # on garde uniquement anglais et français
    "Name ES",
    "Name RU",
    "Name AR",
    "Name ZH",
    "Short Description ES",
    "Short Description RU",
    "Short Description AR",
    "Short Description ZH",
]

for cols in useless_cols:
    datas.drop(cols, inplace=True, axis=1)

# save ce qui nous intéresse
datas.to_csv(data_path / cleaned_datas, index=False, encoding="utf-8")