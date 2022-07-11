from django.shortcuts import render

from django.core.paginator import Paginator
from .models import AaPort
from .models import AaCargo
from .models import AaOrder

from django.shortcuts import render, get_object_or_404, redirect
import json
import datetime, json
from decimal import *
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from decimal import Decimal
# import sys
# sys.path.append(".")

# Create your views here.
from ship.models import AaShip

ship_list2 = AaShip.objects.order_by('-ship_name')
port_list2 = AaPort.objects.order_by('-port')
ship2 =[]

# print('port_list[0].port : ', port_list2[0].port)
# print('ship_list[0].ship_port :', ship_list2[0].ship_port)

for ship in ship_list2:
    ship3 = []
    for port in port_list2:
        if port.port == ship.ship_port :
         #   print('ship_port:',ship.ship_port,' ','port:', port.port,port.latitude,port.longitude)
            ship3.append(ship.ship_name)
            ship3.append(ship.deadweight)
            ship3.append(ship.built)
            ship3.append(ship.ship_date)
            ship3.append(ship.ship_port)
            ship3.append(port.port)
            ship3.append(port.latitude)
            ship3.append(port.longitude)
    ship2.append(ship3)

#print('ship2 :', ship2)

def index(request):
    # page = request.GET.get('page', 1)
    # port_list = AaPort.objects.order_by('-port')
    # paginator = Paginator(port_list, 5)
    # page_obj = paginator.get_page(page)
    # context = {'port_list': page_obj}
    #
    # ship_list = AaShip.objects.order_by('-ship_name')
    # port_list = AaPort.objects.order_by('-port')

     # for ship in ship_list:
     #    print('ship.ship_port : ', ship.ship_port)
     #    for port in port_list:
     #        if port.port == ship.ship_port:
     #            ship.append(port_list.port, port_list.latitude, port_list.longitude)

    # print('port_list[0].port : ', port_list[0].port)
    # print('ship_list[0].ship_port :', ship_list[0].ship_port)

    ship_locations = [
        [s.ship_name, s.deadweight, s.built, s.ship_date, s.ship_port,p.port, p.latitude, p.longitude, i]
        for i, s in enumerate(AaShip.objects.all())
            for j, p in enumerate(AaPort.objects.all())
                if s.ship_port == p.port
    ]

    context = {'ship_locations': json.dumps(ship_locations, default=str)}
    #print("context : ",context)

    return render(request, 'ship/port_ship.html', context)

def index_ship(request):
    ship_size_text = request.POST.get('ship_size')
    print('ship_size_text :',ship_size_text)
    print(type(ship_size_text))

    ship_built_text = request.POST.get('ship_built')
    ship_built_start = ship_built_text
    today = datetime.now()
    start_date_year = today - relativedelta(years = int(ship_built_text))
    print('start_date_year : ', start_date_year)

    ship_date_start_text = request.POST.get('ship_date_start')
    ship_date_end_text = request.POST.get('ship_date_end')
    print('ship_date_start_text : ' , ship_date_start_text)

    ship_area_text = request.POST.get('ship_area')
    print('ship_area_text :' ,ship_area_text)

    if request.method == 'POST':
        ship_locations = [
            [s.ship_name, s.deadweight, s.built, s.ship_date, s.ship_port, p.port, p.latitude, p.longitude, i]
            for i, s in enumerate(AaShip.objects.filter(
                    deadweight__range=(ship_size_text, int(ship_size_text)+10000),
                    built__range=(start_date_year, today),
                    ship_date__range=(ship_date_start_text, ship_date_end_text)
            ))
                for j, p in enumerate(AaPort.objects.filter(area = ship_area_text ))
                    if s.ship_port == p.port
        ]

        context = {'ship_locations': json.dumps(ship_locations, default=str),
            'ship_size_text': json.dumps(ship_size_text, default=str),
            'ship_built_text': json.dumps(ship_built_text, default=str),
            'ship_date_start_text': json.dumps(ship_date_start_text, default=str),
            'ship_date_end_text': json.dumps(ship_date_end_text, default=str),
            'ship_area_text': json.dumps(ship_area_text, default=str), }
        return render(request, 'ship/port_ship.html', context)

    else:
        context = {
                   'ship_size_text': json.dumps(ship_size_text, default=str),
                   'ship_built_text': json.dumps(ship_built_text, default=str),
                   'ship_date_start_text': json.dumps(ship_date_start_text, default=str),
                   'ship_date_end_text': json.dumps(ship_date_end_text, default=str),
                   'ship_area_text': json.dumps(ship_area_text, default=str), }
        return render(request, 'ship/port_ship.html', context)

