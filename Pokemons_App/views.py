from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')


def query_results(request):
    return render(request, 'query_results.html')


def add_pokemon(request):
    return render(request, 'add_pokemon.html')
