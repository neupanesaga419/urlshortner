from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse
from .models import ShortURL

def shorten_url(request):
    context = {}
    if request.method == 'POST':
        original_url = request.POST.get('url')
        if original_url:
            short = ShortURL.objects.create(original_url=original_url)
            context['short_url'] = request.build_absolute_uri(
                reverse('redirect_url', args=[short.short_code])
            )
    return render(request, 'shorten.html', context)

def redirect_url(request, code):
    short = get_object_or_404(ShortURL, short_code=code)
    return redirect(short.original_url)
