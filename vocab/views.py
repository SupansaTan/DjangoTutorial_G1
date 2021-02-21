from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from .models import Vocab


def index(request):
    data = Vocab.objects.all()
    return render(request, 'vocab/index.html', {'vocabulary':data})

def detail(request):
    name = request.POST['name']
    descripion = request.POST['descripion']
    user = User.objects.create_vocabs(
        vocabs_text = name,
        means = descripion
    )
    user.save()

    data = Vocab.objects.all()
    return render(request, 'vocab/index.html', {'vocabulary':data})

def addvocab(request):
    return render(request, 'vocab/formadd.html')