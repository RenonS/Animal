# Generated by Django 2.0.2 on 2018-03-16 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('category', models.CharField(max_length=128)),
                ('date', models.DateField()),
                ('place', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=256)),
                ('photo', models.ImageField(upload_to='pictures')),
                ('price', models.IntegerField()),
            ],
        ),
    ]
