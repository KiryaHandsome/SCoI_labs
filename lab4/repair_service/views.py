from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from account.models import Account
from cart.forms import CartAddProductForm
from repair_service.forms import ServiceForm
from repair_service.models import Service
import requests


def home_screen_view(request):
    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts

    return render(request, 'repair_service/home.html', context)


def page_not_found_handler(request, *args, **kwargs):
    return HttpResponseRedirect('/')


def service_list(request):
    services = Service.objects.all()
    joke_data = requests.get('https://official-joke-api.appspot.com/jokes/programming/random').json()[0]
    joke = joke_data['setup'] + joke_data['punchline']
    return render(request, 'repair_service/services.html', {
        'services': services,
        'joke': joke
    })


def edit_service(request, id):
    service = get_object_or_404(Service, id=id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'repair_service/create.html', {'form': form})


def create_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save()
            return redirect('/services/', pk=service.pk)
    else:
        form = ServiceForm()
    return render(request, 'repair_service/create.html', {'form': form})


def delete_service(request, id):
    service = Service.objects.get(id=id)
    service.delete()
    return redirect('service_list')


def service_detail(request, id):
    service = get_object_or_404(Service, id=id)
    cart_service_form = CartAddProductForm()
    return render(request, 'repair_service/detail.html', {
        'service': service,
        'cart_service_form': cart_service_form
    })
