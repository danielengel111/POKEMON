from django.shortcuts import render
from django.db import connection


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


# Create your views here.
def home(request):
    return render(request, 'home.html')


def query_results(request):
    with connection.cursor() as cursor:
        cursor.execute("""
     SELECT Name, Attack
     FROM Pokemons
     WHERE Legendary=1;
     """)
        sql_res1 = dictfetchall(cursor)
        cursor.execute("""
             SELECT Name, Attack
             FROM Pokemons
             WHERE Legendary=1;
             """)
        sql_res2 = dictfetchall(cursor)
        cursor.execute("""
                     SELECT Name, Attack
                     FROM Pokemons
                     WHERE Legendary=1;
                     """)
        sql_res3 = dictfetchall(cursor)
    return render(request, 'query_results.html', {'sql_res1': sql_res1, 'sql_res2': sql_res2,
                                                  'sql_res3': sql_res3})


def add_pokemon(request):
    return render(request, 'add_pokemon.html')
