import imp
from django.shortcuts import render

# Create your views here.
#CRUD
from .models import Post

def post_list_view (request):
    post_objects = Post.objects.all()
    
    context = {
        "post_objects":post_objects
    }
    
    return render(request, "posts/index.html", context)