from django import forms
from .models import Comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ["posts"]
        labels = {
            "user_name" : "Your Name",
            "user_email" : "Your Email",
            "text" : "Your Comment"
        }