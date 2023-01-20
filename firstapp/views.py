from django.shortcuts import render

# Create your views here.
def load_sample(request):
    return render(request,'sammple.html')