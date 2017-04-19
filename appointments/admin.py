# from django.contrib import admin
# from .models import Appointment, Appointment_Date, Appointment_Time
#
#
# class Appointment_TimesInLine(admin.TabularInline):
#     model=Appointment_Time
#     extra = 0
#
# class Appointment_DatesInLine(admin.TabularInline):
#     model=Appointment_Date
#     extra = 0
#     inlines = [
#         Appointment_TimesInLine
#         ]
#
# @admin.register(Appointment)
#
# class AppointmentAdmin(admin.ModelAdmin):
#     list_display = ("title",)
#     search_fields = ["appointment__title"]
#     inlines = [
#         Appointment_DatesInLine
#         ]
#
#
# # Register your models here.
#
#
#
#
#
#
# """
# from django.contrib import admin
# from .models import Album, BuyLinks
#
# class BuyLinksInLine(admin.TabularInline):
#     model=BuyLinks
#     extra = 0
#
# @admin.register(Album)
#
# class AlbumAdmin(admin.ModelAdmin):
#
#     list_display = ("app_date", '_buylinks')
#
#     search_fields = ["album__title"]
#
#     inlines = [
#         BuyLinksInLine
#     ]
#
#     def _buylinks(self, obj):
#         return obj.buylinks.all().count()"""
