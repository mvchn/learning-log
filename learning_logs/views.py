from django.shortcuts import render

def index(request):
    """ Learning Log homepage """
    return render(request, 'learning_logs/index.html')