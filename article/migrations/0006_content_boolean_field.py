# Generated by Django 5.0.1 on 2024-01-22 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_author_remove_article_content_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='boolean_field',
            field=models.BooleanField(default=False),
        ),
    ]
