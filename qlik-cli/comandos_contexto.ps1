﻿
#LOGAR EM UM TENANT MANUALMENTE
qlik context init

#LISTAR TENANTS
qlik context ls

#CRIAR CONTEXTO
qlik context create "NOME_CONTEXTO" --server "https://SEU_HOST.us.qlikcloud.com" --api-key "<SUA_API_KEY>"

#USAR UM TENANT ESPECIFICO
qlik context use "NOME_CONTEXTO"