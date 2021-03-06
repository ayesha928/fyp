import sys
import os
from pyramid.config import Configurator
from pyramid.session import UnencryptedCookieSessionFactoryConfig

from sqlalchemy import engine_from_config

from models import DBSession

import importlib
from apps import enabled_apps

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    
    load_project_settings()
    
    session_factory = UnencryptedCookieSessionFactoryConfig(settings.get('session.secret', 'hello'))
    
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    config = Configurator(session_factory=session_factory, settings=settings)
    config.include('pyramid_handlers')
    config.add_view('pyramid.view.append_slash_notfound_view',
                context='pyramid.httpexceptions.HTTPNotFound')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('status', '/status')
    config.add_route('settings', '/settings')
    
    
    configure_app_routes(config)
    
    config.scan()
    
    return config.make_wsgi_app()

def load_project_settings():
    here = os.path.dirname(__file__)
    sys.path.insert(0, here+'/apps')
    sys.path.insert(0, here)

def configure_app_routes(config):
    """
    Puggable - Application routes integration
    =========================================
    
    Integrates routes for all applications present in the apps folder and enabled (present in the enabled_apps
    list in apps.__init__.py).
    
    Normally each application is automatically given a route_prefix matching the
    application name. So for example, if you have an application named blog, its route_prefix would be /blog
    and all other application routes will also be prefixed with /blog. If you want to override the route_prefix
    and want the application accessible under some other route prefix (or no route prefix at all), use the
    app_route_prefixes dictionary present in this function to specify an alternate route for the application.
    Specify just / if you want the application routes to be accessible at the same level as the main project's
    routes.
    """
    
    # The app_route_prefixes dictionary for overriding app route prefixes
    app_route_prefixes = {
        #'blog': '/myblog'
    }
    
    for app_name in enabled_apps:
        app_route_prefix = app_route_prefixes.get(app_name, '/%s'%app_name)
        app_module = importlib.import_module(".apps.%s" % app_name, "dojo")
        
        try:
            config.include(app_module.application_routes, route_prefix=app_route_prefix)
        except Exception, e:
            print(repr(e))
    
