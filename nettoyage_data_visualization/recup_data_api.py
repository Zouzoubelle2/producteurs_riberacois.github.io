#%%
import pandas as pd
import numpy as np
import requests
import json
import time
from list_communes import df_cc
from list_code_naf import df_codes_naf

#%%
# df = pd.read_json('jason.json/code0111.json')
# df

#%%
# r = requests.get('https://entreprise.data.gouv.fr/api/sirene/v1/full_text/*?activite_principale=0111Z&code_commune=24352&per_page=100')
# retour_json = r.json()
# data = retour_json['etablissement']
# df = pd.DataFrame(data)
# df

# %%
list_all = []
for naf in df_codes_naf :
  for cc in df_cc :
    r = requests.get(f'https://entreprise.data.gouv.fr/api/sirene/v1/full_text/*?activite_principale={naf}&code_commune={cc}&per_page=100')
    print(r)
    if r.status_code == 200 :
      retour_json = r.json()
      data = retour_json['etablissement']
      for d in data :
        list_all.append(d)
    time.sleep(1)
#print(list_all)

# %%
#list_all[0]
df_all = pd.DataFrame(list_all)
df_all
# %%
#df_all.to_csv('dataframe_all.csv')
# %%
