#Site to create a csv. https://extendsclass.com/csv-generator.html
import csv

with open("./resources/example.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(" ".join(row))