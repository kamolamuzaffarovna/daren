# Generated by Django 5.0.1 on 2024-01-27 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0014_alter_comment_top_level_parent_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='top_level_parent_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
