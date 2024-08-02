from .extensions import db

class UrlMapping(db.Model):
    __tablename__ = 'url_mapping'
    id = db.Column(db.Integer, primary_key=True)
    short_url = db.Column(db.String(7), unique=True, nullable=False)
    long_url = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.now())


# CREATE TABLE url_mapping (
#     id SERIAL PRIMARY KEY,
#     short_url VARCHAR(7) UNIQUE NOT NULL,
#     long_url TEXT NOT NULL,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );