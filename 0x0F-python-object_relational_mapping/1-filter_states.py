#!/usr/bin/python3
"""x"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    engine = db.cursor()

    engine.execute("SELECT * FROM states")
    for record in engine.fetchall():
        if record[1][0] is "N":
            print(record)

    engine.close()
    db.close()
