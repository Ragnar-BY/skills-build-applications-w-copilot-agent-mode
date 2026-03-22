"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework import routers
from . import views

codespace_name = os.environ.get('CODESPACE_NAME')

def api_root(request):
    if codespace_name:
        base = f'https://{codespace_name}-8000.app.github.dev/api'
    else:
        base = request.build_absolute_uri('/api').rstrip('/')

    return JsonResponse({
        'users': f'{base}/users/',
        'teams': f'{base}/teams/',
        'activities': f'{base}/activities/',
        'workouts': f'{base}/workouts/',
        'leaderboard': f'{base}/leaderboard/',
    })

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'activities', views.ActivityViewSet)
router.register(r'workouts', views.WorkoutViewSet)
router.register(r'leaderboard', views.LeaderboardViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', api_root, name='api-root'),
]
