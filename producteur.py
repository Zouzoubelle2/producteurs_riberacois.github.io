#%%
import pandas as pd
import numpy as np
#%%
df = pd.read_csv("clean_data.csv")
df

# %%
df = df.drop(['l2_normalisee', 'l3_normalisee', 'nic','indice_repetition','taille_unite_urbaine'], axis=1)
df
# %%
df = df.drop(['l1_declaree', 'l4_declaree', 'l6_declaree', 'numero_voie', 'type_voie'], axis = 1)
df
# %%
df = df.drop(['libelle_voie', 'code_postal', 'region', 'libelle_region', 'departement', 'arrondissement', 'canton', 'commune', 'libelle_commune', 'departement_unite_urbaine', 'numero_unite_urbaine'], axis=1)
df
# %%
df = df.drop(['etablissement_public_cooperation_intercommunale', 'tranche_commune_detaillee', 'zone_emploi', 'is_siege', 'indicateur_champ_publipostage', 'date_introduction_base_diffusion', 'tranche_effectif_salarie', 'date_validite_effectif_salarie', 'date_creation', 'date_debut_activite'], axis=1)
df

# %%
df = df.drop(['nom_raison_sociale', 'sigle', 'civilite', 'numero_rna', 'nic_siege', 'region_siege', 'departement_commune_siege', 'nature_juridique_entreprise', 'libelle_nature_juridique_entreprise', 'tranche_effectif_salarie_entreprise', 'date_validite_effectif_salarie_entreprise', 'categorie_entreprise', 'date_creation_entreprise', 'date_introduction_base_diffusion_entreprise', 'date_mise_a_jour', 'created_at', 'updated_at', 'geo_score', 'geo_type', 'geo_id', 'geo_ligne', 'geo_l4'], axis=1)
df

# %%
df = df.rename(columns={'l1_normalisee' : 'raison_sociale', 'l6_normalisee' : 'commune'})
df

# %%
df = df.rename(columns={'activite_principale': 'code_naf', 'l4_normalisee' : 'adresse', 'libelle_activite_principale': 'intitule_naf', 'activite_principale_entreprise': 'code_naf_entreprise', 'libelle_activite_principale_entreprise': 'intitule_naf_entreprise'})
df

# %%
count_categorie = df[["code_naf", "intitule_naf", "raison_sociale"]].groupby(['code_naf', 'intitule_naf']).count().sort_values(by="raison_sociale", ascending=False)
count_categorie

# %%
count_categorie_entreprise = df[["code_naf_entreprise","intitule_naf_entreprise", "raison_sociale"]].groupby(['code_naf_entreprise', 'intitule_naf_entreprise']).count().sort_values(by='raison_sociale', ascending=False)
count_categorie_entreprise

# %%
sd = df[['code_naf', 'raison_sociale', 'enseigne']]
sd
# %%
cheval = df.query('code_naf == "0143Z"')
cheval
# %%
df = df.drop(df.index[[560, 561, 562, 563, 564]])
df

# %%
ani = df[['code_naf', 'raison_sociale', 'enseigne']].query('code_naf =="0149Z"').sort_values(by='raison_sociale')
ani

# %%
df.to_csv("nettoyage_df.csv")
# %%
act_s = df.query('code_naf == "0161Z"')
act_s

# %%
