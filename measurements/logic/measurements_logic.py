import measurements
from ..models import Measurement
from variables.logic import variables_logic as vl
def get_measurements():
    measurements = Measurement.objects.all()
    return measurements


def get_measurement(mea_pk):
    measurement = Measurement.objects.get(pk=mea_pk)
    return measurement

def update_measurement(mea_pk, new_mea):
    measurement = get_measurement(mea_pk)
    measurement.variable = vl.get_variable(new_mea["variable"])
    measurement.value= new_mea["value"]
    measurement.unit= new_mea["unit"]
    measurement.place= new_mea["place"]
    measurement.save()
    return measurement

def create_measurement(mea):
    measurement = Measurement(variable= vl.get_variable(mea["variable"]),value= mea["value"],unit= mea["unit"],
                              place= mea["place"])
    measurement.save()
    return measurement

def delete_measurement(mea_pk):
    measurement= get_measurement(mea_pk)
    measurement.delete()
    return measurement