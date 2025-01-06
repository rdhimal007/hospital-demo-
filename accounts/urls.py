from django.urls import path

from . import views


app_name = "accounts"

urlpatterns = [
    path("", views.home, name="home"),
    # Authenticated
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("register/", views.patient_register, name="register"),
    # Admin Control Nurses
    path("admin_panel/nurses/", views.admin_nurses_list, name="admin_nurses"),
    path("admin_panel/new_nurse/", views.admin_nurses_add_new, name="new_nurse"),
    path(
        "admin_panel/edit/<str:username>",
        views.admin_nurses_update,
        name="nerse_update",
    ),
    path(
        "admin_panel/delete/<str:username>",
        views.admin_nurses_delete,
        name="nerse_delete",
    ),
    path(
        "admin_panel/nurse/details/<str:username>",
        views.admin_nurse_details,
        name="nurse_details",
    ),
    # Admin Control Vaccines
    path("admin_panel/vaccines/", views.admin_vaccines_list, name="admin_vaccines"),
    path(
        "admin_panel/vaccines/add", views.admin_vaccines_add, name="admin_vaccine_add"
    ),
    path(
        "admin_panel/vaccines/update/<str:slug>",
        views.admin_vaccines_update,
        name="admin_vaccine_update",
    ),
    path(
        "admin_panel/vaccines/delete/<str:slug>",
        views.admin_vaccines_delete,
        name="admin_vaccines_delete",
    ),
    # Patients
    path("admin_panel/patients/", views.admin_patients_list, name="admin_patients"),
    path(
        "admin_panel/patients/<str:username>",
        views.admin_patients_details,
        name="admin_patients_details",
    ),
]
