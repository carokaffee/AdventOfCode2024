from src.tools.loader import load_data

TESTING = False


#if True:
if __name__ == "__main__":
    print("hello")
    data = load_data(TESTING, "\n")

    reports = []
    for line in data:
        #print(line)
        report = list(map(int,line.split()))
        reports.append(report)

    new_reports = []
    for line in data:
        report_cluster = []
        report = list(map(int, line.split()))
        for i in range(len(report)):
            mod_report = report.copy()
            del mod_report[i]
            report_cluster.append(mod_report)
        report_cluster.append(report)
        new_reports.append(report_cluster)

    #print(reports)
    print(new_reports)

    count = 0

    for reports2 in new_reports:
        safe_in_general = False
        for report in reports2:
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
            #print('###', report, safe)
            if safe:
                safe_in_general = True
            #print(safe_in_general)
        if safe_in_general:
            count += 1

    print(count)