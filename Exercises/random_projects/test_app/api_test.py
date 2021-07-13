import http.client

conn = http.client.HTTPSConnection("imdb8.p.rapidapi.com")

headers = { 'x-rapidapi-host': "imdb8.p.rapidapi.com" }

conn.request("GET", "/auto-complete?q=game%20of%20thr", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


