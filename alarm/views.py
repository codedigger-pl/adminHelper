from django.views.generic import TemplateView


class AlarmOverview(TemplateView):
    """Alarm overview page"""
    template_name = 'alarmOverview.html'
