# Generated by Django 2.0.2 on 2018-03-16 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='advert',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterModelTable(
            name='advert',
            table='advert',
        ),
    ]