# Generated by Django 4.0.6 on 2022-07-11 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='title',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='writer',
        ),
        migrations.AddField(
            model_name='blog',
            name='code',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='lyrics',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='singer',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
