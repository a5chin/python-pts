<div align="center">

<h1>PythonPts</h1>

[![Pytest](https://github.com/a5chin/python-pts/actions/workflows/pytest.yml/badge.svg)](https://github.com/a5chin/python-pts/actions/workflows/pytest.yml)
[![Linting](https://github.com/a5chin/python-pts/actions/workflows/linting.yml/badge.svg)](https://github.com/a5chin/python-pts/actions/workflows/linting.yml)
[![License](https://img.shields.io/pypi/l/ansicolortags.svg)](https://img.shields.io/pypi/l/ansicolortags.svg)

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)

</div>

# Usage
## Installation
```sh
pip install -r requirements.txt
```

## Example
```sh
cd examples
python main.py
```

## Code
```python
from pts import Points


filename = "assets/sample.pts"
points = Points(filename=filename)
"""
array: [
    [623 169] [615 165] [606 162] [597 161] [589 163]
    [584 168] [580 173] [578 182] [580 190] [583 198]
    [587 204] [591 212] [594 217] [600 224] [607 229]
    [611 232] [617 234] [624 235] [630 231] [632 224]
    [616 188] [613 182] [610 173] [604 169] [596 167]
    [589 169] [585 173] [582 179] [581 185] [584 192]
    [587 198] [591.411 203.7] [594.094 210.041] [597.996 214.675] [603.85 219.797]
    [620.435 188.578] [619.46 193.7] [620.923 201.505] [624.826 205.407] [626.045 212.236]
    [618.728 212.724] [614.094 210.285] [608.24 212.724] [604.826 209.797] [602.143 204.919]
    [603.362 200.041] [604.338 195.163] [606.777 191.017] [610.191 187.114] [611.655 183.456]
    [593.85 204.432] [592.387 196.871] [592.143 188.578] [592.63 181.261] [594.582 172.724]
]
filename: assets/sample.pts
n_points: 55
"""
```
