from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'naturestay/home.html')

def gallery(request):
    return render(request, 'naturestay/gallery.html')

def about(request):
    return render(request, 'naturestay/about.html')

def contact(request):
    return render(request, 'naturestay/contact.html')