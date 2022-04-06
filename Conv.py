#  Import des modules
import xml.etree.ElementTree as T
from sqlalchemy import JSON
from csv import DictReader as csv_load
from yaml import safe_load
import xmltodict
from pathlib import Path
from ruamel.yaml import YAML
from yaml import dump 
from dict2xml import dict2xml
from convertir import *
import json
from pathlib import Path
import xmltodict
from ruamel.yaml import YAML
#########################################################



########################## YAML #####################
def yaml_to_dict(file):

    c = Path(file)
    yaml = YAML(typ="safe")
    f =c.open("r", encoding="utf8")
    d = yaml.load(f)
    return d
# print(yaml_to_dict('yaml.yaml')) OK

######################### CSV #######################


def csv_to_dict(file):
    with open(file, 'r') as f:
        liste = []

        r_csv = csv_load(f)
        for i in r_csv:
            liste.append(i)
        return liste

######################### XML ##########################

def xml_to_dict(file):
    with open(file,'r') as f:
        doc = xmltodict.parse(f.read())
        return json.loads(json.dumps(doc))

########################## JSON #########################

def json_to_dict(file):
    f =open(file)
    return json.load(f)