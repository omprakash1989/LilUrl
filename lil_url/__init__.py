from lil_url.url_shortner import shorten_url
from lil_url.libs.url_shortner import UrlShortener


def init_app(app):
    shortener = UrlShortener()
    shortener.init_app(app)
