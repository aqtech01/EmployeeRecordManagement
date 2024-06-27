from django import forms
from .models import *

class EmployeeEducationForm(forms.ModelForm):
    class Meta:
        model = EmployeeEducation
        fields = [
            "postg_course", "postg_passing_year", "postg_institiute", "postg_percentage",
            "graduation_course", "graduation_passing_year", "graduation_institiute", "graduation_percentage",
            "highers_course", "highers_passing_year", "highers_institiute", "highers_percentage",
            "scondary_course", "scondary_passing_year", "scondary_institiute", "scondary_percentage",
        ]
        widgets = {
            'postg_course': forms.TextInput(attrs={'class': 'form-control '}),
            'postg_passing_year': forms.NumberInput(attrs={'class': 'form-control '}),
            'postg_institiute': forms.TextInput(attrs={'class': 'form-control '}),
            'postg_percentage': forms.NumberInput(attrs={'class': 'form-control '}),
            'graduation_course': forms.TextInput(attrs={'class': 'form-control '}),
            'graduation_passing_year': forms.NumberInput(attrs={'class': 'form-control '}),
            'graduation_institiute': forms.TextInput(attrs={'class': 'form-control '}),
            'graduation_percentage': forms.NumberInput(attrs={'class': 'form-control '}),
            'highers_course': forms.TextInput(attrs={'class': 'form-control '}),
            'highers_passing_year': forms.NumberInput(attrs={'class': 'form-control '}),
            'highers_institiute': forms.TextInput(attrs={'class': 'form-control '}),
            'highers_percentage': forms.NumberInput(attrs={'class': 'form-control '}),
            'scondary_course': forms.TextInput(attrs={'class': 'form-control '}),
            'scondary_passing_year': forms.NumberInput(attrs={'class': 'form-control '}),
            'scondary_institiute': forms.TextInput(attrs={'class': 'form-control '}),
            'scondary_percentage': forms.NumberInput(attrs={'class': 'form-control col-sm-6'}),
        }


class EmployeeExperienceForm(forms.Form):
        class Meta:
                model = EmployeeExperience
                fields = [
                    "compnay1_name","company1_desigantion","company1_duration","company1_salary",
                    "compnay2_name","company2_desigantion","company2_duration","company2_salary",
                    "compnay3_name","company3_desigantion","company3_duration","company3_salary",
                    
                    ]