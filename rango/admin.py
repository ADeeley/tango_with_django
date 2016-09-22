from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

# to update the categories on the admin page to show the category names, not
# "category Object"

admin.site.register(Category)
admin.site.register(Page, PageAdmin)
