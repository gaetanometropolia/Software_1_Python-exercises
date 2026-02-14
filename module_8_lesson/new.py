import mariadb

print(mariadb.__version__)

connection = mariadb.connect(
    host="127.0.0.1",
    port = 3306,
    user = "root",
    password = "Gaetrig1992.",
    database = "ankkalinna",
    autocommit = True
)

print("connection established")

def get_ankkalinnalainen_by_etunimi():
    sql = "SELECT * FROM ankkalinnalainen where etunimi = ?"
    cursor = connection.cursor(dictionary=True)
    user_input = input("enter something")
    cursor.execute(sql, (user_input,))
    result = cursor.fetchall()

    if result :
        for a in result:
            print ("I am ", a["etunimi"], a["sukunimi"], "my id is ", a["ID"] )

    else :
        print ("ei nimi found")


get_ankkalinnalainen_by_etunimi()




