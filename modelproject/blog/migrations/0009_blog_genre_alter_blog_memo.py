# Generated by Django 4.0.6 on 2022-07-11 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_rename_body_blog_memo_alter_blog_lyrics'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='genre',
            field=models.CharField(blank=True, choices=[('Pop', 'Pop'), ('K-pop', 'K-pop'), ('Indie', 'Indie'), ('Rock', 'Rock'), ('Else', 'Else')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='memo',
            field=models.TextField(blank=True, null=True),
        ),
    ]