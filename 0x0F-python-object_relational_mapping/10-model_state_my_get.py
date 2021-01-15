#!/usr/bin/python3
"""x"""


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv
    from model_state import Base, State

    engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                           .format(argv[1],
                                   argv[2],
                                   "localhost",
                                   argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    factory = sessionmaker(bind=engine, expire_on_commit=False)
    session = factory()

    out = "Not found"
    for record in session.query(State):
        if argv[4] == record.name:
            out = record.id
    print(out)

    session.close()
