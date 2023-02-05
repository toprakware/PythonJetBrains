import socket
from itertools import product
from string import ascii_lowercase, digits
from sys import argv


def generate_password():
    for rep in range(1, len(chars) + 1):
        for prod in product(chars, repeat=rep):
            yield ''.join(prod)


hostname, port = argv[1], int(argv[2])
address = (hostname, port)
chars = ascii_lowercase + digits

with socket.socket() as client:
    client.connect(address)

    for password in generate_password():
        client.send(password.encode())
        response = client.recv(1024).decode()

        if response == "Connection success!":
            print(password)
            break
