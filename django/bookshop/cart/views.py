from easycart import BaseCart

# We assume here that you've already defined your item model
# in a separate app named "catalog".
from products.models import book


class Cart(BaseCart):

    def get_queryset(self, pks):
        return book.objects.filter(pk__in=pks)
