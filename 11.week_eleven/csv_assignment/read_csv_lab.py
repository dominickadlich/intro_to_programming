# Use the import command to import the csv module.
import csv

def main():
    # Use the with open() command to open grades.csv in read mode.
    with open("grades.csv", "r") as f:
        # Use the csv.reader() command to read the rows.
        grades_reader = csv.reader(f)
    
        # Use a for loop to go through each row.
        for row in grades_reader:
            # Use the print() command to display each row.
            print(row)

if __name__ == "__main__":
    main()