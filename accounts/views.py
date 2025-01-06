from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

from .forms import RegisterForm, NurseUpdateForm
from vaccines.models import Vaccine
from vaccines.forms import VaccineForm
from patients.models import ScheduleVaccine
from .models import PatientProfile

User = get_user_model()


def home(request):
    context = {}
    return render(request, "home.html", context)


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        get_user = User.objects.filter(username__iexact=username).distinct()
        if not get_user.exists() and get_user.count() != 1:
            messages.error(request, "This User Doesn't Exist")
            return redirect("accounts:login")

        user = get_user.first()

        if not user.check_password(password):
            messages.error(request, "Wrong Password")
            return redirect("accounts:login")

        user_login(request, user)
        return redirect("accounts:home")

    context = {}
    return render(request, "accounts/login.html", context)


def logout(request):
    user_logout(request)
    messages.success(request, "Back Soon!")
    return redirect("accounts:login")


def patient_register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("accounts:login")

    context = {"form": form}
    return render(request, "accounts/register.html", context)


def admin_check(user):
    return user.is_admin


@login_required(login_url="accounts:login")
@user_passes_test(admin_check, login_url="accounts:login")  ## will be profile
def admin_nurses_list(request):
    nurses = User.objects.filter(is_nurse=True)
    count_nurses = nurses
    context = {"nurses": nurses, "count_nurses": nurses.count()}
    return render(request, "admin/nurses_list.html", context)


@login_required(login_url="accounts:login")
@user_passes_test(admin_check, login_url="accounts:login")  ## will be profile
def admin_nurses_add_new(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        new_nurse = form.save(commit=False)
        new_nurse.is_nurse = True
        new_nurse.save()
        return redirect("accounts:admin_nurses")
    context = {"form": form}
    return render(request, "admin/nurses_new.html", context)


@login_required(login_url="accounts:login")
@user_passes_test(admin_check, login_url="accounts:login")  ## will be profile
def admin_nurses_update(request, username):
    nurse = get_object_or_404(User, username=username)
    form = NurseUpdateForm(request.POST or None, instance=nurse)
    if form.is_valid():
        form.save()
        return redirect("accounts:admin_nurses")
    context = {"form": form, "nurse": nurse}
    return render(request, "admin/nurses_update.html", context)


@login_required(login_url="accounts:login")
@user_passes_test(admin_check, login_url="accounts:login")  ## will be profile
def admin_nurses_delete(request, username):
    nurse = get_object_or_404(User, username=username)
    nurse.delete()
    return redirect("accounts:admin_nurses")


@login_required(login_url="accounts:login")
@user_passes_test(admin_check, login_url="accounts:login")
def admin_nurse_details(request, username):
    nurse = get_object_or_404(User, username=username)

    schedule_compeleted = ScheduleVaccine.objects.filter(nurse=nurse, on_holding=False)
    schedule_compeleted_count = schedule_compeleted.count()

    schedule_on_hold = ScheduleVaccine.objects.filter(nurse=nurse, on_holding=True)
    schedule_on_hold_count = schedule_on_hold.count()

    context = {
        "profile": nurse,
        "schedule_compeleted": schedule_compeleted,
        "schedule_on_hold": schedule_on_hold,
        "schedule_compeleted_count": schedule_compeleted_count,
        "schedule_on_hold_count": schedule_on_hold_count,
    }
    return render(request, "admin/nurse_details.html", context)


@login_required(login_url="accounts:login")
@user_passes_test(admin_check, login_url="accounts:login")  ## will be profile
def admin_vaccines_list(request):
    vaccines = Vaccine.objects.all()

    context = {"vaccines": vaccines, "vaccines_count": vaccines.count()}
    return render(request, "admin/vaccines_list.html", context)


@login_required(login_url="accounts:login")
@user_passes_test(admin_check, login_url="accounts:login")  ## will be profile
def admin_vaccines_add(request):
    form = VaccineForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("accounts:admin_vaccines")

    context = {"form": form}
    return render(request, "admin/vaccines_add.html", context)


@login_required(login_url="accounts:login")
@user_passes_test(admin_check, login_url="accounts:login")  ## will be profile
def admin_vaccines_update(request, slug):
    vaccine = get_object_or_404(Vaccine, slug=slug)
    form = VaccineForm(request.POST or None, instance=vaccine)
    if form.is_valid():
        form.save()
        return redirect("accounts:admin_vaccines")

    context = {"form": form, "vaccine": vaccine}
    return render(request, "admin/vaccines_update.html", context)


@login_required(login_url="accounts:login")
@user_passes_test(admin_check, login_url="accounts:login")
def admin_vaccines_delete(request, slug):
    vaccine = get_object_or_404(Vaccine, slug=slug)
    vaccine.delete()
    return redirect("accounts:admin_vaccines")


@login_required(login_url="accounts:login")
@user_passes_test(admin_check, login_url="accounts:login")
def admin_patients_list(request):
    patients = User.objects.filter(is_nurse=False, is_admin=False)

    context = {"patients": patients, "count": patients.count()}
    return render(request, "admin/patients_list.html", context)


@login_required(login_url="accounts:login")
@user_passes_test(admin_check, login_url="accounts:login")
def admin_patients_details(request, username):
    user = User.objects.get(username=username)
    profile = user.patientprofile
    schedule_compeleted = ScheduleVaccine.objects.filter(
        patient=profile, on_holding=False
    )
    schedule_compeleted_count = schedule_compeleted.count()

    schedule_on_hold = ScheduleVaccine.objects.filter(patient=profile, on_holding=True)
    schedule_on_hold_count = schedule_on_hold.count()

    context = {
        "profile": user,
        "schedule_compeleted": schedule_compeleted,
        "schedule_on_hold": schedule_on_hold,
        "schedule_compeleted_count": schedule_compeleted_count,
        "schedule_on_hold_count": schedule_on_hold_count,
    }
    return render(request, "admin/patients_details.html", context)
