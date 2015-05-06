from django.views.generic import TemplateView
from djangular.forms import NgModelFormMixin, NgModelForm
from djangular.styling.bootstrap3.forms import Bootstrap3FormMixin

from .models import ACSZone, ACSRule, ACSOrder, ACSRequest


class ACSOverview(TemplateView):
    """ACS overview page"""
    template_name = 'ACSOverview.html'


class AddACSZoneForm(TemplateView):
    """Form allowing user add new ACS zone"""
    template_name = 'defaultForm.html'

    def get_context_data(self, **kwargs):
        """Injecting Angular form"""

        class AngularForm(NgModelFormMixin, NgModelForm, Bootstrap3FormMixin):
            """Angular form helper class"""
            form_name = 'ACSZoneForm'

            class Meta:
                model = ACSZone
                fields = ('name', 'manager', 'description')

            def __init__(self, *args, **kwargs):
                kwargs.update(scope_prefix='ACSZone')
                super(AngularForm, self).__init__(*args, **kwargs)

        context = super(AddACSZoneForm, self).get_context_data(**kwargs)
        context.update(form=AngularForm())
        context.update(form_title='Dodaj strefę systemu kontroli dostępu')
        return context


class AddACSOrderForm(TemplateView):
    """Form allowing user add new rules"""
    template_name = 'addACSOrderForm.html'

    def get_context_data(self, **kwargs):
        """Injecting Angular forms"""

        class RuleAngularForm(NgModelFormMixin, NgModelForm, Bootstrap3FormMixin):
            """Angular form helper class"""
            form_name = 'ACSRuleForm'

            class Meta:
                model = ACSRule
                fields = ('person', 'zone')

            def __init__(self, *args, **kwargs):
                kwargs.update(scope_prefix='ACSRule')
                super(RuleAngularForm, self).__init__(*args, **kwargs)

        class OrderAngularForm(NgModelFormMixin, NgModelForm, Bootstrap3FormMixin):
            """Angular form helper class"""
            form_name = 'ACSOrderForm'

            class Meta:
                model = ACSOrder
                fields = ('grant_privilege', )

            def __init__(self, *args, **kwargs):
                kwargs.update(scope_prefix='ACSOrder')
                super(OrderAngularForm, self).__init__(*args, **kwargs)

        context = super(AddACSOrderForm, self).get_context_data(**kwargs)
        context.update(form_title='Dodaj nowe polecenie')
        context.update(order_form=OrderAngularForm())
        context.update(rule_form=RuleAngularForm())
        return context


class AddACSRequestForm(TemplateView):
    """Form allowing user add new request"""
    template_name = 'addACSRequestForm.html'

    def get_context_data(self, **kwargs):
        """Injecting Angular forms"""

        class RuleAngularForm(NgModelFormMixin, NgModelForm, Bootstrap3FormMixin):
            """Angular form helper class"""
            form_name = 'ACSRuleForm'

            class Meta:
                model = ACSRule
                fields = ('person', 'zone')

            def __init__(self, *args, **kwargs):
                kwargs.update(scope_prefix='ACSRule')
                super(RuleAngularForm, self).__init__(*args, **kwargs)

        class RequestAngularForm(NgModelFormMixin, NgModelForm, Bootstrap3FormMixin):
            """Angular form helper class"""
            form_name = 'ACSRequestForm'

            class Meta:
                model = ACSRequest
                fields = ('grant_privilege',)

            def __init__(self, *args, **kwargs):
                kwargs.update(scope_prefix='ACSRequest')
                super(RequestAngularForm, self).__init__(*args, **kwargs)

        context = super(AddACSRequestForm, self).get_context_data(**kwargs)
        context.update(form_title='Dodaj nową prośbę')
        context.update(request_form=RequestAngularForm())
        context.update(rule_form=RuleAngularForm())
        return context
