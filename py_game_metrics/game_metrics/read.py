import csv

from datetime import datetime

class Read:
    def __init__(self, name, encoding="utf-8"):
        self.name = name
        self.encoding = encoding
        self._data = None
        self._header = None
    
    def _data_(self):
        """Retorna os dados do arquivo CSV em uma lista, separando o cabeçario do restante dos dados."""
        if self._data is None:
            with open(self.name, 'r', encoding = self.encoding) as file:
                dados = csv.reader(file)
                self._data = list(dados)
                self._header = self._data[0]
                self._data = self._data[1:]
        return self._data

    def _header_(self):
        """Retorna o cabeçario do arquivo CSV."""
        if self._header is None:
            self._data_()
        return self._header
    
    def _to_dict_(self):
        """Retorna os dados do arquivo CSV em formato de dicionário."""
        if self._header is None:
            self._data_()
        return [dict(zip(self._header_(), row)) for row in self._data_()]
        
    
    def __len__(self):
        return len(self._to_dict_())
    
    def _valid_date_(self, date_str):
        """Verifica se a data está no formato YYYY-MM-DD para poder realizar os cálculos de jogos por ano."""
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False
    
    def dataset(self):
        """
        Retorna os dados do arquivo CSV já em formato de dicionário. Aqui são realizadas transformações nos dados para adequar as datas no formato YYYY-MM-DD e os preços em float.
        As transformações são feitas para que os dados possam ser utilizados em cálculos e análises dos módulos.
        """
        data_dict = self._to_dict_()
        for row in data_dict:
            if 'Release date' in row:
                try:
                    release_date = datetime.strptime(row['Release date'], '%b %d, %Y')
                    row['Release date'] = release_date.strftime('%Y-%m-%d')
                except:
                    try:
                        release_date = datetime.strptime(row['Release date'], '%b %Y')
                        row['Release date'] = release_date.strftime('%Y-%m-%d')
                    except ValueError:
                        if not self._valid_date_(row['Release date']):
                            print(f'Formato de data não reconhecido: {row["Release date"]}')
            if 'Price' in row:
                row['Price'] = float(row['Price'])
            if 'Average playtime forever' in row:
                row['Average playtime forever'] = int(row['Average playtime forever'])
        return data_dict