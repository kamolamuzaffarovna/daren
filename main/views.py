from django.shortcuts import render, redirect
from archive.models import Article, Category
from .forms import ContactForm
from django.contrib import messages
from django.db.models import Q


def home_view(request):

    tag = request.GET.get('tag')
    q = request.GET.get('q')

    q_condition = Q()
    if q:
        q_condition = Q(title__icontains=q)
    tag_condition = Q()
    if tag:
        tag_condition = Q(tags__title=tag)

    articles = Article.objects.filter(q_condition, tag_condition).order_by('-id')[:3]

    context = {
        'articles': articles
    }

    return render(request, 'main/index.html', context)


def category_view(request):

    articles = Article.objects.order_by('-id')

    context = {
        'articles': articles
    }

    return render(request, 'main/category.html', context)


def contact_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message successfully sent')
            return redirect('.')

    context = {
        'form': form
    }

    return render(request, 'main/contact.html', context)
