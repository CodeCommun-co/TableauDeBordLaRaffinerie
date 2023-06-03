from django.shortcuts import render


def follow_event(request):
    return render(request, 'events/events.html', {})


def goals_and_results(request):
    return render(request, 'goals/goals.html', {})


def follow_volunteering(request):
    return render(request, 'events/volunteering.html', {})

