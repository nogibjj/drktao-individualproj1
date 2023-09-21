[![Install](https://github.com/nogibjj/drktao-individualproj1/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/drktao-individualproj1/actions/workflows/install.yml)
[![Format](https://github.com/nogibjj/drktao-individualproj1/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/drktao-individualproj1/actions/workflows/format.yml)
[![Lint](https://github.com/nogibjj/drktao-individualproj1/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/drktao-individualproj1/actions/workflows/lint.yml)
[![Test](https://github.com/nogibjj/drktao-individualproj1/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/drktao-individualproj1/actions/workflows/test.yml)

# IDS 706 Individual Project 1
This repo builds upon the Week 2 mini-project, in which I used pandas to provide descriptive statistics and data visualization on a data set containing the Rotten Tomatoes scores for all of actor Robert De Niro's movies. I employed two scripts, one containing the necessary functions for data analysis, and the other containing tests. In this project, I analyze the same data set, with the following major updates:

1. Separate Github Actions for install, format, lint, and test, with status badges for each
2. Data analysis conducted in both a python script `descstats.py` and a jupyter notebook `PandasDescriptiveStats.ipynb`, with an additional `lib.py` containing the common functions imported in these two files. Additional corresponding test files `test_descstats.py` and  `test_lib.py` are also implemented.
3. Testing for the jupyter notebook using the nbval plugin for pytest, code formatting using Python black, and linting using Ruff. The corresponding makefile commands were updated accordingly.
4. Package updates to `requirements.txt`, including ruff, nbval, nbqa, and tabulate
5. An additional feature in the main script that generates a summary report of the data analysis to the repo called `report.md`

## Instructions
Use Github codespaces, which will allow for a container to be built with the required packages, as detailed in `requirements.txt`. To begin, use `make install` in the terminal to install the necessary packages from `requirements.txt`. If any changes are made to any scripts, `make format ` and `make lint` can be used to format and lint the code, respectively. Finally, `make test` can be used to run tests on the files performing data analysis.

To generate a summary report and histogram plot to the repo, use `python scripts/descstats.py`, which will save a .png file of the histogram to the repo, as well as a summary report containing descriptive statistics and the histogram together. 

## Video Demo
https://www.youtube.com/watch?v=rcQZIxwBUfA
