from django.shortcuts import render


def profile_home(request):
    context = {
        'title': 'Administration',
        'bodyId': 'page-top',
    }
    return render(request, 'user_profile/dashboard.html', context)
