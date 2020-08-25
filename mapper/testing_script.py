import requests

DOMAIN = "http://127.0.0.1:8000"
MAP = """.........
..C...C..
..STS....
CCTTCCTTS
WWWWWWW.W
"""
KEY="vWGp6fbdam4Sb46bDcqLQcRrBIFZ5WBGCoCywK2pdGEta3CnN6rlOnGZ0973CRQ7N687WN0f18yG5bpZSLkLorn9RUpbdE3xzAO20xYiqKJbhl4TEqmHXEin9SLH3kRB"
print(DOMAIN+"/api/map/")
res = requests.post(DOMAIN+"/api/map/", data={"map":MAP, "key":KEY})
print(res.status_code, res.text)
if res.status_code==200:
    print(DOMAIN+res.json()['url'])