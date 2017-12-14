import serial
import struct
'''data.write(struct.pack('>B', pos))'''
data = serial.Serial('com3', 9600, timeout = 1)
	
 

def p1():
	try:
		pos = input("\n X-Axis> ")
		if (4<pos<174):
			print "\n X-Axis = ", pos
			data.write(struct.pack('>B', pos))
			p2();
		else:
			print "\n Error: This Input is not Exceptable(Input has to be 5-173)"
	except:
		print "\n Error: This Input is not Exceptable(Input has to be 5-173)"
		
	
def p2():
	try:
		pos2 = input("\n Y-Axis> ")
		if (4<pos2<174):
			print "\n Y-Axis = ", pos2
			data.write(struct.pack('>B', pos2))
			p1()
		else:
			print "\n Error: This Input is not Exceptable(Input has to be 5-173)"
			p2()
	except:
		print "\n Error: This Input is not Exceptable(Input has to be 5-173)"
		p2()
		
		
while True:
	p1()

	