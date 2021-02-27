from django.urls import path 
from .views import BlogsView, UpdatePostView , DeletePostView, CategoryView, DetailsView, CreatePostView

urlpatterns=[
    path('', BlogsView.as_view(), name='post'),
    path('<str:slug>/', DetailsView, name='details'),
    path('olustur/', CreatePostView, name='create'),
    path('guncelle/<str:slug>', UpdatePostView.as_view(), name='update'),
    path('<str:slug>/sil/', DeletePostView.as_view(), name="delete"),
    path('kategori/<str:cats>', CategoryView, name='category'),
]