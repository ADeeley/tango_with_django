from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)
    
def about(request):
    context_dict = {'boldmessage': "Meeeeeeeee!"}
    return render(request, 'rango/about.html', context=context_dict)
 
def contact(request):
    return HttpResponse("Rango can be contacted at..., <br/> <a href='/rango'>Index</a>")