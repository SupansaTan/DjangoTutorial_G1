from django.db import models


class Vocab(models.Model):
    vocabs_text = models.CharField(max_length=200)
    means = models.CharField(max_length=200)
