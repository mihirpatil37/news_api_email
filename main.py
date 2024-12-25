import requests

api_key = "dc4543562d5949d0a064c730701b7b8c"

url = ("https://newsapi.org/v2/top-headlines?"
       "sources=techcrunch&"
       "apiKey=dc4543562d5949d0a064c730701b7b8c")

#Make Request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article['title'])
    print(article['description'])