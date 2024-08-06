from flask import jsonify, redirect, request
from flask_restx import Namespace, Resource, fields

from services.url_service import URLService

url_ns = Namespace('urls', description='URL Shortener API')

url_model = url_ns.model('URL', {
    'long_url': fields.String(required=True, description='The long URL to shorten')
})

@url_ns.route('/shorten_url')
class URLShorten(Resource):
    @url_ns.expect(url_model)
    @url_ns.response(201, 'URL shortened successfully')
    @url_ns.response(400, 'Invalid request')
    def post(self):
        data = request.get_json()
        long_url = data.get('long_url')
        if not long_url:
            url_ns.abort(400, "Missing long_url parameter")

        short_url = URLService.shorten_url(long_url)
        response = jsonify({'short_url': short_url})
        response.status_code = 201
        return response

@url_ns.route('/s/<short_url>')
class URLRedirect(Resource):
    @url_ns.response(302, 'Redirecting...')
    @url_ns.response(404, 'URL not found.')
    def get(self, short_url):
        long_url = URLService.get_long_url(short_url)
        if long_url:
            return redirect(long_url)
        else:
            url_ns.abort(404, "URL not found")