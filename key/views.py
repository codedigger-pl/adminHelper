from django.views.generic import TemplateView
from djangular.forms import NgModelFormMixin, NgModelForm
from djangular.styling.bootstrap3.forms import Bootstrap3FormMixin

from .models import Key, KeyRule, KeyOrder, KeyRequest


class KeyOverview(TemplateView):
    """Key overview page"""
    template_name = 'keyOverview.html'


class AddKeyForm(TemplateView):
    """Form allowing user add new Key zone"""
    template_name = 'defaultForm.html'

    def get_context_data(self, **kwargs):
        """Injecting Angular form"""

        class AngularForm(NgModelFormMixin, NgModelForm, Bootstrap3FormMixin):
            """Angular form helper class"""
            form_name = 'KeyForm'

            class Meta:
                model = Key
                fields = ('name', 'manager', 'description')

            def __init__(self, *args, **kwargs):
                kwargs.update(scope_prefix='key')
                super(AngularForm, self).__init__(*args, **kwargs)

        context = super(AddKeyForm, self).get_context_data(**kwargs)
        context.update(form=AngularForm())
        context.update(form_title='Dodaj klucz')
        return context


class AddKeyOrderForm(TemplateView):
    """Form allowing user add new rules"""
    template_name = 'addKeyOrderForm.html'

    def get_context_data(self, **kwargs):
        """Injecting Angular forms"""

        class RuleAngularForm(NgModelFormMixin, NgModelForm, Bootstrap3FormMixin):
            """Angular form helper class"""
            form_name = 'KeyRuleForm'

            class Meta:
                model = KeyRule
                fields = ('person', 'key')

            def __init__(self, *args, **kwargs):
                kwargs.update(scope_prefix='KeyRule')
                super(RuleAngularForm, self).__init__(*args, **kwargs)

        class OrderAngularForm(NgModelFormMixin, NgModelForm, Bootstrap3FormMixin):
            """Angular form helper class"""
            form_name = 'KeyOrderForm'

            class Meta:
                model = KeyOrder
                fields = ('grant_privilege', )

            def __init__(self, *args, **kwargs):
                kwargs.update(scope_prefix='KeyOrder')
                super(OrderAngularForm, self).__init__(*args, **kwargs)

        context = super(AddKeyOrderForm, self).get_context_data(**kwargs)
        context.update(form_title='Dodaj nowe polecenie')
        context.update(order_form=OrderAngularForm())
        context.update(rule_form=RuleAngularForm())
        return context


class AddKeyRequestForm(TemplateView):
    """Form allowing user add new request"""
    template_name = 'addKeyRequestForm.html'

    def get_context_data(self, **kwargs):
        """Injecting Angular forms"""

        class RuleAngularForm(NgModelFormMixin, NgModelForm, Bootstrap3FormMixin):
            """Angular form helper class"""
            form_name = 'KeyRuleForm'

            class Meta:
                model = KeyRule
                fields = ('person', 'key')

            def __init__(self, *args, **kwargs):
                kwargs.update(scope_prefix='KeyRule')
                super(RuleAngularForm, self).__init__(*args, **kwargs)

        class RequestAngularForm(NgModelFormMixin, NgModelForm, Bootstrap3FormMixin):
            """Angular form helper class"""
            form_name = 'KeyRequestForm'

            class Meta:
                model = KeyRequest
                fields = ('grant_privilege',)

            def __init__(self, *args, **kwargs):
                kwargs.update(scope_prefix='KeyRequest')
                super(RequestAngularForm, self).__init__(*args, **kwargs)

        context = super(AddKeyRequestForm, self).get_context_data(**kwargs)
        context.update(form_title='Dodaj nową prośbę')
        context.update(request_form=RequestAngularForm())
        context.update(rule_form=RuleAngularForm())
        return context
