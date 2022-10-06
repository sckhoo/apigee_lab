import os
from csv import DictReader
from pathlib import Path
from fastapi import FastAPI, HTTPException

filename = 'World Happiness Report 2022.csv'
data_folder = Path(os.getcwd())
file_to_open = data_folder / filename

def get_data_csv(file_to_open):
    list_temp1 = []
    if not file_to_open.exists():
        print("Oops, file doesn't exist!")
    else:
        with open(file_to_open, 'r') as f:
            dict_reader = DictReader(f)
            list_temp = list(dict_reader)
    return list_temp

final_list = get_data_csv(file_to_open)

for sub in final_list: 
    if (sub['Country'] == 'Philippines'):
        print(sub['Country'], sub['Happiness score'])