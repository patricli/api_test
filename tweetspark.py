import json
import requests
from flask import Flask, request

from twython import Twython
from py_auth import*
from spark_auth import (accessToken)
#from spark_env import (roomID)

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



#Init Flask web server
app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello():
    filedata = request.get_json()
    roomID = filedata['data']['roomId']
    stat=["Spark"]
    #stat = twitter.get_home_timeline(count=4, trim_user=0) #Get timeline tweets
    for d in stat:
        #message = d['user']['screen_name'] + " tweeted " + d['text']
        message = "Sendit"
        sparkParam = {
            'roomId' : roomID,
            'text': message
        }
        r=requests.post(url = sparkURL, data = json.dumps(sparkParam), headers = sparkHeaders)
        #print(r.status_code)
    return ""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
