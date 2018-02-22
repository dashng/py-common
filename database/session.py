from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from contextlib import contextmanager

@contextmanager
def session_scope():
    engine = create_engine('sqlite:///./sqlalchemy.db', pool_size=20, max_overflow=0)
    _session = sessionmaker(bind=engine)
    session = _session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
