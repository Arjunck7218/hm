from django.shortcuts import render

# Create your views here.
def registerpatiants(request):
    return render (request,"patiants.html")

def getmaster(request):
    return render (request,"master.html")

def gethome(request):
    return render (request,"home.html")

def getcontact(request):
    return render (request,"contact.html")

def getaboutas(reqest):
    return render(reqest,"about as.html")

