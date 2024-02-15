from .database import database

def get_session():
    session = database.local_session()
    yield session
    session.commit()
    session.close()
