import os
from dummy_pcb.dummy_pcb import PCB

P = PCB()

os.system("touch /tmp/pcb_in")   # need to create the file first and files opened for reading must exist first.
infile = open('/tmp/pcb_in', 'rb')
outfile = open('/tmp/pcb_out', 'wb')

P.connect_device(1, 1)
P.connect_device(1, 2)
P.connect_device(1, 3)
P.connect_device(2, 1)
P.connect_device(3, 1)

print("Connected devices - Section 1 (Device 1, 2, 3), Section 2 (Device 1), Section 3 (Device 1)")

P.process_requests(infile, outfile)
