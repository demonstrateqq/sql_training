from django.shortcuts import render
from .models import Auto, Brand, Detail


def home_page(request):
    auto = Auto.objects.filter()
    print(Auto.objects)
    print(dir(Auto.objects))
    context = {}
    return render(request, 'main/index.html', context)
