import os
from pprint import pprint

import controller.controller_new as c

if '__main__' == __name__:
    os.system('touch /tmp/controller_in')
    os.system('touch /tmp/controller_out')
    
    C = c.Controller('/tmp/controller_in', '/tmp/countroller_out')
    
    C.set_section_friendly_name(2, "Living Room")
    C.set_device_friendly_name(2, 1, 'Tube Light')
    C.set_device_friendly_name("Living Room", 1, 'Tube Light')  #using section name instead of number, still works
    C.set_device_status("Living Room" , 'Tube Light', 'OFF')
    C.get_section_friendly_names(2)
    C.get_device_friendly_names( 2 , 1)
    C.get_device_number(2)
    C.get_section_number("Living Room")
    C.get_device_status("Living Room", 'Tube Light')
    
    pprint(C.section_friendly_names)
    print
    print
    
    pprint(C.device_friendly_names)
    print
    print
    
    pprint(C.rev_section_friendly_names)
    print
    print
    
    pprint(C.rev_device_friendly_names)
    print
    print
    


