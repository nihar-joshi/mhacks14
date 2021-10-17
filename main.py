# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python38_app]
# [START gae_python3_app]
import os
from flask import Flask, render_template, request
from collections import defaultdict
import requests
# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)
TWILIO_ACCOUNT_SID="AC2cfa9495dfd2ff6d36d1da3c8d28eda1"
TWILIO_AUTH_TOKEN="d42b9805682790aded8b1191c54076b5"
@app.route('/')
def index():
    """Return a friendly HTTP greeting."""
    # audio_endpoint = "https://api.assemblyai.com/v2/transcript"
    # transcript_endpoint = "https://api.assemblyai.com/v2/transcript/"
    # json = {
    # "audio_url": "https://s3-us-west-2.amazonaws.com/blog.assemblyai.com/audio/8-7-2018-post/7510.mp3"
    # }
    # headers = {
    #     "authorization": "f29b7fadaca042bbbf0852a7a15425ad",
    #     "content-type": "application/json"
    # }
    # response = requests.post(audio_endpoint, json=json, headers=headers)
    # ID = response.json()['id']
    # print(ID)
    # headers = {
    #     "authorization": "f29b7fadaca042bbbf0852a7a15425ad"
    # }
    # transcript_response = requests.get(transcript_endpoint + ID, headers=headers).json()
    # print("tr", transcript_response)
    # while transcript_response["status"] != "completed":
    #     transcript_response = requests.get(transcript_endpoint + ID, headers=headers).json()
    #     print(transcript_response)
    return render_template("login.html")

def read_file(filename, chunk_size=5242880):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data

@app.route('/upload', methods=['POST'])
def upload():
    """Return a friendly HTTP greeting."""
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure

    print(request.form)
    audio_endpoint = "https://api.assemblyai.com/v2/transcript"
    json = { "audio_url": request.form['fileUpload'] }
    print(json)
    headers = { "authorization": "f29b7fadaca042bbbf0852a7a15425ad", "content-type": "application/json"}
    response = requests.post(audio_endpoint,  json=json, headers=headers)
    print(response.json())
    ID = response.json()['id']
    print(ID)
    headers = { "authorization": "f29b7fadaca042bbbf0852a7a15425ad" }
    transcript_endpoint = "https://api.assemblyai.com/v2/transcript/"
    response = requests.get(transcript_endpoint + ID, headers=headers)
    print(response.json())
    transcript_response = response.json()
    print("tr", transcript_response)
    while transcript_response["status"] != "completed":
        transcript_response = requests.get(audio_endpoint + "/" +  ID, headers=headers).json()
    print(transcript_response)

    # message = client.messages.create(
    #                     messaging_service_sid='MG30268df3a0d08a6174d38c21c3a037ad',
    #                     body="result",
    #                     to="phone"
    #                 )

    # print(message.sid)
    return render_template("login.html", text = "Here is your output: " + transcript_response['text'])


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python3_app]
# [END gae_python38_app]
