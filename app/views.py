from unicodedata import name
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from bs4 import BeautifulSoup
import requests
from .news_bot import main as get_news
from .flipkart_bot import main as get_products
from app.models import Contact


# Create your views here.
def dictionary(request):
    if request.method == "POST":
        word = request.POST['word']
        url = 'https://www.dictionary.com/browse/'+word
        r = requests.get(url)
        data = r.content
        soup = BeautifulSoup(data, 'html.parser')
        span = soup.find_all('span', {"class": "one-click-content"})
        param = {'text': span[0].text, 'word': word}
        return render(request, 'dictionary.html', param)
    else:
        return render(request, 'dictionary.html')

def news(request):
    headlines = get_news()
    ctx={
        'headlines':headlines
    }
    return render(request, 'news.html', ctx )

def ecommerce(request):
    ctx = {}
    if request.POST:
        query = request.POST.get('query')
        if query:
            try:
                ctx['products'] = get_products(query)
            except:
                ctx['products'] = None

    return render(request, 'flipkart.html', ctx)

def home(request):
    return render(request, 'home.html')

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        concern=request.POST['concern']
        print(name,email,phone,concern)
        obj=Contact(name=name, email=email, phone=phone, concern=concern)
        obj.save()




    return render(request, 'contact.html')

