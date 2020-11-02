#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# %%
# df = pd.read_csv('dataframe_all.csv')
# df
# %%
# df = df.dropna(axis=1, how='all')
# df
# %%
#df.to_csv('clean_data.csv')
# %%
df_producteurs= pd.read_csv('nettoyage_df.csv')
df_producteurs
# %%
#df_producteurs_par_naf['nombre_producteurs'] = df_producteurs_par_naf.count()
df_producteurs_par_naf = df_producteurs[['intitule_naf', 'id']].groupby(['intitule_naf']).count().sort_values(by='id', ascending=False)
df_producteurs_par_naf.to_csv('producteurs_par_naf.csv')

#%%
#plt.pie(df_producteurs_par_naf["id"], labels= df_producteurs_par_naf.index)

fig, ax = plt.subplots(figsize=(20, 10), subplot_kw=dict(aspect="equal"))

data = df_producteurs_par_naf["id"]
naf = df_producteurs_par_naf.index


def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%".format(pct, absolute)


wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))

ax.legend(wedges, naf,
          title="Intitulé naf",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Nb producteurs par intitulé Naf")

plt.show()

