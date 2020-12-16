from django.urls import path
from products import views
from django.views.generic import RedirectView


app_name = 'products'

urlpatterns = [
    # path('', views.index, name='index'),
    path('', RedirectView.as_view(url='book_list/', permanent=True)),
    path('book_list/', views.BookListView.as_view(), name='index'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('special/', views.special, name='special'),
    path('user_login/', views.user_login, name='user_login'),
    path('book_list/<int:pk>', views.BookDetailView.as_view(), name='details'),
    path('book_list/filter/<int:pk>', views.BookDetailView.as_view(), name='details'),
    path('book_list/filter/', views.search, name='search'),
]
