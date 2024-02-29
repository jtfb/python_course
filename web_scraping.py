import requests
import bs4

result = requests.get("https://example.com/")

type(result)

result.text

# soup = bs4.BeautifulSoup(result.text,"lxml")
# soup

# soup.select('title')