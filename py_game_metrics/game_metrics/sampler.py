import random
import csv
import os

class Sampler:
    def __init__(self, data):
        self._data = data
    
    def _sample_games(self, n = 20):
        """
        Amostragem aleatória do dataset de jogos. O parametro n define o número de jogos que serão amostrados, sendo 20 por padrão.
        É feita uma verificação do tamanho dataset para não permitir uma amostragem (n) maior que o número de jogos disponíveis.
        """
        if len(self._data) > n:
            try:
                return random.sample(self._data, n)
            except ValueError:
                print('O número de jogos solicitados é maior que o número de jogos disponíveis.')
                return self._data

    def save_csv(self, filename, overwrite = None):
        """
        Salva em um arquivo CSV a amostragem aleatória dos jogos realizada em `_sample_games`. 
        O parâmetro filename é o nome do arquivo que será salvo.
        O parâmetro overwrite é opcional e serve para dar a opção ao usuário de sobrescrever o arquivo caso já exista algum .csv com o mesmo nome.
        Caso o arquivo já exista e o usuário selecione 'n', a operação é cancelada. Caso selecione 's', o arquivo é sobrescrito.
        É feita uma verificação com um loop while para garantir que o usuário digite uma opção válida.
        """
        if os.path.exists(filename):
            if overwrite is None:
                print(f'O arquivo {filename} já existe. Deseja sobrescrevê-lo?')
                overwrite = input('Digite "s" para sim ou "n" para não: ')
                while overwrite not in ['s', 'n']:
                    print('Opção inválida.')
                    overwrite = input('Digite "s" para sim ou "n" para não: ')
            if overwrite == 'n':
                print('Operação cancelada.')
                return
        sample = self._sample_games()
        if sample:
            fieldnames = sample[0].keys()

            with open(filename, 'w', newline = '', encoding = 'utf-8') as file:
                writer = csv.DictWriter(file, fieldnames = fieldnames)
                writer.writeheader()
                writer.writerows(sample)
            print(f'Amostra de jogos salva em {filename}')