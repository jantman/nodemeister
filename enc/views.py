# Create your views here.
from django.http import HttpResponse
import enc
import yaml

def puppet(request, hostname):
    (classlist, params) = enc.get_host_data(hostname)
    enc_output = {"classes":classlist, "parameters":params}
    response = yaml.safe_dump(enc_output, default_flow_style=False)
    return HttpResponse(response, content_type="application/x-yaml")
  
  
def walkit(request, hostname):
    (classlist, params) = enc.get_host_data(hostname,'walk')
    enc_output = {"classes":classlist, "parameters":params}
    response = yaml.safe_dump(enc_output, default_flow_style=False)
    return HttpResponse(response)

def classworkit(request, hostname):
    (classlist, params) = enc.get_host_data(hostname,'classwork')
    enc_output = {"classes":classlist, "parameters":params}
    response = yaml.safe_dump(enc_output, default_flow_style=False)
    return HttpResponse(response)


def workit(request, hostname):
    (classlist, params) = enc.get_host_data(hostname,'work')
    enc_output = {"classes":classlist, "parameters":params}
    response = yaml.safe_dump(enc_output, default_flow_style=False)
    return HttpResponse(response)

def optworkit(request, hostname):
    (classlist, params) = enc.get_host_data(hostname,'optwork')
    enc_output = {"classes":classlist, "parameters":params}
    response = yaml.safe_dump(enc_output, default_flow_style=False)
    return HttpResponse(response)
