import csv

def transform_imdb_data(csv_full_name, new_imdb_data_file):
    new_imdb_data = []
    try:
        with open(csv_full_name, newline = '') as csv_file:
            imdb_csv = csv.reader(csv_file, delimiter=',')

            for row_list in imdb_csv:
                if row_list[0] == 'movie' and int(row_list[4]) >= 2015:
                    transformed_row = []
                    transformed_row.append(row_list[0])
                    transformed_row.append(row_list[1])
                    transformed_row.append(row_list[4])
                    transformed_row.append(row_list[6])
                    transformed_row.append(row_list[7])

                    new_imdb_data.append(transformed_row)

        new_file = open(new_imdb_data_file, 'w', newline='')
        with new_file:
            csv_writer = csv.writer(new_file)
            csv_writer.writerows(new_imdb_data)

    except BaseException as errormsg:
        print('Sorry, there has been an error!')
        print(errormsg)

    finally:
        print('Execution complete')


transform_imdb_data('imdb_title.csv', 'transformed_imdb_data.csv')

#---------------------------------------------------------------------------------------------


def transform_imdb_mycriterion(csv_full_name, new_imdb_data_file):
    new_imdb_data = []
    try:
        with open(csv_full_name, newline='') as csv_file:
            imdb_csv = csv.reader(csv_file, delimiter=',')

            for row_list in imdb_csv:
                if 'Documentary' in row_list[-1] and int(row_list[6]) <= 60 and row_list[3] == 0:
                    transformed_row = []
                    transformed_row.append(row_list[0])
                    transformed_row.append(row_list[2])
                    transformed_row.append(row_list[3])
                    transformed_row.append(row_list[6])
                    transformed_row.append(row_list[7])

                    new_imdb_data.append(transformed_row)

        new_file = open(new_imdb_data_file, 'w', newline='')
        with new_file:
            csv_writer = csv.writer(new_file)
            csv_writer.writerows(new_imdb_data)

    except BaseException as errormsg:
        print('Sorry, there has been an error!')
        print(errormsg)

    finally:
        print('Execution complete')

transform_imdb_mycriterion('imdb_title.csv', 'my_criteria_imdb_data.csv')
