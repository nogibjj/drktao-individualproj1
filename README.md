[![Install](https://github.com/nogibjj/drktao-individualproj1/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/drktao-individualproj1/actions/workflows/install.yml)
[![Format](https://github.com/nogibjj/drktao-individualproj1/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/drktao-individualproj1/actions/workflows/format.yml)
[![Lint](https://github.com/nogibjj/drktao-individualproj1/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/drktao-individualproj1/actions/workflows/lint.yml)
[![Test](https://github.com/nogibjj/drktao-individualproj1/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/drktao-individualproj1/actions/workflows/test.yml)

# IDS 706 Week 2 Mini-Project
This repo uses the python template generated in Week 1 to employ a pandas script that provides descriptive statistics and data visualization. The script main.py contains two functions, one of which computes and displays descriptive statistics (mean, median, standard deviation) of a data column of interest, and the other of which generates a histogram of the data. The script test_main.py tests to ensure that the descriptive statistics are computed as expected.

The specific data set used in this project is a simple one; it contains all Robert De Niro movies and their corresponding Rotten Tomatoes scores. The data of interest are the scores themselves. 

I have included a pdf report in the repo that summarises the descriptive statistics of interest and displays the visualization.

## Instructions
Use Github codespaces, which will allow for a container to be built with the required packages, as detailed in requirements.txt. In the terminal, one can use `make lint` to lint the code and `make test` to run the provided tests on the code. One can also directly run the scripts using `python main.py` and `python test_main.py`.
