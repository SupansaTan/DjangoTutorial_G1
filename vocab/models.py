import datetime

from django.db import models
from django.utils import timezone

class Vocabs(models.Model):
    vocabs_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.vocabs_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
class Means(models.Model):
    vocabs = models.ForeignKey(Vocabs, on_delete=models.CASCADE)
    means_text = models.CharField(max_length=200)
    def __str__(self):
        return self.means_text