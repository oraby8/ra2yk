# import form class from django
from django import forms
  
# import GeeksModel from models.py
from .models import Question
  
# create a ModelForm
class QuestionForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Question
        fields = "__all__"