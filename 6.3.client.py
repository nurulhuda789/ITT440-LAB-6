import socket
import sys

client = socket.socket()
host = '192.168.43.81'
port = 8888

try:
    client.connect((host, port))
except socket.error as e:
    print(str(e))

response = client.recv(1024)
print(response)
while True:
	print('\nCalculator Operations')
	print('log - Logarithmic')
	print('sqrt - Square Root')
	print('exp - Exponential function')
	print('exit')
    choice = input('Enter operation: ')
    client.send(choice.encode())
	
	if choice == 'exp':
		print('Exponent')
		no = input('Enter number :')
		client.send(no.encode())
		value = client.recv(1024)
		print('Value :'+ str(value.decode('utf-8'))+'\n')
		
		
	elif choice == 'log':
		print('logarithmic')
		no = input('Enter number :')
		base = input('Enter base :')
		client.send(no.encode())
		client.send(base.encode())
		value=client.recv(1024)
		print('Value :'+ str(value.decode('utf-8'))+'\n')
	  
	elif choice == 'sqrt':
		print('square root')
		no =input('Enter positive number only :')
		client.send(no.encode())
		value=client.recv(1024)
		print('Value :'+ str(value.decode('utf-8'))+'\n')

	elif choice == 'exit':
		client.close()
		sys.exit()


