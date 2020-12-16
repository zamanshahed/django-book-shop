from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class BookAuthor(models.Model):
    author_name = models.CharField(max_length=255)

    def __str__(self):
        return self.author_name


class BookCategory(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name


class book(models.Model):
    name = models.CharField(max_length=255)
    author_name = models.ForeignKey(BookAuthor, on_delete=models.CASCADE, blank=True)
    price = models.FloatField()

    rating_point = models.FloatField()
    description = models.CharField(max_length=2083)

    category_name = models.ForeignKey(BookCategory, on_delete=models.CASCADE, blank=True)
    image_url = models.CharField(max_length=2083)

    """
    def publish(self):
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comments=True)

    
    def get_absolute_url(self):
        return reverse("book_details",  args=[str(self.id)])
    """

    def __str__(self):
        return self.name

    class Meta():
        ordering = ['name']


class Comment(models.Model):
    the_book = models.ForeignKey(
        'products.book', related_name='comments', on_delete=models.DO_NOTHING
    )
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_comments = models.BooleanField(default=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve(self):
        self.approved_comments = True
        self.save()

    def get_absolute_url(self):
        return reverse('book_list')

    def __str__(self):
        return self.text


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Other info
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    full_name = models.CharField(max_length=255)
    present_address = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username


class UserCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # cart info
    price_total = models.FloatField(blank=True)

    def __str__(self):
        return self.price_total


class CartDetails(models.Model):
    cart = models.OneToOneField(UserCart, on_delete=models.CASCADE)

    item_name = models.CharField(max_length=266)
    total_items = models.IntegerField()
    purchase_date = models.DateTimeField()

    def __str__(self):
        return self.purchase_date
