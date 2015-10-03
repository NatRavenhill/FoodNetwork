import MySQLdb

create_db = MySQLdb.connect(user="root", # your username
                            passwd="database123")

create_cursor = create_db.cursor()

def del_database(cursor):
    try:
        cursor.execute("DROP DATABASE new_db;")
    except:
        print "Database doesn't exist"

del_database(create_cursor)
create_cursor.close()
create_db.commit()
