# API-VTEX
Aplicação de extração dos dados da API da VTEX, transformação em um modelo adequado para tabelas e upload em
um banco de dados relacional

### Dependências

Utilizado interpretador Python versão 3.7.9

Dependências estão contidas em _requirements.txt_

```python
$ pip install -r requirements.txt
```

### Uso

São definidos os seguintes parâmetros no momento da execução da aplicação:

`python app.py [dias anteriores - início] [dias anteriores - fim]`

Substituir `[dias anteriores - início]` e `[dias anteriores - fim]`
pela quantidade de dias que deseja subtrair da data atual.

Esses dois parâmetros definem um intervalo fechado das datas que serão extraídas da VTEX.

Exemplo:

`python app.py -2 -1`

Os parâmetros acima definem uma data de 2 dias atrás até 1 dia atrás. Nesse caso, ontem e anteontem.

Se estamos no dia 10/05/21, então as datas selecionadas são de 08/05/21 até 09/05/21.

`python app.py -7 0`

Os parâmetros acima definem uma data de 7 dias atrás até o dia atual.

Se estamos no dia 20/10/18, as datas selecionadas são do dia 13/10/18 até o dia 20/10/18.

### Comportamento

É definido um intervalo de datas utilizando os parâmetros que foram informados no momento da execução da aplicação.

Essas dadas são separadas por dia e o processo de ETL é repetido para cada dia distinto.

A extração dos dados consiste em utilizar a [API List Orders](https://developers.vtex.com/vtex-rest-api/reference/orders#listorders)
para buscar todos os pedidos de um determinado dia e consultar cada pedido usando a
API [Get Order](https://developers.vtex.com/vtex-rest-api/reference/orders#getorder).

#### MySQL

É feito um upsert no banco de dados com o seguinte procedimento:

1. Se o registro existir, atualiza os dados.

2. Se o registro não existir, insere o pedido em todas as tabelas.

### Configuração

Você precisará fonecer as keys de autenticação dos ambientes **abracasa** e **abramais** e os dados de acesso do banco de dados.

1. Criar o arquivo `settings.ini` na raiz da aplicação (mesma pasta do arquivo `app.py`)

2. Inserir os seguintes dados, substituindo onde está `INSIRAAQUI` pelo valor correto:

```ini
[settings]
ABRACASA_APPKEY=INSERIRAQUI
ABRACASA_APPTOKEN=INSIRAAQUI
ABRAMAIS_APPKEY=INSIRAAQUI
ABRAMAIS_APPTOKEN=INSIRAAQUI
DB_HOST=INSIRAAQUI
DB_NAME=INSIRAAQUI
DB_USER=INSIRAAQUI
DB_PASSWORD=INSIRAAQUI
```
