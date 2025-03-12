#!/bin/bash

# Executa o comando e armazena a saída em uma variável
saida=$(/path/qlik app ls --limit 10000)

total=$(echo "$saida" | awk 'END {print NR}')

csv_path="/path/to/salve/objets.csv"

rm -f "$csv_path"

i=2
while [ $i -le $total ]
do

  apps=$(echo "$saida" | awk -v linha="$i" 'NR==linha')
  APP_ID=$(echo "$apps" | awk '{print substr($0, 1, 36)}')


DADOS=$(/path/qlik app object ls --app "$APP_ID" --no-data --json)


# Usar echo para passar o JSON para jq e converter para CSV
echo "$DADOS" | jq -r --arg app_id "$APP_ID" '
    [
        .[] |
        [
            .qId,
            .qType,
            .title,
            $app_id  # Adiciona a nova coluna com o valor de APP_ID
        ] | @csv
    ] | .[]' >> "$csv_path"



  i=$(($i + 1))

done