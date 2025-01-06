from django.urls import path

from . import views

app_name = "patients"


urlpatterns = [
    path("profile/", views.patient_info, name="info"),
    path("profile/update", views.patient_update, name="update"),
    path("profile/update/extra", views.patient_update_extra, name="update_extra"),
    path(
        "profile/schedule_vaccine/",
        views.patient_schedule_vaccine,
        name="schedule_vaccine",
    ),
    path(
        "profile/schedule_vaccine/<int:id>",
        views.patient_schedule_vaccine_delete,
        name="schedule_vaccine_delete",
    ),
]
