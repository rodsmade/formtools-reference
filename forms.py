from django import forms

class StepZeroForm(forms.Form):
    BOOL_CHOICES = [(True, 'Yes'), (False, 'No')]
    forms.BooleanField
    is_business_guest = forms.ChoiceField(
            choices=BOOL_CHOICES,
            widget=forms.RadioSelect,
            required=True
    )

    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=12)

class StepOneForm(forms.Form):
    name = forms.CharField(max_length=100)

class StepTwoForm(forms.Form):
    room_type = forms.CharField(max_length=10, widget=forms.Select(choices=[(0, "Single"), (1, "Double"), (2, "Family")]))
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    number_of_nights = forms.IntegerField()

class DummyForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["no_show"].widget = forms.HiddenInput()

    no_show = forms.Field(required=False)
