# UrlShortener

A simple URL shortening service developed using Python and the Flask framework.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)

## Features

- Shorten long URLs into short URLs
- Redirect from short URLs to original long URLs

## Tech Stack

- Python 3.9
- Flask
- Flask-RESTx
- SQLAlchemy
- PostgreSQL

## Installation

1. Clone the repository:
```
git clone https://github.com/YourUsername/UrlShortener.git
cd UrlShortener
```

2. Install dependencies:
```
pip install -r requirements.txt
```

## Usage

### Running the Application

Using Docker Compose:
```
docker-compose up --build
```

Or run the Python script directly:
```
python url_shortener/run.py
```

The application will run at `http://127.0.0.1:5066`.

### Shortening a URL

Send a POST request to `/api/shorten_url` with JSON data:

```json
{
  "long_url": "https://www.example.com/very/long/url"
}
```

### Accessing a Short URL

Visit `http://127.0.0.1:5066/api/s/{short_url}` in your browser

## API Documentation

Visit `http://127.0.0.1:5066/swagger` to view the Swagger UI API documentation.
