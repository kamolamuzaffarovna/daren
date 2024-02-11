from django.shortcuts import render, redirect, get_object_or_404, reverse

from .models import Article, Category, Tag, Comment
from .forms import CommentForm
from django.contrib import messages


def archive_view(request):
    q = request.GET.get('q')
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    articles = Article.objects.order_by('-id')
    if q:
        articles = Article.objects.filter(title__icontains=q)
    if cat:
        articles = articles.filter(category__title__exact=cat)
    if tag:
        articles = articles.filter(tags__title__exact=tag)
    context = {
        'articles': articles
    }

    return render(request, 'main/archive.html', context)


def detail_view(request, slug):
    articles = Article.objects.order_by('id')
    articles_2 = Article.objects.order_by('-id')[:1]
    categories = Category.objects.all()
    tags = Tag.objects.all()
    parent_id = request.GET.get("pid")
    article = get_object_or_404(Article, slug=slug)
    comments = Comment.objects.filter(article=article)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.article = article
            if parent_id:
                obj.parent = Comment.objects.get(id=parent_id)
            obj.save()
            messages.success(request, 'Your message successfully sent')
            return redirect('.')
    add = []
    for i in articles:
        add.append(i)
    article_1 = add.index(article)
    if article_1 == 0:
        pre_article = False
    else:
        pre_article = add[article_1-1]
    if article_1 == len(add)-1:
        next_article = False
    else:
        next_article = add[article_1+1]
    context = {
        'comments': comments,
        'categories': categories,
        'articles_2': articles_2,
        'tags': tags,
        'article': article,
        'form': form,
        'pre_article': pre_article,
        'next_article': next_article
    }
    return render(request, 'archive/single-blog.html', context)


