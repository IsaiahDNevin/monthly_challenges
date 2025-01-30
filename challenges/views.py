from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
    "january": "Eat only meat for the entire month!",
    "february": "Walk for 20 minutes every day",
    "march": "Complete 100 push-ups at once!.",
    "april": "Do 50 burpees in one session!",
    "may": "complete 200 bodyweight squats in 2 sets!",
    "june": "Run a mile as fast as you can.",
    "july": "Complete 3 rounds of 20 push-ups, 20 squats, and 20 mountain climbers.",
    "august": "Touch your toes and hold for 2 minutes.",
    "september": "Hold a handstand against a wall for 1 minute.",
    "october": "Ride a challenging trail in under a specific time.",
    "november": "Shadowbox for 5 minutes without rest.",
    "december": None

}

# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])  #/challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        raise Http404()
    
