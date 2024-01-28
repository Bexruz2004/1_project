from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from ckeditor.fields import RichTextField
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=225)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=225)
    image = models.ImageField(upload_to='article/author/', null=True, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tag = models.ManyToManyField(Tag)
    slug = models.SlugField(unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='article/', null=True, blank=True)
    title = models.CharField(max_length=225)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


def article_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        instance.slug = slugify(instance.title)


pre_save.connect(article_pre_save, sender=Article)


class Content(models.Model):
    content = RichTextField()
    boolean_field = models.BooleanField(default=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='contents')


class Commentary(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=223)
    parent_comment = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='parent')
    top_level_comment = models.IntegerField(null=True, blank=True)
    message = models.TextField()
    image = models.ImageField(upload_to='article/comment', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def top(instance, *args, **kwargs):
        if not instance.top_level_comment:
            child = Commentary.objects.filter(top_level_comment=instance.id)
            return child
        else:
            return None


def comment_pre_save(sender, instance, *args, **kwargs):
    if instance.parent_comment:
        parent = instance.parent_comment
        if instance.parent_comment.top_level_comment:
            instance.top_level_comment = parent.top_level_comment
        else:
            instance.top_level_comment = parent.id


pre_save.connect(comment_pre_save, sender=Commentary)



