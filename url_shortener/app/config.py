import os

PORT = 5066
DATABASE_URL = os.getenv('DATABASE_URL', f"postgresql://admin:admin@127.0.0.1:5432/url_shortener")