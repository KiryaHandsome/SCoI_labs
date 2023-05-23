from django.http import HttpResponseRedirect
from django.shortcuts import render

from account.models import Account
from repair_service.models import Service


def home_screen_view(request):
    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts

    return render(request, 'home.html', context)


def page_not_found_handler(request, *args, **kwargs):
    return HttpResponseRedirect('/')


def service_list(request):
    content = Service.objects.all()
    return render(request, 'repair_service/home.html')

def edit_service(request):
    pass


def create_service(request):
    pass


def delete_service(request):
    pass
