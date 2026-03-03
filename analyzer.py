def analyze_log(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()

    errors = []
    fail_count = 0
    error_count = 0

    for line in lines:
        line = line.strip()

        if line.startswith("FAIL"):
            errors.append(line)
            fail_count += 1

        elif line.startswith("ERROR"):
            errors.append(line)
            error_count += 1

    return errors, fail_count, error_count


log_errors, fail_count, error_count = analyze_log("sample.log")

print("Znalezione błędy:")
for error in log_errors:
    print(error)

print()
print("Podsumowanie:")
print("Liczba FAIL:", fail_count)
print("Liczba ERROR:", error_count)
print("Łączna liczba błędów:", fail_count + error_count)
