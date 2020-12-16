from allauth.account.forms import SignupForm
from django import forms
from .models import Project


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

    # Изначально тут был save(self, request)
    # Но чтобы он работал надо было 2 раза сохранять пользователя
    def signup(self, request, user):
        user.first_name = self.cleaned_data.pop("first_name")
        user.last_name = self.cleaned_data.pop("last_name")
        user.company_type = self.cleaned_data.pop("company_type")
        user.save()
        return user


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name", "email", "phone", "video", "description"]

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        # you can iterate all fields here
        for fname, f in self.fields.items():
            f.widget.attrs["class"] = "form-control"

    # contact_email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"placeholder": "Contact email"})
    # contact_phone = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Contact phone"})
    # project_name = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Project name"})
    # description = forms.Textarea(required=False)
    # video = forms.FileField(required=False)
    # is_active = forms.BooleanField(required=true, )
