import os
from csv import DictReader
from pathlib import Path
from fastapi import FastAPI, HTTPException

filename = 'world_population.csv'
data_folder = Path(os.getcwd())
file_to_open = data_folder / filename

def get_data_csv(file_to_open):
    if not file_to_open.exists():
        print("Oops, file doesn't exist!")
    else:
        with open(file_to_open, 'r') as f:
            dict_reader = DictReader(f)
            list_temp = list(dict_reader)
            res = None
            for sub in list_temp:
                if sub['Country'] == "Malaysia":
                    res = sub
                    break
    return list_temp


list_of_dict = get_data_csv(file_to_open)
# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = FastAPI()

# Create, Read, Update, Delete

@app.get('/')
async def home():
    #print(len(list_of_dict))
    return {"Hello World": "From FastAPI"}

@app.get('/country_by_id/{id}')
async def get_by_id(id: int):
    try:
        return list_of_dict[id]
    except:
        raise HTTPException(status_code=404, detail="ID Not Found")

@app.get('/country_by_name/{country}')
async def get_by_name(country: str):
    res = None
    try:
        for sub in list_of_dict:
            if sub['Country'] == country.title():
                res = sub
                break
    except:
        raise HTTPException(status_code=404, detail="Country Not Found")
    return res