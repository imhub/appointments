from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from django.db import transaction
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, \
DetailView, TemplateView

from .models import Appointment, Appointment_Date, Appointment_Time, Appointment_Application
from .forms import AppointmentDateFormSet, Appointment_ApplicationForm


class HomeView(TemplateView):
    template_name = "appointments/homepage.html"

@method_decorator(login_required, name='dispatch')
class AppointmentList(ListView):
    model = Appointment

# class AppointmentDetail(DetailView):
#     model = Appointment
#     template_name = "appointments/appointment_detail.html"
#     context_object_name = 'dates'

def appointment_detail(request, pk):
    app = get_object_or_404(Appointment, pk=pk)
    dates = Appointment_Date.objects.filter(appointment=app).order_by('app_date')
    applications = Appointment_Application.objects.all()
    return render(request, 'appointments/appointment_detail.html',
        {
        'app': app,
        'dates': dates,
        'applications': applications
        }
        )

def appointment_application(request, pk):
    app = get_object_or_404(Appointment, pk=pk)
    dates = Appointment_Date.objects.filter(appointment=app).order_by('app_date')
    if request.method == "POST":
        form = Appointment_ApplicationForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                form.save()
            return reverse_lazy('home')
    else:
        form = Appointment_ApplicationForm()

    return render(request, 'appointments/appointment_detail.html',
        {
        'app': app,
        'dates': dates
        }
        )

class ApplicationCreate(CreateView):
    model = Appointment
    fields = ['title', 'description', 'info']

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
        else:
            data['appointment_dates'] = AppointmentDateFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        appointment_dates = context['appointment_dates']
        with transaction.atomic():
            self.object = form.save()

            if appointment_dates.is_valid():
                appointment_dates.instance = self.object
                appointment_dates.save()
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
        else:
            data['appointment_dates'] = AppointmentDateFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        appointment_dates = context['appointment_dates']
        with transaction.atomic():
            self.object = form.save()

            if appointment_dates.is_valid():
                appointment_dates.instance = self.object
                appointment_dates.save()
        return super(AppointmentDateTimeUpdate, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class AppointmentDelete(DeleteView):
    model = Appointment
    success_url = reverse_lazy('appointments')
