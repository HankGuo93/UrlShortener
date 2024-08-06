import random
import string

from repositories.url_repository import URLRepository

class URLService:
    @staticmethod
    def shorten_url(long_url: str) -> str:
        short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
        URLRepository.save_url_mapping(short_url, long_url)
        return f"http://127.0.0.1:5000/api/s/{short_url}"
    
    @staticmethod
    def get_long_url(short_url: str) -> str:
        return URLRepository.get_long_url(short_url)