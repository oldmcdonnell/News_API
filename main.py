import requests
from send_email import send_email

api_key = "ffccde25362e4cfc83655b738f77d832"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-11-15&sortBy=publishedAt&apiKey=" \
      "ffccde25362e4cfc83655b738f77d832"
#makle requst
request = requests.get(url)

#get a gdictionare with dataclasses
content = request.json()

#access article titles and descriptions
body = ""
for article in content["articles"]:
      if article["title"] is not None:
            body = body + article["title"] + "\n" + str(article["description"]) + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)