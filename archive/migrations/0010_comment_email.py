# Generated by Django 5.0.1 on 2024-01-26 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0009_alter_article_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
