from django.shortcuts import render, render_to_response

from .models import Solo


def index(request):
    context = {'solos': Solo.objects.filter(
        instrument=request.GET.get('instrument', None)
    )}
    return render(request, 'solos/index.html', context=context)
