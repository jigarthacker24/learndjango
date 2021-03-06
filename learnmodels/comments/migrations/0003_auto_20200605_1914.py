# Generated by Django 3.0.7 on 2020-06-05 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20200605_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='downvotes',
            field=models.IntegerField(default=0, verbose_name='Down Votes'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Time'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='upvotes',
            field=models.PositiveIntegerField(default=0, verbose_name='Up Votes'),
        ),
    ]
