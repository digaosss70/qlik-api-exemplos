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

#cria um agendamento de carga
qlik reload-task create --appId "<APP_ID>" --recurrence "RRULE:FREQ=DAILY;INTERVAL=1;BYHOUR=5;BYMINUTE=0;BYSECOND=0" --timeZone "America/Sao_Paulo" --retry 3 -q