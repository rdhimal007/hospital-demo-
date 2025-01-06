from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import get_user_model

from accounts.forms import NurseUpdateForm, NurseUpdateDetails
from patients.models import ScheduleVaccine
from vaccines.models import Vaccine

User = get_user_model()


def nurse_check(user):
    return user.is_nurse


# include schedule
@login_required(login_url="accounts:login")
@user_passes_test(nurse_check, login_url="accounts:login")
def nurse_info(request):
    user = request.user
    schedules = ScheduleVaccine.objects.filter(nurse=user, on_holding=False)
    schedule_compeleted = schedules[0:5]
    schedule_compeleted_count = schedule_compeleted.count()
    schedules_on_hold_all = ScheduleVaccine.objects.filter(nurse=user, on_holding=True)
    schedule_on_hold = schedules_on_hold_all[0:5]
    schedule_on_hold_count = schedules_on_hold_all.count()
    context = {
        "profile": user,
        "schedule_compeleted": schedule_compeleted,
        "schedule_on_hold": schedule_on_hold,
        "schedule_compeleted_count": schedule_compeleted_count,
        "schedule_on_hold_count": schedule_on_hold_count,
    }
    return render(request, "nurses/info.html", context)


@login_required(login_url="accounts:login")
@user_passes_test(nurse_check, login_url="accounts:login")
def nurse_update(request):
    username = request.user.username
    profile = get_object_or_404(User, username=username)
    form = NurseUpdateDetails(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect("nurses:info")
    context = {"form": form, "profile": profile}
    return render(request, "nurses/update.html", context)


@login_required(login_url="accounts:login")
@user_passes_test(nurse_check, login_url="accounts:login")
def nurse_add_schedule(request):
    user = request.user
    schedules = ScheduleVaccine.objects.filter(nurse=None)
    context = {"schedules": schedules, "profile": user}
    return render(request, "nurses/add_schedule.html", context)


@login_required(login_url="accounts:login")
@user_passes_test(nurse_check, login_url="accounts:login")
def add_schedule_action(request, id):
    user = request.user
    schedule = ScheduleVaccine.objects.get(id=id)
    schedule.nurse = user
    schedule.save()
    return redirect("nurses:add_schedule")


@login_required(login_url="accounts:login")
@user_passes_test(nurse_check, login_url="accounts:login")
def my_schedule(request):
    user = request.user
    schedules = ScheduleVaccine.objects.filter(nurse=user, on_holding=True)
    context = {"schedules": schedules}
    return render(request, "nurses/my_schedule.html", context)


@login_required(login_url="accounts:login")
@user_passes_test(nurse_check, login_url="accounts:login")
def my_schedule_set_completed(request, id):
    user = request.user
    schedule = ScheduleVaccine.objects.get(id=id, nurse=user)
    schedule.on_holding = False

    vannice = Vaccine.objects.get(id=schedule.vaccine.id)
    vannice.in_holding -= 1
    vannice.save()

    schedule.save()
    return redirect("nurses:my_schedule")


@login_required(login_url="accounts:login")
@user_passes_test(nurse_check, login_url="accounts:login")
def my_schedule_delete_me(request, id):
    user = request.user
    schedule = ScheduleVaccine.objects.get(id=id, nurse=user)
    schedule.nurse = None
    schedule.save()
    return redirect("nurses:my_schedule")


@login_required(login_url="accounts:login")
@user_passes_test(nurse_check, login_url="accounts:login")
def my_schedule_completed(request):
    user = request.user
    schedules = ScheduleVaccine.objects.filter(nurse=user, on_holding=False)
    context = {"schedules": schedules}
    return render(request, "nurses/my_schedule_completed.html", context)

    # context = {}
    # return render(request, "")


# set competeed
#   -  holding - 1


"""
    - compeleted
    - my scudle
"""
