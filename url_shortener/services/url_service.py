import random
import string

from repositories.url_repository import URLRepository

class URLService:
    @staticmethod
    def shorten_url(long_url: str) -> str:
        short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
        URLRepository.save_url_mapping(short_url, long_url)
        return f"http://localhost:5000/{short_url}"