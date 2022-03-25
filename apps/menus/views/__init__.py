from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the menuQ index.")


def detail(request, menu_id):
    return HttpResponse("You're looking at menu %s." % menu_id)


def results(request, menu_id):
    response = "You're looking at the results of menu %s."
    return HttpResponse(response % menu_id)


def create(request, menu_id):
    return HttpResponse("You're on menu %s." % menu_id)
