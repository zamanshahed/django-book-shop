from django.contrib import admin
from .models import book, BookCategory, BookAuthor
from products.models import UserProfileInfo


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author_name', 'price', 'rating_point', 'description', 'category_name', 'image_url')


class UserProfileInfoAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'profile_pic', 'present_address')


class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)


class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ('author_name',)


admin.site.register(book, BookAdmin)
admin.site.register(UserProfileInfo, UserProfileInfoAdmin)
admin.site.register(BookAuthor, BookAuthorAdmin)
admin.site.register(BookCategory, BookCategoryAdmin)
