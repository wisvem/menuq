from django.http import HttpResponse
from django.views import View
from apps.companies.models.company import Company


def detail(request, menu_id):
    return HttpResponse("You're looking at menu %s." % menu_id)


def results(request, menu_id):
    response = "You're looking at the results of menu %s."
    return HttpResponse(response % menu_id)


def create(request, menu_id):
    return HttpResponse("You're on menu %s." % menu_id)

class IndexView(View):
    def get(self, request):
        return HttpResponse(
            Company.objects.all()
        )
