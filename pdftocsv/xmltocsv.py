import xml.etree.ElementTree as ET

def convert_to_csv(xml):
    root = ET.fromstring(xml)

    for page in root:
        for text in page.iter('text'):
            print(text.attrib, text.text)
        break
