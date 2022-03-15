import json
import csv
import xml.etree.ElementTree as T
from sqlalchemy import JSON
import yaml
import xmltodict

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
def dict_to_csv(dic):
    # dic =  [
	# 	{'id': 456, 'name': 'Babacar', 'skills': 'Python'},
	# 	{'id': 892, 'name': 'Adama', 'skills': 'Java'},
	# 	{'id': 178, 'name': 'Ousseynou', 'skills': 'Mongo db'},
	# 	{'id': 155, 'name': 'Samba', 'skills': 'Sql'},
	# 	{'id': 299, 'name': 'Matthieu', 'skills': 'Ruby'},
	# 	]
    
	# header = ['id', 'name', 'skills']
	header = ['name', 'rollnumber', 'age']
	with open('DATA.csv', 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames = header)
		writer.writeheader()
		writer.writerows(dic)



#############################################################
#                             XML                           #
#############################################################
from xml.etree.ElementTree import Element,tostring 
  
def dict_to_xml(tag, d): 
  
    elem = Element(tag) 
    for key, val in d.items(): 
        
        
        child = Element(key) 
        child.text = str(val) 
        elem.append(child) 
          
    return elem 
  
