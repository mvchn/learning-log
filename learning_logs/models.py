from django.db import models

class Topic (models.Model):
    """ Learning Theme """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

class Entry (models.Model):
    """ Theme info """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'entities'

    def __str__(self):
        return f"{self.text[:50]}..."

