# this is mostly a cut and paste job
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# SQLALCHEMY_DATABASE_URL = 'postgresql://<username>:<password>@<ip-address/hostname>/<database_name>' => This is the generic structure of how you connect with an SQL database using SQLAlchemy (port number is optional)

# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:merajshaikh3@localhost/fastapi'

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}' # for some reason when I add port number here, fast API stops working


#the below lines of code are also available on FastAPI's website under SQL Database documentation (https://fastapi.tiangolo.com/tutorial/sql-databases/)
#engine will establish the connection with the SQL database
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#in order to talk to the database we'll need to create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Database connection using raw SQL. Not needed when connecting with SQLAlchemy
# #to avoid manually connecting until the database gets connected we have written a for-loop
# while  True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='merajshaikh3', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successful")
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error: ", error)
#         time.sleep(2)
