from django.db import models
from django.utils import timezone
import datetime

class Vocab(models.Model):
    vocab_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.vocab_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Mean(models.Model):
    vocab = models.ForeignKey(Vocab, related_name='meaning', on_delete=models.CASCADE)
    type = models.CharField(max_length=200)
    means_text = models.CharField(max_length=400)

    def __str__(self):
        return self.means_text