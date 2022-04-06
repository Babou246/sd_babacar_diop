from json import *
import json
import csv
import xml.etree.ElementTree as T
from csv import DictReader as csv_load
from csv import DictWriter as csv_write
import yaml
from Conv import *
from xmltodict import parse

###########################################################
#                            JSON                         #
###########################################################


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
    with open("b.yaml", "w",encoding='utf8') as wfile:
        dic = yaml.dump(dic, wfile)
    print("Fichier crée avec succés")


##############################################################
#                            CSV                             #
##############################################################
def dict_to_csv(data, name):
    with open(f'{name}.csv', 'w',encoding='utf8') as f:
        data = [data]
        fieldnames = data[0].keys()
        output = csv_write(f, fieldnames)
        output.writeheader()
        for elem in data:
            output.writerow(elem)
        print("Fichier crée avec succés")

#############################################################
#                             XML                           #
#############################################################

def dict_to_xml(file):
    reader = loads(json.dumps(parse(file.read())))
    return reader
