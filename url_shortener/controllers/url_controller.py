from flask import Blueprint, jsonify, redirect, request

from services.url_service import URLService

url_bp = Blueprint('url_bp', __name__)

@url_bp.route('/api/shorten_url', methods=['POST'])
def shorten_url():
    data = request.get_json()
    long_url = data.get('long_url')
    if not long_url:
        return jsonify({'error': 'Missing long_url parameter'}), 400

    short_url = URLService.shorten_url(long_url)
    return jsonify({'short_url': short_url}), 201

@url_bp.route('/s/<short_url>', methods=['GET'])
def redirect_to_long_url(short_url):
    long_url = URLService.get_long_url(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return jsonify({"error": "URL not found"}), 404