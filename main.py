import os
import model.host_scanner as hs
import model.port_scanner as ps
import model.colors as color 

try:
    print("")
except KeyboardInterrupt:
    print(f"{color.WARNING}Interrumpiendo la aplicacion...{color.ENDC}")