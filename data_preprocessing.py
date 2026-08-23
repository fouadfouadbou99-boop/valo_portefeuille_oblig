def rename_columns(df):

    mapping = {

        "Description Titres": "Description_Titres",
        "Date Emission": "Date_Emission",
        "Date Jouissance": "Date_Jouissance",
        "Date Règlement": "Date_Reglement",
        "Date Echéance": "Date_Echeance",
        "Taux facial": "Taux_Facial",
        "Nominal Unitaire": "Nominal_Unitaire",
        "Nominal Global": "Nominal_Global",
        "Quantité": "Quantite"

    }

    return df.rename(columns=mapping)
