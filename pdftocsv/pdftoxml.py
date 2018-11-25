import logging
import subprocess
import xml.etree.ElementTree as ET

def convert_to_xml(pdf):
    command = ["pdftohtml", "-i", "-xml", "-stdout", pdf]
    cp = subprocess.run(command, stdout=subprocess.PIPE, encoding="utf-8")

    logging.debug("=============================================")
    logging.debug("xml extracted from %s:", pdf)
    logging.debug("---------------------------------------------")
    logging.debug("%s", cp.stdout)
    logging.debug("=============================================")

    return cp.stdout

def cleanup_xml(xml):
    root = ET.fromstring(xml)

    for page in root:
        for text in page.iter('text'):
            # Remove bold elements while keeping text
            b = text.find("b")
            if b is not None:
                text.text = b.text
                text.remove(b)

    clean_xml = ET.tostring(root, encoding="unicode")

    logging.debug("=============================================")
    logging.debug("cleaned up xml")
    logging.debug("---------------------------------------------")
    logging.debug("%s", clean_xml)
    logging.debug("=============================================")

    return clean_xml
