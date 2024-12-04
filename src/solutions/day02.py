from src.tools.loader import load_data

TESTING = False


def parse_input(data):
    reports = []
    for line in data:
        report = list(map(int,line.split()))
        reports.append(report)
    return reports


def check_safety(report):
    safe = True
    increase = True
    if report[0] == report[1]:
        safe = False
    elif report[0] > report[1]:
        increase = False
    for i in range(len(report)-1):
        if report[i] == report[i+1]:
            safe = False
        elif abs(report[i] - report[i+1]) not in [1,2,3]:
            safe = False
        elif report[i] > report[i+1] and increase == True:
            safe = False
        elif report[i] < report[i+1] and increase == False:
            safe = False
    return safe


def reports_with_error_tolerance(reports):
    tolerance_reports = []
    for line in data:
        report_cluster = []
        report = list(map(int, line.split()))
        for i in range(len(report)):
            mod_report = report.copy()
            del mod_report[i]
            report_cluster.append(mod_report)
        tolerance_reports.append(report_cluster)
    return tolerance_reports


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    reports = parse_input(data)
    tolerance_reports = reports_with_error_tolerance(reports)

    count = 0

    for reports2 in tolerance_reports:
        safe_in_general = False
        for report in reports2:
            if check_safety(report):
                safe_in_general = True
        if safe_in_general:
            count += 1

    print(count)