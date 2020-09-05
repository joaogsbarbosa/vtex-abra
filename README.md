# apiToTable
Aplicação de página única que consome dados de uma API baseada em REST e converte para tabelas do PostgreSQL

### Compatibilidades com REST APIs

- Paginação
- Sem paginação
- Um único objeto
- Multiplos objetos
- Dados contidos dentro de um único objeto

### Dependências

Estão contidas em _requirements.txt_

```python
$ pip install -r requirements.txt
```

### Uso

Abrir _app.py_

Ou para incluir em seu código, use:

```sh
$ import apitotable

# Dados de conexão com o banco de dados
$ api = apitotable.connect(host, database, user, password)

# URL de requisição. Caso paginado, utilizar {} no lugar dos números da página
# Parâmetro headers opcional, caso seja necessário seu uso
# Parâmetro path opcional, caso os dados da resposta estejam dentro de um objeto
$ api.request(url, headers, path)

# Nome da tabela para inserir os dados no banco de dados
$ api.table_name = table_name

# Executar a importação dos dados da API para o banco de dados
$ api.execute()
```