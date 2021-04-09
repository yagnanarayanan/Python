import requests
r = requests.get("https://financialmodelingprep.com/api/v3/profile/AAPL?apikey=demo")
print(f"text: {r.text}")
print(f"status code: {r.status_code}")
print(f"encoding: {r.encoding}")
print(f"cookies: {r.cookies.values()}")
print(f"server header value: {r.headers['Server']}")
print(f"Is redirect: {r.is_redirect}")
print(f"elapsed: {r.elapsed}")
# time elapsed between sending the request and getting back a response
url = "https://www.w3schools.com/python/demopage.php"
data = {'somekey': 'somevalue'}
req = requests.post(url=url, data=data)
print(f"status code: {req.status_code}")
r = requests.get("https://google.co.in")
print(f"Is redirect: {r.is_redirect}")
print(f"cookies: {r.cookies}")
