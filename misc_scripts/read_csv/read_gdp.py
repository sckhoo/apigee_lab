import os
from csv import DictReader
from pathlib import Path
from fastapi import FastAPI, HTTPException

filename = 'world_country_gdp_usd.csv'
data_folder = Path(os.getcwd())
file_to_open = data_folder / filename

def get_data_csv(file_to_open, year : str):
    list_temp1 = []
    if not file_to_open.exists():
        print("Oops, file doesn't exist!")
    else:
        with open(file_to_open, 'r') as f:
            dict_reader = DictReader(f)
            list_temp = list(dict_reader)
    for sub in list_temp: 
        if (sub['year'] == year) and sub['GDP_USD']:
            list_temp1.append(sub)
    return list_temp1

final_list = get_data_csv(file_to_open, '2021')

for sub in final_list: 
    if (sub['Country Name'] == 'Philippines'):
        print(sub)