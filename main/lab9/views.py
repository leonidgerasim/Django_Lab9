from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


def index(request):
    return render(request, 'lab9/index.html')


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        # parameter = Parameter(value=r.randint(0, 10))
        # parameter.save()
        parameters = {}
        count = Parameter.objects.count()
        labels = []
        chart_data = []
        average = 0
        m = []
        percent = False
        error = False
        param1 = Parameter.objects.get(id=count-1).value
        param2 = Parameter.objects.get(id=count).value
        k = count - 9 if count > 10 else 1
        for i in range(k, count+1):
            labels.append(str(i))
            chart_data.append(Parameter.objects.get(id=i).value)
            average += Parameter.objects.get(id=i).value

        for i in range(len(chart_data)):
            m.append(average/count)

        if param2 > 10 or param2 < 0:
            error = True

        elif abs(param2 - param1) > 0.4 * abs(param1):
            percent = True

        for param in Parameter.objects.filter(id__gt=count - 10):
            parameters[param.id] = param.value

        chart_label = "Данные"
        data = {
            "labels": labels,
            "chartlabel": chart_label,
            "chartdata": chart_data,
            "average": m,
            "percent": percent,
            "error": error,
            'parameters': parameters,
        }
        return Response(data=data)