def index_cargo(request):
    cargo_area_text = request.POST.get('cargo_area')
    cargo_size_text = request.POST.get('cargo_size')

    print('cargo_area_text : ', cargo_area_text)
    print('cargo_size_text type :', type(cargo_size_text))

    # cargo_size_start = int(cargo_size_text)
    # cargo_size_end = cargo_size_start+9999

    print('cargo_size_text :', cargo_size_text)

    cargo_date_start_text = request.POST.get('cargo_date_start')
    cargo_date_end_text = request.POST.get('cargo_date_end')
    print('cargo_date_start_text', cargo_date_start_text)

    if request.method == 'POST':

        cargo_locations = [
            [c.cargo_name, c.cargo_quantity, c.cargo_laydate, c.cargo_canceldate, c.cargo_loadingport,
                c.cargo_dischargingport, c.cargo_seq, p.port, p.latitude, p.longitude, i]
            for i, c in enumerate(AaCargo.objects.filter(
                    cargo_quantity__range=(cargo_size_text, int(cargo_size_text)+10000),
                    cargo_laydate__range=(cargo_date_start_text, cargo_date_end_text)
                ))
                for j, p in enumerate(AaPort.objects.filter(area = cargo_area_text ))
                    if c.cargo_loadingport == p.port
        ]

        print('cargo_locations :',cargo_locations)

        context = {'cargo_locations': json.dumps(cargo_locations, default=str),
                   'cargo_size_text': json.dumps(cargo_size_text, default=str),
                   'cargo_date_start_text': json.dumps(cargo_date_start_text, default=str),
                   'cargo_date_end_text': json.dumps(cargo_date_end_text, default=str),
                   'cargo_area_text': json.dumps(cargo_area_text, default=str) }

        return render(request, 'ship/port_cargo.html', context)

    else:
        context = {
                   'cargo_size_text': json.dumps(cargo_size_text, default=str),
                   'cargo_date_start_text': json.dumps(cargo_date_start_text, default=str),
                   'cargo_date_end_text': json.dumps(cargo_date_end_text, default=str),
                   'cargo_area_text': json.dumps(cargo_area_text, default=str)}

        return render(request, 'ship/port_cargo.html', context)

def index_order(request):
    print("index_order")
    order_area_text = request.POST.get('order_area')
    order_size_text = request.POST.get('order_size')
    print('order_size_text :', order_size_text)
    order_date_start_text = request.POST.get('order_date_start')
    order_date_end_text = request.POST.get('order_date_end')

    if request.method == 'POST':
        order_locations = [
            [o.order_cargo, o.order_quantity, o.order_laydate, o.order_canceldate, o.order_loading_area,
                o.order_discharging_area, o.order_seq, p.port, p.latitude, p.longitude, i]
            for i, o in enumerate(AaOrder.objects.filter(
                order_quantity__range=(order_size_text, int(order_size_text) + 10000),
                order_laydate__range=(order_date_start_text, order_date_end_text)
                ))
                for j, p in enumerate(AaPort.objects.filter(area = order_area_text) )
                    if o.order_loading_area == p.port
        ]
        context = {'order_locations': json.dumps(order_locations, default=str),
                   'order_size_text': json.dumps(order_size_text, default=str),
                   'order_date_start_text': json.dumps(order_date_start_text, default=str),
                   'order_date_end_text': json.dumps(order_date_end_text, default=str),
                   'order_area_text': json.dumps(order_area_text, default=str)}
        return render(request, 'ship/port_order.html', context)
    else:
        context = {
            'order_size_text': json.dumps(order_size_text, default=str),
            'order_date_start_text': json.dumps(order_date_start_text, default=str),
            'order_date_end_text': json.dumps(order_date_end_text, default=str),
            'order_area_text': json.dumps(order_area_text, default=str)}
        return render(request, 'ship/port_order.html', context)

def port_ship_list(request, port):

    inputPort = request.POST.get('port')

    port_ship_list = [
        [s.ship_name, s.deadweight, s.built, s.ship_date]
        for i, s in enumerate(AaShip.objects.filter(ship_port__contains= inputPort))
        #
        # [s.ship_name, s.deadweight, s.built, s.ship_date]
        # for i, s in enumerate(AaShip.objects.all())
        #     # built == s.built.slice(2, 4)
        #     # ship_date == s.ship_date.slice(5, 10)
        #     for j, p in enumerate(AaPort.objects.all())
        #         if  s.ship_port == p.port and p.port == port
    ]

    context = {'port_ship_list': json.dumps(port_ship_list, default=str)}
    print("context : ",context)
    print('port_ship_list :',port_ship_list)
    return render(request, 'ship/port_ship.html', context)


def test(request):
    ship_size_text = request.GET.get('ship_size')
    print('ship_size_text : ', ship_size_text)