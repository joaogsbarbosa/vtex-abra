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

A API que é consumida da VTEX é a [Get Order](https://developers.vtex.com/vtex-rest-api/reference/orders#getorder)

Os dados são extraídos dentro do intervalo de datas que foi definido através
dos parâmetros no momento da execução.

Os dados são transformados em queries compatíveis com o banco de dados.

É feito um upsert no banco de dados com o seguinte procedimento:

1. Verifica se o registro existe através da chave primária "orderId" da tabela "orders".

1. Se o registro existir, atualiza as colunas "status" e "statusDescription" da tabela "orders".

2. Se o registro não existir, faz o insert e insere o pedido em todas as tabelas.

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
DB_DRIVER=INSIRAAQUI
DB_HOST=INSIRAAQUI
DB_NAME=INSIRAAQUI
DB_USER=INSIRAAQUI
DB_PASSWORD=INSIRAAQUI
```

Em *DB_DRIVER*, os valores permitidos são:
- mysql
- postgres