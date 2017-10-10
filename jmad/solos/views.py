from django.shortcuts import render, render_to_response
from django.views.generic import DetailView

from .models import Solo


def index(request):
    context = {'solos': []}
    if request.GET.keys():
        solos_queryset = Solo.objects.all()
        if request.GET.get('instrument', None):
            solos_queryset = solos_queryset.filter(
                instrument=request.GET.get(
                    'instrument',
                    None
                )
            )
        if request.GET.get('artist', None):
            solos_queryset = solos_queryset.filter(
                artist=request.GET.get('artist', None)
            )
        context['solos'] = solos_queryset
    return render(request, 'solos/index.html', context=context)


class SoloDetailView(DetailView):
    model = Solo