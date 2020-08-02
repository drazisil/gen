from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
def index(request):
    context = {}
    return render(request, 'api/index.html', context)


def pony(request):
    context = {}
    return render(request, 'api/pony.html', context)


def pony_lookup(request):
    pony_id: str = request.POST['pony']
    if int(pony_id) <= 0 or pony_id is None:
        return HttpResponse('The pony id must be a number greater then 0.', status=500)
    return HttpResponseRedirect(reverse('api:fetch_pony', args=(pony_id, )))


def fetch_pony(request, pony_id):
    if int(pony_id) <= 0 or pony_id is None:
        return HttpResponse('The pony id must be a number greater then 0.', status=500)
    return HttpResponse("You're looking at pony %s." % pony_id)
