from django.shortcuts import render
from .models import Article

# Create your views here.

def index(request):
    aricles = Article.objects.all()

    context = {
        'articles': aricles
    }


    return render(request, 'index.html',context)
