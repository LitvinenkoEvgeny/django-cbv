from django.conf.urls import include, url, patterns
from django.contrib import admin

from books_cbv import views

urlpatterns = patterns("",
                       url(r"^$", views.BookList.as_view(), name="book_list"),
                       url(r"page/(?P<page>\d+)$", views.BookList.as_view(), name="book_list"),
                       url(r"^new$", views.BookCreate.as_view(), name="book_new"),
                       url(r"^edit/(?P<pk>\d+)$", views.BookUpdate.as_view(), name="book_edit"),
                       url(r"^delete/(?P<pk>\d+)$", views.BookDelete.as_view(), name="book_delete"),
                       )
