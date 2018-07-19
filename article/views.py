from django.shortcuts import render
from article.models import Article,Comment

def article(request):
    articles = Article.objects.all()
    itemList = []
    for article in articles:
        items = [article]
        items.extend(list(Comment.objects.filter(article=article)))
        itemList.append(items)
    context = {'itemList': itemList}
    return render(request, 'article/article.html', context)
