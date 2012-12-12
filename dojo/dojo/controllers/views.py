from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from ..models import (
    DBSession,
    #Site,
    )


@view_config(route_name='home', renderer='home.mako')
def my_view(request):
    return {}


@view_config(route_name='status')
def status(request):
    # instead of just returning the status passed by the ajax call here
    # we can call our PCB controlling code library (protocol.py etc.) and
    # actually get or set the device status
    command_type = request.POST['command_type']
    section = request.POST['section']
    device = request.POST['device']
    status = request.POST['status']

    request.response.text = command_type + ':' + section + ':' + device + ':' + status
    return request.response
    return p
    
@view_config(route_name='settings')    
def setting(request):
    sections = DBSession(R)
    section= request.POST['current_sections']
    request.response.text = 'Currently added sections are:' +sections
    return request.response
    