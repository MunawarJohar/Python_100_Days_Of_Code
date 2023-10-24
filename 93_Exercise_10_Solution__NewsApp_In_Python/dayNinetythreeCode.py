import requests
query=input("What type of news are you interested in ? ")
url=f""
res=resquests.get(url)
news=json.Loads(res.text)
for article in news.["articles"]
    print(article.["title"])
    print(article.["description"])
    print("_________________________________")