import requests

api_key = "ffccde25362e4cfc83655b738f77d832"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-11-15&sortBy=publishedAt&apiKey=" \
      "ffccde25362e4cfc83655b738f77d832"

request = requests.get((url))
content = request.json()

#print(type(content))
#print(content["articles"])

for article in content["articles"]:
      print(article["title"])
      print(article["description"])
