# Write a program that asks the user to enter the ICAO code of an airport. The program fetches and prints out the corresponding airport name and location (town) from the airport database used on this course. The ICAO codes are stored in the ident column of the airport table.

import mariadb

print(mariadb.__version__)

connection = mariadb.connect(
    host="127.0.0.1",
    port = 3306,
    user = "root",
    password = "Gaetrig1992.",
    database = "flight_game",
    autocommit = True
)

print("connection established")

def get_airport_by_icao():
    sql = "select name, municipality from airport where ident = ?"
    cursor = connection.cursor(dictionary=True)
    user_input = input("enter the ICAO code of an airport: ").upper()
    cursor.execute(sql, (user_input,))
    result = cursor.fetchall()

    if result :
        for n in result:
            print (n)
    else:
        print("no airport found")

get_airport_by_icao()

