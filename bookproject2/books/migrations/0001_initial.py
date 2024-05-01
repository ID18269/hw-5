# Generated by Django 5.0.4 on 2024-04-30 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=128)),
                ('title', models.CharField(max_length=255)),
                ('info', models.TextField()),
                ('pages', models.IntegerField()),
                ('ebook', models.FileField(blank=True, null=True, upload_to='media/ebooks')),
            ],
        ),
    ]
