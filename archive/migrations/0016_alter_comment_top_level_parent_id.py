# Generated by Django 5.0.1 on 2024-01-27 06:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0015_alter_comment_top_level_parent_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='top_level_parent_id',
            field=models.IntegerField(blank=True, null=True, verbose_name=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='archive.comment')),
        ),
    ]
