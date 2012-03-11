import sys, os

#Adding our src folder to import path so code from within src folder can be imported easily
sys.path.insert(0, os.path.dirname(os.path.abspath('.')) + '/src')

from lib.protocol import encode_command, decode_command

def test_encode_command_1():
    "Encode Command - Test 1 - GET command encoding test"
        
    byte = encode_command("GET", "ON", 5, 3)
    
    assert 'k' == byte
    assert '01101011' == bin(ord(byte))[2:].zfill(8)
    
def test_encode_command_2():
    "Encode Command - Test 2 - SET command encoding test"
        
    byte = encode_command("SET", "OFF", 7, 3)
    
    assert '10111011' == bin(ord(byte))[2:].zfill(8)
    

def test_decode_command_1():
	"Decode Command - Test 1 - GET command decoding test"
	
	d = decode_command(chr(217))
	
	assert d == my_dict("GET", "ON", 5, 3)
	
def test_decode_command_2():
	"Decode Command -Test 2 - SET command decoding test"
	
	d = decode_command(chr(217)
	
	assert d == my_dict("SET", "OFF", 7, 3)