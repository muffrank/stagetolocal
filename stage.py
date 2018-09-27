from flask import Flask,request,json
from flask_cors import CORS
import requests
app = Flask(__name__)

CORS(app)


HEADERS = {'Authorization': 'Token 0814886fb6a7e1247ad149dc62f662c4ef296962'}

COOKIES = dict(csrftoken='xEtbanbIamMfpI0VHHV3Bhde6fOPg8tX',sessionid='5i0h3br0jfaq2n7cnggakphz3gf302qu')

STAGE_URL = "http://example.com/"

PORT = 5000

@app.route("/<path:path>", methods=['GET', 'POST','OPTIONS'])
def loadStage(path):

    # importing the requests library

    # api-endpoint
    URL = STAGE_URL + path


    # defining a params dict for the parameters to be sent to the API
    PARAMS = request.args.to_dict()

    method = request.method.lower()

    r = requests.request(method, headers=HEADERS, url=URL, data=PARAMS,verify=False,cookies=COOKIES)

    data = r.json()

    response = app.response_class(
        response=json.dumps(data),
        mimetype='application/json'
    )
    return response







if __name__ == '__main__':
    app.run(debug=True,threaded=True,port=PORT,host="0.0.0.0")