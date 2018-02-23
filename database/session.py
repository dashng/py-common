from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from contextlib import contextmanager

class DB_Util(object):
    DB_URL = 'sqlite:///./sqlalchemy.db'
    def __init__(self):
        pass

    def session(self):
        engine = self.engine()
        _session = sessionmaker(bind=engine)
        session = _session()
        return session

    def engine(self):
        engine = create_engine(self.DB_URL)
        return engine

@contextmanager
def session_scope():
    try:
        db_util = DB_Util()
        yield db_util.session()
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

if __name__ == '__main__':
    with session_scope() as session:
       print (session)
