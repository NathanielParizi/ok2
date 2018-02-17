from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):
    def _init_(self):
        super()._init_()

    def handle_starttag(self, tag, attrs):
            print(tag)

    def error(self, message):
            pass

    def