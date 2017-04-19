from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from django.db import transaction
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, \
DetailView, TemplateView

from .models import Appointment, Appointment_Date, Appointment_Time
from .forms import AppointmentDateFormSet, AppointmentTimeFormSet


class HomeView(TemplateView):
    template_name = "appointments/homepage.html"

@method_decorator(login_required, name='dispatch')
class AppointmentList(ListView):
    model = Appointment

class AppointmentDetail(DetailView):
    model = Appointment
    template_name = "appointments/appointment_detail.html"
    context_object_name = 'dates'


@method_decorator(login_required, name='dispatch')
class AppointmentCreate(CreateView):
    model = Appointment
    fields = ['title', 'description', 'info']

@method_decorator(login_required, name='dispatch')
class AppointmentDateTimeCreate(CreateView):
    model = Appointment
    fields = ['title', 'description', 'info']
    success_url = reverse_lazy('appointments')

    def get_context_data(self, **kwargs):
        data = super(AppointmentDateTimeCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['appointment_dates'] = AppointmentDateFormSet(self.request.POST)
            data['appointment_times'] = AppointmentTimeFormSet(self.request.POST)
        else:
            data['appointment_dates'] = AppointmentDateFormSet()
            data['appointment_times'] = AppointmentTimeFormSet()

        return data

    def form_valid(self, form):
        context = self.get_context_data()
        appointment_dates = context['appointment_dates']
        appointment_times = context['appointment_times']
        with transaction.atomic():
            self.object = form.save()

            if appointment_dates.is_valid() and appointment_times.is_valid():
                appointment_dates.instance = self.object
                appointment_dates.save()
                appointment_times.instance = self.object
                appointment_times.save()
        return super(AppointmentDateTimeCreate, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class AppointmentDateTimeUpdate(UpdateView):
    model = Appointment
    fields = ['title', 'description', 'info']
    success_url = reverse_lazy('appointments')

    def get_context_data(self, **kwargs):
        data = super(AppointmentDateTimeUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['appointment_dates'] = AppointmentDateFormSet(self.request.POST)
            data['appointment_times'] = AppointmenTimeFormSet(self.request.POST)
        else:
            data['appointment_dates'] = AppointmentDateFormSet(instance=self.object)
            data['appointment_times'] = AppointmentTimeFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        appointment_dates = context['appointment_dates']
        appointment_times = context['appointment_times']
        with transaction.atomic():
            self.object = form.save()

            if appointment_dates.is_valid() and appointment_times.is_valid():
                appointment_dates.instance = self.object
                appointment_dates.save()
                appointment_times.instance = self.object
                appointment_times.save()
        return super(AppointmentDateTimeUpdate, self).form_valid(form)


class AppointmentDelete(DeleteView):
    model = Appointment
    success_url = reverse_lazy('appointments')
