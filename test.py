import requests

endpoint = "https://api.assemblyai.com/v2/transcript"

json = {
  "audio_url": "https://s3-us-west-2.amazonaws.com/blog.assemblyai.com/audio/8-7-2018-post/7510.mp3"
}

headers = {
    "authorization": "f29b7fadaca042bbbf0852a7a15425ad",
    "content-type": "application/json"
}

response = requests.post(endpoint, json=json, headers=headers)
print(response.json())
ID = response.json()['id']

endpoint = "https://api.assemblyai.com/v2/transcript/" + ID
print(endpoint)
headers = {
    "authorization": "f29b7fadaca042bbbf0852a7a15425ad",
}
response = response.json()
while response["status"] != "completed":
    response = requests.get(endpoint, headers=headers).json()
print(response)