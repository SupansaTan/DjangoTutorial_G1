from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question, Vote


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# reverse sort variables
reverseVotes = True;
reverseVoteTime = True;

def index(request):
    button = request.GET.get('sort', False) 
    
    if button == 'votes': # clicked button to sort by votes
        global reverseVotes
        question_list = []
        question_sorted = []
        questions = Question.objects.all()

        # sort questions by sum votes
        for question in questions:
            question_obj = {'question':question, 'votes':question.get_sum_score()} # get sum votes of each question
            question_list.append(question_obj)

        question_list = sorted(question_list, key=lambda question: question['votes'], reverse=reverseVotes)

        for question_obj in question_list:
            question_sorted.append(question_obj['question'])

        # change next reverse sort
        if reverseVotes:
            reverseVotes = False # sort from lowest to highest votes
        else:
            reverseVotes = True # sort from highest to lowest votes 

        return render(request, 'polls/index.html', {
            'latest_question_list': question_sorted
        })

    elif button == 'vote_time': # clicked button to sort by vote time
        global reverseVoteTime
        question_list = []
        question_sorted = []
        questions = Question.objects.all()
       
        for question in questions:
            question_obj = {'question':question, 'votetime':question.get_latest_vote_time()} # get last vote time of each question
            question_list.append(question_obj)

        question_list = sorted(question_list, key=lambda question: question['votetime'], reverse=reverseVoteTime)
        
        for question_obj in question_list:
            question_sorted.append(question_obj['question'])

        # change next reverse sort
        if reverseVoteTime:
            reverseVoteTime = False # sort from oldest to latest vote time
        else:
            reverseVoteTime = True # sort from latest to oldest vote time

        return render(request, 'polls/index.html', {
            'latest_question_list': question_sorted
        })

    return render(request, 'polls/index.html', {
            'latest_question_list': Question.objects.filter(
                pub_date__lte=timezone.now()
            ).order_by('-pub_date')[:5]
    })

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    try:
        choice_id = request.POST['choice']
        selected_choice = question.choice_set.get(pk=choice_id)
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # add score of that choice
        selected_choice.votes_score += 1
        selected_choice.save()

        # add vote time when user submitted vote
        userVote = Vote()
        userVote.choice = selected_choice
        userVote.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))