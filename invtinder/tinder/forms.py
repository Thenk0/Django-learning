from allauth.account.forms import SignupForm
from django import forms


class CustomSignUpForm(SignupForm):
    def __init__(self, *args, **kwargs):
        NONE = ""
        COMPANY = "Company"
        FUND = "Fund"
        PRIVATE = "Private"
        COMPANY_TYPE_CHOICES = [
            (NONE, ""),
            (COMPANY, "Company"),
            (PRIVATE, "Private"),
            (FUND, "Fund"),
        ]
        super(CustomSignUpForm, self).__init__(*args, **kwargs)
        self.fields["first_name"] = forms.CharField(
            required=True, widget=forms.TextInput(attrs={"placeholder": "First Name"})
        )
        self.fields["last_name"] = forms.CharField(
            required=True, widget=forms.TextInput(attrs={"placeholder": "Last Name"})
        )
        self.fields["company_type"] = forms.ChoiceField(required=False, choices=COMPANY_TYPE_CHOICES)

    def save(self, request):
        first_name = self.cleaned_data.pop("first_name")
        last_name = self.cleaned_data.pop("last_name")
        company_type = self.cleaned_data.pop("company_type")
        # Можно ли сделать одно сохранение, вместо вызова метода сохранения дважды?
        user = super(CustomSignUpForm, self).save(request)
        user.first_name = first_name
        user.last_name = last_name
        user.company_type = company_type
        user.save()
        return user
