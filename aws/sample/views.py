from django.shortcuts import render

# Create your views here.
def userView(request, name = "User"):
    return render(request, 'sample/home.html', {"name": name})