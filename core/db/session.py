from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

USER = 'verigin_nv'
PASSWORD = 'csupassword'
DB_PORT = '3306'
DB_NAME = USER
HOST = '192.168.88.176'

db_url = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(db_url, pool_size=20, max_overflow=0)
session = sessionmaker(engine)