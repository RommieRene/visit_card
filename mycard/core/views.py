from django.shortcuts import render
from .models import VisitCard

def home(request):
    card = VisitCard.objects.first()  # or filter by user if needed
    return render(request, 'core/index.html', {
        'card': card
        })

