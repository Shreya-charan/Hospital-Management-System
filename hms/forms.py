from django import forms
from .models import Doctor, Patient, Department
from django.core.exceptions import ValidationError

class PatientIdForm(forms.Form):
    p_id = forms.CharField(label='Patient ID', max_length=6)

class DoctorIdForm(forms.Form):
    doctor_id = forms.CharField(label='Doctor ID', max_length=6)



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class DoctorUpdateForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['d_id', 'name', 'age', 'contact', 'email' ]

    def clean_d_id(self):
        d_id = self.cleaned_data['d_id']
        existing_doctor = Doctor.objects.exclude(pk=self.instance.pk).filter(d_id=d_id)
        if existing_doctor.exists():
            raise ValidationError("Doctor with this D id already exists.")
        return d_id

    def __init__(self, *args, **kwargs):
        super(DoctorUpdateForm, self).__init__(*args, **kwargs)
        self.fields['d_id'].widget.attrs['readonly'] = True


class PatientUpdateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['p_id', 'name', 'age', 'contact', 'email', 'address', 'disease', 'treatment', 'doctor']

    def clean_p_id(self):
        p_id = self.cleaned_data['p_id']
        existing_patient = Patient.objects.exclude(pk=self.instance.pk).filter(p_id=p_id)
        if existing_patient.exists():
            raise forms.ValidationError("Patient with this P id already exists.")
        return p_id

    def __init__(self, *args, **kwargs):
        super(PatientUpdateForm, self).__init__(*args, **kwargs)
        self.fields['p_id'].widget.attrs['readonly'] = True

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['d_id', 'name', 'age', 'contact', 'email', 'department']


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['p_id', 'name', 'age', 'contact', 'email', 'address', 'disease', 'treatment', 'doctor']

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        if Doctor.objects.all() is not None:
            self.fields['doctor'].queryset = Doctor.objects.all()


class DoctorUpdateForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['d_id', 'name', 'age', 'contact', 'email', 'department']


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['id', 'name']
