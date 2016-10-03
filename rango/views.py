from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list,
                         }
                          
    # loops through the category objects and adds the names to the context_dict
    for x in range(0, len(category_list)):
        context_dict['rango' + str(x)] = category_list[x]
   
    return render(request, 'rango/index.html', context=context_dict)
    
def about(request):
    context_dict = {'boldmessage': "Meeeeeeeee!"}
    return render(request, 'rango/about.html', context=context_dict)
 
def contact(request):
    return HttpResponse("Rango can be contacted at..., <br/> <a href='/rango'>Index</a>")
    
 #datetime.datetime.now()