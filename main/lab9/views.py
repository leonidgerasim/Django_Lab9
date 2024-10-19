from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Employee, Waybill, Driver, Automobile
from django.db.models import Sum, Q, Count
from .forms import WaybillForm

# Create your views here.


def index(request):
    drivers = Waybill.objects.values('driver').annotate(sum_milage=Sum('milage'))
    context = {'title': 'Главная',
               'drivers': drivers}
    return render(request, 'lab9/index.html', context)


def create_waybill(request):
    error = ''
    if request.method == 'POST':
        form = WaybillForm(data=request.POST)
        post = request.POST
        un_auto = Waybill.objects.filter(departure_time__gte=post['departure_time'],
                                         check_in_time__lte=post['check_in_time'])
        m = []
        d = []
        for a in un_auto:
            m.append(a.automobile)
            d.append(a.driver)
        driver = Employee.objects.get(id=int(post['driver']))
        auto = Driver.objects.filter(Q(driver=driver) & ~Q(automobile__in=m) & ~Q(driver__in=d))
        if form.is_valid() and auto.first() is not None:
            waybill = Waybill(driver=driver, automobile=auto.first().automobile,
                              departure_time=post['departure_time'], check_in_time=post['check_in_time'],
                              initial_mileage=post['initial_mileage'], final_milage=post['final_milage'],
                              milage=int(post['final_milage']) - int(post['initial_mileage']),
                              consumption=(int(post['final_milage']) - int(post['initial_mileage'])) * auto.first().automobile.consumption)
            waybill.save()
        else:
            error = 'Форма не валидна'
    else:
        form = WaybillForm

    context = {'title': 'Путевой лист',
               'form': form,
               'error': error}
    return render(request, 'lab9/create_waybill.html', context)


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        drivers_labels = []
        drivers_data = []
        m_drivers = []
        drivers = Employee.objects.annotate(sum_milage=Sum('waybill__milage'))
        average_drivers = drivers.aggregate(sum=Sum('sum_milage'))['sum']/drivers.aggregate(count=Count('sum_milage'))['count']
        drivers_label = "километраж по водителям"

        for i in drivers:
            drivers_labels.append(str(i.first_name) + ' ' + str(i.last_name))
            drivers_data.append(i.sum_milage)
            m_drivers.append(average_drivers)

        auto_labels = []
        auto_data = []
        m_auto = []
        auto = Automobile.objects.annotate(sum_consumption=Sum('waybill__consumption'))
        average_auto = auto.aggregate(sum=Sum('sum_consumption'))['sum']/auto.aggregate(count=Count('sum_consumption'))['count']
        auto_label = 'Расход топлива по автомобилям'

        for a in auto:
            auto_labels.append(str(a.mark))
            auto_data.append(a.sum_consumption)
            m_auto.append(average_auto)

        data = {
            "drivers_labels": drivers_labels,
            "drivers_label": drivers_label,
            "drivers_data": drivers_data,
            'average_drivers': m_drivers,
            'auto_labels': auto_labels,
            'auto_label': auto_label,
            'auto_data': auto_data,
            'average_auto': m_auto,
        }
        return Response(data=data)

