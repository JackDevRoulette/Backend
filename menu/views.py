from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Pizza



# Create your views here.


def index(request):
  Pizzas = Pizza.objects.all().order_by("Price")
  return render(request, "menu/index.html", {"Pizzas": Pizzas})


def api_get_pizzas(request):
  Pizzas = Pizza.objects.all().order_by("Price")
  
  json = serializers.serialize("json", Pizzas)
  return HttpResponse(json)




  """Pizzas = Pizza.objects.all()
  PizzasNames = [pizza.Nom + " : " + str(pizza.Price) + "€ " for pizza in Pizzas]
  PizzaNamesStr = ", ".join(PizzasNames)

  
  return HttpResponse(f"Les pizza :  {PizzaNamesStr}€ ")"""
  