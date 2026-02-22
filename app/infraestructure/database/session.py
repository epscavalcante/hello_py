from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'sqlite:///./app.db'
# ou:
# DATABASE_URL = "postgresql+psycopg://user:pass@localhost/dbname"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)


# Dependency para FastAPI (gerador)
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
