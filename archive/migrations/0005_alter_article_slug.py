# Generated by Django 5.0.1 on 2024-01-22 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0004_alter_comment_article_alter_subarticle_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True),
        ),
    ]
