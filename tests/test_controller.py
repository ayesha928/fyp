import unittest
import sys, os

#Adding our src folder to import path so code from within src folder can be imported easily
sys.path.insert(0, os.path.dirname(os.path.abspath('.')) + '/src')

from controller import controller as c


if '__main__' == __name__:
    os.system('touch /tmp/controller_in')
    os.system('touch /tmp/controller_out')
    

class TestCode(unittest.TestCase):
    def setUp(self):
        self.my_controller = c.Controller('/tmp/controller_in', '/tmp/countroller_out')
        
    def test_controller1(self):
        "Controller - Test 1 - Set friendly name of section"
        self.my_controller.set_section_friendly_name(2 , "Living Room")

    def test_controller2(self):
        "Controller - Test 2 - Set friendly name of device"
        self.my_controller.set_device_friendly_name(2, 1, 'Tube Light')
    
    #using section name instead of number
    def test_controller3(self):
        "Controller - Test 3 - Set friendly name of device"
        self.my_controller.set_device_friendly_name("Living Room", 1, 'Tube Light')

    def test_controller4(self):
        "Controller - Test 4 -Set status of device"
        self.my_controller.set_device_status("Living Room" , 'Tube Light' , 'ON')
    
    def test_controller5(self):
        "Controller - Test 5 -Get friendly name of section"
        s = self.my_controller.get_section_friendly_name(2)
    
    def test_controller6(self):
        "Controller - Test 6 -Get friendly name of device"
        d = self.my_controller.get_device_frienldy_name(2, 1)
    
    #using section name instead of number  
    def test_controller7(self):
        "Controller - Test 7 -Get friendly name of device"
        d = self.my_controller.get_device_frienldy_name("Living Room", 1)
          
    def test_controller8(self):
        "Controller - Test 8 -Get number of device"
        n = self.my_controller.get_device_number(2, 'Tube Light')
    
    def test_controller9(self):
        "Controller - Test 9 -Get number of section"
        a = self.my_controller.get_section_number("Living Room")
    
    def test_controller10(self):
        "Controller - Test 10 -Get status of device"
        b = self.my_controller.get_device_status("Living Room" , 'Tube Light')


    