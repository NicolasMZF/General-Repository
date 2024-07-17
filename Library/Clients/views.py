from django.shortcuts import render

def View1(request):
    return render(request, 'client.html')