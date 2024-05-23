import socket
import time

loopback_ip_address = '127.0.0.1'

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ip_address = socket.gethostbyname(loopback_ip_address)
    print(f'You are LEGALLY scanning local host: {loopback_ip_address}')

    starting_time = time.time()

    checkPortConnection(sock, ip_address)
    
    ending_time = time.time()

    time_scanning_ports = ending_time - starting_time

    print(f'It took Python {time_scanning_ports:.3f} seconds to scan the ports.')


def portS(sock, ip_address, port):
    try:
        sock.connect_ex((ip_address, port))
        return True
    except: 
        return False
    ##else:
        ##return True


def checkPortConnection(sock, ip_address):
    port_max = int(input("Enter number of ports to scan (max): [2 - 65,534]\n"))
    for port in range(1, port_max + 1):
        if portS(sock, ip_address, port):
            print(f'Port {port} is open')
        else: 
            print(f'Port {port} is closed') 


if __name__ == "__main__":
    main()