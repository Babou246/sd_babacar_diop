import json

def json_xml():
	with open("dico.json") as f:
		data = json.load(f)
	# dictionnaire
	print(data)

	import xml.etree.ElementTree as T

	root = T.Element("")
	T.SubElement(root, "date").text = data["date"]
	T.SubElement(root, "time").text = data["time"]
	T.SubElement(root, "to").text = data["to"]
	T.SubElement(root, "from").text = data["from"]
	T.SubElement(root, "msg").text = data["msg"]
	result = T.SubElement(root, "result")

	for i in data["result"]:
		T.SubElement(result, "fer").text = i["fer"]
		T.SubElement(result, "score").text = str["score"]
	tree = T.ElementTree(root)
	tree.write("doc1.xml")

