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

    # for display in admin site
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def get_sum_score(self): # total votes for each question
        choices = list(self.choice_set.all()) # all choices of that question
        sum = 0
        for choice in choices:
            sum += choice.votes_score
        return sum

    def get_latest_vote_time(self):
        choices = list(self.choice_set.all())
        latest = choices[0].latest_vote_time_obj()
        for choice in choices:
            votetime = choice.latest_vote_time_obj()
            if  votetime > latest:
                latest = votetime
        
        return latest

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes_score = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    
    def latest_vote_time_obj(self): # object lastest vote time of each choice
        if self.votes.exists():
            latest_vote = self.votes.latest('time').time.astimezone(tz)
            return latest_vote
        return datetime.datetime(2000,1,1).astimezone(tz)
       

    def latest_vote_time(self): # lastest vote time of each choice
        latest_vote = self.votes.latest('time')
        latest_time = latest_vote.time.astimezone(tz).strftime("%d/%m/%Y, %H:%M:%S")
        return latest_time

    def get_percent(self):  # percentage of votes for each choice
        choice_percent = self.votes_score/self.question.get_sum_score() *100
        return "{:.1f}".format(choice_percent)

class Vote(models.Model):
    choice = models.ForeignKey(Choice,related_name= 'votes', on_delete=models.CASCADE)
    time = models.DateTimeField('time', blank=True,default=timezone.now)