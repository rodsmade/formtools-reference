from .forms import StepZeroForm, StepOneForm, StepTwoForm, DummyForm

from django.shortcuts import render
from formtools.wizard.views import SessionWizardView

def show_business_form(formWizard):
    cleaned_data = formWizard.get_cleaned_data_for_step('0') or {}
    value = cleaned_data.get("is_business_guest", None)
    if isinstance(value, str) and value.lower() in ("false", "0"):
        return False
    else:
        return True

class NewOnboardingFlowView(SessionWizardView):
    form_list = [StepZeroForm, StepOneForm, DummyForm, StepTwoForm]
    template_name = "steps.html"

    condition_dict={'1': show_business_form}

    def get_context_data(self, form, **kwargs):
        cleaned_data = super().get_cleaned_data_for_step('0') or {}
        value = cleaned_data.get("is_business_guest", None)
        context = super().get_context_data(form=form, **kwargs)
        if self.steps.current == '1':
            context.update({'batata_frita': "siliga"})
            if isinstance(value, str) and value.lower() in ("true", "0"):
                context.update({'outro_passo': "eh vdd esse bilete"})
        return context

    def done(self, form_list, **kwargs):
        print(form_list)
        # process forms data here (persist to DB)

        return render(request=self.request, template_name="done.html")
