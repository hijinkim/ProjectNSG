# Generated by Django 3.1.5 on 2021-02-11 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yyApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='postID',
        ),
    ]