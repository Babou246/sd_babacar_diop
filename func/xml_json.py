import xmltodict,json

#
# def xml_json(file):
# 	with open(file, 'r') as dfile:
# 		obj = xmltodict.parse(dfile.read())
# 	print(json.dumps(obj))


import csv
with open('file/file1.csv') as file:
    dic = []
    for i in csv.DictReader(file):
        d =dic.append(i)
    print(dic)
