import csv

def save_rows_to_file(csv_file, indexes, output_file):
    with open(csv_file, "r") as csvfile, open(output_file, "w") as output:
        csvreader = csv.reader(csvfile, delimiter=",")
        for i, row in enumerate(csvreader):
            if i in indexes:
                output.write(",".join(row) + "\n")

csv_file = "data.csv"
row_indexes = [0, 10, 20, 50, 100000, 500000]  
output_file = "search_queries.txt"  
save_rows_to_file(csv_file, row_indexes, output_file)
