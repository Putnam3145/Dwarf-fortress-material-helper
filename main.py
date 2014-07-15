__author__ = 'Putnam'

import materials,json

def decode_json_file(json_file_name):
    json_file = open(json_file_name,'r')
    return json.load(json_file)

JSONMats = decode_json_file('mats.json')

output=open('materials.txt','a')

for mat in JSONMats:
        output.write(materials.Material(JSONMats[mat]).rawify()+'\n\n')