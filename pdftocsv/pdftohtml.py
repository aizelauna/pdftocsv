import logging
import subprocess

def convert_to_xml(pdf):
    command = ["pdftohtml", "-i", "-xml", "-stdout", pdf]
    cp = subprocess.run(command, stdout=subprocess.PIPE, encoding="utf-8")

    logging.debug("=============================================")
    logging.debug("xml extracted from %s:", pdf)
    logging.debug("---------------------------------------------")
    logging.debug("%s", cp.stdout)
    logging.debug("=============================================")

    return cp.stdout
