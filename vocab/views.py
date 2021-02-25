from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from .models import Vocab, Mean

def index(request):
    latest_vocab_list = Vocab.objects.order_by('-pub_date')[:4]
    context = {'latest_vocab_list': latest_vocab_list}
    return render(request, 'vocab/index.html', context)

def search(request):
    search_text = request.GET.get('search_box')  # set search_text value from tag input
    vocab_text = Vocab.objects.filter(Q(vocab_text__icontains=search_text.lower())) # get vocabs from database

    if vocab_text.exists(): # if found vocab go to result page
        vocab = list(vocab_text)
        return render(request, 'vocab/result.html', {
            'vocab_list': vocab,
            'seach_text': search_text
        })
    else:
        return render(request, 'vocab/index.html', {
        'error_message': f"'{search_text}' not found.",
        'latest_vocab_list': Vocab.objects.order_by('-pub_date')[:4]
    })

def detail(request, vocab_id):
    word = Vocab.objects.get(pk=vocab_id)
    word_type = word.get_type()
    word_mean = word.get_meaning()
    vocab_detail = [{'vocab_text':word.vocab_text, 'vocab_type':word_type, 'vocab_mean':word_mean}]

    return render(request, 'vocab/detail.html', {
        'vocabulary': vocab_detail,
        'vocab': word
    })  

def addVocab(request):
    if request.method == 'GET':
        return render(request, 'vocab/add.html')

    elif request.method == 'POST': # if submitted form
        word = request.POST.get('word_input').strip()
        word_type = request.POST.get('type')
        meaning = request.POST.get('meaning').strip()

        if not Vocab.objects.filter(Q(vocab_text=word)).exists(): # if it is new word
            # create word and meaning
            create_word = Vocab(vocab_text=word)
            create_meaning = Mean(vocab=create_word, type=word_type, means_text=meaning)
            create_word.save()
            create_meaning.save()
            return render(request,'vocab/add.html',{
                'success': f"Successful ! '{word}' has been added."
            })
        else:
            # if not new word
            existsWord = Vocab.objects.get(vocab_text=word) # get word

            if not Mean.objects.filter(Q(vocab=existsWord) & Q(means_text=meaning)).exists(): # if not have meaning of this vocab
                create_meaning = Mean(vocab=existsWord, type=word_type, means_text=meaning)
                create_meaning.save()
                return render(request,'vocab/add.html',{
                    'success': f"Successful! '{word}' has been added."
                })
        
        return render(request,'vocab/add.html',{
                    'failed': f"Oops ! '{word}' already exists"
                })
                
def deleteVocab(request, vocab_id):
    Vocab.objects.get(id=vocab_id).delete()
    return HttpResponseRedirect('/vocab/')