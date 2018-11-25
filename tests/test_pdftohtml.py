import xml.etree.ElementTree as ET
from pdftocsv.pdftohtml import convert_to_xml

def test_convert_to_xml():
    # Convert pdf to xml
    xml = convert_to_xml("tests/assets/trail-fleur-de-lys-2018.pdf")

    # Check that important tags and attributes are correctly converted
    root = ET.fromstring(xml)

    pages = root.findall('page')
    assert len(pages) == 1

    fontspecs = pages[0].findall('fontspec')
    assert len(fontspecs) == 2
    assert fontspecs[0].attrib['size'] == '12'
    assert fontspecs[0].attrib['family'] == 'Times'

    texts = pages[0].findall('text')
    assert len(texts) == 265
    assert texts[0].find('b').text == 'Pl.'
    assert texts[0].attrib['top'] == '111'
    assert texts[0].attrib['left'] == '95'
    assert texts[0].attrib['width'] == '18'
    assert texts[0].attrib['height'] == '14'
    assert texts[0].attrib['font'] == '0'

    assert texts[5].text == "1."
    assert texts[5].attrib['top'] == '128'
    assert texts[5].attrib['left'] == '89'
    assert texts[5].attrib['width'] == '12'
    assert texts[5].attrib['height'] == '14'
    assert texts[5].attrib['font'] == '1'
