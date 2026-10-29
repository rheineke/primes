# primes
Last-digit patterns of consecutive primes

List of largest known primes: http://primes.utm.edu/primes/

## Setup
```zsh
conda env create -f environment.yaml
conda activate primes
pre-commit install
```

and
```shell
pip install -e ".[dev,test]"
```
The `primesieve` binding compiles against the primesieve C library, which conda installs
(`brew install primesieve` or `apt install libprimesieve-dev` without conda).

## Tests
```shell
pytest
```
