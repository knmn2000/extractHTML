import json

import requests
from flask import Flask, request
from readabilipy import simple_json_from_html_string

app = Flask(__name__)

@app.route('/url', methods=['POST'])
def jsonToHtml():
    # getClientSideRenderedSource()
    url = json.loads(request.data)['URL']
    print(json.loads(request.data)['URL'])
    req = requests.get(url)
    article = simple_json_from_html_string(req.text)
    return article


if __name__ == '__main__':
    app.run()
