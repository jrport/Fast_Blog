from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings

engine = create_engine(settings.database.sql_url, connect_args={"check_same_thread": False})
Base = declarative_base()
local_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
