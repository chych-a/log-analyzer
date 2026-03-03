
# Log Analyzer

Simple Python project that reads a log file and displays lines marked as FAIL or ERROR.

## Project purpose

This project was created to practice:
- reading files in Python,
- analyzing text line by line,
- finding errors in logs,
- creating a simple report in the console.

## Files in this project

- `analyzer.py` - main Python script
- `sample.log` - example log file
- `requirements.txt` - dependencies file
- `.gitignore` - files ignored by Git

## How it works

The program:
1. opens the log file,
2. reads all lines,
3. checks which lines start with `FAIL` or `ERROR`,
4. displays them in the console.

## Example log lines

```text
FAIL: Database connection timeout
ERROR: Unexpected server response

## JSON report

The program also creates a `report.json` file with:
- file name,
- list of found errors,
- number of FAIL messages,
- number of ERROR messages,
- number of WARNING messages,
- total number of errors.

This makes the project more useful for automation and further processing.
