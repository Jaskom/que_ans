from django import forms
class QuestionForm(forms.Form):
    que_owner=forms.CharField()
    que_description=forms.CharField(widget=forms.Textarea)
   
