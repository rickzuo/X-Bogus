from flask import Flask, request, jsonify
import execjs    
import urllib.parse
from common_utils import CommonUtils

app = Flask(__name__)

@app.route('/X-Bogus', methods=['POST'])
def generate_request_params():
    data = request.get_json()
    url = data.get('url')
    user_agent = data.get('user_agent')
    query = urllib.parse.urlparse(url).query
    xbogus = CommonUtils().get_xbogus(query,user_agent)
    new_url = url + "&X-Bogus=" + xbogus
    response_data = {
        "param": new_url,
        "X-Bogus": xbogus
    }
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8787)
