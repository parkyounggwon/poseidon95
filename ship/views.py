from django.shortcuts import render
from django.core.paginator import Paginator
from .models import AaShip
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.


def index(request):
    print("ship의 views의 index호출됨")
    page = request.GET.get('page', 1)
    ship_list = AaShip.objects.order_by('-ship_name')
    paginator = Paginator(ship_list, 5)
    page_obj = paginator.get_page(page)
    context = {'ship_list': page_obj}
    print("ship의 views의 index호출됨 2")
    return render(request, 'ship/google_api.html', context)


def detail(request):
    print("ship의 views의 detail 호출됨 ")
    # get_object_or_404()는 요청 글번호 내용이 존재하지 않을 경우 오류를 404로 처리
    # s = Ship.objects.get(id=ship_id)
    ship_name = AaShip.ship_name;
    s = get_object_or_404(AaShip, ship_name=ship_name)
    context = {'ship': s}
    return render(request, 'ship/ship_detail.html', context)


def maps_multi(request):
    address_list = AaShip.objects.filter(ship_port='ship_port').distinct()
    address_list1 = address_list[0:3]  # temporarily select first three addresses from list to test

    geolocator = GoogleV3()

    add_list = []
    for x in address_list1:
         add_city = x.city
         location = geolocator.geocode(add_city)
         add_list.append(location)
         print(add_list)

    context = {'location': add_list}

    return render(request, 'ship/google_api.html', context)