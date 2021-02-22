from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

from .models import Vocab, Mean

def index(request):
    latest_vocab_list = Vocab.objects.order_by('-pub_date')[:5]
    context = {'latest_vocab_list': latest_vocab_list}
    return render(request, 'vocab/index.html', context)

def detail(request, vocab_id):
    word = Vocab.objects.get(pk=vocab_id)
    word_type = word.mean_set.get(pk=vocab_id).type
    word_mean = word.mean_set.get(pk=vocab_id).means_text
    vocabulary = [{'vocab_text':word.vocab_text, 'vocab_type':word_type, 'vocab_mean':word_mean}]

    return render(request, 'vocab/detail.html', {
        'vocabulary': vocabulary,
        'vocab': word
    })

def addvocab(request):
    return render(request, 'vocab/formadd.html')
