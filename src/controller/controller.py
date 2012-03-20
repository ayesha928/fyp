'''
Controller module contains:
    1). a Controller class
    2). impoert codeWithoutFiling module that contains encode/decode functions
    3). import dummy_pcb module
''' 

import codeWithoutFiling
import dummy_pcb

class Controller:
	section, appliance, status = 0
	
	section_friendly_names = {'0':'' , '1':'' , '2':'' , '3':'' , '4':'' , '5':'' , '6':'' , '7':''} #dictionary for 8 section names
	#nested dictionary for 8 devices per section
	device_friendly_names = {'0':'{'0':'' , '1':'' , '2':'' , '3':'' , '4':'' , '5':'' , '6':'' , '7':''} ',
							 '1':'{'0':'' , '1':'' , '2':'' , '3':'' , '4':'' , '5':'' , '6':'' , '7':''} ',
							 '2':'{'0':'' , '1':'' , '2':'' , '3':'' , '4':'' , '5':'' , '6':'' , '7':''} ', 
							 '3':'{'0':'' , '1':'' , '2':'' , '3':'' , '4':'' , '5':'' , '6':'' , '7':''} ',
							 '4':'{'0':'' , '1':'' , '2':'' , '3':'' , '4':'' , '5':'' , '6':'' , '7':''} ',
							 '5':'{'0':'' , '1':'' , '2':'' , '3':'' , '4':'' , '5':'' , '6':'' , '7':''} ',
							 '6':'{'0':'' , '1':'' , '2':'' , '3':'' , '4':'' , '5':'' , '6':'' , '7':''} ',
							 '7':'{'0':'' , '1':'' , '2':'' , '3':'' , '4':'' , '5':'' , '6':'' , '7':''} '}
	
	def __init__(self, section_friendly_name):
		#self.name = name
		self.rev_section_friendly_names = dict((v,k) for k,v in section_friendly_names.iteritems())
		self.rev_device_friendly_names = dict((v,k) for k,v in device_friendly_names.iteritems())
	
	def get_section_names(self, section_list):
		'''
		get_section_names is a function that
	    # takes a list of length 8 as a parameter
	    :param section_list[]: of length 8
	    # assigns names to 8 sections
	    # returns section_friendly_names
	    '''
	    pass

#---------------------------------------------------------------------------------------------------------------------------------------	
	
	def get_device_names(self, device_list):
	  '''
	  get_device_names is a function that:
	      # takes a two dimentional list having 8 rows and 8 columns as a parameter
	          :param device_list[][]: of 8 rows, 8 columns
	      # assign names to 8 devices per section i.e. 64 devices' names
	      # returns device_friendly_names
	  '''
		pass
#---------------------------------------------------------------------------------------------------------------------------------------				
	def set_one_device(self, section, device, status):
	  ''' 
	  set_one_device is a function that:
	      # takes 3 parameters: section, device and status
	          :param section: Numerical number or character string for the section
	          :param device: Numerical number or character string for the device
	      # locate specified device of a particular section via calling query_section and query_device functions
	      # set status of one device in one section
	      # returns nothing
	  '''
		pass
#---------------------------------------------------------------------------------------------------------------------------------------

	def set_one_section(self, section, status):
	'''
	set_one_section is a function that:
	    # takes two parameters - section and status
	        :param status: Can either be 'ON' or 'OFF'
	        :param section: Numerical number or character string for the section
	    # locate specified section via calling query_section function
	    # locate all devices of a specified section
	    # set status ON/OFF to all devices of specified section
	    # returns nothing
	    ''' 
	    pass
#---------------------------------------------------------------------------------------------------------------------------------------

	def set_all_sections(self, status):
	  ''' 
	  set_all_sections is a function that:
	      # takes 1 parameter i.e. status
	          :param status: Can either be 'ON' or 'OFF'
	      # locate all devices of all sections
	      # set status ON/OFF to all devices of all sections
	      # returns nothing
	   '''
	      pass
#---------------------------------------------------------------------------------------------------------------------------------------	
	
	def get_one_device(self, section, device):
	  '''
	  get_status_of_one_device is a function that:
	      # takes 2 parameters: section and device
	          :param section: Numerical number or character string for the section
	          :param device: Numerical number or character string for the device
	      # locate specified device of a particular section via calling query_section and query_device functions
	      # print status of one device in one section
	      # returns nothing
	   '''
		pass
#---------------------------------------------------------------------------------------------------------------------------------------

	def get_one_section(self, section):
	  '''
	  get_status_of_one_section is a function that:
	      # takes 1 parameter i.e. section
	          :param section: Numerical number or character string for the section
	      # locate specified section from dictionary via calling query_section function
	      # print status of all devices
	      # returns nothing
	   '''
	      pass
#---------------------------------------------------------------------------------------------------------------------------------------	  
	def get_all_sections(self):
	  '''
	  get_all_sections is a function that:
	      # takes no parameters
	      # locate all section from dictionary via calling query_section function
	      # print status of all devices of all sections
	      # returns nothing
	   '''
	      pass
#---------------------------------------------------------------------------------------------------------------------------------------	  
	 def query_section(self, section_name):
	  '''
	  query_section is a function that:
	      # takes 1 parameter i.e. section_name
	          :param section_name: Numerical number or character string for the section
	      # search the required section_name from dictionary
	      # returns the section which is going to be queried
	  '''
		pass
#---------------------------------------------------------------------------------------------------------------------------------------

	def query_device(self, device_name):
	  '''
	  query_device is a function that:
	      # takes 1 parameter i.e. device_name
	          :param device_name: Numerical number or character string for the device
	      # search the required device_name (from dictionary) of a particular section which was queried by query_section function
	      # returns the device which is going to be queried
	   '''
		pass 
