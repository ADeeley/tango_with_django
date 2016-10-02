from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

def index(request):
    cat = Category.objects.all()
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!", 
                          'categories': cat,
                         }
                          
    # loops through the category objects and adds the names to the context_dict
    for x in range(0, len(cat)):
        context_dict['rango' + str(x)] = cat[x]
   
    return render(request, 'rango/index.html', context=context_dict)
    
def about(request):
    context_dict = {'boldmessage': "Meeeeeeeee!"}
    return render(request, 'rango/about.html', context=context_dict)
 
def contact(request):
    return HttpResponse("Rango can be contacted at..., <br/> <a href='/rango'>Index</a>")
    
    
# ..***Response:  [{'True': True, 'None': None, 'False': False}, {'request': <WSGIRequest: GET '/rango/'>,
 # 'user': <SimpleLazyObject: <function AuthenticationMiddleware.process_request.<locals>.<lambda> at 0x00
# 0001DC9A5968C8>>, 'perms': <django.contrib.auth.context_processors.PermWrapper object at 0x000001DC9A697
# 8D0>, 'csrf_token': <SimpleLazyObject: <function csrf.<locals>._get_val at 0x000001DC9A5961E0>>, 'DEFAUL
# T_MESSAGE_LEVELS': {'SUCCESS': 25, 'WARNING': 30, 'DEBUG': 10, 'INFO': 20, 'ERROR': 40}, 'messages': <dj
# ango.contrib.messages.storage.fallback.FallbackStorage object at 0x000001DC97077668>}, {}, {'categories'
# : <QuerySet [<Category: test>, <Category: temp>, <Category: tmp>, <Category: tmp test temp>]>, 'boldmess
# age': 'Crunchy, creamy, cookie, candy, cupcake!'}]
# F.