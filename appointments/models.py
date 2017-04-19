from django.db import models

class Appointment(models.Model):

    class Meta(object):
        verbose_name="Appointment"
        verbose_name_plural="Appointments"

    title = models.CharField(
        max_length=200,
        blank=False,
        verbose_name="Appointment Title"
        )

    description = models.CharField(
        max_length=200,
        blank=False,
        verbose_name="Appointment Description"
        )

    info = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Aditional Info"
        )

    def __str__(self):
        return "%s" %(self.title)


class Appointment_Date(models.Model):

    class Meta(object):
        verbose_name="Appointment Date"
        verbose_name_plural="Appointment Dates"

    appointment = models.ForeignKey(
        Appointment,
        on_delete=models.CASCADE,
        related_name="dates",
        verbose_name="appointment"
        )

    app_date = models.DateField(
        blank=False,
        verbose_name="Appointment Date"
        )

    def __str__(self):
        return self.app_date.strftime("%B %d, %Y")

class Appointment_Time(models.Model):

    class Meta(object):
        verbose_name="Appointment Time"
        verbose_name_plural="Appointment Times"

    app_date = models.ForeignKey(
        Appointment_Date,
        on_delete=models.CASCADE,
        related_name="times",
        verbose_name="dates"
        )

    start_time = models.TimeField(
        blank=False,
        verbose_name="Appointment Start Time"
        )

    end_time = models.TimeField(
        blank=False,
        verbose_name="Appointment End Time"
        )

    def __str__(self):
        return "%s - %s" %(self.start_time.strftime("%H : %M"),
            self.end_time.strftime("%H : %M"))

class Appointment_Application(models.Model):

    class Meta(object):
        verbose_name="Appointment Application"
        verbose_name_plural="Appointment Applications"

    appointment = models.ForeignKey(
        Appointment,
        on_delete=models.CASCADE,
        related_name="applications",
        verbose_name="appointment"
        )

    app_date = models.ForeignKey(
        Appointment_Date,
        on_delete=models.CASCADE,
        related_name="applications",
        verbose_name="dates"
        )

    email = models.EmailField(
        blank=False,
        verbose_name="Email"
        )

    name = models.CharField(
        max_length=200,
        blank=False,
        verbose_name="Full Name"
        )

    def __str__(self):
        return "%s, %s, %s, %s" %(self.appointment,
            self.app_date.strftime("%B %d, %Y"),
            self.name,
            self.email)
