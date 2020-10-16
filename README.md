# apiToTable
Aplicação de extração dos dados da API da VTEX, transformação em um modelo adequado para tabelas e upload no PostgreSQL

### Dependências

Utilizado interpretador Python versão 3.7.9

Dependências estão contidas em _requirements.txt_

```python
$ pip install -r requirements.txt
```

### Uso

##### Com menu interativo

Caso você esteja dentro de um ambiente gráfico, abrir _app.py_

##### Com argumentos

Método ideal para servidores, usar:

`python app.py [data]`

Substituir `[data]` pela data no formato **aaaa-mm-dd**

Essa será a data inicial que será usada para baixar os dados

### Configuração

Você precisará fonecer as keys de autenticação dos ambientes **abracasa** e **abramais** e os dados de acesso do banco de dados PostgreSQL.

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