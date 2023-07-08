import json
import xmltodict

def convert_xml_to_json(xml_file, json_file):
    with open(xml_file, 'r') as f:
        xml_data = f.read()

    json_data = json.dumps(xmltodict.parse(xml_data), indent=4)

    with open(json_file, 'w') as f:
        f.write(json_data)

# Пример использования
convert_xml_to_json('input.xml', 'output.json')
