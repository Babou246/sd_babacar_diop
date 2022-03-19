from json import *
import json
import csv
import xml.etree.ElementTree as T
from csv import DictReader as csv_load
from csv import DictWriter as csv_write
from sqlalchemy import JSON
import yaml
from Conv import *
from xmltodict import parse

###########################################################
#                            JSON                         #
###########################################################


d = {'students': {'student': [{'name': 'Rick Grimes', 'rollnumber': '1', 'age': '15'}, {'name': 'Lori Grimes', 'rollnumber': '2', 'age': '16'}, {'name': 'Carl Grimes', 'rollnumber': '3', 'age': '14'}, {'name': 'Judith Grimes', 'rollnumber': '4', 'age': '13'}]}}
def dict_to_json(dico):
    try:
        with open("moi.json", "w") as file:
            file = json.dump(dico, file)
            return (file)
    except Exception as e:
        print(e)
# print(dict_to_json(d))


##############################################################
#                           YAML                             #
##############################################################
def dict_to_yaml(dic):
    with open("yama.yaml", "w") as wfile:
        dic = yaml.dump(dic, wfile)
    print(dic)
# dict_to_yaml(d)





##############################################################
#                            CSV                             #
##############################################################
def dict_to_csv(data):
    with open('file.csv', 'w') as f:   
        data = [data]
        fieldnames = data[0].keys()
        output = csv_write(f, fieldnames)
        output.writeheader()
        for elem in data:
            output.writerow(elem)


#############################################################
#                             XML                           #
#############################################################

def dict_to_xml(file):
    reader = loads(json.dumps(parse(file.read())))
    return reader
