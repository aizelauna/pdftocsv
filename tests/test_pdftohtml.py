import xml.etree.ElementTree as ET
from pdftocsv.pdftohtml import convert_to_xml

def test_convert_to_xml():
    xml = convert_to_xml("tests/assets/trail-fleur-de-lys-2018.pdf")
    root = ET.fromstring(xml)

    pages = root.findall('page')

    assert len(pages) == 1

    texts = pages[0].findall('text')

    assert len(texts) == 265
    assert texts[0].find('b').text == 'Pl.'
    assert texts[0].attrib['top'] == '111'
    assert texts[5].text == "1."
    assert texts[5].attrib['top'] == '128'
    assert texts[238].text == "44. POUX Jean-Paul"
    assert texts[239].attrib['top'] == '944'
