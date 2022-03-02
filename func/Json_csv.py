from flatten_json import flatten
import csv
json_data = "d1"
json_flatten_data = flatten(json_data)

file = open("data.csv","w")
all_keys = []
for elts in json_flatten_data:
	all_keys.append(elts)
writter = csv.DictWriter(file,all_keys)
writter.writeheader()
writter.writerow(json_flatten_data)
file.close()