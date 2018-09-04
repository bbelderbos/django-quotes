from datetime import timedelta

from django.db import models
from django.utils import timezone

ONE_DAY_AGO = timezone.now() - timedelta(days=1)


class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=100)
    source = models.URLField(blank=True, null=True)
    cover = models.URLField(blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.quote} - {self.author}'

    class Meta:
        ordering = ['-added']

    @property
    def recently_added(self):
        """Quote that was added <= 1 day ago"""
        return self.added >= ONE_DAY_AGO
