from django.views.generic import TemplateView
from djangular.forms import NgModelFormMixin, NgModelForm
from djangular.styling.bootstrap3.forms import Bootstrap3FormMixin

from .models import AlarmZone, AlarmRule, AlarmOrder


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
            form_name = 'alarmZoneForm'

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


class AddAlarmOrderForm(TemplateView):
    """Form allowing user add new rules"""
    template_name = 'addAlarmOrderForm.html'

    def get_context_data(self, **kwargs):
        """Injecting Angular forms"""

        class RuleAngularForm(NgModelFormMixin, NgModelForm, Bootstrap3FormMixin):
            """Angular form helper class"""
            form_name = 'alarmRuleForm'

            class Meta:
                model = AlarmRule
                fields = ('person', 'zone')

            def __init__(self, *args, **kwargs):
                kwargs.update(scope_prefix='alarmRule')
                super(RuleAngularForm, self).__init__(*args, **kwargs)

        class OrderAngularForm(NgModelFormMixin, NgModelForm, Bootstrap3FormMixin):
            """Angular form helper class"""
            form_name = 'alarmOrderForm'

            class Meta:
                model = AlarmOrder
                fields = ('grant_privilege', 'user')

            def __init__(self, *args, **kwargs):
                kwargs.update(scope_prefix='alarmOrder')
                super(OrderAngularForm, self).__init__(*args, **kwargs)

        context = super(AddAlarmOrderForm, self).get_context_data(**kwargs)
        context.update(form_title='Dodaj nowe polecenie')
        context.update(order_form=OrderAngularForm())
        context.update(rule_form=RuleAngularForm())
        return context
