from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import (
    Article,
    Tag,
    Commentary,
    Category
)
from .forms import CommentaryForm
from django.db.models import Q
from django.contrib import messages


def article_list(request):
    tags = Tag.objects.all()
    categories = Category.objects.all()
    article_2 = Article.objects.order_by('-id')[:2]
    if request.GET.get('cat'):
        cat = request.GET.get('cat')
    else:
        cat = False
    if request.GET.get('tag'):
        tag = request.GET.get('tag')
    else:
        tag = False
    articles = Article.objects.all()
    q = request.GET.get('q')
    if q:
        q_search = Q(title__icontains=q)
        articles = Article.objects.filter(q_search)
    if cat:
        articles = Article.objects.filter(category__title__exact=cat)
    if tag:
        articles = Article.objects.filter(tag__name__exact=tag)
    context = {
        "articles": articles,
        "article_2": article_2,
        "tags": tags,
        "categories": categories,
        "cat": cat,
        "tag": tag
    }
    return render(request, 'article/archive.html', context)


def article_detail(request, slug):
    pid = request.GET.get('pid')
    article_2 = Article.objects.order_by('-id')[:3]
    tags = Tag.objects.all()
    categories = Category.objects.all()
    article = Article.objects.get(slug=slug)
    articles = Article.objects.all()
    article_l = []
    for i in articles:
        article_l.append(i)
    article_id = article_l.index(article)
    if article_id == 0:
        prev_article = False
    else:
        prev_article = article_l[article_id - 1]

    if article_id == (len(article_l)-1):
        next_article = False
    else:
        next_article = article_l[article_id+1]

    form = CommentaryForm
    if request.method == "POST":
        form = CommentaryForm(request.POST, files=request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            if pid:
                comment.parent_comment = Commentary.objects.get(id=pid)
            comment.save()
            messages.success(request, "Comment sent successfully")
            reverse_url = reverse('article:detail', args=[slug])
            return redirect(reverse_url)
    # article_id = articles.filter(slug=article.slug).first().id
    # prev_article = articles.filter(id=article_id - 1).last()
    # next_article = articles.filter(id=article_id + 1).first()
    context = {
        "article": article,
        "prev_article": prev_article,
        "next_article": next_article,
        "form": form,
        "tags": tags,
        "categories": categories,
        "article_2": article_2
    }
    return render(request, "article/single-blog.html", context)


