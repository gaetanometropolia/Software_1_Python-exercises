# Write a program that asks the user to enter the area code (for example FI) and prints out the airports located in that country ordered by airport type. For example, Finland has 65 small airports, 15 helicopter airports and so on.

import mariadb

connection = mariadb.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password = "Gaetrig1992.",
    database="flight_game",
    autocommit=True
)
print("Connected to MariaDB")

def get_airport_by_area():
    sql = "select type, COUNT(*) as amount from airport where iso_country = ? group by type  "
    cursor = connection.cursor(dictionary=True)
    user_input = input("Enter area code: ")
    cursor.execute(sql, (user_input,))
    result = cursor.fetchall()

    if result :
        for n in result:
            print(n)
    else:
        print("not found")

get_airport_by_area()



