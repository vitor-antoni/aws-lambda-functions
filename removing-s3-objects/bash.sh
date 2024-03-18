#!/bin/bash

# Baixar o a package "pytz"
pip install pytz -t ./

# Zipa os arquivos e manda para o AWS Lambda
zip -r pytz.zip pytz/
