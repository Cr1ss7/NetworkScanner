import scapy.all as sc

def res_tcp(ip_dst, ip_src):
    sc.send(sc.IP(src=ip_src,dst=ip_dst)/sc.TCP())