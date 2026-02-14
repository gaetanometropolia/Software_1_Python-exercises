# Write a program that asks the user to enter the ICAO codes of two airports. The program prints out the distance between the two airports in kilometers. The calculation is based on the airport coordinates fetched from the database.

import mariadb
import geopy.distance

connection = mariadb.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="Gaetrig1992.",
    database="flight_game",
    autocommit=True
)

print("connection established")

user_input1 = input("enter first ICAO: ").upper()
user_input2 = input("enter second ICAO: ").upper()

sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = ?"

cursor = connection.cursor(dictionary=True)

cursor.execute(sql, (user_input1,))
result1 = cursor.fetchone()

cursor.execute(sql, (user_input2,))
result2 = cursor.fetchone()

if result1 is None:
    print("First ICAO not found:", user_input1)
if result2 is None:
    print("Second ICAO not found:", user_input2)

if result1 and result2:
    coordinates1 = (result1["latitude_deg"], result1["longitude_deg"])
    coordinates2 = (result2["latitude_deg"], result2["longitude_deg"])

    km = geopy.distance.geodesic(coordinates1, coordinates2).kilometers
    print(f"The distance is {km:.2f} km")



