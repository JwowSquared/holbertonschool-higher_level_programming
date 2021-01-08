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

    engine.execute("SELECT * FROM states WHERE name = '{}'".format(argv[4]))
    for record in engine.fetchall():
        if record == argv[4]:
            print(record)

    engine.close()
    db.close()
