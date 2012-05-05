from dummy_pcb.dummy_pcb import PCB

P = PCB()

infile = open('/tmp/infile.txt', 'rb')
outfile = open('/tmp/outfile.txt', 'wb')

P.process_requests(infile, outfile)
