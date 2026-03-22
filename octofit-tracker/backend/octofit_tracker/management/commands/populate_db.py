from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Очистка коллекций
        User.objects.all().delete()
        app_models.Team.objects.all().delete()
        app_models.Activity.objects.all().delete()
        app_models.Leaderboard.objects.all().delete()
        app_models.Workout.objects.all().delete()

        # Создание команд
        marvel = app_models.Team.objects.create(name='Marvel')
        dc = app_models.Team.objects.create(name='DC')

        # Создание пользователей
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel)
        captain = User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='password', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='password', team=dc)

        # Создание активностей
        app_models.Activity.objects.create(user=ironman, type='run', duration=30, calories=300)
        app_models.Activity.objects.create(user=batman, type='cycle', duration=45, calories=400)

        # Создание воркаутов
        app_models.Workout.objects.create(name='Hero HIIT', description='High intensity workout for heroes')
        app_models.Workout.objects.create(name='Power Lift', description='Strength workout for super strength')

        # Создание лидерборда
        app_models.Leaderboard.objects.create(user=ironman, score=1000)
        app_models.Leaderboard.objects.create(user=batman, score=950)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
