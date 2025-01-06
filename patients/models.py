from django.db import models
from django.conf import settings
from django.utils import timezone

from vaccines.models import Vaccine
from accounts.models import PatientProfile

User = settings.AUTH_USER_MODEL


class ScheduleVaccine(models.Model):
    nurse = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"is_nurse": True},
    )
    patient = models.ForeignKey(
        PatientProfile,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    vaccine = models.ForeignKey(
        Vaccine,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"availability": True},
    )
    schedule_date = models.DateField()
    schedule_time = models.TimeField()
    on_holding = models.BooleanField(default=True)

    # PatientX received dose 1 of Pfizer, by NurseY at me-slot
    def __str__(self):
        return f"{str(self.patient.user.username)} received dose 1 of {self.vaccine}, by {str(self.nurse)}"
