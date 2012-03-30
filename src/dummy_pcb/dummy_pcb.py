from lib.protocol import encode_command, decode_command
class PCB(object):
	"""
	This class contains those functions and methods which reflects the pcb as dummy (software of pcb) 
	
	Varibale pcb_status stores the status of all the sections and devices in the form of nested lists
	""" 
	pcb_status = [
		['Not Connected','Not Connected','Not Connected','Not Connected','Not Connected','Not Connected','Not Connected'],
		['Not Connected','Not Connected','Not Connected','Not Connected','Not Connected','Not Connected','Not Connected'],
		['Not Connected','Not Connected','Not Connected','Not Connected','Not Connected','Not Connected','Not Connected'],
		['Not Connected','Not Connected','Not Connected','Not Connected','Not Connected','Not Connected','Not Connected'],
		['Not Connected','Not Connected','Not Connected','Not Connected','Not Connected','Not Connected','Not Connected'],
		['Not Connected','Not Connected','Not Connected','Not Connected','Not Connected','Not Connected','Not Connected'],
		['Not Connected','Not Connected','Not Connected','Not Connected','Not Connected','Not Connected','Not Connected']
		]
		
	def set_status(self, section, device, status):
		"""
		This method sets the status of devices as per requirement
		
		:param section: Numerical number for the section
		:param device: Numerical number for the device
		:param status: Can either be 'ON' or 'OFF'
		""" 
		self.pcb_status[section][device] = status

	def get_status(self, section, device):
		"""
		This method gets the status of devices as per requirement
		
		Returns the status of device
		
		:param section: Numerical number for the section
		:param device: Numerical number for the device
		""" 
		
		return self.pcb_status[section][device]
	
	def connect_device(self, section, device):
		"""
		This method connects the device
		
		:param section: Numerical number for the section
		:param device: Numerical number for the device
		""" 
		self.pcb_status[section][device] = 'OFF'
	
	def disconnect_device(self, section, device):
		"""
		This method disconnects the devices
		
		:param section: Numerical number for the section
		:param device: Numerical number for the device
		""" 
		self.pcb_status[section][device] = 'Not Connected'
		
	def process_request():
		"""
		This method reads the first byte form infile and after processing writes the encoded command in the outfile. 
		This method uses infinite loop that will process request after evry second.  
		
		"""
		infile = open('infile.txt', 'rb')
		outfile = open('outfile.txt', 'wb')
		
		while True:
			
			time.sleep(1)
			infile.seek(-1,2)
			byte = infile.read(1)
			cmd = decode_command(byte)
			if 'GET' == cmd['command_type']:
				section = cmd['section']
				device = cmd['device']
				status = self.pcb_status[section][device]
				cmd['status'] = status
			new_byte = encode_command( cmd['command_type'], cmd['status'], cmd['section'], cmd['device'] )
			outfile.write(new_byte)
			outfile.flush()