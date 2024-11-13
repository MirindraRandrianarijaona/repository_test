from django.shortcuts import render
from django.utils import timezone

def home(request):
    context = {'timestamp': timezone.now().timestamp()}
    return render(request, 'index.html', context)
