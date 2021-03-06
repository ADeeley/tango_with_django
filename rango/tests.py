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
        self.assertEqual((cat.views >= 0), True)
        
    def test_slug_line_creation(self):
        """
        slug_line_creation checks to make sure that when we add a category, that 
        an appropriate slug line is created.
        i.e. "Random Category String" -> "random-category-string"
        """
        cat = Category(name='test', views=-1, likes=0)
        cat.name = 'Random Category String'
        cat.save()
        self.assertEqual(cat.slug, 'random-category-string')

class IndexViewTest(TestCase):

    def add_cat(self, name, views, likes):
        c = Category.objects.get_or_create(name=name)[0]
        c.views=views
        c.likes=likes
        c.save()
        return c
    
    def test_index_view_with_no_categories(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200) # code 200 is returned OK#
        self.assertContains(response, "There are no categories present.")
        # currently returns: ..<HttpResponse status_code=200, "text/html; charset=utf-8">
        self.assertQuerysetEqual(response.context['categories'], [])
        
        
        
    def test_index_view_with_categories(self):
        """
        If no questions exist, an appropriate message should be displays.
        """
        
        self.add_cat('test',1,1)
        self.add_cat('temp',1,1)
        self.add_cat('tmp',1,1)
        self.add_cat('tmp test temp',1,1)

        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        
        cat = Category.objects.all()

        
        self.assertContains(response, "tmp test temp")
    
        num_cats = len(response.context['categories'])
        self.assertEqual(num_cats, 4)

    def test_index_view_shows_top_five(self):
        """
        Checks if the top 5 views are shown and in the correct order
        """
        
        self.add_cat('First place',1,1)
        self.add_cat('Second place',1,2)
        self.add_cat('Third place',1,3)
        self.add_cat('Fourth place',1,4)
        self.add_cat('Fifth place',1,5)
        self.add_cat('Sixth place',1,0)

        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "First place")
        self.assertContains(response, "Fifth place")
   
         
        