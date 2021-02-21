from django.shortcuts import get_object_or_404, render

from .models import Vocabs


def index(request):
    latest_vocabs_list = Vocabs.objects.order_by('-pub_date')[:5]
    context = {'latest_vocabs_list': latest_vocabs_list}
    return render(request, 'vocab/index.html', context)

def detail(request, vocabs_id):
    vocabs = get_object_or_404(Vocabs, pk=vocabs_id)
    return render(request, 'vocab/detail.html', {'vocabs': vocabs})