from django.db import models
from django.urls import reverse

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=100)
    issue_a = models.CharField(max_length=100)
    issue_b = models.CharField(max_length=100)
    image_a = models.ImageField(blank=True)
    image_b = models.ImageField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('eithers:detail', kwargs={'either_pk': self.pk})


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    pick = models.IntegerField()
    comment = models.CharField(max_length=100)

    class Meta:
        ordering = ['-pk']
