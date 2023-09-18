#  A port scanning tool used to to scan for potential & entry ports(open) for a given target.
import socket      # we are using 'socket' library (can be helpfull for identifying open ports)
def scan_port(target, port):      # Defining the function 'scan_port'
    try:                          # It is used to handle an exception
                                  # That is some operations within this block might rise some exceptions

        # Creating a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # It creates a new socket object using the 'socket' class
                                                                 # We used 'AF_INET' as the address family (IPv4)
                                                                 # WE USED 'SOCK_STREAM' as the socket type
                                                                 # *** THIS SOCKET WILL BE USED FOR A TCP CONNECTION

        sock.settimeout(1)        # This sets a time of 1 sec for the socket's connection.
                                  # If the connection is not established then, a 'socket.timeout' will be raised

        sock.connect((target, port))   # Establishes a connection to the targeted IP/hostname and port
                                       #If it is successfull then it means the port is open
        print(f"Port {port} is open")                                 
        sock.close()                   # This line closes the socket connection

    except socket.error:            # 'socket.error' is basically indicating that the port is closed and there is an error connecting
        pass                        # In this case we generally pass and do nothig so that the program doesnot gets terminate

def port_scan(target, start_point, end_point):     # Defining the 'port_scan' function
    print(f"Scanning ports for {target}......")    # Here is 'f' is a prefix used to insert value in the variable 'target'

    for port in range(start_port, end_port +1):    # It's a loop, Here the program will go through the each port in the range of 'start_port' & 'end_port'
        scan_port(target, port)                    # Calls the function 'scan_port()' to scan that specified port on the target


if __name__ == "__main__":
    target_host = "csas.in"    # Change the 'localhost' to the target host you want to scan  
    start_port = 1               # 'start_point' is set to '1'
    end_port = 1024              # 'end_port' is set to '1024'

    port_scan(target_host, start_port, end_port)   # 'port_scan' function is called