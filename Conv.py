#  Import des modules
import xml.etree.ElementTree as T
from sqlalchemy import JSON
from csv import DictReader as csv_load
from csv import DictWriter as csv_write
import yaml
import xmltodict
from pathlib import Path
from ruamel.yaml import YAML
from dict2xml import dict2xml
from convertir import *
from dict import *
import csv
import json
from pathlib import Path
import xmltodict
from ruamel.yaml import YAML
#########################################################
file = """
    {
        "employees":
        [
            { 
              "firstName":"John",
              "lastName":"Doe" 
            },
            { 
              "firstName":"Anna", 
              "lastName":"Smith" 
            },
            { 
              "firstName":"Peter", 
              "lastName":"Jones" 
            }
        ]
    }
"""
########################## YAML #####################
def yaml_to_dict(file):
    c = Path(file)
    yaml = YAML(typ="safe")
    f =c.open("r", encoding="utf8")
    d = yaml.load(f)
    return d
#print(yaml_dict(file))

######################### CSV #######################
import csv
file = 'doc.csv'

def csv_to_dict(file):
    with open('file.csv', 'w') as f:   
        data = [data]
        fieldnames = data[0].keys()
        output = csv_write(f, fieldnames)
        output.writeheader()
        for elem in data:
            output.writerow(elem)


######################### XML ##########################
# file = 'doc.xml'
def xml_to_dict(file):
    with open(file) as f:
        doc = xmltodict.parse(f.read())
        return json.loads(json.dumps(doc))

# print(xml_to_dict((file)))

########################## JSON #########################
file = 'doc.json'
def json_to_dict(file):
    f =open(file)
    return json.load(f)

print(json_to_dict(file))