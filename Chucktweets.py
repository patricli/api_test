import json
import requests

from flask import Flask, request
from twython import Twython
from py_auth import *

from Chuck_auth import (accessToken)


#connect to TWTR
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

#connect to Spark
sparkURL = 'https://api.ciscospark.com/v1/messages'
sparkHeaders = {
    'Content-type': 'application/json; charset=utf-8',
    'Authorization': 'Bearer '+accessToken
}

twUser = 'ChuckRobbins'  #Twitter screenname

#Init Flask web server
app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello():
    filedata = request.get_json()
    roomID = filedata['data']['roomId']
    #roomID = 'Y2lzY29zcGFyazovL3VzL1JPT00vMWNkNjVkNjAtOGVjZC0xMWU3LWJmYTQtYzEzMzRiMGRlYjJj'

    print('Initiate twitter')
    stat = twitter.get_user_timeline(count=6, screen_name=twUser)  #Get tweet timelines
    for d in stat:
        message = d['user']['screen_name'] + " tweeted " + d['text']
        #message = "Sendit"
        sparkParam = {
            'roomId' : roomID,
            'text': message
        }
        print(sparkParam)
        r=requests.post(url = sparkURL, data = json.dumps(sparkParam), headers = sparkHeaders)
        print(r.status_code)
    r.close()
    return ""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
