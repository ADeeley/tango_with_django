from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page

def show_category(request, category_name_slug):
    # create a context dictionaty which we can pass to the
    # template rendering engine
    context_dict = {}
    
    try:
        # can we find a caetgory name slug with the given name?
        # If we can't, the get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or returns an exception.
        category = Category.objects.get(slug=category_name_slug)
        
        # Retrieves all of the associated pages.
        # Note that the filter() will return a list of page objects or an empty list.
        pages = Page.objects.filter(category=category)
        
        # Adds our results list to the template context under name pages
        context_dict['pages'] = pages
        
        # we also add the category object from the database to the context
        # dictionary. We'll use this in the template to verify the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything -
        # the template will display the "no category"message for us.
        context_dict['category'] = None
        context_dict['pages'] = None
    
    #go render the response and return it to the client
    return render(request, 'rango/category.html', context_dict)
        

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
                          
    # render the response and send it back!
    return render(request, 'rango/index.html', context=context_dict)
    
def about(request):
    context_dict = {'boldmessage': "Meeeeeeeee!"}
    return render(request, 'rango/about.html', context=context_dict)
 
def contact(request):
    return HttpResponse("Rango can be contacted at..., <br/> <a href='/rango'>Index</a>")
    
 #datetime.datetime.now()