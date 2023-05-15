from django.shortcuts import render


# Create your views here.

def home_screen_view(request):
    data_list = ['hello, world', 'fuck u', 1818, 'AfterNumber']
    context = {'data_list': data_list}
    return render(request, 'home.html', context)
