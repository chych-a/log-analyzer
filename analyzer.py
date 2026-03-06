import json


def analyze_log(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()

    errors = []
    fail_count = 0
    error_count = 0
    warning_count = 0

    for line in lines:
        line = line.strip()

        if line.startswith("FAIL"):
            errors.append(line)
            fail_count += 1
        elif line.startswith("ERROR"):
            errors.append(line)
            error_count += 1
        elif line.startswith("WARNING"):
            warning_count += 1

    report = {
        "file_name": file_name,
        "errors": errors,
        "fail_count": fail_count,
        "error_count": error_count,
        "warning_count": warning_count,
        "total_errors": fail_count + error_count,
    }

    return report


def main():
    report = analyze_log("sample.log")

    print("Znalezione błędy:")
    for error in report["errors"]:
        print(error)

    print()
    print("Podsumowanie:")
    print("Liczba FAIL:", report["fail_count"])
    print("Liczba ERROR:", report["error_count"])
    print("Liczba WARNING:", report["warning_count"])
    print("Łączna liczba błędów:", report["total_errors"])

    with open("report.json", "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    print()
    print("Raport został zapisany do pliku report.json")


if __name__ == "__main__":
    main()
