import os
from csv import DictReader
from pathlib import Path
from csv2list import get_data_csv

data_folder = Path(os.getcwd())
population_filename = data_folder / 'world_population.csv'
gdp_filename = data_folder / 'world_country_gdp_usd.csv'
happiness_filename = data_folder / 'World Happiness Report 2022.csv'

list_of_dict = get_data_csv(population_filename)

print(len(list_of_dict))
print(list_of_dict[0])