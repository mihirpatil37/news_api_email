import requests
from Send_Emails import send_email

# Get the data
topic = "tesla"
api_key = "dc4543562d5949d0a064c730701b7b8c"
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "from=2025-03-12&"
       "sortBy=publishedAt&"
       "apiKey=dc4543562d5949d0a064c730701b7b8c")

# Make Request
request = requests.get(url)

# Get a dictionary with data
content = request.json()


# Access the article titles and description
body_content = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body_content += (article["title"] + "\n"
                         + article["description"] + "\n"
                         + article["url"] + 2 * "\n")

# Add subject to the message
body = "Subject: Today's news\n\n" + body_content
body = body.encode("utf-8")

# Send the message
send_email(message=body)