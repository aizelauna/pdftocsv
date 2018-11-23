import argparse
from .pdftohtml import convert_to_xml
from .xmltocsv import convert_to_csv

def main():
    parser = argparse.ArgumentParser(description='Convert PDF table to CSV')
    parser.add_argument('pdf',
        help='path to pdf containing the table(s) to extract')
    args = parser.parse_args()

    xml = convert_to_xml(args.pdf)

    csv = convert_to_csv(xml)
