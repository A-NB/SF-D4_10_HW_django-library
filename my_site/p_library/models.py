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
                                         #   on_delete=models.CASCADE,
                                         #   verbose_name=_("Издательство"),
                                         #   related_name="pub_house",)
                                         #  #  default=1,)
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



# # class Reader(models.Model):
# #     # id = models.UUIDField(default=uuid.uuid4, primary_key=True,
# #     #                       verbose_name=_("Уникальный ключ"))
# #     name = models.CharField(max_length=256, verbose_name=_("Имя"))

# #     books = models.ManyToManyField("p_library.Book",
# #                                     verbose_name=_("Книги"),
# #                                     through="p_library.BookReading")

# #     def __str__(self):
# #         return self.name


# # class BookReading(models.Model):
# #     # id = models.UUIDField(default=uuid.uuid4, primary_key=True,
# #     #                       verbose_name=_("Уникальный ключ"))
# #     book = models.ForeignKey("p_library.Book", on_delete=models.CASCADE,
# #                              verbose_name=_("Книга"),
# #                              related_name="bookreading_book")
# #     reader = models.ForeignKey("p_library.Reader", on_delete=models.CASCADE,
# #                                verbose_name=_("Читатель"),
# #                                related_name="bookreading_reader")
# #     completion = models.NullBooleanField(default=None,
# #                                          verbose_name=_("Чтение завершено"))

# #     def __str__(self):
# #         return "-".join((str(self.book),
# #                          str(self.reader),
# #                          str(self.completion),))        