from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(username='testuser', email='test@example.com')
        self.assertEqual(user.email, 'test@example.com')

    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

    def test_activity_creation(self):
        activity = Activity.objects.create(name='Test Activity', user_email='test@example.com')
        self.assertEqual(activity.name, 'Test Activity')

    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(team='Test Team', points=100)
        self.assertEqual(leaderboard.points, 100)

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout', description='Test Desc')
        self.assertEqual(workout.name, 'Test Workout')
