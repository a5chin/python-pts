from typing import Union
from pathlib import Path

import numpy as np


class Points:
    def __init__(self, filename: Union[str, bytes, Path]) -> None:
        self.filename = filename
        self.array = self._read_pts()
        self.n_points = len(self.array)

    def _read_pts(self) -> np.ndarray:
        """Read a .PTS landmarks file into a numpy array"""
        with open(self.filename, "rb") as f:
            rows = version = None
            for line in f:
                if line.startswith(b"//"):
                    continue
                header, _, value = line.strip().partition(b":")
                if not value:
                    if header != b"{":
                        raise ValueError("Not a valid pts file")
                    if version != 1:
                        raise ValueError(
                            f"Not a supported PTS version: {version}"
                        )
                    break
                try:
                    if header == b"n_points":
                        rows = int(value)
                    elif header == b"version":
                        version = float(value)  # version: 1 or version: 1.0
                    elif not header.startswith(b"image_size_"):
                        # returning the image_size_* data
                        # is left as an excercise for the reader.
                        raise ValueError
                except ValueError:
                    raise ValueError("Not a valid pts file")

            # if there was no n_points line, make sure the closing } line
            # is not going to trip up the numpy reader
            # by marking it as a comment
            points = np.loadtxt(f, max_rows=rows, comments="}")

        if rows is not None and len(points) < rows:
            raise ValueError(f"Failed to load all {rows} points")

        return points

    def __str__(self) -> str:
        return f"{self.filename} has {self.n_points} points."
