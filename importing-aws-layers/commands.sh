#!/bin/bash

# Define o diretório raiz e
# instala a package dentro do diretório `python`
cd ~
mkdir python
pip install requests -t python/

# Algumas bibliotecas possuem dependências
# então podemos identifica-lás pelo comando abaixo
pip show requests | grep Requires
>>> "Requires: certifi, charset-normalizer, idna, urllib3"

pip install certifi, charset-normalizer, idna, urllib3 -t python/

# Zipar a pasta Python
zip -r python.zip python/
