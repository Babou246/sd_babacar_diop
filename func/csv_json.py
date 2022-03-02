import json,csv

def csv_json(file):
	with open(file, 'r') as f:
		reader = csv.reader(f)
		next(reader)
		data = []
		for row in reader:
			data.append({"name": row[0], "rollnumber": row[1], "age": row[2]})
	open("file.json", 'w')
	d = json.dumps(data, indent=4)
	print(d)

