from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session,sessionmaker
from application.config.config import Config
conf = Config()
##Increase Timeout
##Retry incase of sql server gone away error
engine = create_engine(conf.SQLITE_URI,convert_unicode=True,connect_args={'connect_timeout': 120},pool_recycle=3600,pool_pre_ping=True)

db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))

Base  = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import application.models.UserMaster
    Base.metadata.create_all(bind=engine)

def shutdown_db_session():
    db_session.remove()
