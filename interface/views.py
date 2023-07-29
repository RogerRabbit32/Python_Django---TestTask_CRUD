from django.shortcuts import render


def home_page(request):
    return render(request, 'home.html')


def create_delete_post(request):
    return render(request, 'create_delete_post.html')
