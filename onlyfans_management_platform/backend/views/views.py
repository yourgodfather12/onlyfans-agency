
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from ..models.models import (
    CreatorVault,
    AdminAccessLog,
    Fan,
    ActionSuggestion,
    AnalyticsData,
    AutomationFlow,
    ContentSchedule,
    UserProfile,
    AIRecommendation
)
from datetime import datetime
import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, filename='logs/backend/actions.log',
                    format='%(asctime)s %(levelname)s:%(message)s')

@method_decorator(login_required, name='dispatch')
class VaultView(View):
    def get(self, request):
        if request.user.is_superuser:
            vaults = CreatorVault.objects.all()
        else:
            vaults = CreatorVault.objects.filter(creator=request.user)
        logging.info(f"User {request.user.username} accessed their vaults.")
        return render(request, 'vault.html', {'vaults': vaults})

@login_required
def admin_access_vault(request, vault_id):
    if request.user.is_superuser:
        creator_vault = get_object_or_404(CreatorVault, pk=vault_id)
        AdminAccessLog.objects.create(admin_user=request.user, creator_vault=creator_vault)
        logging.info(f"Admin {request.user.username} accessed the vault of user {creator_vault.creator.username}.")
        messages.success(request, 'Successfully accessed the creator vault.')
        return render(request, 'admin_view_vault.html', {'creator_vault': creator_vault})
    logging.warning(f"Unauthorized access attempt by {request.user.username} to vault {vault_id}.")
    messages.error(request, 'You do not have permission to access this vault.')
    return redirect('vault')

@login_required
def fan_management_dashboard(request):
    fans = Fan.objects.filter(creator=request.user)
    logging.info(f"User {request.user.username} accessed the fan management dashboard.")
    return render(request, 'fan_management_dashboard.html', {'fans': fans})

@login_required
def action_suggestions(request):
    if request.method == 'POST':
        action_description = request.POST.get('action_description')
        projected_outcome = f"If you {action_description}, you'll likely see a 15% boost in engagement!"
        ActionSuggestion.objects.create(
            creator=request.user,
            action_description=action_description,
            projected_outcome=projected_outcome,
            timestamp=datetime.now()
        )
        logging.info(f"User {request.user.username} submitted an action suggestion: {action_description}.")
        messages.success(request, f"Action suggestion recorded: {action_description}.")
        return render(request, 'action_suggestion_result.html', {'action_description': action_description, 'projected_outcome': projected_outcome})
    return render(request, 'action_suggestions.html')

@login_required
def analytics_data(request):
    analytics = AnalyticsData.objects.filter(creator=request.user)
    logging.info(f"User {request.user.username} accessed their analytics dashboard.")
    return render(request, 'analytics_dashboard.html', {'analytics': analytics})

@login_required
def automation_flows(request):
    if request.method == 'POST':
        trigger_event = request.POST.get('trigger_event')
        action_taken = request.POST.get('action_taken')
        AutomationFlow.objects.create(
            creator=request.user,
            trigger_event=trigger_event,
            action_taken=action_taken
        )
        logging.info(f"User {request.user.username} created an automation flow: Trigger - {trigger_event}, Action - {action_taken}.")
        messages.success(request, 'Automation flow created successfully.')
        return redirect('automation_flows')
    return render(request, 'automation_dashboard.html')

@login_required
def content_scheduling(request):
    if request.method == 'POST':
        content = request.FILES['content']
        schedule_time = request.POST.get('schedule_time')
        ContentSchedule.objects.create(
            creator=request.user,
            content=content,
            schedule_time=schedule_time
        )
        logging.info(f"User {request.user.username} scheduled new content for {schedule_time}.")
        messages.success(request, 'Content scheduled successfully.')
        return redirect('content_scheduling')
    return render(request, 'content_scheduling.html')

@login_required
def onboarding(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        user_profile.onboarding_complete = True
        user_profile.save()
        logging.info(f"User {request.user.username} completed onboarding.")
        messages.success(request, 'Onboarding completed successfully.')
        return redirect('vault')
    return render(request, 'onboarding.html')

@login_required
def ai_recommendations(request):
    if request.method == 'POST':
        recommendation = f"We recommend focusing on engaging with your fans by doing live Q&A sessions every week."
        AIRecommendation.objects.create(
            creator=request.user,
            recommendation=recommendation,
            timestamp=datetime.now()
        )
        logging.info(f"User {request.user.username} received AI recommendation.")
        messages.success(request, 'AI recommendation generated successfully.')
        return render(request, 'ai_recommendation_result.html', {'recommendation': recommendation})
    return render(request, 'ai_recommendations.html')
