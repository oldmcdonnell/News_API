import requests
from send_email import send_email

topic = "tesla"

api_key = "ffccde25362e4cfc83655b738f77d832"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-11-17&" \
      "sortBy=publishedAt&" \
      "apiKey=ffccde25362e4cfc83655b738f77d832&" \
      "language=en"
#makle requst
request = requests.get(url)

#get a gdictionare with dataclasses
content = request.json()

#access article titles and descriptions
body = ""
for article in content["articles"][:20]:
      if article["title"] is not None:
            body = "Subject: FUCK TESLA" \
                   + "\n" + "Today's News" + "\n" + body + article["title"] + "\n" + \
                   str(article["description"]) + str(article["url"]) + "\n" + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)