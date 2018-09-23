from bottle import route, run
import json

with open("gengi.json", "r", encoding='utf-8') as skra:
    gogn = json.load(skra)

@route('/')
for x in gogn["results"]:
    for k, v in x.items():
        print(k, v)


run(host="localhost", port=8080)