#!/usr/bin/python3
"""Script that changes the name of a State object from the database"""

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

    # Query the State object with id = 2
    state_to_update = session.query(State).filter(State.id == 2).first()

    # Update the name to "New Mexico"
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    # Close session
    session.close()
