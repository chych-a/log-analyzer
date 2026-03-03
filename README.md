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
3. checks which lines start with `FAIL`, `ERROR`, or `WARNING`,
4. displays the results in the console,
5. saves a JSON report to `report.json`.

## Example log lines

```text
FAIL: Database connection timeout
ERROR: Unexpected server response
WARNING: Retrying connection
