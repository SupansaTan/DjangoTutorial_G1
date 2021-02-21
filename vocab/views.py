from django.shortcuts import get_object_or_404, render

from .models import Vocab


def index(request):
    latest_vocab_list = Vocab.objects.order_by('-pub_date')[:5]
    context = {'latest_vocab_list': latest_vocab_list}
    return render(request, 'vocab/index.html', context)

def detail(request, vocabs_id):
    vocabs = get_object_or_404(Vocab, pk=vocabs_id)
    return render(request, 'vocab/detail.html', {'vocabs': vocabs})