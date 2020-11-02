#%%
import pandas as pd
# %%
df_communes = pd.read_csv('Communes_CP_CC.csv')
df_communes
# %%
df_by_cp = df_communes.groupby('Code Postal').count()
df_by_cp
# %%
df_cc = df_communes['Code commune']
df_cc
# %%
