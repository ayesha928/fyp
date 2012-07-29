from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from ..models import (
    DBSession,
    #Site,
    )

@view_config(route_name='home', renderer='home.mako')
def my_view(request):
    return {}
    
@view_config(route_name='control', renderer='control.mako')
def my_control(request):
    return {}

@view_config(route_name='audio', renderer='audio.mako')
def my_audio(request):
    return {}

@view_config(route_name='security', renderer='security.mako')
def my_security(request):
    return {}
 
@view_config(route_name='status', renderer='status.mako')
def my_status(request):
    return {} 
    
@view_config(route_name='settings', renderer='settings.mako')
def my_settings(request):
    return {}
