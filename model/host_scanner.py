from plyer import notification 
import psutil
import socket

#Informacion ip y mascara
info = []

def obtencion_datos(interfaz=""):
    try:
        direcciones = psutil.net_if_addrs()[interfaz]
        for direccion in direcciones:
            if direccion.family == socket.AF_INET:
                ip = direccion.address
                mascara = direccion.netmask
                return [ip,mascara]
    except KeyError:
        print("Error!. Interfaz no existente")

#notification.notify(
#    title='Simulacion',
#    message='Esto es una prueba'
#)

