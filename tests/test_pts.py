import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
sys.path.append(current_dir.as_posix() + "/../")

from pts import Points


def test_pts():
    filename = Path("assets/sample.pts").expanduser()
    points = Points(filename=filename)

    assert points.n_points == 55
