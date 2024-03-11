from mysql.connector import connect, Error

def create_database(host, user, password, database):
    try:
        connection = connect(
            host = host,
            user = user,
            password = password,
            database = None
        )
        cursor = connection.cursor()
        cursor.execute("SHOW DATABASES LIKE %s", (database,))
        result = cursor.fetchone()
        if not result:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database} DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci")
            cursor.execute(f"USE {database}")
            create_logins_table_query = """
            CREATE TABLE IF NOT EXISTS accounts(
                id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) NOT NULL,
                password VARCHAR(255) NOT NULL,
                emalil VARCHAR(100) NOT NULL
            ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
            """
            cursor.execute(create_logins_table_query)
            cursor.close()
            print(f"Database {database} created.")
        else:
            print(f"Database {database} is already created.")
    except Error as e:
        print(f"Error connecting to the database:{e}")
