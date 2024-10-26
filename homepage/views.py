from django.shortcuts import render

from category.models import Category


def homepage(request):
    category = Category.objects.all()
    context = {
        'category': category
    }
    return render(request, 'index.html', context)
    # return render(request, 'home.html')
