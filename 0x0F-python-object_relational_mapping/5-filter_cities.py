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
                      INNER JOIN cities ON states.id=cities.state_id
                      WHERE states.name = %(x)s""", {"x": argv[4]})
    out = ""
    for record in engine.fetchall():
        out += record[1] + ", "
    print(out[:-2])

    engine.close()
    db.close()
