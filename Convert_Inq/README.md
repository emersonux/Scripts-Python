## Conversor da saida do comando inq para csv

### Requisitos
Necessário já ter criado o arquivo com a saída do inq no formato de texto sem cabecalhos, somente os dados.

Comando recomendado
 
inq -nodots | grep emcp > arquivo.txt



Em breve terá a versão que suporta o formado de WWN
inq -nodots -wwn | grep emcp
