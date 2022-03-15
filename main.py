
from Conv import *
from convertir import *


print("##################################################")
x = input("""Taper csv pour les fichiers csv
Taper json pour les fichiers json
Taper yaml pour les fichiers yaml
Taper xml pour les fichiers xml
""")
print("##################################################")


if x == "json":
    i = int(input("Taper 1 pour convertir en YAML\nTaper 2 pour convertir en XML\n"))
    if i == 1:
        dic = json_to_dict("doc.json")
        dict_to_yaml(dic)
    elif i == 2:
        dic = json_to_dict("doc.json")
        dic = dic[0]
        e = dict_to_xml('O_D_C', dic)

        print(e)

        print(tostring(e))

        e.set('_id', '1000')

        print(tostring(e))
print("##################################################")
if x == "csv":
    i = int(input("Taper 1 pour convertir en JSON\nTaper 2 pour convertir en XML\n"))
    if i == 1:
        try:
            x = input("Entrer le nom du fichier et l'extension\n")
            dic = csv_dict(x)
            dict_to_json(dic)
        except Exception as e:
            print(e)
    elif i == 2:
        dic = json_dic("doc.json")
        # print(dic)
        dic = dic[2]
        e = dict_to_xml('O_D_C', dic)

        print(e)

        print(tostring(e))

        e.set('_id', '1000')

        print(tostring(e))
########################## json #####################################
elif x == "xml":
    i = int(input("Taper 1 pour convertir en JSON\nTaper 2 pour convertir en YAML\nTaper 3 pour convertir en CSV\n"))
    if i == 1:
        try:
            dic = xml_to_dic("doc.xml")
            dict_to_xml(dic)
        except:
            print("Veuillez verifié le fichier consommé")
    elif i == 2:
        infile = "doc.xml"
        try:
            if str(infile):
                dic = xml_to_dic(infile)
                dict_to_yaml(dic)
            else:
                print("Ce dossier n'existe pas")

        except:
            print("Le fichier ne marche pas")
    elif i == 3:
        try:
            dic= (xml_to_dict("doc.xml"))
            dict_to_csv(dic)
            print("succés")
        except Exception as e:
            print(e)

############################# ######################################
elif x == "yaml":
    dic = yaml_dict("dioum.yaml")
    i = int(input("Taper 1 pour convertir en JSON\nTaper 2 pour convertir en XML\nTaper 3 pour convertir en CSV\n"))
    if i == 1:
        dic = yaml_to_dict('dioum.yaml')
        dict_to_json(dic)
    if i == 2:
        dic = yaml_to_dict("dioum.yaml")
        dict_to_xml(dic)
    if i == 3:
        try:
            dict_to_csv()
        except Exception as e:
            print(e)
else:
    print("Oops vous avez fait un mauvais choix")
############################### ########################################
