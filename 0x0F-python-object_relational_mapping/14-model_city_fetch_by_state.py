#!/usr/bin/python3
"""x"""


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv
    from model_state import Base, State
    from model_city import City

    engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                           .format(argv[1],
                                   argv[2],
                                   "localhost",
                                   argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    factory = sessionmaker(bind=engine, expire_on_commit=False)
    session = factory()

    raw = session.query(State.name, City.id, City.name)
    for record in raw.filter(State.id == City.state_id):
        print("{}: ({}) {}".format(record[0], record[1], record[2]))

    session.close()
