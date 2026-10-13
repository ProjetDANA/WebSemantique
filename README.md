# Liste du Patrimoine mondial de l'UNESCO, Projet DANA
## Source des données

- **Jeu de données** : Liste du Patrimoine mondial (UNESCO), catalogue de données ouvertes de l'UNESCO
- **Description** : Ce jeu de données contient la liste du patrimoine mondial de l'UNESCO, qui présente les sites d'une valeur universelle exceptionnelle reconnus pour leur importance culturelle, naturelle ou mixte. Il comprend des informations sur l'emplacement des sites, les critères d'inscription et l'année d'inscription, soutenant ainsi les efforts de sauvegarde du patrimoine mondial pour les générations futures.

## Colonnes conservées (27)
### Identification du site

| Colonne | Description |
|---|---|
| `ID` | Identifiant numérique UNESCO du site (pour lier dans wikidata) |
| `UUID` | Identifiant unique universel du site dans le jeu de données |
| `Name EN` | Nom du site en anglais |
| `Name FR` | Nom du site en français |
| `Short Description EN` | Description courte du site en anglais |
| `Short Description FR` | Description courte du site en français |

### Inscription et statut

| Colonne | Description |
|---|---|
| `Date inscribed` | Année d'inscription du site sur la Liste du patrimoine mondial |
| `Secondary dates` | Années correspondant à d'autres dates liées à l'inscription (extensions ou modifications du site) |
| `Danger` | Booléen : le site est (ou a été) sur la liste du patrimoine mondial en péril |
| `Danger list` | Années d'inscription sur la liste en péril |
| `Area hectares` | Superficie du bien, en hectares |

### Critères et catégorie

| Colonne | Description |
|---|---|
| `Cultural Criteria` | Critères culturels satisfaits, au format `c1` à `c6` (ex. `c2, c4`) |
| `Natural Criteria` | Critères naturels satisfaits, au format `n7` à `n10` (ex. `n8`) |
| `Criteria` | Critères d'inscription en chiffres romains, de (i) à (x) (ex. `(ii)(iv)`) |
| `Catégorie` | Catégorie du site : `Cultural`, `Natural` ou `Mixed` |
| `Category ID` | Identifiant numérique de la catégorie |

### Localisation

| Colonne | Description |
|---|---|
| `States Names` | Nom(s) du ou des États parties concernés, séparés par des virgules |
| `ISO Codes` | Code(s) pays ISO correspondants |
| `Region` | Région UNESCO (ex. `Europe and North America`, `Asia and the Pacific`, `Arab States`) |
| `Region Code` | Code de la région (ex. `EUR`, `APA`, `ARB`) |
| `Transboundary` | Booléen : le site s'étend sur plusieurs pays |
| `Coordonnées` | Coordonnées géographiques du site |
| `Components` | Liste des composants du site, avec nom, référence, latitude et longitude |
| `Components Count` | Nombre de composants du site |

### Média

| Colonne | Description |
|---|---|
| `Main Image` | URL de l'image principale du site |
| `Main Image Caption EN` | Légende de l'image principale en anglais |
| `Main Image Caption FR` | Légende de l'image principale en français |
