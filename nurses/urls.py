from django.urls import path

from . import views

app_name = "nurses"


urlpatterns = [
    path("profile/", views.nurse_info, name="info"),
    path("profile/update/", views.nurse_update, name="update"),
    path("profile/add/schedule", views.nurse_add_schedule, name="add_schedule"),
    path(
        "profile/add/schedule/action/<str:id>",
        views.add_schedule_action,
        name="add_schedule_action",
    ),
    path("profile/my_schedule/", views.my_schedule, name="my_schedule"),
    path(
        "profile/my_schedule/delete_me/<str:id>",
        views.my_schedule_delete_me,
        name="delete_me",
    ),
    path(
        "profile/my_schedule/completed",
        views.my_schedule_completed,
        name="my_schedule_completed",
    ),
    path(
        "profile/my_schedule/my_schedule_set_completed/<str:id>",
        views.my_schedule_set_completed,
        name="my_schedule_set_completed",
    ),
]
