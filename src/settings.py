import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


DATASET = "matheusgratz/world-university-rankings-2021"
TABLE_NAME = "universities_ranking"
JSON_FILENAME = f"{TABLE_NAME}.json"
DB_NAME = "university.db"
ENGINE = sa.create_engine(f"sqlite:///{DB_NAME}")
SESSION = scoped_session(sessionmaker(bind=ENGINE))
BASE = declarative_base()
