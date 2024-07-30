from django.shortcuts import render

# Create your views here.


def genia(request):
    return render(request, "gen_ia/index_gen_ia.html")

def cadastro(request):
    return render(request, "gen_ia/cadastro_template.html")