#!/usr/bin/python
import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path =f"{dir_path}/gDorks.json"
f = open(file_path)

data = json.load(f)
for i in data:
    print(i['url'])

