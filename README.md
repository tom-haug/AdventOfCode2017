# AdventOfCode2017

## Get Data
[advent-of-code-data](https://github.com/wimglenn/advent-of-code-data)

- Make day directory
```
$ mkdir -p src/day02
```
- Get Session token from browser `session` cookie
```
$ export AOC_SESSION={SESSION_TOKEN}
```
- Create input
```
# option 1
$ aocd 1 2017 > src/day02/input.txt

# option 2
$ pipenv shell
$ python
>>> from aocd import get_data
>>> get_data(day=1, year=2017)
```

## Run Day Part
```
$ pipenv shell
$ python -m src.day02.a
```

## Submit
```python
from aocd import submit
submit(my_answer, part="a", day=1, year=2017)
```