import requests
import urllib.request
import time


while True:
    message = "E ai 9vinhos"
    r = requests.post("http://localhost:8888/", data={'data': message})
    print(r.text)
    time.sleep(10)
