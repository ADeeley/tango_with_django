import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE',  
                      'tango_with_django_project.settings'  ) 

import django
django.setup()
from rango.models import Category, Page

def populate():

    python_pages = [
        {"title": "Official Python Tutorial",
        "url": "http://docs.python.org/2/tutorial/"},
        {"title": "How to Think like a Computer Scientist",
        "url":"http://www.greenteapress.com/thinkpython/"},
        {"title": "Learn Python in 10 Minutes",
         "url": "http://www.korokitthakis.net/tutorials/python/"}]
         
    django_pages = [
        {"title": "Official Django Tutorial",
         "url": "http://docs.djangoproject.com/en/1.9/intro/tutorial101/"},
        {"title": "Django Rocks",
         "url": "http://www.djangorocks.com/"},
        {"title": "How to Tango With Django",
         "url": "http://www.tangowithdjango.com/"}]
         
    other_pages = [
        {"title": "Bottle",
         "url": "http://bottle.org/docs/dev/"},
        {"title": "Flask",
         "url": "http//flask.pocoo.org"},
        {"title": "Learn Python the Hard Way",
         "url": "http://learnpythonthehardway.org/"}]

    cats = {"Python": {"pages": python_pages, "views": 128, "likes": 64},
            "Django": {"pages": django_pages, "views": 64, "likes": 32},
            "Other Frameworks": {"pages": other_pages,  "views": 32, "likes": 16}}
            
            
    for cat, cat_data in cats.items(): 
        c = add_cat(cat, cat_data["views"], cat_data["likes"]) # update to provide views and likes arguments?
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"])
            
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))
           
def add_page(cat, title, url):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url 
    p.save()
    return p
    
def add_cat(name, views, likes): # added views and likes here
    c = Category.objects.get_or_create(name=name)[0] # something probably goes here
    c.views = views
    c.likes = likes
    c.save()
    return c
    
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
            
#test note change
#second test note