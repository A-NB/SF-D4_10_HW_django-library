from django.contrib import admin
from p_library.models import Author, Book, PublishingHouse

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # @staticmethod
    # def author_full_name(obj):
    #     return obj.author.full_name#.verbose_name
    list_display = ('title', 'author', 'price', 'copy_count',) # 'author_full_name', 'price', 'copy_count',)
    fields = ('ISBN', 'title', 'author', 'description', 'year_release', 'price', 'copy_count', 'year_publishing', 'publishing_house',)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birth_year', 'country',) 

@admin.register(PublishingHouse)
class PublishingHouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'city',)    




# [admin.site.register(item) for item in (Author, Book, PublishingHouse,)]