#  Import des modules
import csv
import xml.etree.ElementTree as T
import yaml
import json
import xmltodict
from ruamel.yaml import YAML
from dict2xml import dict2xml
from func import xml_json
# from func import yaml_json
# from func import json_yaml


##############################################
#                 JSON                       #
##############################################
# Convertion JSON to Dic


def json_dic(infile):
	with open(infile) as file_:
		dico = json.load(file_)
	#print(dico)


def dic_to_json(dico=None):
	json_dic(x)
	with open("dico.json", "a") as file:
		file = json.dump(dico, file)
	print(file)

def json_yaml(infile, oufile):
	# infile = "dico.json"
	# oufile = "yaml_file.yaml"
	yaml = YAML(typ="safe")

	with open(infile, "r", encoding="utf8") as i:
		data = yaml.load(i)
	# print(data)

	open(oufile, 'w', encoding="utf8")
	d = json.dumps(data, indent=4, ensure_ascii=False)
	print(d)


##############################################################
#                           YAML                             #
##############################################################
# YAML ==> dictionnaire
def yaml_dict(infile):
	yaml = YAML(typ="safe")
	with open(infile, "r", encoding="utf8") as i:
		data = yaml.load(i)
	print(data)

def yaml_json(infile):
	oufile = "file.json_out.file"
	yaml = YAML(typ="safe")

	with open(infile, "r", encoding="utf8") as i:
		data = yaml.load(i)
	# print(data)

	open(oufile, 'w', encoding="utf8")
	d = json.dumps(data, indent=4, ensure_ascii=False)
	print(d)




def yalm_dic(infile):
	open(infile)
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


def xml_to_csv(file_path,csv_name):
	tree = T.parse(file_path)
	root = tree.getroot()

	with open("file/file1.csv", 'w') as csv_file:
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
			print(xml_to_csv(file_path, csv_name))
		else:
			sys.exit(f'On a pas trouvé le {file_path}')


# xml_to_csv("doc.xml", "ok.csv")
# CSV TO DICTIONNAIRE


def csv_path(file_csv, sep=";"):
	with open("notes.csv", "r") as f:
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
		if len(ligne) == 4:
			ligne = ligne.split(";")
			id = ligne[0]
			tri = ligne[1]
			mat = ligne[2]
			notes = ligne[3]
		# print(f"identiant :{id} Trimestre:{tri} Matiére:{mat} Notes:{notes}")

		dictionnaire = {id0: id, id1: tri, id2: mat, id3: notes}
def csv_dict(file):
	with open(file) as f:
		for i in csv.DictReader(f):
			d = (dict(i))
		#print(d)

def dic_to_csv(dic):
	with open('file/names.csv', 'w', newline='') as csvfile:
		# header du dictionnaire
		header = ["black", "description", "name", "species", "thumbnail"]
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


# modifier("notes.csv", 0, 0, "Id", sep=";")


########################################################
#                       XML                            #
# ######################################################
def xml_to_dic(infile):
	# Conversion de xml to dic
	with open(infile) as f:
		doc = xmltodict.parse(f.read())
		# En fait cette seconde permet de nous donner un dic propre
		dic = json.loads(json.dumps(doc))
	#print(dic)


def dic_xml(dic):
	with open("file/file.xml", "w") as f:
	# J'ai transformé le dictionnaire en xml
		file = dict2xml(dic)
		# Puis je l'ai téléversé dans mon fichier file111.xml
		fi = f.write(file)
		print(fi)



print("##################################################")
x = input("""Taper csv pour les fichiers csv
Taper json pour les fichiers json
Taper yaml pour les fichiers yaml
Taper xml pour les fichiers xml
""")
print("##################################################")
if x == "json":
	i = int(input("Taper 1 pour convertir en YAML\nTaper 2 pour convertir en XML"))
	if i == 1:
		json_yaml("file/dico.json","namo.yaml")
	elif i == 2:
		dic = json_dic("file/dico.json")
		dic_xml(dic)
print("##################################################")
if x == "csv":
	i = int(input("Taper 1 pour convertir en JSON\nTaper 2 pour convertir en XML"))
	if i == 1:
		dic = csv_dict("file1.csv")
		dic_to_json(dic)
	elif i == 2:
		dic = json_dic("file/dico.json")
		dic_xml(dic)
##########################json#####################################
elif x == "xml":
	i = int(input("Taper 1 pour convertir en JSON\nTaper 2 pour convertir en YAML\nTaper 3 pour convertir en CSV\n"))
	if i == 1:
		try:
			xml_json("file/doc.xml")
		except:
			print("Veuillez verifié le fichier consommé")
	elif i == 2:
		infile = "file/doc.xml"
		try:
			if str(infile):
				dic = xml_to_dic("file/doc.xml")
			else:
				print("Ce dossier n'existe pas")
			dic_to_json(dic)
		except:
			print("Le fichier ne marche pas")
	elif i == 3:
		xml_to_csv("file/doc.xml","namo.csv")
###################################################################
elif x == "yaml":
	i = int(input("*Taper 1 pour convertir en JSON\nTaper 2 pour convertir en XML\nTaper 3 pour convertir en CSV\n"))
	if i == 1:
		yaml_json('file/dioum.yaml')
	if i == 2:
		dic = yaml_dict("file/dioum.yaml")
		dic_xml(dic)
	if i == 3:
		dic = yaml_dict("file/dioum.yaml")
		dic_to_csv(dic)
else:
	print("Oops vous avez fait un mauvais choix")
#######################################################################