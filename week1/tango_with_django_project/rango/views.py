from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page

#def index(request):
#    return HttpResponse("Rango says hey there partner! Visit the <a href='rango/about'>About</a> page")

def index(request):
        #context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
        #return render(request, 'rango/index.html', context=context_dict)
        category_list = Category.objects.order_by('-likes')[:5]
        context_dict = {'categories': category_list}

        return render(request, 'rango/index.html', context_dict)

def about(request):
    return HttpResponse("Rango says there is an about page! Go back to the <a href='/'>Home</a> page")

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)

        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages

        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context_dict)
