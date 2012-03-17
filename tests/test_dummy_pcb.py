import sys, os

#Adding our src folder to import path so code from within src folder can be imported easily
sys.path.insert(0, os.path.dirname(os.path.abspath('.')) + '/src')

from dummy_pcb.dummy_pcb import get_status,set_status,connect_device,disconnect_device

my_pcb = dummy_pcb.PCB()

def test_dummy_pcb1():
	"Dummy PCB - Test 1 - Set status test"
	my_pcb.set_status(1,4,'ON')
	
def test_dummy_pcb2():
	"Dummy PCB - Test 2 - Get status test"
	s = my_pcb.get_status(1,4)
		
def test_dummy_pcb3():
	"Dummy PCB - Test 3 - Connect device test"
	my_pcb.connect_device(1,4)

def test_dummy_pcb4():
	"Dummy PCB - Test 4 - Disconnect device test"
	my_pcb.disconnect_device(1,4)

