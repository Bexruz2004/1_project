from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import ContactForm
from article.models import (
    Article,
    Category,
    Tag
)
from django.contrib import messages


def home_view(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    comment_counts = []
    list_display = []
    list_display2= []
    for article in articles:
        comment_counts.append(article.comments.count())
        comment_counts.sort()
    for article in articles:
        if article.comments.count() in comment_counts[-3:]:
            list_display.append(article)
        else:
            list_display2.append(article)
    context = {
        "list_display": list_display,
        "list_display2": list_display2,
        "categories": categories,
        "tags": tags
    }
    return render(request, 'main/index.html', context)


def contact_view(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Contact sent successfully")
            reverse_url = reverse('main:contact')
            return redirect(reverse_url)
    context = {
        "form": form,

    }
    return render(request, 'main/contact.html', context)
