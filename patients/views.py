from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import get_user_model

from accounts.forms import NurseUpdateForm
from .forms import PatientProfileForm, ScheduleVaccineForm
from .models import ScheduleVaccine
from accounts.models import PatientProfile
from vaccines.models import Vaccine

User = get_user_model()


def nurse_check(user):
    return not user.is_nurse and not user.is_admin


# include schedule
@login_required(login_url="accounts:login")
@user_passes_test(nurse_check, login_url="accounts:login")
def patient_info(request):
    user = request.user
    patientprofile = user.patientprofile
    vaccines = ScheduleVaccine.objects.filter(patient=patientprofile)
    vaccines_holding = ScheduleVaccine.objects.filter(
        patient=patientprofile, on_holding=True
    )
    context = {
        "profile": user,
        "vaccines": vaccines,
        "vaccines_holding": vaccines_holding,
    }
    return render(request, "patients/info.html", context)


@login_required(login_url="accounts:login")
@user_passes_test(nurse_check, login_url="accounts:login")
def patient_update(request):
    username = request.user.username
    profile = get_object_or_404(User, username=username)
    form = NurseUpdateForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect("patients:info")
    context = {"form": form, "profile": profile}
    return render(request, "patients/update.html", context)


@login_required(login_url="accounts:login")
@user_passes_test(nurse_check, login_url="accounts:login")
def patient_update_extra(request):
    user = request.user
    profile = get_object_or_404(PatientProfile, user=user)
    form = PatientProfileForm(
        request.POST or None, request.FILES or None, instance=profile
    )
    if form.is_valid():
        form.save()
        return redirect("patients:info")
    context = {"form": form, "profile": user}
    return render(request, "patients/update_extra.html", context)


## select time
## delete


@login_required(login_url="accounts:login")
@user_passes_test(nurse_check, login_url="accounts:login")
def patient_schedule_vaccine(request):
    user = request.user
    patientprofile = user.patientprofile
    vaccines = ScheduleVaccine.objects.filter(patient=patientprofile)
    vaccines_holding = ScheduleVaccine.objects.filter(
        patient=patientprofile, on_holding=True
    )
    form = ScheduleVaccineForm(request.POST or None)
    if form.is_valid():
        new = form.save(commit=False)
        new.patient = patientprofile
        new.save()
        get_vaccine = new.vaccine
        get_vaccine.in_holding += 1
        get_vaccine.available -= 1
        get_vaccine.save()

        # when nurse done -> holding false

        return redirect("patients:schedule_vaccine")

    context = {
        "form": form,
        "profile": user,
        "vaccines": vaccines,
        "vaccines_holding": vaccines_holding,
    }
    return render(request, "patients/schedule_vaccine.html", context)


@login_required(login_url="accounts:login")
@user_passes_test(nurse_check, login_url="accounts:login")
def patient_schedule_vaccine_delete(request, id):
    vaccine = get_object_or_404(ScheduleVaccine, id=id)
    vaccine.delete()
    return redirect("patients:schedule_vaccine")
