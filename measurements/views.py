from django.shortcuts import render

from measurements.models import Measurement
from .logic import measurements_logic as ml
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def measurements_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            measurement_dto = ml.get_measurement(id)
            measurement = serializers.serialize('json', [measurement_dto,])
            return HttpResponse(measurement, 'application/json')
        else:
            measurement_dto = ml.get_measurements()
            measurement = serializers.serialize('json', measurement_dto)
            return HttpResponse(measurement, 'application/json')       
    if request.method == 'POST':
        measurement_dto = ml.create_measurement(json.loads(request.body))
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, 'application/json')      

@csrf_exempt
def measurement_view(request, pk):
    if request.method == 'PUT':
        measurement_dto = ml.update_measurement(pk, json.loads(request.body))
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, 'application/json')
    if request.method == 'DELETE':
        measurement_dto= ml.delete_measurement(pk)
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, 'application/json')
