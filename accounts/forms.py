from django import forms

class StudentForm(forms.Form):
    studentid = forms.IntegerField()
    first_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    

    def clean(self):
        cleaned_data = super().clean()
        