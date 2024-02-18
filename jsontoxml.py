import json
import xmltodict

def json_to_xml(input_json_path, output_xml_path):
    with open(input_json_path, 'r') as input_json_file:
        json_data = json.load(input_json_file)
        xml_data = xmltodict.unparse(json_data, pretty=True)
        with open(output_xml_path, 'w') as output_xml_file:
            output_xml_file.write(xml_data)

if __name__ == "__main__":
    input_json_path = "books.json"
    output_xml_path = "output.xml"

    json_to_xml(input_json_path, output_xml_path)
