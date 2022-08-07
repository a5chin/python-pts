import argparse
import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
sys.path.append(current_dir.as_posix() + "/../")

from pts import Points


def make_parse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--filename",
        default="../assets/sample.pts",
        type=str,
        help="plese set filename",
    )

    return parser.parse_args()


def main():
    args = make_parse()
    filename = Path(args.filename).expanduser()
    points = Points(filename=filename)

    print(points)


if __name__ == "__main__":
    main()
