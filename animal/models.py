from django.db import models

# Create your models here.

class Advert(models.Model):
    class Meta:
        db_table = "advert"

    All = 0
    Dogs = 1
    Puppies = 2
    Cats = 3
    Kitens = 4
    category_list = (
        (All, 'Все'),
        (Dogs, 'Собаки'),
        (Puppies, 'Щенки'),
        (Cats, 'Кошки'),
        (Kitens, 'Котята'),
    )

    sex_list = (
        (0, 'Все'),
        (1, 'Мальчик'),
        (2, 'Девочка'),
    )

    title = models.CharField(max_length = 128)
    category = models.IntegerField(choices = category_list, default = All)
    date = models.DateTimeField()
    place = models.CharField(max_length=128)
    description = models.TextField()
    photo = models.ImageField(upload_to='pictures')
    price = models.IntegerField()
    views = models.IntegerField(default = 0)
    sex = models.IntegerField(choices=sex_list, default = 0)
