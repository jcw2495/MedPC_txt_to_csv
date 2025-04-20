# MedPC_txt_to_csv
By. Jonathan Walsh and Josiah Walsh

## Overview
This repository offers a .txt to .csv converter for a specific .txt file format.
The sample `sampleFile1.txt` is a general example of the format this program will process.
## Usage
In order to use this script:
- clone the repository to the location you would like to execute it from
- Move the files you would like to convert into the same directory as the `main.py` and `LineContentProcessor.py` files
- On Windows systems:
  - Ensure you install Git Bash, and then use that as your terminal.
  - Follow the same steps as Mac system below.
- On Mac systems:
  - Since MacOS typically comes with the Zsh or Bash shells pre-installed, using globbing to select multiple files at once is possible.
  - From your terminal:
      - run `python3 main.py <filename>.txt` (for converting a single file)
      - or run `python3 main.py *.txt` (for converting all files in current directory with extention `.txt`)
