from controller import controller
from lib.protocol import encode_command, decode_command
import time
import os

os.system("touch /tmp/pcb_out")   # need to create the file first and files opened for reading must exist first.
outfile = open('/tmp/pcb_in', 'wb')
infile = open('/tmp/pcb_out', 'rb')

C = controller.Controller(infile, outfile)
C.set_section_friendly_name( 1, 'Kitchen')
C.set_device_friendly_name( 'Kitchen', 1 , 'Fan')

print("Setting status of Kitchen Fan to ON")
if C.set_device_status('Kitchen', 'Fan', 'ON'):
    print("Status successfully set to ON for Kitchen Fan")

print("Fetching status of Kitchen Fan")
status = C.get_device_status('Kitchen', 'Fan')
print("... status is " + status)
