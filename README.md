# Puzzle Solver

This is just another Puzzle Solver written in Python. It shows how to use `requets` to solve a puzzle using an API. `Pytest` was used for writing mocks and unit tests.

### Requirements

* Python 3.x (Pre-installed)
* Pip (Pre-installed)
* Virtualenv

```
pip install virtualenv
```

The rest of this guide assumes the repository was cloned in `HOME=/project/local/directory` and you have a terminal poiting to the project's root folder 

### SetUp Local Environment

```
cd $HOME
virtualenv .venv -p 3.8
source .venv/bin/activate
pip install -r requirements.txt
```

### Executing the PuzzleSolver

```
python main.py -e <your@email.com>
```

### Running tests

```
pytest tests
```

### Project Structure

- [tests](./tests/): UnitTest folder
  * [test_api](./tests/test_api.py): Unit Tests for the `api` module
  * [test_puzzle](./tests/test_puzzle.py): Unit Tests for the `puzzle` module
- [api.py](./api.py): Module that communicates with the Puzzle API
- [main.py](./main.py): Entrypoint for executing the PuzzleSolver
- [puzzle.py](./puzzle.py): PuzzleSolver module. It cointains the required`check` function


### Licence

[MIT](LICENCE.md)