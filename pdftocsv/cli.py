import argparse
import sys
from logging import basicConfig, DEBUG, INFO, WARNING
from .pdftohtml import convert_to_xml
from .xmltocsv import convert_to_csv

def main():
    parser = argparse.ArgumentParser(description='Convert PDF table to CSV')
    parser.add_argument('pdf',
        help='path to pdf containing the table(s) to extract')
    parser.add_argument("-v", "--verbosity", action="count", default=0,
        help="increase output verbosity (0:warning, 1:info, 2:debug)")
    args = parser.parse_args()

    if args.verbosity >= 2:
        basicConfig(stream=sys.stdout, level=DEBUG, format="%(message)s")
    elif args.verbosity >= 1:
        basicConfig(stream=sys.stdout, level=INFO, format="%(message)s")
    else:
        basicConfig(stream=sys.stdout, level=WARNING, format="%(message)s")

    xml = convert_to_xml(args.pdf)

    csv = convert_to_csv(xml)
