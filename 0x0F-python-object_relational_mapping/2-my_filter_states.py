#!/usr/bin/python3
# takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
# traitement: ./2-my_filter_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
import sys
import MySQLdb

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
