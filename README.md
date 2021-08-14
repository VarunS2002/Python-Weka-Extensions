# Python-Weka-Extensions

## [Downloads](https://github.com/VarunS2002/Python-Weka-Extensions/releases)

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

Programs to improve some features in Weka.

## Requirements:

- Install Weka or download `weka.jar` from https://waikato.github.io/weka-wiki/downloading_weka/

## 1. append_multiple.py

- Program to append multiple `.arff` files to one `.arff` file since Weka only supports appending 2 files

- ### Usage:

  > #### Method 1 (Windows):

    - Requirements:
        - Java Runtime Environment

    - Download the `.exe` (Windows Executable) file

    - Open a terminal with the working directory set to the location of the `.exe` file

    - Syntax: `append_multiple.exe 1.arff 2.arff 3.arff 4.arff outputfile.arff`

    - Use only the filenames of the `.arff` files without the path

    - Follow the on screen instructions

  > #### Method 2 (Windows and Linux):

    - Requirements:
        - Java Runtime Environment
        - Python 3.9
        - For Windows https://www.python.org/downloads/ is recommended

    - Download the `.py` (Python Source Code) file

    - Open a terminal with the working directory set to the location of the `.py` file

    - Syntax: `python append_multiple.py 1.arff 2.arff 3.arff 4.arff outputfile.arff`

    - Use only the filenames of the `.arff` files without the path

    - Wrap filename in double quotes if it contains spaces

    - Follow the on screen instructions

## Dependencies:

- [auto-py-to-exe](https://pypi.org/project/auto-py-to-exe/) is used for compiling the program to a .exe file
