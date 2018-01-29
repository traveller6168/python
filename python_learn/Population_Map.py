#!/usr/bin/env python3

import json

file_name = 'population_data.json'

with open(file_name) as f:
    pop_data = json.load((f))

for pop_dic in pop_data:
    if pop_dic["Year"] == '2010':
        country_name = pop_dic['Country Name']
        population = int(float(pop_dic['Value']))
        print(country_name+":"+population)




