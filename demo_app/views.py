from django.shortcuts import render, redirect

from demo_app.models import News


def index(request):
    objs = News.objects.all().order_by('-id')
    context = {
        'objs': objs,
    }
    return render(request, 'home_page.html', context)


from googletrans import Translator


# https://pypi.org/project/googletrans/

def save_news(request):
    title = request.POST.get('title')
    text = request.POST.get('text')
    translator = Translator()

    try:
        title_mr = translator.translate(title, dest='mr').text
        title_ur = translator.translate(title, dest='ur').text

        text_mr = translator.translate(text, dest='mr').text
        text_ur = translator.translate(text, dest='ur').text
        News.objects.create(title_en=title, title_mr=title_mr, title_ur=title_ur, text_en=text, text_mr=text_mr,
                            text_ur=text_ur)
    except:
        pass
    return redirect('/')
