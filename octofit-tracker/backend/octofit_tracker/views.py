
from rest_framework import viewsets, permissions, response, reverse
from .models import User, Team, Activity, Workout, Leaderboard
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, WorkoutSerializer, LeaderboardSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [permissions.AllowAny]

class TeamViewSet(viewsets.ModelViewSet):
	queryset = Team.objects.all()
	serializer_class = TeamSerializer
	permission_classes = [permissions.AllowAny]

class ActivityViewSet(viewsets.ModelViewSet):
	queryset = Activity.objects.all()
	serializer_class = ActivitySerializer
	permission_classes = [permissions.AllowAny]

class WorkoutViewSet(viewsets.ModelViewSet):
	queryset = Workout.objects.all()
	serializer_class = WorkoutSerializer
	permission_classes = [permissions.AllowAny]

class LeaderboardViewSet(viewsets.ModelViewSet):
	queryset = Leaderboard.objects.all()
	serializer_class = LeaderboardSerializer
	permission_classes = [permissions.AllowAny]

from rest_framework.decorators import api_view
@api_view(['GET'])
def api_root(request, format=None):
	return response.Response({
		'users': reverse.reverse('user-list', request=request, format=format),
		'teams': reverse.reverse('team-list', request=request, format=format),
		'activities': reverse.reverse('activity-list', request=request, format=format),
		'workouts': reverse.reverse('workout-list', request=request, format=format),
		'leaderboard': reverse.reverse('leaderboard-list', request=request, format=format),
	})
