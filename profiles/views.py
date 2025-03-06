from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Uploadform
from .models import UserProfile

# Create your views here.

# def store_file(file):
#     with open("temp/image2.jpg", "wb+") as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)
    


def index(request):
    
    if request.method == "POST":
        form = Uploadform(request.POST, request.FILES)
        if form.is_valid():
            profile = UserProfile(image = request.FILES["user_file"])
            profile.save()
            return HttpResponseRedirect("/profiles", {"form": form})
        # return render(request, "profiles/create_profiles.html")
        # store_file(request.FILES["image"])
        # return HttpResponseRedirect("/profiles", {"form": form})
    else:
        form = Uploadform()
    return render(request, "profiles/create_profiles.html", {"form": form})