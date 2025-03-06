from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
# Create your views here.
def index(request):
    
    if request.method == "POST":
        # entered_username = request.POST["username"]
        forms = ReviewForm(request.POST)
        if forms.is_valid():
            review = Review(username = forms.cleaned_data["username"], review_text = forms.cleaned_data["review_text"], rating = forms.cleaned_data["rating"])
            review.save()
            # print(forms.cleaned_data)
            return HttpResponseRedirect("/review")
    else:
        forms = ReviewForm()
        return render(request, "reviews/index.html", {
        
        "form": forms
    })

def review(request):
    return render(request, "reviews/review.html")    
    

    