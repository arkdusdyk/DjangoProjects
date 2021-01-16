from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
class IndexView(TemplateView):#Generic TemplateView only used in views that only shows template
	template_name = 'kilogram/index.html'