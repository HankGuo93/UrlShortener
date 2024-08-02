from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import DATABASE_URL
from infrastructure.db.models import UrlMapping

class URLRepository:
    @staticmethod
    def save_url_mapping(short_url: str, long_url: str) -> None:
        engine = create_engine(DATABASE_URL)
        session_maker_instance = sessionmaker(bind=engine)
        session = session_maker_instance()

        url_mapping = UrlMapping(short_url=short_url, long_url=long_url)
        session.add(url_mapping)
        session.commit()
        session.close()
