from django.forms import ModelForm, inlineformset_factory

from .models import Appointment, Appointment_Date, Appointment_Time, Appointment_Application


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        exclude = ()

class Appointment_DateForm(ModelForm):
    class Meta:
        model = Appointment_Date
        exclude = ()

class Appointment_TimeForm(ModelForm):
    class Meta:
        model = Appointment_Time
        exclude = ()

AppointmentDateFormSet = inlineformset_factory(Appointment, Appointment_Date,
                                            form=Appointment_DateForm, extra=1)

AppointmentTimeFormSet = inlineformset_factory(Appointment_Date, Appointment_Time,
                                            form=Appointment_TimeForm, extra=1)

class Appointment_ApplicationForm(ModelForm):
    class Meta:
        model = Appointment_Application
        fields = ('appointment', 'app_date', 'name', 'email',)
