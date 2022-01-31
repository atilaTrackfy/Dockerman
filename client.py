import requests
import urllib.request
import time

while True:
    message = "E ai 9vinhos"
    # r = requests.post("http://localhost:8888/", data={'data': message})
    r = requests.post("http://dockerman-my-test.apps.13.68.137.63.nip.io/", data={'data': message})
    print(r.text)
    time.sleep(10)
