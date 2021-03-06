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

    engine.execute("""SELECT cities.id, cities.name, states.name FROM states
                      INNER JOIN cities ON states.id=cities.state_id""")
    for record in engine.fetchall():
        print(record)

    engine.close()
    db.close()
