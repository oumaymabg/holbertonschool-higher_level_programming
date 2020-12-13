#!/usr/bin/python3
""" Python x MySQL : Listing data from a database using args """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    c = db.cursor()
    c.execute("SELECT * from states ORDER BY states.id")
    for state in c.fetchall():
        print(state)
    c.close()
    db.close()
