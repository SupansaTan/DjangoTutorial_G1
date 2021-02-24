from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from .models import Vocab, Mean

def index(request):
    latest_vocab_list = Vocab.objects.order_by('-pub_date')[:5]
    context = {'latest_vocab_list': latest_vocab_list}
    return render(request, 'vocab/index.html', context)

def search(request):
    search_text = request.GET.get('search_box')  # set search_text value from tag input
    vocab_text = Vocab.objects.filter(Q(vocab_text__contains=search_text)) # get vocabs from database

    if vocab_text.exists(): # if found vocab
        vocab = vocab_text[0]
        return HttpResponseRedirect(reverse('vocab:detail', args=(vocab.id,)))
    else:
        return render(request, 'vocab/index.html', {
        'error_message': "Not Found",
        'latest_vocab_list': Vocab.objects.order_by('-pub_date')[:5]
    })

def detail(request, vocab_id):
    word = Vocab.objects.get(pk=vocab_id)
    word_type = word.meaning.get(pk=vocab_id).type
    word_mean = word.meaning.get(pk=vocab_id).means_text
    vocab_detail = [{'vocab_text':word.vocab_text, 'vocab_type':word_type, 'vocab_mean':word_mean}]

    return render(request, 'vocab/detail.html', {
        'vocabulary': vocab_detail,
        'vocab': word
    })

def addvocab(request):
    return render(request, 'vocab/formadd.html')