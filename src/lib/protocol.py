#function 1:
def encode_command( command_type, status, section_number, device_number ): #return the byte
	binary_bit_sequence = bin(section_number)[2:] + bin(device_number)[2:] #concatinate binary numbers for protocol
	if 'ON' == status:
		binary_bit_sequence = '1' + binary_bit_sequence
	else:
		binary_bit_sequence = '0' + binary_bit_sequence
	if 'SET' == command_type:
		binary_bit_sequence = '1' + binary_bit_sequence
	else:
		binary_bit_sequence = '0' + binary_bit_sequence
	decimal_of_binary_sequence = int(binary_bit_sequence, 2) #convert binary (string/Byte/set of bits) to decimal
	ascii_char = chr(decimal_of_binary_sequence) #convert decimal to ASCII character
	return ascii_char #return ASCII character for bit sequence

#function 2:
def decode_command(input_byte): #return a dictionary
	byte_binary_sequence = bin(ord(input_byte))[2:] # byte ka binary sequence a jaey ga as string jis ki ap slicing bhi kar saktay hain
	command_type = byte_binary_sequence[0] #first bit of Byte
	status = byte_binary_sequence[1] #second bit of Byte
	section_number = byte_binary_sequence[2:3] #3rd, 4th, 5th bits of Byte
	device_number = byte_binary_sequence[5:3] #last 3 bits of Byte
	dec_section_number = int(section_number, 2)
	dec_device_number = int(device_number, 2)
	if '1' == byte_binary_sequence[0]:
		command_type = 'SET'
	else:
		command_type = 'GET'
	if '1' == byte_binary_sequence[1]:
		status = 'ON'
	else:
		status = 'OFF'
	my_dict = dict(command_type = command_type, status = status, section_number = dec_section_number, device_number = dec_device_number) #dictionary
	return my_dict #return a dictionary containing command_type, status, section_number, device_number
		
	
##test code
a = encode_command( 'SET','ON', 3, 2 )
b = decode_command( 'U' )