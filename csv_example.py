import csv
# Here we load the CSV
     # open the file
     # read line by line
     # seperate in commas

# with open('user_details.csv', newline = '') as csv_file:
#     csvreader = csv.reader(csv_file, delimiter = ',')
#     print(csvreader)
#     for row in csvreader:
#         print(row[-1])

# iter() to make an iteratable object and next to skip the next line

# with open('user_details.csv', newline = '') as csv_file:
#     csvreader = csv.reader(csv_file, delimiter = ',')
#
#     iteratable = iter(csvreader)
#     headers = next(iteratable)
#     for row in iteratable:
#         print(row)
#
#     for row in csvreader:
#         print(row[-1])

# list()
with open('user_details.csv', newline='') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    list_list = list(csvreader)
    print(list_list)
    print(type(list_list))
    print(len(list_list))


# Transforming and writing to CSV
