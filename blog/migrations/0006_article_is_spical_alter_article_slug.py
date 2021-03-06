# Generated by Django 4.0.3 on 2022-04-05 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_category_options_article_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_spical',
            field=models.BooleanField(default=False, verbose_name='مقاله ویژه'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='آدرس مقاله'),
        ),
    ]
