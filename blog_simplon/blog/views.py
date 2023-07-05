from django.shortcuts import render
from .models import Article

# Create your views here.


def liste_articles(request):
    articles = Article.objects.all()
    return render(request, 'blog/liste_articles.html', {'articles': articles})

def detail_article(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'blog/detail_article.html', {'article': article})

def ajouter_article(request):
    # Code pour ajouter un nouvel article
    pass

def ajouter_commentaire(request, article_id):
    # Code pour ajouter un nouveau commentaire à un article
    pass
