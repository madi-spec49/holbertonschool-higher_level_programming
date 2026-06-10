#!/usr/bin/python3
"""List State objects containing 'a' from hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL credentials from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine to connect to MySQL server
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects with name containing letter 'a'
    states = session.query(State)\
        .filter(State.name.contains('a'))\
        .order_by(State.id)\
        .all()

    # Display results
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
