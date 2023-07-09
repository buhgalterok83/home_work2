import xml.etree.ElementTree as ET
import json

def convert_xml_to_json(xml_file, json_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    result = {}
    for page in root.findall('page'):
        page_name = page.get('name')
        elements = {}
        for element in page.findall('element'):
            element_name = element.get('name')
            locators = {}
            for locator in element.findall('locator'):
                platform = locator.get('platform')
                locator_type = locator.get('locator_type')
                locator_value = locator.text
                locators[platform] = [locator_type, locator_value]
            elements[element_name] = locators
        result[page_name] = elements

    with open(json_file, 'w') as f:
        json.dump(result, f, indent=4)

# Пример использования
convert_xml_to_json('/Users/vitaliigoncharov/Desktop/pages.xml', '/Users/vitaliigoncharov/Desktop/pages.json')
