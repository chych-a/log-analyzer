def analyze_log(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()

    errors = []

    for line in lines:
        line = line.strip()

        if line.startswith("FAIL") or line.startswith("ERROR"):
            errors.append(line)

    return errors


log_errors = analyze_log("sample.log")

print("Znalezione błędy:")
for error in log_errors:
    print(error)
