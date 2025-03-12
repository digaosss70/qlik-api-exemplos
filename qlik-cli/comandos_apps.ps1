﻿
#CRIANDO APP EM UM ESPAÇO
qlik app create --attributes-description "App de teste2" --attributes-name "APP_TESTE2" --attributes-spaceId "<SPACE_ID>"

#CRIANDO APP NO ESPAÇO PESSOAL
qlik app create --attributes-description "App de teste" --attributes-name "APP_TESTE1"

#LISTA DE APPS EM UM ESPAÇO
qlik app ls --spaceId "<SPACE_ID>" --limit 100
 
#LISTA DE APPS QUE VOCE TEM ACESSO
qlik app ls

#lista apps em um determinado collection
qlik app ls --collectionId "<COLLECTION_ID>" --limit 1000

#unbuil de app
qlik app unbuild --app "<APP_ID>" --dir "\\PATH\TO\SALVE"

#buil de app objects
qlik app build --app "<APP_ID>" --objects "\\PATH\TO\SALVE\objects\sheet*.json"

#COLOCA SCRIPT NO APP ATRAVES DE UM QVS
qlik app script set "PATH\TO\SCRIPT\SCRIPT_TESTE_CRT00.qvs" --app "<APP_ID>"

#APAGA UM APLICATIVO
qlik app rm "<SPACE_ID>"

#ATUALIZA SCRIPT DO APP
qlik app reload --app "<SPACE_ID>"

#CRIA UMA MÉTRICA NO APP ATRAVES DE UM JSON
qlik app measure set "PATH\TO\SCRIPT\CRIA_METRICAS.json" --app "<APP_ID>"

#LISTA AS MÉTRICAS DO APP
qlik app measure ls --app "<APP_ID>"

#DELETA MÉTRICA DE UM APP
qlik app measure rm mtc_dias_01 --app "<APP_ID>"

#RELOAD BACKGOUND
qlik reload create --appId "<APP_ID>"