from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^appointments/', views.AppointmentList.as_view(), name='appointments'),
    url(r'^(?P<pk>\d+)/$', views.appointment_application,
        name='appointment_detail'),
    url(r'^apply/(?P<pk>\d+)/$', views.appointment_application,
        name='appointment_application'),
    url(r'^add/$', views.AppointmentDateTimeCreate.as_view(),
        name='add_appointment'),
    url(r'^(?P<pk>\d+)/edit/$', views.AppointmentDateTimeUpdate.as_view(),
        name='edit_appointment'),
    url(r'^(?P<pk>\d+)/delete/$', views.AppointmentDelete.as_view(),
        name='delete_appointment'),
    ]
