import sqlite3

# creating connection for the database
# creates database if it does not exixt
with sqlite3.connect('sample.db') as connection:
    c = connection.cursor() #defining a cursor that allows to interact with db
    c.execute("DROP TABLE posts ")
    c.execute("CREATE TABLE posts( title TEXT , description TEXT)")
    c.execute(' INSERT INTO posts VALUES("Good","I/m good.") ')
    c.execute(' INSERT INTO posts VALUES("Well","I/m well.") ')