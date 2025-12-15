import requests
from bs4 import BeautifulSoup



def scrape(URL):
	response = requests.get(URL)
	soup = BeautifulSoup(response.text, "lxml")

	quotes = soup.find_all("div", class_="quote")

	for quote in quotes:
		text = quote.find("span", class_="text").get_text()
		author = quote.find("small", class_="author").get_text()
		all_tags = quote.find_all("a", class_="tag")
		tags = []
		for tag in all_tags:
			value = tag.get_text()
			tags.append(value)
		
		print("Author: ", author)
		print("Quote: ", text)
		print("Tags: ", tags)
		
		print("#"*30)
		print("\n\n")

URL = "https://quotes.toscrape.com/"

pages_to_collect = 20

# First Page
scrape(URL)

# From Second Page

for page_no in range(2, 21):
	URL = f"https://quotes.toscrape.com/page/{page_no}/"
	scrape(URL)



















	
