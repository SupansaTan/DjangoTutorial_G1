from django.shortcuts import get_object_or_404, render

from .models import Vocab


def index(request):
    data = Vocab.objects.all()
    return render(request, 'vocab/index.html', {'vocabulary':data})

def addvocab(request):
    return render(request, 'vocab/formadd.html')