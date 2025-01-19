from plyer import notification 
import psutil, math, socket

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

def obetencion_red(ip,mascara):
    mascara = str.split(mascara,".")
    ip = str.split(ip,".")
    print(mascara)
    prefijo = 0
    red=""
    bin = ""
    wild = []
    u=0
    for i in mascara:
        wild.append(str(255-int(i)))
        u+=1
        for x in range(0,8):
            j=int(i)%2
            bin+=str(j)
            i=int(i)/2
            if j == 1: prefijo+=1
            if x == 7 and u != 4: bin+="." 
    cidr = int((math.pow(2,(32-prefijo))-2))
    for i in range(0,4):
        if wild[i] != "0":
            ip[i]=255
            ip[i]=int(ip[i])-int(wild[i])
        red+=str(ip[i])
        if i != 3: red+="."
    print(cidr)
    print(bin)
    print(wild)
    print(red)

#def busqueda(red, wild):

#notification.notify(
#    title='Simulacion',
#    message='Esto es una prueba'
#)