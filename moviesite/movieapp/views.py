import os

from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import Context, loader

from .models import Movie


def index(request):
    print(request)

    item_list = Movie.objects.all().order_by("-id")  # desc -id asc id
    print(item_list)
    template = loader.get_template('index.html')

    context = Context({
        'item_list': item_list,
        'item_count': len(item_list),
    })

    return HttpResponse(template.render(context))


def delete(request, item_id):
    print("start delete request")
    print("item_id : " + item_id)

    item = Movie.objects.get(pk=item_id).delete()
    print(item)

    print("end delete request")
    return redirect('/movie/')


def deleteAll(request):
    print("start deleteAll request")

    item = Movie.objects.all().delete()
    print(item)

    print("end deleteAll request")
    return redirect('/movie/')


#    return index(request)

def run(request):
    print("start run request")

    os.system("./scrapy.sh")

    print("end run request")
    return redirect('/movie/')

#    return index(request)
