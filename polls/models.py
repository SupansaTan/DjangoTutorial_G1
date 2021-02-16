import datetime

from django.db import models
from django.utils import timezone

tz = timezone.get_default_timezone()
# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes_score = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    
    def latest_vote_time(self):
        latest_vote = self.votes.latest('time')
        latest_time = latest_vote.time.astimezone(tz).strftime("%d/%m/%Y, %H:%M:%S")
        return latest_time

class Vote(models.Model):
    choice = models.ForeignKey(Choice,related_name= 'votes', on_delete=models.CASCADE)
    time = models.DateTimeField('time', blank=True,default=timezone.now())