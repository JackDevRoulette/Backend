from django.contrib import admin

# Register your models here.

from .models import Pizza



class PizzaAdmin(admin.ModelAdmin):
    list_display = ('Nom', 'Price', 'Ingredients', 'Vegetarian')
    search_fields = ["Nom"]
    
admin.site.register(Pizza, PizzaAdmin)