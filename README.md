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
- create files in the `day` folder for each sample data provided
- add the samples to the `DayController` in the `part` file with filepath and expected result
```python
def sample_files(self) -> list[(str, int)]:
    return [("src/day02/input_sample01.txt", 18)]
```
Failure to set test data will result in:
```
$ pipenv run python -m src.day{day}.a

Exception: No sample files setup. Add these to: Day03PartAController
```
Failure to pass test data will result in:
```
$ pipenv run python -m src.day{day}.a

Exception: Test Fail: Sample src/day03/input_sample01.txt, expecting: 0, actual: None
```

## Testing
Flake8
```
$ pipenv run test
```

## Submit
Once tests pass, run to submit:
```
$ pipenv run python -m src.day{day}.a --submit
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