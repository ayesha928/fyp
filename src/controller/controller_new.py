from lib.protocol import encode_command, decode_command

class Controller(object):
    """
    controller class contains those methods and functions which are part of controller module.
    It is the part which will interact with PCB as well as smart phone! 
    friendly names are the human readable names for the section and devices.
    """
           
    def __init__(self, infilename, outfilename):
        self.infile = open(infilename, 'rb')
        self.outfile = open(outfilename, 'wb')
        
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
        self.section_friendly_names[section_number] = friendly_name
        self.rev_section_friendly_names[friendly_name] = section_number
    
    def set_device_friendly_name(self, section, device_number, friendly_name):
        
        #check if section is a number, if not, its a friendly name, translate it to section number
        if not str(section).isdigit():
            section = self.rev_section_friendly_names[section]
        
        self.device_friendly_names[section][device_number] = friendly_name
        
        if section not in self.rev_device_friendly_names.keys():
            self.rev_device_friendly_names[section] = {}
            
        self.rev_device_friendly_names[section][friendly_name] = device_number
        
    def get_section_friendly_names(self, section_number):
        return self.section_friendly_names[section_number]
        return self.rev_section_friendly_names[section_number]
        
    def get_device_friendly_name(self , section , device_number):
        
        if not str(section).isdigit():
            section = self.rev_section_friendly_names[section]
        
        self.device_friendly_names[section][device_number] = friendly_name
        
        if section not in self.rev_device_friendly_names.keys():
            self.rev_device_friendly_names[section] = {}
            
        return self.rev_device_friendly_names[section][device_number]
        
    def get_device_number(self,section_number, device_number):
        self.device_friendly_names[section_number][device_number]
        return self.rev_device_friendly_names[section_number][device_number]
        
    def get_section_number(self,section_name):
         self.section_friendly_names[section_name]
         return self.section_friendly_names[section_name]
    
    def set_device_status(self,section_name, device_name, status):
        self.device_friendly_names[section_name][device_name] = status
        self.rev_device_friendly_names[section_name][device_name] = status
        
        
    def get_device_status(self,section_name, device_name):
        self.device_friendly_names[section_name][device_name]
        return self.rev_device_friendly_names[section_name][device_name]
        
        
        