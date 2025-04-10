
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def main_menu(request):
    template = loader.get_template('main_menu.html')
    return HttpResponse(template.render())