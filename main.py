import requests
from Send_Emails import send_email

api_key = "dc4543562d5949d0a064c730701b7b8c"

url = ("https://newsapi.org/v2/top-headlines?"
       "sources=techcrunch&"
       "apiKey=dc4543562d5949d0a064c730701b7b8c")

#Make Request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is None:
        body = body + article["title"] + "\n" + article["description"] + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)