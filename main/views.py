from django.shortcuts import render, get_object_or_404, redirect, reverse

def home(request):
    template_name = 'main/home.html'
    context = {}    
    return render(request, template_name, context)