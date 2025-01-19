import os
import model.host_scanner as hs
import model.port_scanner as ps
import model.tcp_ack as ta 
import model.colors as color 

try:
    interfaz = input("\nColoque el nombre de la interfaz conectada a la red\n")
    data = hs.obtencion_datos(interfaz)
    red = hs.obetencion_red(data[0],data[1])
except KeyboardInterrupt:
    print(f"{color.WARNING}Interrumpiendo la aplicacion...{color.ENDC}")