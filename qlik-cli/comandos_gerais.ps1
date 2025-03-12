#seta proxy caso necessario
$env:https_proxy="http://XXX.XXX.XXX.XX:2020"

# Crie um alias para o comando com caminho completo
New-Alias -Name qlik -Value "\\paht\to\qlik.exe"

#unbuil de app
qlik app unbuild --app "<APP_ID>" --dir "\\PATH\TO\SALVE"

#buil de app objects
qlik app build --app "<APP_ID>" --objects "\\PATH\TO\SALVE\objects\sheet*.json"

#lista as configurações de carga
qlik reload-task ls --appId "<APP_ID>"

#lista as configurações de carga apenas atributo recurrence
$(qlik reload-task ls --appId "<APP_ID>" | ConvertFrom-Json ).recurrence

#lista as configurações de carga apenas atributo recurrence
$(qlik reload-task ls --appId "<APP_ID>" | ConvertFrom-Json ).id

#obtem dados sobre uma configuração de carga
qlik reload-task get "<RELOAD_TASK_ID>"

#apaga configuração de carga
qlik reload-task rm "<RELOAD_TASK_ID>"

#obtem dados sobre uma configuração de carga
qlik reload-task get $(qlik reload-task ls --appId "<APP_ID>" | ConvertFrom-Json ).id

#lista apps em um determinado space
qlik app ls --spaceId "<SPACE_ID>" --limit 100

#lista apps em um determinado collection
qlik app ls --collectionId "<COLLECTION_ID>" --limit 1000

#cria um agendamento de carga
qlik reload-task create --appId "<APP_ID>" --recurrence "RRULE:FREQ=DAILY;INTERVAL=1;BYHOUR=5;BYMINUTE=0;BYSECOND=0" --timeZone "America/Sao_Paulo" --retry 3 -q