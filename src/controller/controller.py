from lib.protocol import encode_command, decode_command

class controller(object):
	"""
    controller class contain those methods and functions which are part of controller module.
    It is the part which will interact with PCB as well as smart phone! 
    friendly names are the human readable names for the section and devices.
    """
	section = 0
	device = 0
	status = 0
           
	section_friendly_names = {'1':'' , '2':'' , '3':'' , '4':'' , '5':'' , '6':'' , '7':'' , '8':''}
	device_friendly_names = {section_friendly_names['1']:{'1':'' , '2':'' , '3':'' , '4':'' , '5':'', '6':'' , '7':'' , '8':''},
		section_friendly_names['2']:{'1':'' , '2':'' ,'3':'' , '4':'' , '5':'' , '6':'' , '7':'' , '8':''},
		section_friendly_names['3']:{'1':'' , '2':'' ,'3':'' , '4':'' , '5':'' , '6':'' , '7':'' , '8':''},
		section_friendly_names['4']:{'1':'' , '2':'' ,'3':'' , '4':'' , '5':'' , '6':'' , '7':'' , '8':''},
		section_friendly_names['5']:{'1':'' , '2':'' ,'3':'' , '4':'' , '5':'' , '6':'' , '7':'' , '8':''},
		section_friendly_names['6']:{'1':'' , '2':'' ,'3':'' , '4':'' , '5':'' , '6':'' , '7':'' , '8':''},
		section_friendly_names['7']:{'1':'' , '2':'' ,'3':'' , '4':'' , '5':'' , '6':'' , '7':'' , '8':''},
		section_friendly_names['8']:{'1':'' , '2':'' ,'3':'' , '4':'' , '5':'' , '6':'' , '7':'' , '8':''} }
           
	def reverse_dict (self, section_friendly_name):
		rev_section_friendly_names = dict((v,k) for k,v in self.section_friendly_names.iteritems())
		rev_device_friendly_names = dict((v,k) for k,v in self.device_friendly_names.iteritems())
           
	def get_section_names(self, section_list):
		"""
		get_section_names is a function that assigns names to sections
		:param section_list: a list of length 8
		"""
		for s in section_list:
			self.section_friendly_names['s'] = section_list[s]
			return self.section_friendly_names[section_list]
           
	def get_device_names(self, device_list):
		"""
		get_device_names is a function that gets names of the devices.
		:param device_list: a device list of 8 rows, 8 columns
		"""
		for s in device_list:
			for d in s:
				self.device_friendly_names['d'] = device_list[s][d]
				return self.device_friendly_names[device_list]

	def set_one_device(self, section, device, status):
		"""
		set_one_device is a function that sets status of one device in a section
		:param section: Numerical number or character string for the section
		:param device: Numerical number or character string for the device
		"""
		if isinstance(section, device, str):
			for s in self.device_friendly_names:selfself
			if self.device_friendly_names[s] == section:
				section_number = self.section_friendly_names[s]
				for d in s:
					if self.device_friendly_names['s']['d'] == device:
						device_number = self.device_friendly_names[s][d]
		if isinstance(section, device, str):
			for s in rev_device_friendly_names:
				if self.rev_device_friendly_names['s'] == section:
					section_number = section_friendly_names[s]
					for d in s:
						if self.rev_device_friendly_names['s']['d'] == device:
							device_number =self.rev_device_friendly_names[s][d]
							byte = encode_command(1, status, section_number, device_number)
							try:
								f = open('/home/sumera/python/infile.txt', 'a')
								input_byte = f.write(byte)
								f.close()
							except Exception, e:
								print "Error Writing File!" + str(e)
								sleep(1)
							try:
								f = open('/home/sumera/python/outfile.txt', 'r')
								f.seek(-1, 2) 
								byte = f.read()
								f.close()
							except Exception, e:
								print "Error Reading File!" +str(e)
								dict_status = decode_command(byte)
								if section == dict_status['section'] and device == dict_status['device'] and status ==dict_status['status']:
									print "Status of " + dict_status['device'] + " in " + section + " as " + dict_status['status'] + " has been set successfully!"
								else:
										print "Device: " + dict_status['device'] + " in " + section + " as " + dict_status['status'] + " cannot be set successfully!"
										self.rev_device_friendly_names[section][device] = status
     
	def set_one_section(self, section, status):
		"""
		set_one_section is a function that takes two parameters - section and status
		:param status: Can either be 'ON' or 'OFF'
		:param section: Numerical number or character string for the section
		"""
		for s in self.device_friendly_names:
			if section == self.device_friendly_names[s]:
				for d in s:
					set_one_device(self, section, device_friendly_names['d'],status)
					self.device_friendly_names[section] =  status
     
	def set_all_sections(self, section , status):
		"""
		set_all_sections is a function that set status ON/OFF to all devices of all sections
		:param status: Can either be 'ON' or 'OFF'
		"""
		for s in device_friendly_names:
			set_one_section(self, device_friendly_names[s], status)
			self.device_friendly_names[section] =  status
           
	def get_one_device(self, section, device):
		"""
		get_status_of_one_device is a function that print status of one device in one section
		:param section: Numerical number or character string for the section
		:param device: Numerical number or character string for the device
		"""
		if isinstance(section, device, str):
			for s in self.device_friendly_names:
				if self.device_friendly_names[s] == section:
					section_number = section_friendly_names[s]
					for d in s:
						if self.device_friendly_names['s']['d'] == device:
							device_number = self.device_friendly_names[s][d]
							if isinstance(section, device, str):
								for s in self.rev_device_friendly_names:
									if self.rev_device_friendly_names['s'] == section:
										section_number = section_friendly_names[s]
										for d in s:
											if self.rev_device_friendly_names['s']['d'] == device:
												device_number =self.rev_device_friendly_names[s][d]
												byte = encode_command(0, 0, section_number, device_number)
												
												infile = open('infile.txt', 'wb')
												input_byte = infile.write(byte)
												infile.close()
												time.sleep(1)
												
												outfilef = open('outfile.txt', 'rb')
												f.seek(-1, 2) 
												byte = outfile.read()
												outfile.close()
												dict_status = decode_command(byte)
												if section == dict_status['section'] and device == dict_status['device']:
													print "Status of " + device + " in " + section + " : " + dict_status['status']
												else:
													print "Device: " + dict_status['device'] + " is unavailable!"
													return self.rev_device_friendly_names[section][device]
     
	def get_one_section(self, section):
		"""
		get_status_of_one_section is a function that print status of all devices
		:param section: Numerical number or character string for the section
		"""
		for s in self.device_friendly_names:
			if section == self.device_friendly_names[s]:
				for d in s:
					get_one_device(self, section, device_friendly_names['d'])
					return self.device_friendly_names[section]
                    
                    
	def get_all_sections(self , section):
		"""
	get_all_sections is a function that print status of all devices of all sections
		"""
		for s in device_friendly_names:
			get_one_section(self, device_friendly_names[s])
			return self.device_friendly_names[section][section]

