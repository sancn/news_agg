# import requests
# from bs4 import BeautifulSoup

# url = "https://ekantipur.com/"
# response = requests.get(url,verify=False)
# soup = BeautifulSoup(response.content, "html.parser")

# news_title = soup.find("h2", class_="headline__title")
# image_link = soup.find("div", class_="headline__thumb").find("img")["src"]
# news_link = soup.find("h2", class_="headline__title").find("a")["href"]
