import geopandas as gpd
import plotly.express as px
from shapely.geometry import Point
import pandas as pd

# Read GeoJSON file using GeoPandas
geojson_file = "map2.geojson"
gdf = gpd.read_file(geojson_file)

points_data = {'name': ['Point A', 'Point B', 'Point C'],
               'latitude': [40, 42, 45],  # Replace with the desired latitudes
               'longitude': [-75, -73, -80]}

points_gdf = gpd.GeoDataFrame(points_data, geometry=gpd.points_from_xy(points_data['longitude'], points_data['latitude']))
new_point = gpd.GeoDataFrame(geometry=[Point( 73.130730,19.236280)])  # Replace with the desired longitude and latitude
new_point['name'] = 'New Point'  # Optional: Add a name or any other attribute for the new point

gdf.crs = 'EPSG:4326'  # Assuming the original CRS is WGS 84
points_gdf.crs = 'EPSG:4326'

# Combine the original GeoDataFrame with the new point GeoDataFrame
combined_gdf = gpd.GeoDataFrame(pd.concat([gdf, points_gdf], ignore_index=True))

# Create a Plotly Express figure
fig = px.scatter_mapbox(
    combined_gdf,
    lon=combined_gdf.geometry.x,
    lat=combined_gdf.geometry.y,
    text=combined_gdf['name'],  # Change this to the attribute you want to display on hover
    mapbox_style="carto-positron",
    zoom=1
)

# Show the figure
fig.show()
