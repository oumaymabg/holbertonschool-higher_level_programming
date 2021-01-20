#!/usr/bin/python3
"""takes in an argument and displays all values in the states"""
import MySQLdb
from sys import argv

if name == "main":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY\
              'N%' ORDER BY states.id")
    [print(state) for state in cursor.fetchall()]
cursor.close()
db.close()
