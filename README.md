# apiToTable
Aplicação de extração dos dados da API da VTEX, transformação em um modelo adequado para tabelas e upload no PostgreSQL

### Dependências

Estão contidas em _requirements.txt_

```python
$ pip install -r requirements.txt
```

### Uso

Abrir _app.py_

### Configuração

Você precisará fonecer as keys de autenticação dos ambientes **abracasa** e **abramais**

1. Criar o arquivo `settings.ini` na raiz da aplicação (mesma pasta do arquivo `app.py`)

2. Inserir os seguintes dados, substituindo onde está `INSIRAAQUI` pelo valor correto:

```ini
[settings]
ABRACASA_APPKEY=INSERIRAQUI
ABRACASA_APPTOKEN=INSIRAAQUI
ABRAMAIS_APPKEY=INSIRAAQUI
ABRAMAIS_APPTOKEN=INSIRAAQUI
```