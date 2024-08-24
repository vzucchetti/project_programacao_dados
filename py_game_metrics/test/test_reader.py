from pathlib import Path
from game_metrics import read

def test_read():
    script_dir = Path(__file__).resolve().parent
    file_path = script_dir.parent.parent / 'test.csv'
    test = read.Read(file_path)
    test = test.dataset()
    assert test is not None