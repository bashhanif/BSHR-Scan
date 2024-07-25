#!/usr/bin/env python
import pyfiglet
import socket 
import argparse


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



def main():
   

    ascii_banner = pyfiglet.figlet_format("BSHR SCANNER")
    print(ascii_banner)
    print("-" * 50)

    parser = argparse.ArgumentParser(description="port scanner")
    parser.add_argument("target_ip", help="IP address to scan")
    parser.add_argument("-p","--port", type=int, help= "port to scan (single scan)")
    parser.add_argument("-r","--range", type=str, help="Range of ports to scan, Format: start-end ")
    


    args = parser.parse_args()

    if args.port is not None:
        open1 = scan_singleport(args.target_ip, args.port)
        if open1:
            print(f"Port {args.port} is open")
        else:
            print("Port is closed or unreachable.")
    elif args.range is not None:
        try:
            start,end = map(int,args.range.split('-'))
            open_ports = scan_ports(args.target_ip, start, end)
            print(f"Open ports: {open_ports}")

        except ValueError:
            print("Invalid format please use: start-end.")
    else:
        print("Please specify a port (-p) or a range of ports (-r) to scan.")


if __name__ == "__main__":
    main()



