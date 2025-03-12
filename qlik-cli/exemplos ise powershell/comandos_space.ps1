
#Criar espaço com o nome QLIK-CLI_EPACO do tipo shared
qlik space create --name "NOME_SPACO" --type "shared"

#Listar espaços
qlik space ls | jq '.[] |{nome: .name,id: .id}'

#Deletar espaço QLIK-CLI_EPACO usando o id
qlik space rm "<SPACE_ID>"

#Editar Descrição espaço
qlik space update "<SPACE_ID>" --description "Espaço de testes"