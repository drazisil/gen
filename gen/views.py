from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the main index. Visit <a href=\"/api\">the api</a>")
