from core.models import *
from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    model= Mascot
    template_name ='index.html'

    def get_context_data(self, **kwargs):       
        context=super(IndexView,self).get_context_data(**kwargs)
        context['tittle']='Mascota'
        context['listMascota']= Mascot.objects.all()
        return context
