from django.shortcuts import render, redirect, get_object_or_404
from article.models import Article,Comment
from article.forms import ArticleForm
from django.contrib import messages
from django.db.models.query_utils import Q
from django.contrib.auth.decorators import login_required
from main.views import admin_required

def article(request):
    articles = Article.objects.all()
    itemList = []
    for article in articles:
        items = [article]
        items.extend(list(Comment.objects.filter(article=article)))
        itemList.append(items)
    context = {'itemList': itemList}
    return render(request, 'article/article.html', context)

@admin_required
def articleCreate(request):
    template = 'article/articleCreateUpdate.html'
    if request.method == 'GET':
        return render(request, template, {'articleForm':ArticleForm()})
    #POST
    articleForm = ArticleForm(request.POST)
    if not articleForm.is_valid():
        return render(request, template, {'articleForm':articleForm})
    articleForm.save()
    messages.success(request, '文章已新增')
    return redirect('article:article')

def articleRead(request,articleId):
    article = get_object_or_404(Article, id=articleId)
    context = {
        'article': article,
        'comments': Comment.objects.filter(article=article)
    }
    return render(request, 'article/articleRead.html', context)

@admin_required
def articleUpdate(request, articleId):
    article = get_object_or_404(Article, id=articleId)
    template = 'article/articleCreateUpdate.html'
    if request.method == 'GET':
        articleForm = ArticleForm(instance=article)
        return render(request, template, {'articleForm':articleForm})
    #POST
    articleForm = ArticleForm(request.POST, instance=article)
    if not articleForm.is_valid():
        return render(request, template, {'articleForm':articleForm})
    articleForm.save()
    messages.success(request, '文章已修改')
    return redirect('article:articleRead',articleId=articleId)

@admin_required
def articleDelete(request, articleId):
    if request.method == 'GET':
        return article(request)
    #POST
    article = get_object_or_404(Article, id=articleId)
    article.delete()
    messages.success(request, '文章已刪除')
    return redirect('article:article')

def articleSearch(request):
    searchTerm = request.GET.get('searchTerm')
    articles = Article.objects.filter(Q(title__icontains=searchTerm) |
                                      Q(content__icontains=searchTerm))
    context = {'articles': articles, 'searchTerm': searchTerm}
    return render(request, 'article/articleSearch.html', context)

@login_required
def articleLike(request, articleId):
    article = get_object_or_404(Article, id=articleId)
    if request.user not in article.likes.all():
        article.likes.add(request.user)
    return articleRead(request, articleId)

@login_required
def commentCreate(request, articleId):
    if request.method == 'GET':
        return articleRead(request, articleId)

    #POST
    comment = request.POST.get('comment')
    if comment:
        comment = comment.strip()
    if not comment:
        return redirect('article:articleRead', articleId=articleId)
    article = get_object_or_404(Article, id=articleId)
    Comment.objects.create(article=article, user=request.user, content=comment)
    return redirect('article:articleRead',articleId=articleId)

@login_required
def commentUpdate(request, commentId):
    if request.method == 'GET':
        comment = get_object_or_404(Comment, id=commentId)
        return articleRead(request, comment.article.id)
    #POST
    commentToUpdate = get_object_or_404(Comment, id=commentId)
    article = get_object_or_404(Article, id=commentToUpdate.article.id)

    if commentToUpdate.user != request.user:
        messages.error(request, '無權修改')
        return redirect('article:articleRead', articleId=article.id)

    comment = request.POST.get('comment', '').strip()
    if not comment:
        commentToUpdate.delete()
    else:
        commentToUpdate.content = comment
        commentToUpdate.save()
    return redirect('article:articleRead', articleId=article.id)

@login_required
def commentDelete(request, commentId):
    if request.method == 'GET':
        comment = get_object_or_404(Comment, id=commentId)
        return articleRead(request, articleId=comment.article.id)
    #POST
    comment = get_object_or_404(Comment, id=commentId)
    article = get_object_or_404(Article, id=comment.article.id)

    if comment.user != request.user:
        messages.error(request, '無刪除權限')
        return redirect('article:articleRead', articleId=article.id)
    comment.delete()
    return redirect('article:articleRead',articleId=article.id)