############## ПРИМЕР ############## ПРИМЕР ############## ПРИМЕР ##############
# from django.shortcuts import render
# def home(request):
#     template = 'core/home.html'
#     context = {
#         'name': 'Иван',
#     }
#     return render(request, template, context)
############## ПРИМЕР ############## ПРИМЕР ############## ПРИМЕР ##############
# def home(request):
#     list_art = Articles.objects.all()
#     template = 'core/home.html'
#     context = {
#         'name': list_art,
#     }
#     return render(request, template, context)
# def detail_page(request, id):
#     get_article = Articles.objects.get(id=id)
#     template = 'core/detail_page.html'
#     context = {
#         'get_article': get_article,
#
#     }
#     return render(request, template, context)

from django.views.generic import ListView, DetailView
from .models import Articles


class HomeListView(ListView): ## Работает с моделью, "name" отправляет в шаблон
    model = Articles
    template_name = "core/home.html"
    context_object_name = "name"

class EditPage(ListView):  ## Работает с моделью, "name" отправляет в шаблон
    model = Articles
    template_name = "core/edit_page.html"
    context_object_name = "name"

class HomeDetailView(DetailView):
    model = Articles
    template_name = 'core/detail_page.html'
    context_object_name = "get_article"



