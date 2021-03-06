import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE',  
                      'tango_with_django_project.settings'  ) 

import django
django.setup()
from rango.models import Category, Page

def populate():

    python_pages = [
        {"title": "Official Python Tutorial",
         "url": "http://docs.python.org/2/tutorial/",
         "views": 5},
        {"title": "How to Think like a Computer Scientist",
         "url":"http://www.greenteapress.com/thinkpython/",
         "views": 10},
        {"title": "Learn Python in 10 Minutes",
         "url": "http://www.korokitthakis.net/tutorials/python/",
         "views": 15}]
         
    django_pages = [
        {"title": "Official Django Tutorial",
         "url": "http://docs.djangoproject.com/en/1.9/intro/tutorial101/",
         "views": 20},
        {"title": "Django Rocks",
         "url": "http://www.djangorocks.com/",
         "views": 25},
        {"title": "How to Tango With Django",
         "url": "http://www.tangowithdjango.com/",
         "views": 30}]
         
    other_pages = [
        {"title": "Bottle",
         "url": "http://bottle.org/docs/dev/",
         "views": 35},
        {"title": "Flask",
         "url": "http//flask.pocoo.org",
         "views":40},
        {"title": "Learn Python the Hard Way",
         "url": "http://learnpythonthehardway.org/",
         "views":45}]
 
    random_pages = [
        {"title": "Reddit",
         "url": "http://reddit.com",
         "views": 50},
        {"title": "google",
         "url": "http//google.com",
         "views": 55},
        {"title": "wimp",
         "url": "http://wimp.com",
         "views":60}]

    cats = {"Python": {"pages": python_pages, "views": 128, "likes": 64},
            "Django": {"pages": django_pages, "views": 64, "likes": 32},
            "Other Frameworks": {"pages": other_pages,  "views": 32, "likes": 16},
            "Random Sites": {"pages": random_pages,  "views": 16, "likes": 8}}
            
            
    for cat, cat_data in cats.items(): 
        c = add_cat(cat, cat_data["views"], cat_data["likes"]) # update to provide views and likes arguments?
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"], p["views"])
            
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))
           
def add_page(cat, title, url, views):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url 
    p.views = views
    p.save()
    return p
    
def add_cat(name, views, likes): # added views and likes here
    c = Category.objects.get_or_create(name=name)[0] 
    c.views = views
    c.likes = likes
    c.save()
    return c
    
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
            
#test note change
#second test note