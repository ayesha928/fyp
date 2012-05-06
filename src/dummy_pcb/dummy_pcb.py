from lib.protocol import encode_command, decode_command
import time
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
        
    def process_requests(self, infile, outfile):
        """
        This method reads the first byte form infile and after processing writes the encoded command in the outfile. 
        This method uses infinite loop that will process request after evry second.  
        
        """
        
        print("Running dummy PCB and waiting to process requests...")
        prev_byte = ''
        
        while True:
            time.sleep(1)
            #first check if file is not empty
            infile.seek(0,2)
            if 0 == infile.tell():
                continue
            
            infile.seek(-1,2)
            byte = infile.read(1)
            
            if byte==prev_byte:
                continue  #only do processing if there is a new command
            
            prev_byte = byte
            cmd = decode_command(byte)
            print("    Got command" + repr(cmd))
            
            if 'GET' == cmd['command_type']:
                status = self.get_status(cmd['section_number'], cmd['device_number'])
                new_byte = encode_command(cmd['command_type'], status, cmd['section_number'], cmd['device_number'] )
                
            elif 'SET' == cmd['command_type']:
                self.set_status(cmd['section_number'], cmd['device_number'], cmd['status'])
                new_byte = byte
            
            outfile.write(new_byte)
            outfile.flush()
    