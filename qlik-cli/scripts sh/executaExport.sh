# #!/bin/bash

# # Executa o comando e armazena a saída em uma variável
saida=$(/path/qlik app ls  --limit 10000)

total=$(echo "$saida" | awk 'END {print NR}')

i=2
while [ $i -le $total ]
do

  apps=$(echo "$saida" | awk -v linha="$i" 'NR==linha')

  APP_ID=$(echo "$apps" | awk '{print substr($0, 1, 36)}')
  APP_NOME=$(echo "$apps" | awk '{print substr($0, 42, 1000)}')


  /path/qlik app export "$APP_ID" --NoData --output-file "/path/to/appExport/${APP_NOME}_${APP_ID}.qvf" -q

  i=$(($i + 1))

done
