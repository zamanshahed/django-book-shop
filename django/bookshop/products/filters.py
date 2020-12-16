import django_filters
from .models import book


class BookCategoryFilter(django_filters.FilterSet):
    class Meta:
        model = book
        fields = ['category_name', 'author_name', 'name']
