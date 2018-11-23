from .pdftohtml import convert_to_xml

def convert_to_csv(pdf):
    xml = convert_to_xml(pdf)
    print(xml)
