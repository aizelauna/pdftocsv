import subprocess

def convert_to_xml(pdf):
    command = ["pdftohtml", "-i", "-xml", "-stdout", pdf]
    cp = subprocess.run(command, stdout=subprocess.PIPE, encoding="utf-8")
    return cp.stdout
