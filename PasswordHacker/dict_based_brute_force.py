import socket
from itertools import product
from sys import argv


def get_passwords():
    with open("passwords.txt", "r") as passwords:
        for _password in passwords.readlines():
            yield _password.strip()


hostname, port = argv[1], int(argv[2])
address = (hostname, port)

with socket.socket() as client:
    client.connect(address)

    for password in get_passwords():

        for combination in map(''.join, product(*zip(password.upper(), password.lower()))):
            client.send(combination.encode())
            response = client.recv(1024).decode()

            if response == "Connection success!":
                print(combination)
                exit()
