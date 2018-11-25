import logging
import xml.etree.ElementTree as ET

def convert_to_csv(xml):
    root = ET.fromstring(xml)

    for page in root:
        for text in page.iter('text'):
            logging.info("%s %s", text.attrib, text.text)
        break
