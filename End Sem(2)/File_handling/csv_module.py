import csv

# Data to write to CSV file
data_to_write = [
    ['Name', 'Age', 'City'],
    ['Samrat', 21, 'Kolkata'],
    ['Bob', 21, 'Samastipur'],
    ['Charlie', 21, 'Darbhanga']
]

# Writing data to CSV file
with open('people.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data_to_write)  # writing multiple rows at once
print("Data written to 'people.csv' successfully.")

# Reading data from the same CSV file
with open('people.csv', mode='r') as file:
    reader = csv.reader(file)
    print("Reading data from 'people.csv':")
    for row in reader:
        print(row)
