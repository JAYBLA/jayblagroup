from django.shortcuts import render, get_object_or_404, redirect, reverse

def home(request):
    template_name = 'main/home.html'
    context = {
        'title':"Home"    
        
    }    
    return render(request, template_name, context)

def graphic_design(request):
    template_name = 'main/graphic_design.html'
    context = {
        'title':"Graphic Design"    
        
    }    
    return render(request, template_name, context)

def tshirt_printing(request):
    template_name = 'main/tshirt_printing.html'
    context = {
        'title':"Tshirt-Printing"    
        
    }    
    return render(request, template_name, context)

def signages(request):
    template_name = 'main/signages.html'
    context = {
        'title':"2D & 3D Signages"    
        
    }    
    return render(request, template_name, context)

def banners_stickers(request):
    template_name = 'main/banners_stickers.html'
    context = {
        'title':"Banners and Stickers"    
        
    }    
    return render(request, template_name, context)

def promotional_materials(request):
    template_name = 'main/promotional_materials.html'
    context = {
        'title':"Home"    
        
    }    
    return render(request, template_name, context)

def contact(request):
    template_name = 'main/contact.html'
    context = {
        'title':"Contacts"    
        
    }    
    return render(request, template_name, context)
