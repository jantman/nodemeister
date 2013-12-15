# Create your views here.
from django.http import HttpResponse
import enc
import yaml


def puppet(request, hostname):
    """
    The view used to generate YAML for the puppet node_terminus script.

    Calls enc.get_host_data(hostname), formats that into a dict,
    and returns the yaml.safe_dump() of that as the response content.

    :param request: Django request object
    :param hostname: name of the host to return YAML for
    :type hostname: string
    :returns:  HttpResponse of YAML
    """
    (classlist, params) = enc.get_host_data(hostname)
    enc_output = {"classes": classlist, "parameters": params}
    response = yaml.safe_dump(enc_output, default_flow_style=False)
    return HttpResponse(response, content_type="application/x-yaml")


def walkit(request, hostname):
    """
    Unused. Appears to be left over from testing/debugging.
    May, in fact, be better/more efficient than the used puppet() method.
    """
    (classlist, params) = enc.get_host_data(hostname, 'walk')
    enc_output = {"classes": classlist, "parameters": params}
    response = yaml.safe_dump(enc_output, default_flow_style=False)
    return HttpResponse(response)


def classworkit(request, hostname):
    """
    Unused. Appears to be left over from testing/debugging.
    May, in fact, be better/more efficient than the used puppet() method.
    """
    (classlist, params) = enc.get_host_data(hostname, 'classwork')
    enc_output = {"classes": classlist, "parameters": params}
    response = yaml.safe_dump(enc_output, default_flow_style=False)
    return HttpResponse(response)


def workit(request, hostname):
    """
    Unused. Appears to be left over from testing/debugging.
    May, in fact, be better/more efficient than the used puppet() method.
    """
    (classlist, params) = enc.get_host_data(hostname, 'work')
    enc_output = {"classes": classlist, "parameters": params}
    response = yaml.safe_dump(enc_output, default_flow_style=False)
    return HttpResponse(response)


def optworkit(request, hostname):
    """
    Unused. Appears to be left over from testing/debugging.
    May, in fact, be better/more efficient than the used puppet() method.
    """
    (classlist, params) = enc.get_host_data(hostname, 'optwork')
    enc_output = {"classes": classlist, "parameters": params}
    response = yaml.safe_dump(enc_output, default_flow_style=False)
    return HttpResponse(response)
