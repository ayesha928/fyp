from controller import controller
from lib.protocol import encode_command, decode_command
import time

C = Controller() 
C.set_section_friednly_name( 0, 'Kitchen')
C.set_device_friednly_name( 'Kitchen', 0 , 'Fan')
C.set_device_status('SET''Kitchen', 'Fan', 'ON')


def communicate_pcb(self, infile,outfile):
        
        cmd = C.encode_command('SET','ON','Kitchen','Fan')

        if 'SET' == cmd['command_type']:
            section = cmd['section']
            device  = cmd ['device']
            byte = encode_command( cmd['command_type'], cmd['status'], cmd['section'], cmd['device'] )
        return True

        infile.write(byte)
        infile.flush()

        time.sleep(1)
        outfile.seek(-1,2)
        byte = outfile.read
        cmd = C.decode_command(byte)

    
    
     
        