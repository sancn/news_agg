from sched import scheduler
from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
from .models import Samachar

from django.views.generic import ListView
from django.db.models import Q
from django.shortcuts import render

def ekantipur_news(request):
    url = "https://ekantipur.com/health"
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.content, "html.parser")
    teasers = soup.find_all("div", class_=["teaser", "normal"])

    samachars = []
    for teaser in teasers:
        news_title = teaser.find('a').text.strip()
        news_link = teaser.find('a')['href']
        normal = teaser.find('div', class_='normal')
        
        image_div = None
        if normal is not None:
            image_div = normal.find('div', class_='image')

        image_link = ''
        image_tag = None

        if image_div is not None:
            image_tag = image_div.find('a')

        if image_tag is not None:
            image_link = image_tag['href']

        samachar = Samachar.objects.filter(title=news_title).first()
        if samachar is not None:
            samachar.image_link = image_link
            samachar.news_link = 'https://ekantipur.com'+ news_link
            samachar.save()
        else:
            samachar = Samachar(title=news_title, image_link=image_link, news_link=news_link)
            samachar.save()
            samachars.append(samachar)

    # context = {
    #     "samachars": samachars,
    # }
    # return render(request, "news.html", context)


def index(request):
    samachars = Samachar.objects.all()
    context = {
        'samachars': samachars
    }
    return render(request, 'news.html', context)


def search_results_list(request):
    query = request.GET.get("q")
    quotes = Samachar.objects.filter(title__icontains='q')

    context = {'samachars': quotes}
    return render(request, "news.html", context)

