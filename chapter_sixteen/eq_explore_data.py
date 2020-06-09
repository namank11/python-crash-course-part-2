import json

file_name = 'data_json/eq_data_1_day_m1.json'

with open(file_name) as f:
    all_eq_data = json.load(f)
readable_file = 'data_json/readable_data.json'
with open(readable_file, 'a') as f:
    json.dump(all_eq_data, f, indent=4)
