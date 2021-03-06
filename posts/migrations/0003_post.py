# Generated by Django 3.2 on 2021-04-09 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0002_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('publisher', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
