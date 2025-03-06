#  This is to check form via Django form validation

from django import forms

class ReviewForm(forms.Form):
  username = forms.CharField(label = "Your Name", max_length = 10, error_messages={
      "reqiured": "Ypur name must not be empty",
      "max_length": "Please enter a shorter name"
      })
  
  review_text = forms.CharField(label = "Your Feedback",max_length=500, widget=forms.Textarea)
  rating = forms.IntegerField(label = "Your Rating", min_value=1, max_value=5)