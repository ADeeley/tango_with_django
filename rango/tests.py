from django.test import TestCase
from rango.models import Category
from django.core.urlresolvers import reverse




class CategoryMethodTests(TestCase):
    def test_ensure_views_are_positive(self):
        """ 
        ensure_views_are_positive should result True for categories
        where views are zero or positive.
        """
        cat = Category(name='test', views=-1, likes=0)
        cat.save()
        
        #checks if views are >= 0 and reverts views to 0 if not.
        result = cat.views >=0 
        if not result:
            cat.views = 0
            result = self.assertEqual((cat.views >=0), True)    

    def test_slug_line_creation(self):
        """
        slug_line_creation checks to make sure that when we add a category, that 
        an appropriate slug line is created.
        i.e. "Random Category String" -> "random-category-string"
        """
        cat = cat('Random Category String')
        cat.save()
        self.assertEqual(cat.slug, 'random-category-string')
    
def IndexViewTest(TestCase):

    def add_cat(name, views, likes):
        c = Category.objects.get_or_create(name=name)[0]
        c.views=views
        c.likes=likes
        c.save()
        return c
    
    def text_index_view_with_no_categories(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200) # code 200 is returned OK
        self.assertContains(response, "There are no categories present.")
        self.assertQuerysetEqual(response.context['categories'], [])
    
    def add_cat(name, views, likes):
        c = Category.objects.get_or_create(name=name)[0]
        c.views = views
        c.likes = likes
        c.save()
        return c
    
    def test_index_view_with_categories(self):
        """
        If no questions exist, an appropriate message should be displays.
        """
        
        add_cat('test',1,1)
        add_cat('temp',1,1)
        add_cat('tmp',1,1)
        add_cat('tmp test temp',1,1)
        
        response = self.cliet.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "tmp test temp")
    
        num_cats = len(response.context['categories'])
        self.assertEqual(num_cats, 4)
        
        