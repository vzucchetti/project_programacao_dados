from datetime import datetime

class Stats:
    def __init__(self, data):
        self._data = data
    
    def free(self):
        """Retorna os jogos gratuitos do dataset ('Price = 0)."""
        free = [game for game in self._data if game['Price'] == 0]
        return len(free)

    def paid(self):
        """Retorna os jogos pagos do dataset ('Price > 0)."""
        paid = [game for game in self._data if game['Price'] > 0]
        return len(paid)

    def percentage(self):
        """Calcula a porcentagem de jogos gratuitos e pagos em função do número total de jogos no dataset."""
        total = len(self._data)
        free = (self.free()/total)*100
        paid = (self.paid()/total)*100
        return [free, paid]
    
    def games_per_year(self):
        """
        Identifica o ano de lançamente de cada jogo, faz uma contagem de jogos por ano e retorna um dicionário com essas informações.
        É feita uma verificação do formato da data para que seja possível realizar a contagem por cada ano.
        """
        games_by_year = {}
        for game in self._data:
            if 'Release date' in game and isinstance(game['Release date'], str):
                try:
                    year = datetime.strptime(game['Release date'], '%Y-%m-%d').year
                except TypeError:
                    print(f'Formato de data não reconhecido: {game["Release date"]}')
                    continue
            if year in games_by_year:
                games_by_year[year] += 1
            else:
                games_by_year[year] = 1
        return games_by_year
    
    def year_most_games(self):
        """Identifica o ano com o maior número de jogos lançados e retorna uma lista com o(s) ano(s) e a quantidade total de jogos lançados."""
        games_by_year = self.games_per_year()
        if games_by_year:
            max_games = max(games_by_year.values())
            year_max = [year for year, count in games_by_year.items() if count == max_games]
            return [year_max, max_games]
        else:
            return None, 0
        
    def _genres(self):
        """Separa os gêneros dos jogos e retorna uma lista com os gêneros únicos."""
        genres = set()
        n = 0
        for game in self._data:
            if 'Genres' in game:
                try:
                    for genre in game['Genres'].split(','):
                        if genre == '':
                            pass
                        else:
                            genres.add(genre)
                except ValueError:
                    n += 1
                    print(f'{n} jogo(s) não possui(em) gênero específicado.')
                    continue
        return list(genres)
    
    def playtime_per_gender(self):
        """"
        Pega o tempo médio de cada jogo e calcula a somatória por gênero, retorna um dicionário com essas informações.
        O tempo médio por gênero é convertido de minutos para horas.
        """
        playtime = {}
        for genre in self._genres():
                playtime[genre] = 0                   
        for game in self._data:
            if 'Average playtime forever' in game:
                for genre in game['Genres'].split(','):
                    if genre == '':
                        pass
                    else:
                        playtime[genre] += game['Average playtime forever'] / 60
        return playtime
    
    def top5_playtime(self):
        """Faz um ordenamento decrescente do tempo médio de jogo por gênero e cria uma lista dos 5 gêneros com maior tempo médio de jogo em horas."""
        top_5 = []
        sorted_genders = sorted(self.playtime_per_gender().items(), key=lambda x: x[1], reverse=True)
        top_sorted = sorted_genders[:5]
        for genre, playtime in top_sorted:
            top_5.append([genre, playtime])
        return top_5