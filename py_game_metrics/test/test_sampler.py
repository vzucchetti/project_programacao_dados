from pathlib import Path
import os
from game_metrics import read
from game_metrics import sampler

def test_sampler():
    script_dir = Path(__file__).resolve().parent
    file_path = script_dir.parent.parent / 'steam_games.csv'
    df = read.Read(file_path)
    data = df.dataset()
    samp = sampler.Sampler(data)
    samp.save_csv('test.csv', overwrite='n')
    assert os.path.exists('test.csv')