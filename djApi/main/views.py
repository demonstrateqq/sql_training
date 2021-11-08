from django.shortcuts import render
from .models import Auto, Brand, Detail


def home_page(request):
    auto = Auto.objects.filter(pk=1)
    print(auto.query)
    print(auto[0].brand)
    # print(dir(Auto.objects))
    context = {'auto': auto}
    return render(request, 'main/index.html', context)
