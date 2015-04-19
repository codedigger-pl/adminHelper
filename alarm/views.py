from django.views.generic import TemplateView
from djangular.forms import NgModelFormMixin, NgModelForm
from djangular.styling.bootstrap3.forms import Bootstrap3FormMixin

from .models import AlarmZone


class AlarmOverview(TemplateView):
    """Alarm overview page"""
    template_name = 'alarmOverview.html'


class AddAlarmZoneForm(TemplateView):
    """Form allowing user add new alarm zone"""
    template_name = 'defaultForm.html'

    def get_context_data(self, **kwargs):
        """Injecting Angular form"""

        class AngularForm(NgModelFormMixin, NgModelForm, Bootstrap3FormMixin):
            """Angular form helper class"""
            form_name = 'personGroupForm'

            class Meta:
                model = AlarmZone
                fields = ('name', 'manager', 'description')

            def __init__(self, *args, **kwargs):
                kwargs.update(scope_prefix='alarmZone')
                super(AngularForm, self).__init__(*args, **kwargs)

        context = super(AddAlarmZoneForm, self).get_context_data(**kwargs)
        context.update(form=AngularForm())
        context.update(form_title='Dodaj strefę systemu alarmowego')
        return context
