from django.shortcuts import render
from .models import PostCar


def post_view(request):
    if request.method == "GET":
        post = PostCar.objects.all()
        return render(request, template_name='post.html', context={'post': post})
