
from django.urls import path
from ..views.views import (
    VaultView,
    admin_access_vault,
    fan_management_dashboard,
    action_suggestions,
    analytics_data,
    automation_flows,
    content_scheduling,
    onboarding,
    ai_recommendations
)

urlpatterns = [
    path('vault/', VaultView.as_view(), name='vault'),
    path('admin/vault/<int:vault_id>/', admin_access_vault, name='admin_vault_access'),
    path('fan_management/', fan_management_dashboard, name='fan_management_dashboard'),
    path('action_suggestions/', action_suggestions, name='action_suggestions'),
    path('analytics/', analytics_data, name='analytics_data'),
    path('automation/', automation_flows, name='automation_flows'),
    path('content_scheduling/', content_scheduling, name='content_scheduling'),
    path('onboarding/', onboarding, name='onboarding'),
    path('ai_recommendations/', ai_recommendations, name='ai_recommendations'),
]
