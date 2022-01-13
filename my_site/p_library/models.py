from django.utils.translation import gettext as _
from django.db import models
# import uuid

class Author(models.Model):
    # id = models.UUIDField(default=uuid.uuid4, primary_key=True,
    #                       verbose_name=_("Уникальный ключ"))
    full_name = models.TextField(verbose_name=_("Имя автора"),)
    birth_year = models.SmallIntegerField(verbose_name=_("Год рождения"),)
    country = models.CharField(max_length=2,
                               verbose_name=_("Страна"),)
    def __str__(self):
        return f'{self.full_name}'

class Book(models.Model):
    # id = models.UUIDField(default=uuid.uuid4, primary_key=True,
    #                       verbose_name=_("Уникальный ключ"))
    ISBN = models.CharField(max_length=13,
                            verbose_name=_("Международный стандартный "
                                           "книжный номер"),)
    title = models.TextField(verbose_name=_("Название"),)
    description = models.TextField(verbose_name=_("Аннотация"),)
    year_release = models.SmallIntegerField(verbose_name=_("Год выхода в свет"),)
    copy_count = models.SmallIntegerField(verbose_name=_("Число копий"),)
    price = models.DecimalField(max_digits=12,
                                decimal_places=2,
                                verbose_name=_("Цена"),)
    author = models.ForeignKey("p_library.Author",
                                on_delete=models.CASCADE,
                                verbose_name=_("Автор"),
                                related_name="book_author",)
    publishing_house = models.ForeignKey("p_library.PublishingHouse",
                                          verbose_name=_("Издательство"),
                                          on_delete=models.SET_NULL,
                                          null=True,
                                          blank=True,
                                          related_name="books",)
    year_publishing = models.SmallIntegerField(verbose_name=_("Год издания"),
                                                default=0,)
    def __str__(self):
        return f'{self.title}'

class PublishingHouse(models.Model):
    name = models.TextField(verbose_name=_("Издательство"),)
    country = models.CharField(max_length=2,
                               verbose_name=_("Страна"),)
    city = models.CharField(max_length=25, default="unknown",
                            verbose_name=_("Город"),)
    def __str__(self):
        return f'{self.name}'