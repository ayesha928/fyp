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
		
	def set_status(self,section,device,status):
		"""
		This method sets the status of devices as per requirement
		
		:param section: Numerical number for the section
		:param device: Numerical number for the device
		:param status: Can either be 'ON' or 'OFF'
		""" 
		pass

	def get_status(self,section,device):
		"""
		This method gets the status of devices as per requirement
		
		Returns the status of device
		
		:param section: Numerical number for the section
		:param device: Numerical number for the device
		""" 
		
		pass
	
	def connect_device(section,device):
		"""
		This method connects the device
		
		:param section: Numerical number for the section
		:param device: Numerical number for the device
		""" 
		pass
	
	def disconnect_device(section,device):
		"""
		This method disconnects the devices
		
		:param section: Numerical number for the section
		:param device: Numerical number for the device
		""" 
		pass 