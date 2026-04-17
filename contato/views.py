from django.shortcuts import render

# Create your views here.
def index(request):
    return render(
        request,
        'contato/index.html'
    )
    
def insert(request):
    return render(
        request,
        'contato/inserir.html'
    )