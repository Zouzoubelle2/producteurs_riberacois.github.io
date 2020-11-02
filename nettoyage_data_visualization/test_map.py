#%%
import folium
import pandas as pd
from folium.plugins import MarkerCluster
#%%
my_map = folium.Map(
    location=[45.25,0.33333],
    tiles='OpenStreetMap',
    zoom_start=10
)
my_map

# %%
df_map = pd.read_csv('nettoyage_df.csv')
df_map = df_map[['latitude','longitude', 'geo_adresse', 'raison_sociale', 'code_naf']]
df_map = df_map.fillna(0)
# %%
marker_cluster = MarkerCluster().add_to(my_map)
for index, point in df_map.iterrows() :
  latitude = point[0]
  longitude = point[1]
  nom = point[3]
  adresse = point[2]
  code_naf = point[4]
  folium.Marker(
    location=[latitude, longitude],
    popup=f'Nom : {nom} Adresse : {adresse}',
    icon=folium.Icon(color='green', icon='leaf', prefix='fa')
  ).add_to(marker_cluster)
my_map
# %%
my_map.save('map.html')

# %%
