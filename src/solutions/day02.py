from src.tools.loader import load_data

TESTING = False


def parse_input(data):
    reports = []
    for line in data:
        reports.append(list(map(int, line.split())))
    return reports


def check_safety(report):
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    return set(differences).issubset([1, 2, 3]) or set(differences).issubset([-1, -2, -3])


def count_safe_reports(reports):
    safe_reports = sum([check_safety(report) for report in reports])
    return safe_reports


def count_safe_reports_with_tolerance(reports):
    tolerance_reports = [[report[:i] + report[i + 1 :] for i in range(len(report))] for report in reports]
    safe_reports = sum([any([check_safety(report) for report in reports]) for reports in tolerance_reports])
    return safe_reports


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    reports = parse_input(data)

    # PART 1
    # test:     2
    # answer: 321
    print(count_safe_reports(reports))

    # PART 1
    # test:     4
    # answer: 386
    print(count_safe_reports_with_tolerance(reports))
