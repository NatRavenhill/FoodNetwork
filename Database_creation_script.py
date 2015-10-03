import MySQLdb

create_db = MySQLdb.connect(user="root", # your username
                            passwd="database123")

create_cursor = create_db.cursor()

def create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE new_db;")
    except:
        print "Database already exists"

def fill_out_database(cursor):
    try:
        cursor.execute('''
USE new_db;
CREATE TABLE accounts (id INTEGER, email TEXT, password TEXT);
''')
    except:
        print "Table already exists"

create_database(create_cursor)
create_cursor.close()
create_cursor = create_db.cursor()
fill_out_database(create_cursor)
create_cursor.close()
create_db.commit()

#INSERT INTO accounts (id, email, password) VALUES (1, "aaquib8@yahoo.co.uk", "myname");
