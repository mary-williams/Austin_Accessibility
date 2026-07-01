import requests
import geopandas as gpd
from shapely.geometry import shape
import pandas as pd

NEIGHBOR_URL = "https://data.austintexas.gov/resource/a7ap-j2yt.geojson"
PARKS_URL = "https://data.austintexas.gov/resource/v8hw-gz65.geojson"
SCHOOLS_URL = "https://data.austintexas.gov/resource/63ig-4knr.json"
# Only "Austin Public Health" locations
HOSPITALS_URL = "https://data.austintexas.gov/resource/6v78-dj3u.json"

def fetch_data(url):
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    data = response.json()
    return gpd.GeoDataFrame.from_features(data['features'])

parks = fetch_data(PARKS_URL)
neighborhoods = fetch_data(NEIGHBOR_URL)
schools = fetch_data(SCHOOLS_URL)
hospitals = fetch_data(HOSPITALS_URL)

#standardize

target_crs = "EPSG:3857"

parks = parks.to_crs(target_crs)
schools = schools.to_crs(target_crs)
hospitals = hospitals.to_crs(target_crs)
neighborhoods = neighborhoods.to_crs(target_crs)
