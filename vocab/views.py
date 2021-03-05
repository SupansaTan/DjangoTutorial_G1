from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from .models import Vocab, Mean

def index(request): # show recently added vocabulary
    latest_vocab_list = Vocab.objects.order_by('-pub_date')[:4] # 4 recently added words
    context = {'latest_vocab_list': latest_vocab_list}
    return render(request, 'vocab/index.html', context)

def search(request): # when submitted search button 
    search_text = request.GET.get('search_box')  # set search_text value from tag input
    vocab_text = Vocab.objects.filter(Q(vocab_text__icontains=search_text.lower())) # get vocabs from database

    if vocab_text.exists(): # if found vocab go to result page
        vocab = list(vocab_text)
        return render(request, 'vocab/result.html', {
            'vocab_list': vocab,
            'seach_text': search_text
        })
    else:
        # not found vocab
        return render(request, 'vocab/index.html', {
        'error_message': f"'{search_text}' not found.",
        'latest_vocab_list': Vocab.objects.order_by('-pub_date')[:4] # 4 recently added words
    })

def detail(request, vocab_id): # show detail about that vocab
    # get detail
    word = Vocab.objects.get(pk=vocab_id)
    word_mean = word.get_meaning_type()
    vocab_detail = [{'vocab_text':word.vocab_text, 'vocab_mean':word_mean}]

    return render(request, 'vocab/detail.html', {
        'vocabulary': vocab_detail,
        'vocab': word
    })
    
def addVocab(request):
            
    if request.method == 'GET': # show form input
        return render(request, 'vocab/add.html')

    elif request.method == 'POST': # if submitted form
        word = request.POST.get('word_input').strip()
        word_type = request.POST.get('type')
        meaning = request.POST.get('meaning').strip()

        if not Vocab.objects.filter(Q(vocab_text=word)).exists(): # if it is new word
            # create word and meaning & save to database
            create_word = Vocab(vocab_text=word)
            create_meaning = Mean(vocab=create_word, type=word_type, means_text=meaning)
            create_word.save()
            create_meaning.save()

            # show alert successful
            return render(request,'vocab/add.html',{
                'success': f"Successful ! '{word}' has been added."
            })
        else:
            # if not new word
            existsWord = Vocab.objects.get(vocab_text=word) # get word

            if not Mean.objects.filter(Q(vocab=existsWord) & Q(means_text=meaning)).exists(): # if not have meaning of this vocab
                # create new meaning & save to database
                create_meaning = Mean(vocab=existsWord, type=word_type, means_text=meaning)
                create_meaning.save()

                # show alert successful
                return render(request,'vocab/add.html',{
                    'success': f"Successful! '{word}' has been added."
                })
        
        # show alert danger
        return render(request,'vocab/add.html',{
                    'failed': f"Oops ! '{word}' already exists"
                })
                
def deleteVocab(request, vocab_id):
    Vocab.objects.get(id=vocab_id).delete() # delete vocab
    return HttpResponseRedirect('/vocab/') # redirect to index page

def edit(request, vocab_id): 
    vocab = Vocab.objects.get(id=vocab_id)
    # edit vocab
    if request.method == 'GET':
        vocab_text = vocab.vocab_text
        vocab_type = vocab.get_type
        vocab_meaning = vocab.get_meaning
        return render(request, 'vocab/edit.html', {
            'vocab': vocab_text,
            'vocab_type': vocab_type,
            'vocab_meanning': vocab_meaning
        })

    elif request.method == 'POST':
        new_vocab = request.POST.get('vocab_input', 'None').strip()
        new_type = request.POST.get('type_input', 'None')
        new_meanning = request.POST.get('meanning_input', 'None').strip()

        if new_vocab != 'None' and new_vocab != "":
            vocab.vocab_text =  new_vocab
            vocab.save()
        
        if new_type != 'None':
            vocab.meaning.get(id=vocab_id).type = new_type
            vocab.save()

        if new_meanning != 'None' and new_vocab != "":
            vocab.meaning.get(id=vocab_id).means_text = new_meanning
            vocab.save()
        
        return redirect(f'/vocab/{vocab_id}') #return to index