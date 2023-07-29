from django.urls import path

from .views import home_page, create_delete_post


urlpatterns = [
    path('', home_page, name='home-page'),
    path('create-delete-post/', create_delete_post, name='create-delete-post'),
]
