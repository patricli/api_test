import json
import requests

from twython import Twython
from py_auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

from spark_auth import (accessToken)
from spark_env import (roomID)

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


#Get timeline tweets
twUser = 'ChuckRobbins'
stat = twitter.get_user_timeline(count=12, screen_name=twUser)

for d in stat:
     #print(d['user']['screen_name'] + " tweeted " + d['text'])
     message = d['user']['screen_name'] + " tweeted >>" + d['text']
     sparkParam = {
         'roomId' : roomID,
         'text': message
     }
     r=requests.post(url = sparkURL, json = sparkParam, headers = sparkHeaders)
     #print(r.status_code)


r.close()