from json import dump as jdump
from json import load
from json import loads
from json import dumps
from yaml import dump as ydump
from yaml import safe_load
from csv import DictReader as csv_load
from csv import DictWriter as csv_write
from xmltodict import parse
from dicttoxml import dicttoxml as dtx


# fonction permettant de lire un fichier avec une extension donnée et de le mettre sous format dico en python
def python_structure(file):
    reader = ''
    with open(file, 'r',encoding='utf8') as thefile:
        if file.endswith('.json'):
            reader = load(thefile)
        elif file.endswith('.yaml') or file.endswith('.yml'):
            reader = safe_load(thefile)
        elif file.endswith('.csv'):
            # this = {}
            this = []
            k = 0
            reader = csv_load(thefile)

            for element in reader:
                this.append(element)
            reader = this
        elif file.endswith('.xml'):
            reader = loads(dumps(parse(thefile.read())))
        return reader

# fonction permettant de convertir un dico en un format fichier de donnée en parametre
def converter(pdata, name, extent):
    with open(f'{name}.{extent}', 'w',encoding='utf8') as target:
        if extent == 'json':
            jdump(dumps(pdata), target)
        elif extent == 'yaml' or extent == 'yml':
            ydump(pdata, target)
        elif extent == 'csv':
            pdata = [pdata]
            fieldnames = pdata[0].keys()

            output = csv_write(target, fieldnames)
            output.writeheader()
            for elem in pdata:
                output.writerow(elem)
        elif extent == 'xml':
            xml = dtx(pdata)
            target.write(str(xml, 'utf-8'))
        else:
            print("Ce format de fichier n'est pas pris en compte !")

    print(f"{name}.{extent} est créé avec succès ! " )
