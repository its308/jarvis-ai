import requests

# Your API endpoint and key
url = "https://newsapi.org/v2/top-headlines"
api_key = "f0946a34f0424000a00e4e93e071de86"
country = "in"

# Making the GET request
response = requests.get(f"{url}?country={country}&apiKey={api_key}")

# Checking if the request was successful
if response.status_code == 200:
    data = response.json()  # Parse the response as JSON
    articles = data.get("articles", [])

    # Loop through the articles and print the headlines
    for article in articles:
        print(article.get("title"))
else:
    print("Failed to fetch the headlines:", response.status_code)
