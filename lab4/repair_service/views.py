from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from account.models import Account
from repair_service.forms import ServiceForm
from repair_service.models import Service


def home_screen_view(request):
    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts

    return render(request, 'repair_service/home.html', context)


def page_not_found_handler(request, *args, **kwargs):
    return HttpResponseRedirect('/')


def service_list(request):
    services = Service.objects.all()
    return render(request, 'repair_service/services.html', {'services': services})


def edit_service(request):
    pass


def create_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save()
            return redirect('/services/', pk=service.pk)
    else:
        form = ServiceForm()
    return render(request, 'repair_service/create.html', {'form': form})


def delete_service(request):
    pass
