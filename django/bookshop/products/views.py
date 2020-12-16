from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render
from .filters import BookCategoryFilter

from . import models
from .models import book

from products.forms import UserForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


def index(request):
    products = book.objects.all()
    return render(request, 'bookshop/homepage.html', {'books':products})


def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # validity
        if user_form.is_valid() and profile_form.is_valid():
            # save data directly to database
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'bookshop/registration.html',
                  {'user_form':user_form,
                   'profile_form': profile_form,
                   'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('products:index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone failed to login !")
            print("Username: {} and Password: {}".format(username, password))
            return HttpResponse("Username or Password Wrong")
    else:
        return render(request, 'bookshop/user_login.html', {})


@login_required
def special(request):
    return HttpResponse("You are LOGGED IN Now!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('products:index'))


class BookListView(ListView):
    context_object_name = 'books'
    model = models.book


class CategoryListView(ListView):
    context_object_name = 'categories'
    model = models.BookCategory


class AuthorListView(ListView):
    context_object_name = 'authors'
    model = models.BookAuthor


class FilterCategoryList(ListView):
    context_object_name = 'filter_books'
    model = models.book


class BookDetailView(DetailView):
    context_object_name = 'book_detail'
    model = models.book
    template_name = 'products/book_detail.html'


def search(request):
    book_list = book.objects.all()
    book_filter = BookCategoryFilter(request.GET, queryset=book_list)
    return render(request, 'products/filters.html', {'filter':book_filter})








