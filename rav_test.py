
#Run a counter
import csv

content = "lorem ipsum dolar si abet cramer loyalism protestantism"
counts = {}
counts["republican"] = 0
with open('classification.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count != 0:
          print(row)
          counts["republican"] += content.count(row["keyword"])

print(counts)