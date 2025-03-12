
#VERIFICA O ID DO DATAFILES (CONECTION ID) BUSCANDO PELO ID DO ESPAÇO
qlik data-file connection ls | jq '[.[] | select(.spaceId == """"<SPACE_ID>"""") | {id: .id}][0].id' 

#UPLOAD DE NOVO ARQUIVO EM UM ESPAÇO COM O DATAFILES (CONECTION ID)
qlik data-file create -f "C:\Users\Asus\Desktop\dfsdf.txt" --name "ArquivoTeste.txt" --connectionId "<CONNECTION_ID>"

##UPLOAD DE NOVO ARQUIVO NO ESPAÇO PESSOAL
qlik data-file create -f "C:\Users\Asus\Desktop\dfsdf.txt" --name "ArquivoTeste1.txt"

#LISTAR AQUIVOS DO MEU ESPAÇO PESSOAL
qlik data-file ls 

#LISTAR AQUIVOS DE UM ESPAÇO BUSCADO PELO (CONECTION ID) BUSCANDO PELO ID DO ESPAÇO
qlik data-file ls --connectionId "<CONNECTION_ID>"

#UPDATE DE ARQUIVO CRIADO EM UM ESPAÇO BUSCADO PELO (CONECTION ID) BUSCANDO PELO ID DO ESPAÇO
qlik data-file update "<DATA_FILE_ID>" --connectionId "<CONNECTION_ID>" --file "C:\Users\Asus\Desktop\dfsdf.txt"

#UPDATE DE ARQUIVO CRIADO NO MEU ESPAÇO PESSOAL
qlik data-file update "<DATA_FILE_ID>" --file "C:\Users\Asus\Desktop\dfsdf.txt"

#UPDATE DE ARQUIVO CRIADO NO MEU ESPAÇO PESSOAL E GERANDO UM LOG CONCATENANDO
qlik data-file update "<DATA_FILE_ID>" --file "C:\Users\Asus\Desktop\dfsdf.txt" >> "C:\Users\Asus\Desktop\LOG.txt"

#UPDATE DE ARQUIVO CRIADO NO MEU ESPAÇO PESSOAL E GERANDO UM LOG UNICO
qlik data-file update "<DATA_FILE_ID>" --file "C:\Users\Asus\Desktop\dfsdf.txt" > "C:\Users\Asus\Desktop\LOG.txt"

#DELETAR UM UNICO ARQUIVO
qlik data-file rm "<DATA_FILE_ID>"