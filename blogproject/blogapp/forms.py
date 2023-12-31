from django import forms
from blogapp.models import Comment

class EmailSendForm(forms.Form):
	name = forms.CharField(max_length=50)
	email = forms.EmailField()
	to = forms.CharField(max_length=50)
	comments =forms.CharField(required=False,widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
    	model = Comment
    	fields=('name','email','body')
   