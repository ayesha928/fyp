import unittest
import sys, os

#Adding our src folder to import path so code from within src folder can be imported easily
sys.path.insert(0, os.path.dirname(os.path.abspath('.')) + '/src')

from lib.protocol import encode_command, decode_command
from dummy_pcb import dummy_pcb

class TestCode(unittest.TestCase):
	def setUp(self):
		self.my_pcb = dummy_pcb.PCB()

	def test_dummy_pcb1(self):
		s = self.my_pcb.get_status(1,4)

	def test_dummy_pcb2(self):
		s = self.my_pcb.get_status(1,4)

	def test_dummy_pcb3(self):
		self.my_pcb.connect_device(1,4)

	def test_dummy_pcb4(self):
		self.my_pcb.disconnect_device(1,4)