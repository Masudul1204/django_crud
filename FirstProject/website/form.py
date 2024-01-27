from django import forms
from website.models import student_info

class std(forms.ModelForm):
    class Meta:
        model = student_info
        fields = "__all__"
        # fields = ('std_name','std_roll')