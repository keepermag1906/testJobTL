from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *
import sys
import random
import datetime


@csrf_exempt
def index(request):

    employees = Employee.objects.all()
    context = {}

    for i in range(1,26):
        context[f'd{i}'] = employees.filter(division=f'division_{i}')
        
    return render(request, 'mainPage.html', context)

