from django.shortcuts import get_object_or_404, render
from .models import Vocab, Mean, Type

def index(request):
    latest_vocab_list = Vocab.objects.order_by('-pub_date')[:5]
    context = {'latest_vocab_list': latest_vocab_list}
    return render(request, 'vocab/index.html', context)

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
