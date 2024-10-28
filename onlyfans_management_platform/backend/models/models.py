
from django.db import models
from django.contrib.auth.models import User

class CreatorVault(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    content_file = models.FileField(upload_to='creator_vault/')
    is_public = models.BooleanField(default=False)

class AdminAccessLog(models.Model):
    admin_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="admin_access")
    creator_vault = models.ForeignKey(CreatorVault, on_delete=models.CASCADE)
    access_time = models.DateTimeField(auto_now_add=True)

class Fan(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    fan_name = models.CharField(max_length=255)
    fan_data = models.JSONField()  # Store interaction data
    segment = models.CharField(max_length=50)
    last_interaction = models.DateTimeField(auto_now=True)

class ActionSuggestion(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    action_description = models.CharField(max_length=255)
    projected_outcome = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class AnalyticsData(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    engagement_rate = models.FloatField()
    fan_growth = models.IntegerField()
    revenue = models.FloatField()
    content_performance = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)

class AutomationFlow(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    trigger_event = models.CharField(max_length=255)
    action_taken = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class ContentSchedule(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.FileField(upload_to='scheduled_content/')
    schedule_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    onboarding_complete = models.BooleanField(default=False)

class AIRecommendation(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    recommendation = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
