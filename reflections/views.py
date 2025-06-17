from django.shortcuts import render
from .models import GospelReflection, SundayInfo

def index(request):
    sunday = SundayInfo.objects.last()
    reflection = GospelReflection.objects.filter(sunday_info=sunday).last()
    return render(request, 'index.html', {
        'sunday': sunday,
        'reflection': reflection,
    })
