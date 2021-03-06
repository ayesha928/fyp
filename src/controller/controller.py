from lib.protocol import encode_command, decode_command
import time

class Controller(object):
    """
    controller class contains those methods and functions which are part of controller module.
    It is the part which will interact with PCB as well as smart phone! 
    friendly names are the human readable names for the section and devices.
    """
           
    def __init__(self, infile, outfile):
        self.infile = infile
        self.outfile = outfile
        
        self.section_friendly_names = {1:'' , 2:'' , 3:'' , 4:'' , 5:'' , 6:'' , 7:''}
        self.device_friendly_names = {1:{1:'', 2:'' , 3:'' , 4:'' , 5:'', 6:'' , 7:'' },
                                      2:{1:'', 2:'' , 3:'' , 4:'' , 5:'' , 6:'' , 7:''},
                                      3:{1:'', 2:'' , 3:'' , 4:'' , 5:'' , 6:'' , 7:''},
                                      4:{1:'', 2:'' , 3:'' , 4:'' , 5:'' , 6:'' , 7:''},
                                      5:{1:'', 2:'' , 3:'' , 4:'' , 5:'' , 6:'' , 7:''},
                                      6:{1:'', 2:'' , 3:'' , 4:'' , 5:'' , 6:'' , 7:''},
                                      7:{1:'', 2:'' , 3:'' , 4:'' , 5:'' , 6:'' , 7:''}
                                     }
        
        self.rev_section_friendly_names = {}
        self.rev_device_friendly_names = {}
    
    def __del__(self):
        self.infile.close()
        self.outfile.close()
    
    def set_section_friendly_name(self, section_number, friendly_name):
        """
        This is a function that assigns names to sections
        :param sectiom_number: Numerical number of section
        :param friendly_name: Human readable name of the section
        """
        self.section_friendly_names[section_number] = friendly_name
        self.rev_section_friendly_names[friendly_name] = section_number
    
    def set_device_friendly_name(self, section, device_number, friendly_name):
        """
        This is a function that sets the human readable name of device
        :param section: Numerical number or character string for the section
        :param device_number: Numerical number for the device
        :param friendly_name: Human readable name for the device
        """

        if not str(section).isdigit():
            section = self.get_section_number(section)
        
        self.device_friendly_names[section][device_number] = friendly_name
        
        if section not in self.rev_device_friendly_names.keys():
            self.rev_device_friendly_names[section] = {}
            
        self.rev_device_friendly_names[section][friendly_name] = device_number
        
    def get_section_friendly_name(self, section_number):
        """
        This function returns the friendly name for section.
        :param section_number: Numerical number for the section
        """
        return self.section_friendly_names[section_number]

    def get_device_friendly_name(self , section , device_number):
        """
        This function returns a human readable name for the device
        :param section: Numerical number or character string for the section
        :device_number: Numerical number for the device
        """
        
        if not str(section).isdigit():
            section = self.rev_section_friendly_names[section]

        return self.device_friendly_names[section][device_number]

        
    def get_device_number(self,section, device):
        """
        This is a function that returns status of one device
        :param section: Numerical number or character string for the section
        :param device: Numerical number or character string for the device
        """
        if not str(section).isdigit():
            section = self.rev_section_friendly_names[section]
        
        return self.rev_device_friendly_names[section][device]
        
    def get_section_number(self, section_name):
        """
        This function returns the number of section
        :param section_name: Character string for the section
        """
        #print(self.rev_section_friendly_names)
        return self.rev_section_friendly_names[section_name]
    
    def set_device_status(self, section_name, device_name, status):
        """
        This is a function that sets status of one device
        :param section_name: Character string for the section
        :param device_name: Character string for the device
        :status: Can either be 'ON' or 'OFF'
        """
        
        # What language is this? Why are there commas after the lines?
        
        #SET = 1, 
        #GET = 0, 
        #ON = 1, 
        #OFF = 0,
        
        # apart from the spelling mistakes, are we trying to set the section number or get it?
        #self.rev_section_friendly_names[section_number] = sectiom_number
        #self.rev_device_friendly_names[device_number] = device_number
        
        section_number = self.get_section_number(section_name)
        device_number = self.get_device_number(section_number, device_name)
        
        # What is C???????
        #cmd = C.encode_command(command_type, status, section_number, device_number )
        cmd = encode_command('SET', status, section_number, device_number)
        
        self.outfile.write(cmd)
        self.outfile.flush()
        
        self.infile.seek(0,2)
        while 0 == self.infile.tell():
            self.infile.seek(0,2)
            time.sleep(1)
        
        self.infile.seek(-1,2)
        byte = self.infile.read()
        
        #cmd_response = decode_command(byte)
        #print (ord(byte), ord(cmd))
        if byte == cmd:
            return True
        else:
            return False
    
    def get_device_status(self, section_name, device_name):
        """
        This function returns the status of device
        :param section_name: Character string for the section 
        :param device_name: Character string for the device
        """
        #self.rev_section_friendly_names[section_number] = sectiom_number
        #self.rev_device_friendly_names[device_number] = device_number
        #
        #cmd = C.encode_command(command_type, status, section_number, device_number )
        
        section_number = self.get_section_number(section_name)
        device_number = self.get_device_number(section_number, device_name)
        
        cmd = encode_command('GET', 'OFF', section_number, device_number)
        self.outfile.write(cmd)
        self.outfile.flush()
        
        self.infile.seek(0,2)
        while 0 == self.infile.tell():
            self.infile.seek(0,2)
            time.sleep(1)
        
        self.infile.seek(-1,2)
        byte = self.infile.read()
        
        cmd_response = decode_command(byte)
        return cmd_response['status']
