from django.shortcuts import render

from demo_app.models import News


def index(request):
    objs = News.objects.all().order_by('-id')
    context = {
        'objs': objs,
    }
    return render(request, 'home_page.html', context)
