import json

from flask import Flask, request

from util import HeadlessBrowser
from util import extractFromHTMLHandler

app = Flask(__name__)


@app.route('/')
def home():
    return """USAGE: \n\t[GET] /url : returns readability content by loading given URL on a browser.\n
                       \t[GET] /html: returns readability content by parsing through given HTML body.\n"""


@app.route('/html', methods=['GET'])
def extractFromHTML():
    return extractFromHTMLHandler(json.loads(request.data)['HTML'])


@app.route('/url', methods=['GET'])
def extractFromURL():
    """Extract HTML content from given URL.

    Returns:
        json: HTML content
    """
    url = json.loads(request.data)['URL']
    with HeadlessBrowser(url) as browser:
        readability_content = browser.fetchContent()
        return readability_content


if __name__ == '__main__':
    app.debug = True
    app.run()
