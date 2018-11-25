# pdftocsv

CLI tool to convert PDF table to CSV

## Prerequisites

```shell
$ sudo apt install python3-pip python3-pytest poppler-utils
```

> poppler-utils: *pdftohtml* is used to convert pdf file to xml.

## Install / Uninstall

```shell
# Install pdftocsv into ~/.local/bin
$ pip3 install -e .

# Uninstall
$ pip3 uninstall .
```

# Test suite

```shell
$ pytest-3
```
