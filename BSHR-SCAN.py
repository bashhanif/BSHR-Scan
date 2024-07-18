#! /usr/bin/env python
import pyfiglet
import socket 


def scan_singleport(ip , port ):

    try:
       socket1 = socket.socket(socket.AF_INET , socket.SOCK_STREAM)  #create socket ipv4 and tcp 
       socket1.settimeout(3)  #socket time out to 4 second
       results = socket1.connect_ex((ip,port)) #connect to scojket 
       socket1.close()   
       return results == 0
    except:
       print(f"error occured scanning {port} ")
       return False


def scan_ports(ip , start_port , end_port):
    print(f"Scanning ports {start_port} to {end_port}")
    #loop to scan each port , adding each open port to a running list , return list 
    openports = []
    for port in range(start_port , end_port + 1):
        if scan_singleport(ip , port):
            openports.append(port)
    

    return openports



if __name__ == "__main__":
   

    ascii_banner = pyfiglet.figlet_format("BSHR SCANNER")
    print(ascii_banner)
    print("-" * 50)

    target_ip = input("please enter ip address to scan:")

    scan_choice = input("single scan or range scan  (single/range):")


    if scan_choice == "single":
        target_port = int(input("Enter port to scan:"))

        open1 = scan_singleport(target_ip , target_port)

        if open1 == True:
            print(f"Port {target_port} is open ")
        else:
            print("lol that shit aint working rn ")
    elif scan_choice == "range":

        
        start = int(input("Enter starting port:"))
        end = int(input("Enter ending port:"))

        open_ports = scan_ports(target_ip , start , end)

        print(f"Open ports: {open_ports}")

    else:

        print("invalid choice please choose single or range")
        




