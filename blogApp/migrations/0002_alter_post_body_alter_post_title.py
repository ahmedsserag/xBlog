# Generated by Django 4.2.6 on 2023-10-19 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(max_length=1250, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(help_text='Max lenght is 100.', max_length=100),
        ),
    ]
