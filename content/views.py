from django.shortcuts import render
from django.http import HttpResponse

from .models import Article, Dimension, Nature

import json

def homepage(request):
    articles = Article.objects.all()
    dimensions = Dimension.objects.all()
    natures = Nature.objects.all()
    return render(request, "content/homepage.html", {"articles": articles, "dimensions": dimensions, "natures": natures})

def article(request, id):
    article = Article.objects.get(pk=id)
    dimensions = Dimension.objects.all()
    natures = Nature.objects.all()

    return render(request, 'content/article.html', {'article': article, "dimensions": dimensions, "natures": natures})

def dimension(request, id):
    dimension = Dimension.objects.get(pk=id)
    
    dimensions = Dimension.objects.all()
    natures = Nature.objects.all()

    return render(request, 'content/dimension.html', {'dimension': dimension, "dimensions": dimensions, "natures": natures})

def nature(request, id):
    nature = Nature.objects.get(pk=id)
    
    dimensions = Dimension.objects.all()
    natures = Nature.objects.all()

    return render(request, 'content/nature.html', {'nature': nature, "dimensions": dimensions, "natures": natures})