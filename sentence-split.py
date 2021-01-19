import csv

with open('transcript.txt') as file_, open('transcript.csv', 'w') as csvfile:
    lines = [x for x in file_.read().strip().split('.') if x]
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(('ID', 'text'))
    for idx, line in enumerate(lines, 1):
        writer.writerow((idx, line.strip('.')))