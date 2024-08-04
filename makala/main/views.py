from django.shortcuts import render
from . import models

def index(request):
    return render(request, 'index.html')

def article_list(request):
    if request.method == 'POST':
        article = request.POST['article']
        categories = models.ArticleCategory.objects.all()
        article_list = models.Arcticle.objects.filter(title__icontains=article)
        context = {'article_list': article_list, 'categories': categories}
        return render(request, 'article.html', context)
