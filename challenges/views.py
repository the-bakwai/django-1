from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse

monthly_challenges = {
    "january": "No meat",
    "february": "Walk",
    "march": "django",
    "april": "No meat",
    "may": "Walk",
    "june": "django",
    "july": "No meat",
    "august": "Walk",
    "september": "django",
    "october": "No meat",
    "november": "Walk",
    "december": None
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {"months": months})


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound()

    redirect_path = reverse("month-challenge", args=[months[month - 1]])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {"text": challenge_text, "month_name": month})
    except:
        raise Http404()
