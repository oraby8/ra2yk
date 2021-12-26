from django.db import models


class Question(models.Model):
    id=models.AutoField(primary_key=True)
    question_text = models.CharField(max_length=200)
    public = models.BooleanField(default=False)
    #pub_date = models.DateTimeField('date published')
    photo = models.ImageField(upload_to='images/')
