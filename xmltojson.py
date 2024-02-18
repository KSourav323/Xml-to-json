import xmltodict
import json

def convert_xml_to_json(xml_file_path, json_file_path):
    with open(xml_file_path, 'r') as xml_file:
        xml_data = xml_file.read()
        json_data = xmltodict.parse(xml_data)
        with open(json_file_path, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)

xml_file_path = 'books.xml'
json_file_path = 'books.json'

convert_xml_to_json(xml_file_path, json_file_path)
