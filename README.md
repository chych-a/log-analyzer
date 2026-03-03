# Log Analyzer

Simple Python project that reads a log file and analyzes lines marked as FAIL, ERROR, or WARNING.

## Project purpose

This project was created to practice:
- reading files in Python,
- analyzing text line by line,
- finding errors in logs,
- creating a simple report in the console,
- saving results to a JSON file.

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
4. saves FAIL and ERROR lines as detected errors,
5. counts FAIL, ERROR, and WARNING messages,
6. displays the results in the console,
7. saves a JSON report to `report.json`.

## Example log lines

```text
FAIL: Database connection timeout
ERROR: Unexpected server response
WARNING: Retrying connection
```

## How to run

Make sure Python is installed, then run:

```bash
python analyzer.py
```

## Example output

```text
Znalezione błędy:
FAIL: Database connection timeout
FAIL: User authentication failed
ERROR: Unexpected server response
FAIL: Payment processing failed

Podsumowanie:
Liczba FAIL: 3
Liczba ERROR: 1
Liczba WARNING: 1
Łączna liczba błędów: 4

Raport został zapisany do pliku report.json
```

## JSON report

The program also creates a `report.json` file with:
- file name,
- list of found errors,
- number of FAIL messages,
- number of ERROR messages,
- number of WARNING messages,
- total number of errors.

This makes the project more useful for automation and further processing.
