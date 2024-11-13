from django.shortcuts import render
from django.utils import timezone

def home(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Render 'member_home.html' if the user is logged in
        return render(request, 'espace_member/member_home.html', {'timestamp': timezone.now().timestamp()})
    else:
        # Render 'index.html' if the user is not logged in
        return render(request, 'index.html', {'timestamp': timezone.now().timestamp()})
