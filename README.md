# AdventOfCode2017

## Code Gen
### Get Session Token 
- got to https://adventofcode.com/ 
- make sure you are logged in
- open devtools
- copy value of `session` cookie
- paste into AOC_SESSION in [.env](.env)

## Run Code Gen
```
$ pipenv run python -m src.code_gen.create_day -d {day}
```

## Set Test Data
- create files in the `inputs` folder for each sample data provided
- add the samples to the `DayController` in the `part` file with filepath and expected result
```python
def sample_files(self) -> list[(str, int)]:
    return [("src/days/day02/inputs/sample01.txt", 18)]
```
Failure to set test data will result in:
```
Exception: No sample files setup. Add these to: Day03PartAController
```
Failure to pass test data will result in:
```
Exception: Test Fail: Sample src/day03/input_sample01.txt, expecting: 0, actual: None
```

## Run Day Part
```
$ pipenv run part {day} {part}

example: 
$ pipenv run part 1 a
```

## Submit Result
```
$ pipenv run submit {day} {part}

example: 
$ pipenv run submit 1 a
```

## Testing
Flake8
```
$ pipenv run test
```

## Linting
Flake8
```
$ pipenv run lint
```

## Formatting
Black
```
$ pipenv run fmt
```

## CI
[Github Actions](https://github.com/tom-haug/AdventOfCode2017/actions/workflows/ci.yml)

[pipeline config](.github/workflows/ci.yml)