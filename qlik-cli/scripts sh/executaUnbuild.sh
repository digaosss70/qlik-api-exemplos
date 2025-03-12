#!/bin/bash

saida=$(/path/qlik app ls --limit 10000)


# Processa cada linha da saída
while read -r linha; do

     # Ignora a linha de cabeçalho
     if [[ "$linha" == "ID"* ]]; then
         continue
     fi

     # Extrai os substrings usando awk
     APP_ID=$(echo "$linha" | awk '{print substr($0, 1, 36)}')
     APP_NOME=$(echo "$linha" | awk '{print substr($0, 42, 1000)}')  

     /path/qlik app unbuild --app "${APP_ID}" --dir "/path/to/salve/${APP_NOME}_${APP_ID}/"

done <<< "$saida"