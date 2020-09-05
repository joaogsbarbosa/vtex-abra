import psycopg2
import requests


class ApiToTable():

    def __init__(self, host, database, user, password):
        self.connection = psycopg2.connect(
            host=host, database=database, user=user, password=password)
        self.cursor = self.connection.cursor()

    def request(self, url, headers=None, path=None):
        self.url = url
        self.headers = headers
        self.path = path
        self.table = Table(requests.get(url.format(1), headers=headers), path)

    @property
    def table_name(self):
        return self.table.table_name

    @table_name.setter
    def table_name(self, name):
        self.table.table_name = name

    def execute(self):
        # with pagination
        if '{}' in self.url:
            i = 1
            table_list = []
            while True:
                print('Fetching page ' + str(i) + '...')
                response = requests.get(self.url.format(i), headers=self.headers)
                try:
                    current_table = Table(response, self.path)
                except:
                    if i == 1:
                        raise
                    break
                if not current_table.data:
                    break
                current_table.table_name = self.table_name
                table_list.append(current_table)
                i += 1
            print('Total: ' + str(i - 1) + ' pages.')
            self.cursor.execute(self.table.table_query)
            for each_table in table_list:
                if type(each_table.insert_query) == type(list()):
                    for query in each_table.insert_query:
                        self.cursor.execute(query)
                else:
                    self.cursor.execute(each_table.insert_query)

        # without pagination
        else:
            self.cursor.execute(self.table.table_query)
            if type(self.table.insert_query) == type(list()):
                for query in self.table.insert_query:
                    self.cursor.execute(query)
            else:
                self.cursor.execute(self.table.insert_query)

        self.connection.commit()
        print("Operation sucess!")


class Table():

    def __init__(self, response, path=None):
        self.path = path
        self.response = response
        self.status_code = response.status_code

    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, response):
        if response.status_code == 200:
            if self.path:
                data = response.json()
                for path in self.path.split('/'):
                    if isinstance(data, list):
                        temp = []
                        for each_data in data:
                            temp.append(each_data[path])
                        data = temp
                        del temp
                    else:
                        if isinstance(data[path], list):
                            data = data[path]
                        else:
                            data = [data[path]]
                self.data = data
                if self.data:
                    if type(self.data) == type(list()):
                        self.response_keys = self.data[0].keys()
                    else:
                        self.response_keys = self.data.keys()
            else:
                if isinstance(response.json(), list):
                    self.data = response.json()
                else:
                    self.data = [response.json()]
                self.response_keys = self.data[0].keys()
        else:
            raise requests.exceptions.InvalidURL(
                'The status code received is ' + str(response.status_code) + ', but 200 is expected')
        self.response_keys = [x.replace('-', '_') for x in self.response_keys]
        self._response = response

    @property
    def table_name(self):
        return self._table_name

    @table_name.setter
    def table_name(self, name):
        alphanumeric = [character for character in name if character.isalnum()]
        alphanumeric = "".join(alphanumeric)
        self._table_name = alphanumeric

    @property
    def table_query(self):
        keys = ', '.join(
            ['col_' + str(key) + ' VARCHAR(50000)' for key in self.response_keys])
        return 'CREATE TABLE IF NOT EXISTS tbl_' + self.table_name + '(' + keys + ');'

    @property
    def insert_query(self):
        keys = ', '.join(['col_' + str(key) for key in self.response_keys])
        if type(self.data) == type(list()):
            insert_list = []
            for each_data in self.data:
                values = "'" + "','".join(map(str, each_data.values())) + "'"
                values = values.replace("''", "NULL")
                insert_list.append('INSERT INTO tbl_' + self.table_name +
                                   ' (' + keys + ')' + ' VALUES ' +
                                   '(' + values + ')' + ';')
            return insert_list
        else:
            values = "'" + "','".join(map(str, self.data.values())) + "'"
            values = values.replace("''", "NULL")
            insert = 'INSERT INTO tbl_' + self.table_name + \
                     ' (' + keys + ')' + ' VALUES ' + '(' + values + ')' + ';'
            return insert
