import os
import model.host_scanner as hs
import model.port_scanner as ps
import model.tcp_ack as ta 
import model.colors as color 

try:
    ta.res_tcp("192.168.1.23", "192.168.1.1")
except KeyboardInterrupt:
    print(f"{color.WARNING}Interrumpiendo la aplicacion...{color.ENDC}")