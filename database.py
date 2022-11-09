import sqlite3 as sl
import csv


def create_db():
    con = s1.connect('test.db')
    cur = con.cursor()

    cur.execute('CREATE TABLE filteredData(packet, VoltageMag, VoltageAngle, CurrentMag, CurrentAngle, ActualFreq, ROCOF')

    res = cur.execute('SELECT name FROM sqlite_master')
    print(res.fetchone())

def add_data_to_db(data: list):
    con = s1.connect('test.db')
    cur = con.cursor()

    cur.executemany('INSERT INTO filteredData VALUES(?, ?, ?, ?, ?, ?, ?)', data)
    con.commit()

def csv_to_sqlite(csv_file_path: str):
    data = list()
    with open(csv_file_path, 'r') as f:
        csv_data = csv.reader(f)
        for row in csv_data:
            row.pop(0)
            data.append(tuple(row))

    data.pop(0)

    return data

def print_data_in_db():
    con = sl.connect('test.db')
    cur = con.cursor()

    for row in cur.execute("SELECT * FROM filteredData"):
        print(row)

def main():
    # create_db()
    # data = csv_to_sqlite(csv_file_path='filteredData.csv')
    #add_data_to_db(data)
    print_data_in_db()

if __name__ == '__main__':
    main()