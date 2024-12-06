matrix = []
safe_reports = 0

try:
    with open('input', 'r') as file:
        for line in file:
            row = list(map(int, line.strip().split()))
            matrix.append(row)
except FileNotFoundError:
    print("Error: file not found")
except ValueError:
    print("Error: only int type allowed in file")


def is_safe(report):
    increase = True
    decrease = True

    if len(report) != len(set(report)):
        return False

    for i in range(len(report) - 1):
        if report[i] >= report[i + 1]:
            increase = False
        if report[i] <= report[i + 1]:
            decrease = False

        if abs(report[i] - report[i + 1]) < 1 or abs(report[i] - report[i + 1]) > 3:
            return False

    return increase or decrease


def is_safe_removed(report):
    for i in range(len(report)):
        new_report = report[:i] + report[i + 1:]
        if is_safe(new_report):
            return True


for report in matrix:
    if is_safe(report) or is_safe_removed(report):
        safe_reports += 1

print("Safe reports:", safe_reports)
