import json

file_name = 'data_json/eq_data_30_day_m1.json'

with open(file_name) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
meta_data_title = all_eq_data['metadata']['title']
print(len(all_eq_dicts))

hover_texts = []
mags = []
lons = []
lats = []

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)
print(mags[:10])
print(lons[:10])
print(lats[:10])
