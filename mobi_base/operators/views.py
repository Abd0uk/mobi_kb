from django.shortcuts import render
from .models import Operator

def index(request):
   
    return render(request, 'operators/index.html', {
        'Operators': Operator.objects.all()
    })


def operator_detail(request, pk):
    operator_instance = Operator.objects.get(id=pk)
    return render(request, 'operators/operator_detail.html', {
        'operator': operator_instance
    })
