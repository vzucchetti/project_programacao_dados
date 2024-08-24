from pathlib import Path
from game_metrics import read
from game_metrics import stats

class TestClass():
    def setup_method(self):
        script_dir = Path(__file__).resolve().parent
        file_path = script_dir.parent.parent / 'test.csv'
        df = read.Read(file_path)
        data = df.dataset()
        self.st = stats.Stats(data)

    def test_percentage(self):
        assert self.st.percentage() == [10.0, 90.0]

    def test_games_per_year(self):
        assert self.st.games_per_year() == {2021: 7, 2019: 1, 2022: 1, 2023: 1, 2017: 3, 2018: 2, 2014: 2, 2016: 1, 2020: 2}

    def test_year_most_games(self):
        assert self.st.year_most_games() == [[2021], 7]

    def test_playtime_per_gender(self):
        assert self.st.playtime_per_gender() == {'Accounting': 0.0, 'Free to Play': 0.0, 'Action': 0.0, 'Early Access': 0.0, 'Adventure': 2.7333333333333334, 'Indie': 3.6, 'RPG': 8.283333333333333, 'Strategy': 0.8833333333333334, 'Sports': 0.0, 'Simulation': 0.8666666666666667, 'Casual': 3.6}

    def test_top5_playtime(self):
        expected = [['RPG', 8.283333333333333], ['Indie', 3.6], ['Casual', 3.6], ['Adventure', 2.7333333333333334], ['Strategy', 0.8833333333333334]]
        actual = self.st.top5_playtime()
        assert expected == actual