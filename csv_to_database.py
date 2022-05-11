import csv


def data_converter():
    filename = 'new_data.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Pull the Time values from the file
        dates = []
        temperatures = []
        for row in reader:
            date = ''
            try:
                # Collect the digits for each section of the date
                day = (row[1][:2])
                month = (row[1][3:5])
                # Add 2000 to get the year (e.g., 22 -> 2022)
                year = int(row[1][6:8]) + 2000
                year = str(year)
                # Convert temperatures to float
                temp_float = float(row[0])
            except ValueError:
                print('Something went wrong.')
            else:
                # Reconstruct the specific dates
                # CSV: DD/MM/YYYY
                date = f'{day}/{month}/{year}'

                # Add the dates to the list of all dates
                dates.append(date)
                # Append the float temperatures
                temperatures.append(temp_float)
        f.close()

    # Generate tuples to append to the database
    data_tuples = []
    for i in range(len(temperatures)):
        data_tuples += [(temperatures[i], dates[i])]
    return data_tuples
