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
        print("cat: ", cat[0], cat[1],cat[2],cat[3], "catlen: ", len(cat))
        print("***Response: ", response.context)
        
        self.assertContains(response, "tmp test temp")
    
        num_cats = len(response.context['categories'])
        self.assertEqual(num_cats, 4)


         
        