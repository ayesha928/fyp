    '''
    Controller module contains:
       # a Controller class
       # impoert protocol module (user defined) that contains encode/decode functions
       # import time.sleep (built-in)
    '''
     
    from protocol import encode_command, decode_command
    from time import sleep
     
    class Controller(object):
            section = 0
            device = 0
            status = 0
           
            section_friendly_names = {'1':'' , '2':'' , '3':'' , '4':'' , '5':'' , '6':'' , '7':'' , '8':''}#dictionary for 8 section names
            #nested dictionary for 8 devices per section
            device_friendly_names = {section_friendly_names['1']:{'1':'' , '2':'' , '3':'' , '4':'' , '5':'', '6':'' , '7':'' , '8':''},
                                                             section_friendly_names['2']:{'1':'' , '2':'' ,'3':'' , '4':'' , '5':'' , '6':'' , '7':'' , '8':''},
                                                             section_friendly_names['3']:{'1':'' , '2':'' ,'3':'' , '4':'' , '5':'' , '6':'' , '7':'' , '8':''},
                                                             section_friendly_names['4']:{'1':'' , '2':'' ,'3':'' , '4':'' , '5':'' , '6':'' , '7':'' , '8':''},
                                                             section_friendly_names['5']:{'1':'' , '2':'' ,'3':'' , '4':'' , '5':'' , '6':'' , '7':'' , '8':''},
                                                             section_friendly_names['6']:{'1':'' , '2':'' ,'3':'' , '4':'' , '5':'' , '6':'' , '7':'' , '8':''},
                                                             section_friendly_names['7']:{'1':'' , '2':'' ,'3':'' , '4':'' , '5':'' , '6':'' , '7':'' , '8':''},
                                                             section_friendly_names['8']:{'1':'' , '2':'' ,'3':'' , '4':'' , '5':'' , '6':'' , '7':'' , '8':''} }
           
            def reverse_dict (self, section_friendly_name):
                    #self.name = name
                    rev_section_friendly_names = dict((v,k) for k,v in self.section_friendly_names.iteritems())
                    rev_device_friendly_names = dict((v,k) for k,v in self.device_friendly_names.iteritems())
           
            def get_section_names(self, section_list):
                    '''
                    get_section_names is a function that
                # takes a list of length 8 as a parameter
                :param section_list[]: of length 8
                # assigns names to 8 sections
                # returns section_friendly_names
                '''
                    for s in section_list:
                            self.section_friendly_names['s'] = section_list[s]
    #---------------------------------------------------------------------------------------------------------------------------------------       
           
            def get_device_names(self, device_list):
                    '''
                    get_device_names is a function that:
                # takes a two dimentional list having 8 rows and 8 columns as a parameter
                :param device_list[][]: of 8 rows, 8 columns
                # assign names to 8 devices per section i.e. 64 devices' names
                # returns device_friendly_names
                    '''
                    for s in device_list:
                            for d in s:
                                    self.device_friendly_names['d'] = device_list[s][d]
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
                    if isinstance(section, device, str):
                            for s in self.device_friendly_names:
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
                            f.seek(-1, 2) #2 uses EOF as reference point
                            byte = f.read()
                            f.close()
                    except Exception, e:
                            print "Error Reading File!" +str(e)
                    dict_status = decode_command(byte)
                    if section == dict_status['section'] and device == dict_status['device'] and status ==dict_status['status']:
                            print "Status of " + dict_status['device'] + " in " + section + " as " + dict_status['status'] + " has been set successfully!"
                    else:
                            print "Device: " + dict_status['device'] + " in " + section + " as " + dict_status['status'] + " cannot be set successfully!"
                    return
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
                # returns to calling function
                    '''
                    for s in self.device_friendly_names:
                            if section == self.device_friendly_names[s]:
                                    for d in s:
                                            set_one_device(self, section, device_friendly_names['d'],status)
                    return
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
                    for s in device_friendly_names:
                            set_one_section(self, device_friendly_names[s], status)
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
                get status is a function of pcb
                    '''
                    #if isinstance(section, str):
                            #for s in range(len(section_friendly_names)):
                                    #if section_friendly_names['s'] == section: #match value
                                            #section_number = section_friendly_names[s] #assign key
                    #if isinstance(section, int):
                            #for s in self.rev_section_friendly_names:
                                    #if rev_section_friendly_names['s'] == section: #match value
                                            #section_number = rev_section_friendly_names[s] #assign key
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
                    try:
                            f = open('/home/sumera/python/infile.txt', 'a')
                            input_byte = f.write(byte)
                            f.close()
                    except Exception, e:
                            print "Error Writing File!" + str(e)
                    sleep(1)
                    try:
                            f = open('/home/sumera/python/outfile.txt', 'r')
                            f.seek(-1, 2) #2 uses EOF as reference point
                            byte = f.read()
                            f.close()
                    except Exception, e:
                            print "Error Reading File!" +str(e)
                    dict_status = decode_command(byte)
                    if section == dict_status['section'] and device == dict_status['device']:
                            print "Status of " + device + " in " + section + " : " + dict_status['status']
                    else:
                            print "Device: " + dict_status['device'] + " is unavailable!"
                    return
    #---------------------------------------------------------------------------------------------------------------------------------------
     
            def get_one_section(self, section):
                    '''
                    get_status_of_one_section is a function that:
                # takes 1 parameter i.e. section
                :param section: Numerical number or character string for the section
                # locate specified section from dictionary via calling query_section function
                # print status of all devices
                # returns back to calling function
                    '''
                    for s in self.device_friendly_names:
                            if section == self.device_friendly_names[s]:
                                    for d in s:
                                            get_one_device(self, section, device_friendly_names['d'])
                    return
    #---------------------------------------------------------------------------------------------------------------------------------------         
            def get_all_sections(self):
                    '''
                    get_all_sections is a function that:
                # takes no parameters
                # locate all section from dictionary via calling query_section function
                # print status of all devices of all sections
                # returns nothing
                    '''
                    for s in device_friendly_names:
                            get_one_section(self, device_friendly_names[s])

