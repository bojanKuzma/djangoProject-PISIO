from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=128,)
    description = models.TextField(max_length=384, null=True, blank=True)
    time_asked = models.DateTimeField(auto_now_add=True)
    original_poster = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)


class Answer(models.Model):
    time_answered = models.DateTimeField(auto_now_add=True)
    answer = models.CharField(max_length=384)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    author = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
