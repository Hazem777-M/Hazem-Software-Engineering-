from django.shortcuts import render

def index(request):
    return render(request, 'icons/index.html')

# Add this new function
def about(request):
    return render(request, 'icons/About.html')#اعاده بناء