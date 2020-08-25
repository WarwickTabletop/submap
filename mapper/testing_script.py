import requests

DOMAIN = "http://127.0.0.1:8000"
MAP = """.........
..C...C..
..STS....
CCTTCCTTS
WWWWWWW.W
"""
KEY="mmSSsgBijcRqvbjdRq5f0WocMjblUxAxhUM7r0Z94OlKiP4W1Y5v1BQpmkvw0I6V8GKOaPNhDdZKR2ROsdacPmJXvpReLWOW4Iw8xFtUqxas2cTBBblstYCqyif6IZOg"
print(DOMAIN+"/api/map/")
res = requests.post(DOMAIN+"/api/map/", data={"map":MAP, "key":KEY})
print(res.status_code, res.text)
if res.status_code==200:
    print(DOMAIN+res.json()['url'])