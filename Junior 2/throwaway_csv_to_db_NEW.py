import csv
import sqlite3

conn = sqlite3.connect('testing.db')
c = conn.cursor()
csv_readings = 0


def create_database():
    c.execute("""CREATE TABLE pico (
                 moist float,
                 temperature float,
                 between_measurements float ,
                 waterings int,
                 active float,
                 inactive float,
                 waterings_skipped int,
                 csv_index int
                 )""")


def insert_data():
    with conn:
        with open('log_to_marcus.csv') as f:
            reader = csv.reader(f)
            next(reader) # CHANGE?
            global csv_readings
            csv_readings += 1
            for row in reader:
                c.execute("INSERT INTO pico VALUES "
                          "(:moist, "
                          ":temperature, "
                          ":between_measurements, "
                          ":waterings, "
                          ":active, "
                          ":inactive, "
                          ":waterings_skipped,"
                          ":csv_index) ",
                          {'moist': row[0],
                           'temperature': row[1],
                           'between_measurements': row[2],
                           'waterings': row[3],
                           'active': row[4],
                           'inactive': row[5],
                           'waterings_skipped': row[6],
                           'csv_index': csv_readings})


def retrieve_data():
    c.execute("SELECT * FROM Pico")
    all_values = c.fetchall()
    for i in all_values:
        print(i)


def avg_total(column):
    c.execute("SELECT * FROM Pico")
    all_values = c.fetchall()
    list1 = 0
    period_length = 0
    for i in all_values:
        list1 += float(i[column])
        period_length += 1
    avg = round(list1/period_length, 2)
    print(avg)


def time_sum():
    c.execute("SELECT * FROM Pico")
    all_values = c.fetchall()
    total_seconds = 0
    for i in all_values:
        total_seconds += float(i[2]) + float(i[4]) + float(i[5])
    return total_seconds
