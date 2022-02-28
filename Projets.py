#  Import des modules
import csv
from tkinter.filedialog import askopenfilename
import xml.etree.ElementTree as T
import yaml
import json
import xmltodict
from dict2xml import dict2xml

##############################################
#                 JSON                       #
##############################################
# Convertion JSON to Dic


def json_dic(file):
    with open(file) as file_:
        dico = json.load(file_)
        print(dico)


def dic_to_json(dico=None):
    json_dic(x)
    with open("dico.json", "a") as file:
        file = json.dump(dico, file)
    print(file)

##############################################################
#                           YAML                             #
##############################################################

# YAML => DICTIONNAIRE => YAML


def yalm_dic(filepath):
    with open(filepath) as file:
        dic = yaml.safe_load(file)
    print(dic)


def dict_yaml(dic=None):
    yalm_dic(x)
    with open("yaml_file.yaml", "a") as wfile:
        dic = yaml.dump(dic, wfile)
    print(dic)


##############################################################
#                            CSV                             #
##############################################################
# XML_CSV
file_path = "doc.xml"
csv_name = "ok.csv"


def xml_to_csv(file_path, csv_name) -> None:
    tree = T.parse(file_path)
    root = tree.getroot()

    with open(csv_name, 'w') as csv_file:
        writer = csv.writer(csv_file)
        headers = (child.tag for child in root[0])
        writer.writerow(headers)
        num_records = len(root)

        for record in range(num_records):
            rec = (child.text for child in root[record])
            writer.writerow(rec)
    import sys
    import pathlib
    try:
        file_path = sys.argv[1]
        csv_name = sys.argv[2]
    except IndexError:
        sys.exit("")
    with pathlib.Path(file_path) as xml_file:
        if xml_file.is_file():
            xml_to_csv(file_path, csv_name)
        else:
            sys.exit(f'On a pas trouvé le {file_path}')


xml_to_csv("doc.xml", "ok.csv")
# CSV TO DICTIONNAIRE


def csv_path(file_csv, sep=";"):
    with open(file_csv, "r") as f:
        lire = f.read()
        lignes = lire.split("\n")
        # print(lignes[0])
        liste = lignes[0].split(";")
        # Configuration du header
        id0 = liste[0]
        id1 = liste[1]
        id2 = liste[2]
        id3 = liste[3]

    for ligne in lignes:
        # print(ligne)
        dictionnaire = {}
        ligne = ligne.split(";")
        id = ligne[0]
        tri = ligne[1]
        mat = ligne[2]
        notes = ligne[3]
        # print(f"identiant :{id} Trimestre:{tri} Matiére:{mat} Notes:{notes}")

        dictionnaire = {id0: id, id1: tri, id2: mat, id3: notes}


def dic_to_csv(dic=None):
    csv_path(x)
    with open('names.csv', 'w', newline='') as csvfile:
        # header du dictionnaire
        header = ["nom", "ret", "age", "rang", "niveau", "professeur"]
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        writer.writerow(dic)
    print(csvfile)

# csv_path("notes.csv")
#############################################################
#                   TO MODIFY FILE CSV                      #
#############################################################


def modifier(file, ligne, col, val, sep=";"):
    with open(file, "r+", newline="") as f:
        r = csv.reader(f, delimiter=sep)
        lignes = list(r)
        try:
            lignes[ligne][col] = val
            f.seek(0)
            w = csv.writer(f, delimiter=sep)
            w.writerows(lignes)
            f.truncate()
        except:
            pass


modifier("notes.csv", 0, 0, "Id", sep=";")


########################################################
#                       XML                            #
# ######################################################
def xml_to_dic(filepath):
    # Conversion de xml to dic
    with open(filepath) as f:
        doc = xmltodict.parse(f.read())
        # En fait cette seconde permet de nous donner un dic propre
        dic = json.loads(json.dumps(doc))
    print(dic)


def dic_xml(dic=None):
    xml_to_dic(x)
    with open("file.xml", "w") as f:
        # J'ai transformé le dictionnaire en xml
        file = dict2xml(dic)
        # Puis je l'ai téléversé dans mon fichier file111.xml
        fi = f.write(file)
        print(fi)

################################################################
#   CONFIGURATION DE LA DIRECTION POUR CHARGER LES FICHIERS    #
################################################################
def Open():
    Directory = askopenfilename(initialdir=r"/home/abubakr/Bureau/LES_TP_SONATEL_ACADEMY/TP_Python", title="Ouvrir le fichier",
                filetypes=(("fichier json","*.json"),
                ("fichier csv","*.csv"),
                ("fichier xml","*.xml"),
                ("fichier YAML","*.yaml")))
    ext = Directory.split(".")[-1]
    if ext == "csv":
        csv_path(Directory)
    elif ext == "xml":
        dic = dic_xml(Directory)
        return dic
    elif ext == "json":
        dic = dic_to_json(Directory)
        return dic
    elif ext == "yaml":
        dic = dict_yaml(Directory)
        return dic
