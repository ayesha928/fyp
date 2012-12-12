import os
import sys
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

import importlib
from ..apps import enabled_apps
from .. import load_project_settings

from ..models import (
    DBSession,
    Section, Device,
    Base,
    )

def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd)) 
    sys.exit(1)

def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)
    
    load_project_settings()
    
    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    
    has_records = DBSession.query(Section).count()
    if has_records < 1:
        with transaction.manager:
            sections = [[1, 'Main Gate'], [2,'Drawing/Dining'], [3, 'Tv Lounge'] , [4, 'Living Room'], [5, 'Washroom'], [6, 'Kitchen']]
            for S in sections:
                R = Section()
                R.section_number = S[0]
                R.section_name = S[1]
                DBSession.add(R)

                
    has_records = DBSession.query(Device).count()
    if has_records < 1:
        with transaction.manager:
            devices = [[1, 'Door Lights'], [2,'Dining Energy savers'], [3, 'Dining Fan'], [4, 'TV lounge Tube Light'],[5, 'Living rooms lamp'], [6 ,'Washrooms energy saver'], [7, 'Kitchen fan'],]
            for I in devices:
                T = Device()
                T.device_number = I[0]
                T.device_name = I[1]
                DBSession.add(T)          
    #populate application models
    for app_name in enabled_apps:
        
        app_module = importlib.import_module("apps.%s.scripts.populate" % app_name)
        #print("App Module: %s\n" % app_module.__name__)
        
        try:
            app_module.populate_app(engine, DBSession)
        except Exception, e:
            print(repr(e))
    
